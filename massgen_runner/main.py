#!/usr/bin/env python3
"""
Run MassGen (direct Python import) on dataset queries and emit eval-compatible files.

Outputs per query index:
  - final_report.md
  - intro.md
  - paper.csv
  - stats.json
"""

import argparse
import asyncio
import json
import re
import time
import traceback
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

ARXIV_ABS_URL_RE = re.compile(r"https?://arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)")
ARXIV_PDF_URL_RE = re.compile(r"https?://arxiv\.org/pdf/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)(?:\.pdf)?")
ARXIV_TEXT_RE = re.compile(r"\barxiv[:\s]+([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)\b", flags=re.IGNORECASE)
ARXIV_VERSION_RE = re.compile(r"v\d+$")
TEXT_FILE_SUFFIXES = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}
MAX_ARTIFACT_FILE_SIZE_BYTES = 2_000_000
DEFAULT_MAX_ARTIFACT_FILES = 300

QUERY_TEMPLATE = """Your task is to write a Related Works section for an academic paper given the paper's abstract. Your response should provide the Related Works section and references. Only include references from arXiv that are published before {cutoff_date}. Mention them in a separate, numbered reference list at the end and use the reference numbers to provide in-line citations in the Related Works section for all claims referring to a source (e.g., description of source [3]. Further details [6][7][8][9][10].) Each in-line citation must consist of a single reference number within a pair of brackets. Do not use any other citation format. Do not exceed 600 words for the related works section. Here is the paper abstract: {abstract}"""


def _base_arxiv_id(arxiv_id: str) -> str:
    return ARXIV_VERSION_RE.sub("", arxiv_id.strip())


def _normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def _safe_read_text(path: Path, max_chars: int = 500_000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    return text[:max_chars]


def _looks_like_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_FILE_SUFFIXES


def _dedupe_arxiv_ids(arxiv_ids: list[str]) -> list[str]:
    deduped: list[str] = []
    seen_base: set[str] = set()
    for arxiv_id in arxiv_ids:
        base_id = _base_arxiv_id(arxiv_id)
        if base_id in seen_base:
            continue
        seen_base.add(base_id)
        deduped.append(arxiv_id)
    return deduped


def extract_arxiv_ids(text: str) -> list[str]:
    """Extract unique arXiv IDs from markdown links and plain-text mentions."""
    ordered_ids: list[str] = []
    seen: set[str] = set()
    for pattern in (ARXIV_ABS_URL_RE, ARXIV_PDF_URL_RE, ARXIV_TEXT_RE):
        for match in pattern.findall(text):
            arxiv_id = match.strip()
            if arxiv_id and arxiv_id not in seen:
                seen.add(arxiv_id)
                ordered_ids.append(arxiv_id)
    return ordered_ids


def _parse_arxiv_id_from_entry(entry_id_text: str) -> str | None:
    match = ARXIV_ABS_URL_RE.search(entry_id_text)
    if match:
        return match.group(1)
    match = ARXIV_PDF_URL_RE.search(entry_id_text)
    if match:
        return match.group(1)
    return None


def fetch_arxiv_metadata(arxiv_ids: list[str], timeout_seconds: float = 20.0) -> dict[str, dict[str, str]]:
    """
    Fetch title/abstract from arXiv API by ID.

    Returns a map keyed by the requested IDs.
    """
    if not arxiv_ids:
        return {}

    try:
        import xml.etree.ElementTree as ET
    except Exception:
        return {}

    metadata: dict[str, dict[str, str]] = {}
    chunk_size = 50

    for i in range(0, len(arxiv_ids), chunk_size):
        chunk = arxiv_ids[i : i + chunk_size]
        try:
            resp = requests.get(
                "https://export.arxiv.org/api/query",
                params={"id_list": ",".join(chunk)},
                timeout=timeout_seconds,
            )
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
        except Exception:
            continue

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns):
            entry_id_text = entry.findtext("atom:id", default="", namespaces=ns)
            entry_arxiv_id = _parse_arxiv_id_from_entry(entry_id_text)
            if not entry_arxiv_id:
                continue

            title = _normalize_whitespace(entry.findtext("atom:title", default="", namespaces=ns))
            abstract = _normalize_whitespace(entry.findtext("atom:summary", default="", namespaces=ns))
            entry_base = _base_arxiv_id(entry_arxiv_id)

            for requested_id in chunk:
                if requested_id in metadata:
                    continue
                if requested_id == entry_arxiv_id or _base_arxiv_id(requested_id) == entry_base:
                    metadata[requested_id] = {"title": title, "abstract": abstract}

    return metadata


def build_paper_dataframe(
    arxiv_ids: list[str],
    metadata: dict[str, dict[str, str]],
    preferred_rows: dict[str, dict[str, str]] | None = None,
) -> pd.DataFrame:
    preferred_rows = preferred_rows or {}
    rows = []
    for arxiv_id in arxiv_ids:
        info = metadata.get(arxiv_id, {}).copy()
        preferred = preferred_rows.get(_base_arxiv_id(arxiv_id), {})
        if preferred.get("title"):
            info["title"] = preferred["title"]
        if preferred.get("snippet"):
            info["abstract"] = preferred["snippet"]
        url = preferred.get("url") or f"https://arxiv.org/abs/{arxiv_id}"
        rows.append(
            {
                "id": arxiv_id,
                "title": info.get("title", ""),
                "snippet": info.get("abstract", ""),
                "url": url,
            }
        )

    if rows:
        return pd.DataFrame(rows)
    return pd.DataFrame(columns=["id", "title", "snippet", "url"])


def load_queries(queries_file: str) -> pd.DataFrame:
    """Load query CSV, generating it from papers_with_related_works.csv when missing."""
    query_path = Path(queries_file)
    if query_path.exists():
        return pd.read_csv(query_path)

    papers_path = query_path.parent / "papers_with_related_works.csv"
    if not papers_path.exists():
        raise FileNotFoundError(
            f"Neither {query_path} nor {papers_path} found. Please provide query data."
        )

    print(f"⚠️  {queries_file} not found. Generating queries from papers_with_related_works.csv...")
    papers_df = pd.read_csv(papers_path)
    queries_df = papers_df.copy()
    queries_df["query"] = queries_df.apply(
        lambda row: QUERY_TEMPLATE.format(
            cutoff_date=row["published_date"],
            abstract=row["abstract"],
        ),
        axis=1,
    )
    queries_df.to_csv(query_path, index=False)
    print(f"✅ Generated and saved queries to {query_path}")
    return queries_df


def _candidate_root_paths(result: dict[str, Any]) -> list[Path]:
    roots: list[Path] = []

    for key in ("final_answer_path", "log_directory"):
        value = result.get(key)
        if not value or not isinstance(value, str):
            continue
        path = Path(value).expanduser()
        if path.exists():
            roots.append(path)

    answers = result.get("answers")
    if isinstance(answers, list):
        for answer in answers:
            if not isinstance(answer, dict):
                continue
            answer_path = answer.get("answer_path")
            if not answer_path or not isinstance(answer_path, str):
                continue
            path = Path(answer_path).expanduser()
            if path.exists():
                roots.append(path)

    unique_roots: list[Path] = []
    seen: set[str] = set()
    for root in roots:
        root_key = str(root.resolve())
        if root_key in seen:
            continue
        seen.add(root_key)
        unique_roots.append(root)
    return unique_roots


def _read_final_answer_from_result_paths(result: dict[str, Any]) -> tuple[str, str]:
    selected_agent = result.get("selected_agent")
    final_answer_path = result.get("final_answer_path")
    if not isinstance(final_answer_path, str):
        text = str(result.get("final_answer", "") or "")
        return text, "massgen_result.final_answer"

    path = Path(final_answer_path).expanduser()
    if not path.exists():
        text = str(result.get("final_answer", "") or "")
        return text, "massgen_result.final_answer"

    # Two passes: first prefer the canonical workspace `intro.md` (per the
    # agent system message) but only if it has substantial content. The
    # agent sometimes leaves intro.md as a tiny stub (e.g. a leftover
    # comment) while writing the real Related Works into answer.txt, and
    # other times the reverse — answer.txt contains only narration while
    # intro.md is the real deliverable. Falling back to a non-empty check
    # alone picks the wrong file in either edge case.
    MIN_DELIVERABLE_BYTES = 500

    primary_candidates: list[Path] = []
    fallback_candidates: list[Path] = []
    if path.is_file():
        primary_candidates.append(path)
    else:
        if selected_agent and isinstance(selected_agent, str):
            selected_intro = path / selected_agent / "workspace" / "intro.md"
            if selected_intro.exists():
                primary_candidates.append(selected_intro)
            selected_answer = path / selected_agent / "answer.txt"
            if selected_answer.exists():
                primary_candidates.append(selected_answer)
        primary_candidates.extend(path.rglob("intro.md"))
        primary_candidates.extend(path.rglob("final_report.md"))
        primary_candidates.extend(path.rglob("answer.txt"))
        fallback_candidates.extend(path.rglob("*.md"))
        fallback_candidates.extend(path.rglob("*.txt"))

    # Pass 1: prefer candidates that meet the deliverable size threshold,
    # in priority order.
    for candidate in primary_candidates:
        text = _safe_read_text(candidate)
        if len(text.strip()) >= MIN_DELIVERABLE_BYTES:
            return text, str(candidate)

    # Pass 2: accept any non-empty primary candidate (handles short
    # legitimate outputs).
    for candidate in primary_candidates:
        text = _safe_read_text(candidate)
        if text.strip():
            return text, str(candidate)

    # Pass 3: last-resort fallback to any markdown/text file.
    for candidate in fallback_candidates:
        text = _safe_read_text(candidate)
        if text.strip():
            return text, str(candidate)

    text = str(result.get("final_answer", "") or "")
    return text, "massgen_result.final_answer"


def _iter_artifact_files(result: dict[str, Any], max_files: int = DEFAULT_MAX_ARTIFACT_FILES) -> list[Path]:
    files: list[Path] = []
    seen: set[str] = set()

    def add_file(path: Path) -> None:
        if len(files) >= max_files:
            return
        try:
            path_key = str(path.resolve())
        except Exception:
            return
        if path_key in seen:
            return
        if not path.is_file() or not _looks_like_text_file(path):
            return
        try:
            if path.stat().st_size > MAX_ARTIFACT_FILE_SIZE_BYTES:
                return
        except Exception:
            return
        seen.add(path_key)
        files.append(path)

    roots = _candidate_root_paths(result)

    for root in roots:
        if len(files) >= max_files:
            break

        if root.is_file():
            add_file(root)
            continue

        if root.name == "final":
            scan_dirs = [root]
        elif root.name.startswith("log_"):
            scan_dirs = [
                root / "final",
                root / "agent_outputs",
            ]
        else:
            scan_dirs = [root]

        for scan_dir in scan_dirs:
            if len(files) >= max_files:
                break
            if not scan_dir.exists():
                continue
            if scan_dir.is_file():
                add_file(scan_dir)
                continue
            try:
                candidates = sorted(scan_dir.rglob("*"))
            except Exception:
                continue
            for path in candidates:
                if len(files) >= max_files:
                    break
                add_file(path)

    return files


def _extract_text_artifacts(result: dict[str, Any], max_files: int = DEFAULT_MAX_ARTIFACT_FILES) -> tuple[list[str], list[Path], str, str]:
    final_answer_text, final_answer_source = _read_final_answer_from_result_paths(result)
    artifact_files = _iter_artifact_files(result=result, max_files=max_files)

    texts: list[str] = []
    seen: set[str] = set()

    def add_text(value: str) -> None:
        text = (value or "").strip()
        if not text:
            return
        if text in seen:
            return
        seen.add(text)
        texts.append(text)

    add_text(final_answer_text)

    raw_answer = result.get("final_answer")
    if isinstance(raw_answer, str):
        add_text(raw_answer)

    answers = result.get("answers")
    if isinstance(answers, list):
        for answer in answers:
            if isinstance(answer, dict) and isinstance(answer.get("content"), str):
                add_text(answer["content"])

    for path in artifact_files:
        add_text(_safe_read_text(path))

    return texts, artifact_files, final_answer_text, final_answer_source


def _first_matching_column(columns: list[str], candidates: tuple[str, ...]) -> str | None:
    lowered = {col.strip().lower(): col for col in columns}
    for candidate in candidates:
        if candidate in lowered:
            return lowered[candidate]
    return None


def _extract_preferred_rows_from_csv_files(csv_files: list[Path]) -> dict[str, dict[str, str]]:
    preferred_rows: dict[str, dict[str, str]] = {}
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
        except Exception:
            continue
        if df.empty:
            continue

        columns = [str(c) for c in df.columns]
        id_col = _first_matching_column(columns, ("id", "arxiv_id", "paper_id"))
        url_col = _first_matching_column(columns, ("url", "arxiv_link", "link"))
        title_col = _first_matching_column(columns, ("title", "paper_title"))
        snippet_col = _first_matching_column(columns, ("snippet", "abstract", "summary", "text"))

        if not id_col and not url_col:
            continue

        for _, row in df.iterrows():
            row_id = str(row.get(id_col, "")).strip() if id_col else ""
            row_url = str(row.get(url_col, "")).strip() if url_col else ""

            if not row_id and row_url:
                matches = ARXIV_ABS_URL_RE.findall(row_url) + ARXIV_PDF_URL_RE.findall(row_url)
                if matches:
                    row_id = matches[0]

            row_id = row_id.strip()
            if not row_id:
                continue

            key = _base_arxiv_id(row_id)
            existing = preferred_rows.get(key, {})
            title = str(row.get(title_col, "")).strip() if title_col else ""
            snippet = str(row.get(snippet_col, "")).strip() if snippet_col else ""
            if row_url and not row_url.startswith("http"):
                row_url = ""
            merged = {
                "id": existing.get("id") or row_id,
                "title": existing.get("title") or title,
                "snippet": existing.get("snippet") or snippet,
                "url": existing.get("url") or row_url,
            }
            preferred_rows[key] = merged
    return preferred_rows


async def run_massgen_query(
    query: str,
    massgen_config: str | None = None,
    verbose: bool = False,
    parse_at_references: bool = False,
) -> dict[str, Any]:
    """Run one MassGen query via direct Python import."""
    try:
        import massgen
    except Exception as e:
        raise ImportError(
            "Failed to import `massgen`. Install it with `pip install massgen` "
            "and ensure the active environment is the one used for this run."
        ) from e

    run_kwargs: dict[str, Any] = {
        "query": query,
        "enable_logging": True,
        "verbose": verbose,
        "parse_at_references": parse_at_references,
    }
    if massgen_config:
        run_kwargs["config"] = massgen_config

    result = await massgen.run(**run_kwargs)
    if isinstance(result, dict):
        if "final_answer" not in result and "answer" in result:
            result["final_answer"] = result["answer"]
        return result
    return {"final_answer": str(result)}


async def process_query(
    idx: int,
    query: str,
    arxiv_id: str,
    output_folder: Path,
    massgen_config: str | None = None,
    verbose: bool = False,
    parse_at_references: bool = False,
) -> dict[str, Any]:
    """Process a single query and save files expected by eval parsers."""
    query_output_folder = output_folder / str(idx)
    query_output_folder.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 60}")
    print(f"Processing query {idx}: {arxiv_id}")
    print(f"{'=' * 60}")
    started = time.perf_counter()

    try:
        result = await run_massgen_query(
            query=query,
            massgen_config=massgen_config,
            verbose=verbose,
            parse_at_references=parse_at_references,
        )
        text_artifacts, artifact_files, final_answer, final_answer_source = _extract_text_artifacts(
            result=result,
            max_files=DEFAULT_MAX_ARTIFACT_FILES,
        )

        final_report_path = query_output_folder / "final_report.md"
        with open(final_report_path, "w", encoding="utf-8") as f:
            f.write(final_answer)
        print(f"✅ Saved final report to {final_report_path}")

        intro_path = query_output_folder / "intro.md"
        with open(intro_path, "w", encoding="utf-8") as f:
            f.write(final_answer)
        print(f"✅ Saved intro section to {intro_path}")

        extracted_arxiv_ids: list[str] = []
        for text in text_artifacts:
            extracted_arxiv_ids.extend(extract_arxiv_ids(text))
        arxiv_ids = _dedupe_arxiv_ids(extracted_arxiv_ids)

        csv_files = [path for path in artifact_files if path.suffix.lower() == ".csv"]
        preferred_rows = _extract_preferred_rows_from_csv_files(csv_files)

        # Ensure IDs found in preferred rows are represented even if absent from answer text.
        for row in preferred_rows.values():
            row_id = row.get("id", "").strip()
            if row_id:
                arxiv_ids.append(row_id)
        arxiv_ids = _dedupe_arxiv_ids(arxiv_ids)

        missing_metadata_ids: list[str] = []
        for arxiv_id in arxiv_ids:
            row = preferred_rows.get(_base_arxiv_id(arxiv_id), {})
            if not row.get("title") or not row.get("snippet"):
                missing_metadata_ids.append(arxiv_id)
        metadata = fetch_arxiv_metadata(_dedupe_arxiv_ids(missing_metadata_ids))
        papers_df = build_paper_dataframe(arxiv_ids, metadata, preferred_rows=preferred_rows)
        paper_csv_path = query_output_folder / "paper.csv"
        papers_df.to_csv(paper_csv_path, index=False)
        print(f"✅ Saved papers to {paper_csv_path}")

        elapsed = time.perf_counter() - started
        stats: dict[str, Any] = {
            "engine": "massgen_import",
            "duration_seconds": elapsed,
            "num_extracted_arxiv_ids": len(arxiv_ids),
            "extracted_arxiv_ids": arxiv_ids,
            "final_answer_source": final_answer_source,
            "num_artifact_files_scanned": len(artifact_files),
            "artifact_files_scanned": [str(path) for path in artifact_files],
            "massgen_result": result,
        }
        stats_path = query_output_folder / "stats.json"
        with open(stats_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, default=str)
        print(f"✅ Saved stats to {stats_path}")

        return {
            "idx": idx,
            "arxiv_id": arxiv_id,
            "status": "success",
            "num_papers": len(papers_df),
        }
    except Exception as e:
        print(f"❌ Error processing query {idx}: {e}")
        error_path = query_output_folder / "error.txt"
        with open(error_path, "w", encoding="utf-8") as f:
            f.write(f"Error: {e}\n\n")
            f.write(traceback.format_exc())
        return {
            "idx": idx,
            "arxiv_id": arxiv_id,
            "status": "error",
            "error": str(e),
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run MassGen (direct Python API import) on query CSV and save eval-compatible outputs."
    )
    parser.add_argument(
        "--queries-file",
        type=str,
        default="dataset/queries.csv",
        help="Path to query CSV (default: dataset/queries.csv)",
    )
    parser.add_argument(
        "--output-folder",
        type=str,
        default=None,
        help="Output folder (required)",
    )
    parser.add_argument(
        "--start-idx",
        type=int,
        default=0,
        help="Start index (inclusive)",
    )
    parser.add_argument(
        "--end-idx",
        type=int,
        default=None,
        help="End index (exclusive, default: all)",
    )
    parser.add_argument(
        "--massgen-config",
        type=str,
        default=None,
        help="Path to MassGen YAML config passed to massgen.run(config=...)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose MassGen execution output",
    )
    parser.add_argument(
        "--parse-at-references",
        action="store_true",
        help="Enable MassGen @path reference parsing in prompts",
    )
    args = parser.parse_args()

    if not args.output_folder:
        parser.error("--output-folder is required")
    if args.start_idx < 0:
        parser.error("--start-idx must be >= 0")
    if args.end_idx is not None and args.end_idx < args.start_idx:
        parser.error("--end-idx must be >= --start-idx")
    if args.massgen_config:
        config_path = Path(args.massgen_config)
        if not config_path.exists():
            parser.error(f"--massgen-config not found: {config_path}")
    return args


async def main() -> None:
    args = parse_args()
    load_dotenv()

    output_folder = Path(args.output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 60}")
    print("MassGen Direct-Import Runner")
    print(f"{'=' * 60}")
    print(f"Queries file:         {args.queries_file}")
    print(f"Output folder:        {args.output_folder}")
    print(f"MassGen config:       {args.massgen_config or '(massgen defaults)'}")
    print(f"{'=' * 60}\n")

    print(f"Loading queries from {args.queries_file}...")
    queries_df = load_queries(args.queries_file)
    print(f"✅ Loaded {len(queries_df)} queries")

    if args.end_idx is not None:
        queries_df = queries_df.iloc[args.start_idx : args.end_idx]
    else:
        queries_df = queries_df.iloc[args.start_idx :]
    print(f"Processing queries {args.start_idx} to {args.start_idx + len(queries_df)}")

    results = []
    for idx, row in queries_df.iterrows():
        result = await process_query(
            idx=idx,
            query=row["query"],
            arxiv_id=row.get("arxiv_id", f"unknown_{idx}"),
            output_folder=output_folder,
            massgen_config=args.massgen_config,
            verbose=args.verbose,
            parse_at_references=args.parse_at_references,
        )
        results.append(result)

    summary_path = output_folder / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    success_count = sum(1 for item in results if item["status"] == "success")
    error_count = sum(1 for item in results if item["status"] == "error")
    print(f"\n{'=' * 60}")
    print("✅ Processing complete!")
    print(f"{'=' * 60}")
    print(f"Processed {len(results)} queries")
    print(f"Success: {success_count}")
    print(f"Errors:  {error_count}")
    print(f"Summary saved to {summary_path}")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    asyncio.run(main())
