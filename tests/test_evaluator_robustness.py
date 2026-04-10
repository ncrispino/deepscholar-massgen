from types import SimpleNamespace

import eval.evaluator.cite_p as cite_mod
import eval.evaluator.claim_coverage as claim_mod
from eval.evaluator.cite_p import CitePEvaluator
from eval.evaluator.claim_coverage import ClaimCoverageEvaluator


def test_cite_p_handles_missing_text_and_mismatched_citations(monkeypatch):
    monkeypatch.setattr(cite_mod, "sent_tokenize", lambda text: [text] if text else [])
    monkeypatch.setattr(cite_mod, "get_support", lambda premise, hypothesis: 1)

    parser = SimpleNamespace(
        clean_text=None,
        docs=[{"title": "Doc 1", "sent": "Abstract 1"}],
        citations_for_cite_quality=[],
        folder_path="dummy/0",
    )

    score = CitePEvaluator()._calculate(parser)
    assert score == 0.0


def test_claim_coverage_handles_missing_text_and_mismatched_citations(monkeypatch):
    monkeypatch.setattr(claim_mod, "sent_tokenize", lambda text: [text] if text else [])
    monkeypatch.setattr(claim_mod, "get_support", lambda premise, hypothesis: 1)

    parser = SimpleNamespace(
        clean_text=None,
        docs=[{"title": "Doc 1", "sent": "Abstract 1"}],
        citations_for_cite_quality=[],
        s_map_groundtruth={"title": "", "abstract": ""},
        folder_path="dummy/0",
    )

    score = ClaimCoverageEvaluator()._calculate(parser, window_size=1)
    assert score == 0.0
