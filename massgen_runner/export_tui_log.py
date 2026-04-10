#!/usr/bin/env python3
"""
Convert a MassGen TUI log directory into eval-compatible output files.

This creates, for a given file ID:
  - intro.md
  - final_report.md
  - paper.csv
  - stats.json

under: <output_folder>/<file_id>/
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

import pandas as pd

try:
    from .main import (
        MAX_ARTIFACT_FILE_SIZE_BYTES,
        _base_arxiv_id,
        _dedupe_arxiv_ids,
        _extract_preferred_rows_from_csv_files,
        _safe_read_text,
        build_paper_dataframe,
        extract_arxiv_ids,
        fetch_arxiv_metadata,
    )
except ImportError:
    from main import (  # type: ignore
        MAX_ARTIFACT_FILE_SIZE_BYTES,
        _base_arxiv_id,
        _dedupe_arxiv_ids,
        _extract_preferred_rows_from_csv_files,
        _safe_read_text,
        build_paper_dataframe,
        extract_arxiv_ids,
        fetch_arxiv_metadata,
    )

CSV_ARTIFACT_SUFFIXES = {".csv"}
MAX_ARTIFACT_FILES = 200
IGNORED_DIR_NAMES = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "node_modules",
}


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            value = json.load(f)
        if isinstance(value, dict):
            return value
    except Exception:
        pass
    return {}


def _resolve_attempt_dir(log_dir: Path) -> Path:
    if (log_dir / "status.json").exists():
        return log_dir

    candidates = []
    for path in log_dir.glob("turn_*/attempt_*"):
        if path.is_dir():
            try:
                mtime = path.stat().st_mtime_ns
            except Exception:
                mtime = 0
            candidates.append((mtime, path))

    if not candidates:
        raise FileNotFoundError(
            f"Could not find any attempt directory under: {log_dir}"
        )

    candidates.sort(key=lambda item: item[0])
    return candidates[-1][1]


def _newest_nonempty_text(paths: list[Path]) -> tuple[str, Path | None]:
    ranked: list[tuple[int, Path]] = []
    for path in paths:
        if not path.is_file():
            continue
        try:
            ranked.append((path.stat().st_mtime_ns, path))
        except Exception:
            continue

    ranked.sort(key=lambda item: item[0], reverse=True)
    for _, path in ranked:
        text = _safe_read_text(path, max_chars=1_000_000)
        if text.strip():
            return text, path
    return "", None


def _pick_final_answer(attempt_dir: Path) -> tuple[str, Path | None]:
    priority_groups = [
        list((attempt_dir / "final").glob("*/answer.txt")),
        list((attempt_dir / "final").glob("*/workspace/intro.md")),
        list((attempt_dir / "agent_outputs").glob("final_presentation_*.txt")),
        list(attempt_dir.rglob("answer.txt")),
        list(attempt_dir.rglob("workspace/intro.md")),
        list((attempt_dir / "agent_outputs").glob("*.txt")),
    ]

    for group in priority_groups:
        text, path = _newest_nonempty_text(group)
        if text.strip():
            return text, path

    return "", None


def _pick_intro_text(answer_text: str, answer_path: Path | None) -> tuple[str, str]:
    if answer_path is not None and answer_path.name == "answer.txt":
        workspace_intro = answer_path.parent / "workspace" / "intro.md"
        if workspace_intro.exists():
            intro_text = _safe_read_text(workspace_intro, max_chars=1_000_000)
            if intro_text.strip():
                return intro_text, str(workspace_intro)

    if answer_path is not None and answer_path.name == "intro.md":
        intro_text = _safe_read_text(answer_path, max_chars=1_000_000)
        if intro_text.strip():
            return intro_text, str(answer_path)

    return answer_text, "final_answer_fallback"


def _collect_supporting_csv_artifacts(
    attempt_dir: Path,
    max_files: int = MAX_ARTIFACT_FILES,
) -> list[Path]:
    collected: list[tuple[int, Path]] = []
    seen: set[str] = set()

    for root, dirs, files in os.walk(attempt_dir):
        dirs[:] = [name for name in dirs if name not in IGNORED_DIR_NAMES]
        for filename in files:
            path = Path(root) / filename
            if path.suffix.lower() not in CSV_ARTIFACT_SUFFIXES:
                continue
            lower_name = path.name.lower()
            if not any(token in lower_name for token in ("paper", "citation", "reference")):
                continue
            try:
                stat = path.stat()
            except Exception:
                continue
            if stat.st_size > MAX_ARTIFACT_FILE_SIZE_BYTES:
                continue
            key = str(path.resolve())
            if key in seen:
                continue
            seen.add(key)
            collected.append((stat.st_mtime_ns, path))

    collected.sort(key=lambda item: item[0], reverse=True)
    return [path for _, path in collected[:max_files]]


def export_log_to_eval(
    log_dir: Path,
    output_folder: Path,
    file_id: str,
) -> Path:
    started = time.perf_counter()
    attempt_dir = _resolve_attempt_dir(log_dir)

    final_answer_text, final_answer_path = _pick_final_answer(attempt_dir)
    if not final_answer_text.strip():
        raise RuntimeError(
            f"Could not find non-empty final answer text under attempt directory: {attempt_dir}"
        )
    intro_text, intro_source = _pick_intro_text(final_answer_text, final_answer_path)
    artifacts = _collect_supporting_csv_artifacts(attempt_dir)

    extracted_ids: list[str] = []
    for text in (final_answer_text, intro_text):
        extracted_ids.extend(extract_arxiv_ids(text))
    arxiv_ids = _dedupe_arxiv_ids(extracted_ids)

    preferred_rows = _extract_preferred_rows_from_csv_files(artifacts)
    for row in preferred_rows.values():
        row_id = str(row.get("id", "")).strip()
        if row_id:
            arxiv_ids.append(row_id)
    arxiv_ids = _dedupe_arxiv_ids(arxiv_ids)

    missing_metadata_ids: list[str] = []
    for arxiv_id in arxiv_ids:
        preferred = preferred_rows.get(_base_arxiv_id(arxiv_id), {})
        if not preferred.get("title") or not preferred.get("snippet"):
            missing_metadata_ids.append(arxiv_id)

    metadata = fetch_arxiv_metadata(_dedupe_arxiv_ids(missing_metadata_ids))
    papers_df = build_paper_dataframe(arxiv_ids, metadata, preferred_rows=preferred_rows)

    target_dir = output_folder / file_id
    target_dir.mkdir(parents=True, exist_ok=True)

    final_report_path = target_dir / "final_report.md"
    intro_path = target_dir / "intro.md"
    paper_csv_path = target_dir / "paper.csv"
    stats_path = target_dir / "stats.json"

    final_report_path.write_text(final_answer_text, encoding="utf-8")
    intro_path.write_text(intro_text, encoding="utf-8")
    papers_df.to_csv(paper_csv_path, index=False)

    status = _load_json(attempt_dir / "status.json")
    elapsed = time.perf_counter() - started
    stats: dict[str, Any] = {
        "engine": "massgen_tui_log_export",
        "duration_seconds": elapsed,
        "source_log_dir": str(log_dir),
        "source_attempt_dir": str(attempt_dir),
        "source_answer_file": str(final_answer_path) if final_answer_path else "",
        "source_intro_file": intro_source,
        "num_extracted_arxiv_ids": len(arxiv_ids),
        "extracted_arxiv_ids": arxiv_ids,
        "num_artifact_files_scanned": len(artifacts),
        "artifact_files_scanned": [str(path) for path in artifacts],
        "status_meta": status.get("meta", {}),
        "status_finish_reason": status.get("finish_reason"),
        "status_is_complete": status.get("is_complete"),
    }
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, default=str)

    return target_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a MassGen TUI log directory to eval-compatible output files."
    )
    parser.add_argument(
        "--log-dir",
        type=str,
        required=True,
        help="Path to MassGen log_* directory or a specific attempt_* directory",
    )
    parser.add_argument(
        "--output-folder",
        type=str,
        default="outputs/results",
        help="Target results folder (default: outputs/results)",
    )
    parser.add_argument(
        "--file-id",
        type=str,
        required=True,
        help="Eval file ID folder name to write under output-folder (usually dataset row index)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_dir = Path(args.log_dir).expanduser()
    output_folder = Path(args.output_folder).expanduser()
    if not log_dir.exists():
        raise FileNotFoundError(f"--log-dir does not exist: {log_dir}")

    target_dir = export_log_to_eval(
        log_dir=log_dir,
        output_folder=output_folder,
        file_id=args.file_id,
    )
    print(f"✅ Exported TUI log to eval folder: {target_dir}")


if __name__ == "__main__":
    main()
