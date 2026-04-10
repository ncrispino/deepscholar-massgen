import pandas as pd

from eval.parsers.massgen import MassGenParser
from eval.parsers.parser_type import ParserType
from massgen_runner.main import (
    _extract_preferred_rows_from_csv_files,
    _read_final_answer_from_result_paths,
)


def _sample_dataset() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "title": "Parent Paper",
                "abstract": "Parent abstract.",
                "arxiv_link": "https://arxiv.org/abs/9999.00001",
                "clean_latex_related_works": "",
                "arxiv_id": "9999.00001",
            }
        ]
    )


def test_massgen_parser_parses_numbered_references(tmp_path):
    folder = tmp_path / "0"
    folder.mkdir(parents=True, exist_ok=True)

    intro = """Recent methods improved alignment [1, 2] and retrieval quality [2].

References
[1] Some paper arXiv:1234.5678
[2] Another paper https://arxiv.org/abs/2345.67890v2
"""
    (folder / "intro.md").write_text(intro, encoding="utf-8")

    pd.DataFrame(
        [
            {
                "id": "1234.5678",
                "title": "Some paper",
                "snippet": "Snippet one.",
                "url": "https://arxiv.org/abs/1234.5678",
            },
            {
                "id": "2345.67890v2",
                "title": "Another paper",
                "snippet": "Snippet two.",
                "url": "https://arxiv.org/abs/2345.67890v2",
            },
        ]
    ).to_csv(folder / "paper.csv", index=False)

    parser = MassGenParser(
        str(folder),
        {
            "mode": ParserType.MASSGEN,
            "file_id": "0",
            "dataset": _sample_dataset(),
        },
    )

    assert parser.clean_text is not None
    assert "[1][2]" in parser.clean_text
    assert len(parser.docs) == 2
    assert parser.docs[0]["title"] == "Some paper"
    assert parser.docs[1]["title"] == "Another paper"
    assert len(parser.citations_for_cite_quality) == 2


def test_read_final_answer_prefers_final_path_answer_file(tmp_path):
    final_dir = tmp_path / "final"
    winner_dir = final_dir / "agent_a"
    winner_dir.mkdir(parents=True, exist_ok=True)
    answer_path = winner_dir / "answer.txt"
    answer_path.write_text("from-final-path", encoding="utf-8")

    text, source = _read_final_answer_from_result_paths(
        {
            "selected_agent": "agent_a",
            "final_answer_path": str(final_dir),
            "final_answer": "from-result",
        }
    )

    assert text == "from-final-path"
    assert source.endswith("answer.txt")

def test_extract_preferred_rows_from_csv_files_supports_alias_columns(tmp_path):
    csv_path = tmp_path / "references.csv"
    pd.DataFrame(
        [
            {
                "arxiv_id": "2101.00001v2",
                "paper_title": "Alias Title",
                "abstract": "Alias Abstract",
                "arxiv_link": "https://arxiv.org/abs/2101.00001v2",
            }
        ]
    ).to_csv(csv_path, index=False)

    rows = _extract_preferred_rows_from_csv_files([csv_path])
    assert "2101.00001" in rows
    assert rows["2101.00001"]["title"] == "Alias Title"
    assert rows["2101.00001"]["snippet"] == "Alias Abstract"
