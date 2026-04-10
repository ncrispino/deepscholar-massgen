#!/usr/bin/env python3
"""
Run the agentic-tools MCP server in stdio mode and call `search_arxiv` directly.

Use this to isolate/debug MCP tool behavior outside MassGen orchestration.

Examples (run from project root):
  python scripts/mcp/example_clients/client_agentic_search_arxiv_stdio.py \
    --query "agent-based modeling taxation economic policy economic inequality" \
    --query "optimal income tax saez model heterogenous agents" \
    --end-date 2025-06-03

  python scripts/mcp/example_clients/client_agentic_search_arxiv_stdio.py \
    --tool-mode arxiv \
    --server-config configs/deepscholar_base.yaml \
    --query "llm multi-agent system policy design"
"""

import argparse
import asyncio
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Project root (parent of scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def _content_text(result) -> str:
    parts: list[str] = []
    for item in getattr(result, "content", []) or []:
        text = getattr(item, "text", None)
        if isinstance(text, str) and text:
            parts.append(text)
    return "\n".join(parts).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Debug `search_arxiv` via agentic-tools MCP stdio server."
    )
    parser.add_argument(
        "--query",
        action="append",
        required=True,
        help="ArXiv query string. Repeat flag for multiple queries.",
    )
    parser.add_argument(
        "--end-date",
        default=None,
        help="Optional cutoff date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--tool-mode",
        choices=["arxiv", "web", "both"],
        default="arxiv",
        help="Tool mode to pass to agentic_tools_server.py (default: arxiv).",
    )
    parser.add_argument(
        "--server-config",
        default="configs/deepscholar_base.yaml",
        help="Config path passed to agentic_tools_server.py --config.",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    server_args = [
        "scripts/mcp/agentic_tools_server.py",
        "--tool-mode",
        args.tool_mode,
        "--config",
        args.server_config,
    ]
    server_params = StdioServerParameters(
        command="python",
        args=server_args,
        cwd=str(PROJECT_ROOT),
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            mode_result = await session.call_tool("get_agentic_tool_mode", {})
            print("=== Tool Mode ===")
            print(_content_text(mode_result))
            print()

            payload: dict = {"queries": args.query}
            if args.end_date:
                payload["end_date"] = args.end_date

            result = await session.call_tool("search_arxiv", payload)
            print("=== search_arxiv result ===")
            print(_content_text(result))


if __name__ == "__main__":
    asyncio.run(main())
