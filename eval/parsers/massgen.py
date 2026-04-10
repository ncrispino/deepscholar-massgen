import csv
import os
import re
from collections import OrderedDict

try:
    from parsers.deepscholar_base import DeepScholarBaseParser
    from parsers.parser import ParserType
except ImportError:
    from .deepscholar_base import DeepScholarBaseParser
    from .parser import ParserType


class MassGenParser(DeepScholarBaseParser):
    """
    MassGen parser with robust fallback behavior for both:
    - DeepScholar-style markdown links: [Title](https://arxiv.org/abs/...)
    - Numbered references: [1] ... / 1. ... (common final-answer style)
    """

    parser_type = ParserType.MASSGEN

    citation_number_pattern = re.compile(r"\[(\d+)\]")
    multi_citation_pattern = re.compile(r"\[(\d+(?:\s*,\s*\d+)+)\]")
    reference_block_pattern = re.compile(
        r"(?:^|\n)\s*(?:\[(\d+)\]|(\d+)\.)\s*(.+?)(?=\n\s*(?:\[\d+\]|\d+\.)\s+|\Z)",
        flags=re.DOTALL,
    )
    arxiv_abs_url_pattern = re.compile(
        r"https?://arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)"
    )
    arxiv_pdf_url_pattern = re.compile(
        r"https?://arxiv\.org/pdf/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)(?:\.pdf)?"
    )
    arxiv_prefix_pattern = re.compile(
        r"arxiv[:\s]+([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)",
        flags=re.IGNORECASE,
    )
    arxiv_standalone_pattern = re.compile(r"\b([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)\b")
    arxiv_version_pattern = re.compile(r"v\d+$")

    def _load_file(self):
        self.file_path = self._get_file_path()
        self.raw_generated_text = open(self.file_path, "r", encoding="utf-8").read()

        paper_csv_path = os.path.join(self.folder_path, "paper.csv")
        reference_map = self._reference_parsing(paper_csv_path)

        # Primary parse path: DeepScholar markdown links.
        self.clean_text, self.docs = self._to_autoais(self.raw_generated_text, reference_map)

        # Fallback for MassGen-style numbered references.
        if not self.docs:
            self.clean_text, self.docs = self._to_autoais_numbered_references(
                self.raw_generated_text,
                reference_map,
            )

        # Last-resort fallback: if citations are malformed but paper.csv exists,
        # keep the generated text and expose all known docs.
        if not self.docs and reference_map:
            self.clean_text = self._normalize_multi_citations(self.raw_generated_text).strip()
            self.docs = [
                {"title": info.get("title", ""), "sent": info.get("abstract", "")}
                for info in reference_map.values()
            ]

        # Some evaluators consume tuple form rather than dict docs.
        self.citations_for_cite_quality = [
            (doc.get("title", ""), doc.get("sent", ""))
            for doc in (self.docs or [])
        ]

    def _reference_parsing(self, file_path: str):
        """Parse paper.csv with a tolerant schema fallback."""
        if not os.path.exists(file_path):
            return {}
        try:
            return super()._reference_parsing(file_path)
        except Exception:
            return self._reference_parsing_fallback(file_path)

    def _reference_parsing_fallback(self, file_path: str) -> dict[str, dict[str, str]]:
        result: dict[str, dict[str, str]] = {}
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                normalized = {str(k).strip().lower(): (v or "") for k, v in row.items()}

                paper_id = (
                    normalized.get("id")
                    or normalized.get("arxiv_id")
                    or self._extract_arxiv_id(normalized.get("url", ""))
                    or ""
                ).strip()
                if not paper_id:
                    continue

                title = (normalized.get("title") or normalized.get("paper_title") or "").strip()
                abstract = (
                    normalized.get("snippet")
                    or normalized.get("abstract")
                    or normalized.get("summary")
                    or ""
                ).strip()
                result[paper_id] = {"title": title, "abstract": abstract}
        return result

    def _to_autoais_numbered_references(
        self,
        text: str,
        reference_map: dict[str, dict[str, str]],
    ) -> tuple[str, list[dict[str, str]]]:
        body_text, reference_section = self._split_body_and_references(text)
        body_text = self._normalize_multi_citations(body_text)

        numbered_reference_map = self._build_numbered_reference_map(
            reference_section,
            reference_map,
        )

        citation_to_idx: OrderedDict[str, int] = OrderedDict()
        docs: list[dict[str, str]] = []

        def repl(match: re.Match) -> str:
            citation_number = match.group(1)
            if citation_number not in citation_to_idx:
                citation_to_idx[citation_number] = len(citation_to_idx) + 1
                ref_info = numbered_reference_map.get(citation_number) or self._fallback_reference_by_position(
                    citation_number,
                    reference_map,
                )
                docs.append(
                    {
                        "title": ref_info.get("title", ""),
                        "sent": ref_info.get("abstract", ""),
                    }
                )
            return f"[{citation_to_idx[citation_number]}]"

        clean_text = self.citation_number_pattern.sub(repl, body_text).strip()
        return clean_text, docs

    def _split_body_and_references(self, text: str) -> tuple[str, str]:
        markers = [
            "\n## references",
            "\n# references",
            "\n**references**",
            "\nreferences",
        ]
        lower_text = text.lower()
        for marker in markers:
            idx = lower_text.find(marker)
            if idx != -1:
                return text[:idx], text[idx:]
        return text, ""

    def _normalize_multi_citations(self, text: str) -> str:
        def repl(match: re.Match) -> str:
            numbers = [item.strip() for item in match.group(1).split(",")]
            numbers = [number for number in numbers if number.isdigit()]
            return "".join(f"[{number}]" for number in numbers) if numbers else match.group(0)

        return self.multi_citation_pattern.sub(repl, text)

    def _build_numbered_reference_map(
        self,
        reference_section: str,
        reference_map: dict[str, dict[str, str]],
    ) -> dict[str, dict[str, str]]:
        numbered_reference_map: dict[str, dict[str, str]] = {}
        for match in self.reference_block_pattern.finditer(reference_section):
            citation_number = match.group(1) or match.group(2)
            entry = (match.group(3) or "").strip()
            if not citation_number:
                continue
            numbered_reference_map[citation_number] = self._resolve_reference_entry(entry, reference_map)
        return numbered_reference_map

    def _resolve_reference_entry(
        self,
        entry: str,
        reference_map: dict[str, dict[str, str]],
    ) -> dict[str, str]:
        arxiv_id = self._extract_arxiv_id(entry)
        if arxiv_id:
            info = self._lookup_reference_info(arxiv_id, reference_map)
            if info:
                return info
            return {"title": f"arXiv:{arxiv_id}", "abstract": ""}

        cleaned = self._strip_reference_entry(entry)
        return {"title": cleaned, "abstract": ""}

    def _fallback_reference_by_position(
        self,
        citation_number: str,
        reference_map: dict[str, dict[str, str]],
    ) -> dict[str, str]:
        if not reference_map:
            return {"title": "", "abstract": ""}

        try:
            position = int(citation_number) - 1
        except ValueError:
            return {"title": "", "abstract": ""}

        items = list(reference_map.values())
        if 0 <= position < len(items):
            return items[position]
        return {"title": "", "abstract": ""}

    def _lookup_reference_info(
        self,
        arxiv_id: str,
        reference_map: dict[str, dict[str, str]],
    ) -> dict[str, str] | None:
        base_id = self._base_arxiv_id(arxiv_id)
        if arxiv_id in reference_map:
            return reference_map[arxiv_id]
        for key, value in reference_map.items():
            if self._base_arxiv_id(key) == base_id:
                return value
        return None

    def _base_arxiv_id(self, arxiv_id: str) -> str:
        return self.arxiv_version_pattern.sub("", arxiv_id.strip())

    def _extract_arxiv_id(self, text: str) -> str | None:
        for pattern in (
            self.arxiv_abs_url_pattern,
            self.arxiv_pdf_url_pattern,
            self.arxiv_prefix_pattern,
            self.arxiv_standalone_pattern,
        ):
            match = pattern.search(text)
            if match:
                return match.group(1).strip()
        return None

    def _strip_reference_entry(self, entry: str) -> str:
        cleaned = re.sub(r"https?://\S+", "", entry)
        cleaned = re.sub(r"arxiv[:\s]+[0-9]{4}\.[0-9]{4,5}(?:v\d+)?", "", cleaned, flags=re.IGNORECASE)
        cleaned = cleaned.strip(" .;-")
        return cleaned
