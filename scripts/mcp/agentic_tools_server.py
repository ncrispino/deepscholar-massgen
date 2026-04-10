#!/usr/bin/env python3
"""
MCP Server exposing DeepScholar agentic-search tools only.

Usage (from project root):
    python scripts/mcp/agentic_tools_server.py
    python scripts/mcp/agentic_tools_server.py --tool-mode arxiv
    python scripts/mcp/agentic_tools_server.py --transport sse --port 8081
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Literal

from dotenv import load_dotenv
from fastmcp import FastMCP

# Allow running as `python scripts/mcp/agentic_tools_server.py` from repo root.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from deepscholar_base.configs import Configs
from deepscholar_base.search.agentic_search import (
    AgentContext,
    ToolTypes,
    _read_content,
    _search,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

_DEFAULT_CONFIG_YAML = "configs/deepscholar_base.yaml"
_TOOL_MODE: Literal["arxiv", "web", "both"] = "both"

load_dotenv()

mcp = FastMCP("deepscholar-agentic-tools")


def _load_configs(path: str) -> Configs:
    p = Path(path)
    if p.exists():
        logger.info(f"Loaded config from {p}")
        return Configs.from_yaml(p)
    logger.warning(f"Config not found: {p}; using defaults.")
    return Configs()


_configs = _load_configs(_DEFAULT_CONFIG_YAML)


class _ContextWrapper:
    """Minimal wrapper compatible with internal agentic search helper signatures."""

    def __init__(self, context: AgentContext):
        self.context = context


def _parse_end_date(end_date: Optional[str]) -> Optional[datetime]:
    if not end_date:
        return None
    try:
        return datetime.fromisoformat(end_date)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {end_date!r}. Expected YYYY-MM-DD.") from e


def _build_wrapper(end_date: Optional[str]) -> _ContextWrapper:
    parsed_end_date = _parse_end_date(end_date)
    context = AgentContext(
        configs=_configs,
        end_date=parsed_end_date,
        papers_df=None,
        queries=[],
    )
    return _ContextWrapper(context)


def _ensure_mode_allows(family: Literal["arxiv", "web"]) -> None:
    if _TOOL_MODE == "both":
        return
    if _TOOL_MODE != family:
        raise ValueError(
            f"Tool family {family!r} is disabled by --tool-mode {_TOOL_MODE!r}. "
            f"Use --tool-mode both to enable all agentic tools."
        )


@mcp.tool()
def get_agentic_tool_mode() -> str:
    """Return current tool-mode and enabled tools."""
    enabled = {
        "arxiv": _TOOL_MODE in ("arxiv", "both"),
        "web": _TOOL_MODE in ("web", "both"),
    }
    return json.dumps(
        {
            "tool_mode": _TOOL_MODE,
            "enabled": enabled,
            "tools": {
                "arxiv": ["search_arxiv", "read_arxiv_abstracts"],
                "web": ["search_web", "read_webpage_full_text"],
            },
        }
    )


@mcp.tool()
async def search_arxiv(queries: list[str], end_date: Optional[str] = None) -> str:
    """
    Search arXiv using DeepScholar agentic search implementation.

    Args:
        queries: arXiv search queries.
        end_date: Optional YYYY-MM-DD cutoff.
    """
    _ensure_mode_allows("arxiv")
    wrapper = _build_wrapper(end_date)
    return await _search(wrapper, ToolTypes.ARXIV, queries)


@mcp.tool()
async def search_web(queries: list[str], end_date: Optional[str] = None) -> str:
    """
    Search the web (Tavily) using DeepScholar agentic search implementation.

    Args:
        queries: web search queries.
        end_date: Optional YYYY-MM-DD cutoff.
    """
    _ensure_mode_allows("web")
    wrapper = _build_wrapper(end_date)
    return await _search(wrapper, ToolTypes.WEB, queries)


@mcp.tool()
async def read_arxiv_abstracts(
    paper_ids: list[str], end_date: Optional[str] = None
) -> str:
    """
    Read arXiv abstracts/full text snippets for provided arXiv IDs.

    Args:
        paper_ids: arXiv identifiers.
        end_date: Optional YYYY-MM-DD cutoff.
    """
    _ensure_mode_allows("arxiv")
    wrapper = _build_wrapper(end_date)
    return await _read_content(wrapper, ToolTypes.ARXIV, paper_ids)


@mcp.tool()
async def read_webpage_full_text(
    urls: list[str], end_date: Optional[str] = None
) -> str:
    """
    Read webpage full text for provided URLs.

    Args:
        urls: URLs to extract.
        end_date: Optional YYYY-MM-DD cutoff.
    """
    _ensure_mode_allows("web")
    wrapper = _build_wrapper(end_date)
    return await _read_content(wrapper, ToolTypes.WEB, urls)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="MCP Server exposing DeepScholar agentic-search tools only"
    )
    parser.add_argument(
        "--config",
        default=_DEFAULT_CONFIG_YAML,
        help=f"Path to YAML config file (default: {_DEFAULT_CONFIG_YAML})",
    )
    parser.add_argument(
        "--tool-mode",
        choices=["arxiv", "web", "both"],
        default="both",
        help="Which tool family to expose (default: both).",
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="Transport mode (default: stdio)",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host for SSE/HTTP transport (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8081,
        help="Port for SSE/HTTP transport (default: 8081)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    _TOOL_MODE = args.tool_mode

    # Re-load configs if a non-default path was given
    if args.config != _DEFAULT_CONFIG_YAML:
        _configs = _load_configs(args.config)

    # If tool mode disables web, keep behavior explicit in config too.
    if _TOOL_MODE == "arxiv":
        _configs.enable_web_search = False
    elif _TOOL_MODE in ("web", "both"):
        _configs.enable_web_search = True

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
