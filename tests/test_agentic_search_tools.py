import asyncio
import logging
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

# Ensure the project package wins over tests/deepscholar_base.py module shadowing.
_TESTS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _TESTS_DIR.parent
sys.path = [p for p in sys.path if Path(p).resolve() != _TESTS_DIR]
sys.path.insert(0, str(_PROJECT_ROOT))
shadowed = sys.modules.get("deepscholar_base")
if shadowed is not None and str(getattr(shadowed, "__file__", "")).endswith("tests/deepscholar_base.py"):
    del sys.modules["deepscholar_base"]

from deepscholar_base.search import agentic_search  # noqa: E402
from deepscholar_base.search.agentic_search import AgentContext, ToolTypes  # noqa: E402


class _DummyConfigs:
    def __init__(self):
        self.logger = logging.getLogger("test_agentic_search")
        self.per_query_max_search_results_count = 10
        self.max_search_retries = 3


class _DummyWrapper:
    def __init__(self):
        self.context = AgentContext(
            configs=_DummyConfigs(), end_date=None, papers_df=None, queries=[]
        )


def test_search_handles_none_papers_df(monkeypatch):
    async def _fake_handle_one_search_query(*_args, **_kwargs):
        return "=== QUERY 1: test ===\nNo results found.", None

    monkeypatch.setattr(
        agentic_search, "_handle_one_search_query", _fake_handle_one_search_query
    )

    wrapper = _DummyWrapper()
    result = asyncio.run(agentic_search._search(wrapper, ToolTypes.ARXIV, ["test"]))

    assert "No results found." in result
    assert wrapper.context.papers_df is None
    assert wrapper.context.queries == [["arxiv_search"]]


def test_read_content_handles_none_papers_df(monkeypatch):
    def _fake_extract_contents(*_args, **_kwargs):
        return (
            "No valid results found.",
            pd.DataFrame(columns=["title", "url", "snippet", "query", "context", "date"]),
        )

    monkeypatch.setattr(agentic_search, "_extract_contents", _fake_extract_contents)

    wrapper = _DummyWrapper()
    result = asyncio.run(
        agentic_search._read_content(wrapper, ToolTypes.ARXIV, ["1234.56789"])
    )

    assert "No valid results found." in result
    assert wrapper.context.papers_df is None
    assert wrapper.context.queries == [["arxiv_read"]]


def test_handle_one_search_query_retries_transient_arxiv_errors(monkeypatch):
    calls = {"count": 0}

    def _fake_web_search(*_args, **_kwargs):
        calls["count"] += 1
        raise RuntimeError("HTTP 500 from arxiv")

    async def _fake_sleep(_seconds):
        return None

    monkeypatch.setattr(agentic_search, "web_search", _fake_web_search)
    monkeypatch.setattr(agentic_search.asyncio, "sleep", _fake_sleep)

    wrapper = _DummyWrapper()
    section, successful = asyncio.run(
        agentic_search._handle_one_search_query(
            wrapper,
            ToolTypes.ARXIV,
            1,
            None,
            "agent-based modeling taxation",
        )
    )

    assert successful is None
    assert calls["count"] == wrapper.context.configs.max_search_retries
    assert "Error searching arxiv for query" in section


def test_handle_one_search_query_arxiv_end_date_sets_valid_start_date(monkeypatch):
    captured: dict = {}

    def _fake_web_search(**kwargs):
        captured.update(kwargs)
        return pd.DataFrame()

    monkeypatch.setattr(agentic_search, "web_search", _fake_web_search)

    wrapper = _DummyWrapper()
    cutoff = datetime(2025, 6, 3, 0, 0)
    section, successful = asyncio.run(
        agentic_search._handle_one_search_query(
            wrapper,
            ToolTypes.ARXIV,
            1,
            cutoff,
            "agent-based modeling taxation",
        )
    )

    assert successful == "agent-based modeling taxation"
    assert "No results found." in section
    assert captured["end_date"] == cutoff
    assert captured["start_date"] == agentic_search.ARXIV_MIN_SUBMITTED_DATE
