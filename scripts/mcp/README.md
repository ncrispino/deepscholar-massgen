# DeepScholar-Base MCP Server

Exposes the DeepScholar-Base pipeline as a single MCP tool (`run_deepscholar_base`) via [FastMCP](https://github.com/jlowin/fastmcp).

Also includes a dedicated **agentic tools** MCP server that exposes only search/read primitives:
- `search_arxiv`
- `read_arxiv_abstracts`
- `search_web`
- `read_webpage_full_text`

## Installation

From the **project root** (e.g. `deepscholar-bench/`):

```bash
# Install main project dependencies and MCP server deps
uv pip install -r requirements.txt --overrides requirements-overrides.txt
uv pip install -r scripts/mcp/requirements.txt
```

Ensure your environment is activated (e.g. `conda activate dsbench`) and that a `.env` with `OPENAI_API_KEY` and `TAVILY_API_KEY` exists in the project root.

## Running the Server

Run the server from the **project root** so that `configs/` and `deepscholar_base` resolve correctly.

```bash
# From project root
cd /path/to/deepscholar-bench

# Stdio (default — for Claude Desktop, Cursor, etc.)
python scripts/mcp/server.py

# SSE transport (for HTTP clients)
python scripts/mcp/server.py --transport sse --port 8080

# Streamable HTTP
python scripts/mcp/server.py --transport streamable-http --port 8080

# Custom config
python scripts/mcp/server.py --config path/to/my_config.yaml

# All options
python scripts/mcp/server.py --help
```

### Agentic Tools Server (search/read only)

```bash
# Expose all four tools
python scripts/mcp/agentic_tools_server.py

# ArXiv-only mode (web tools disabled)
python scripts/mcp/agentic_tools_server.py --tool-mode arxiv

# Web-only mode (arXiv tools disabled)
python scripts/mcp/agentic_tools_server.py --tool-mode web

# SSE transport
python scripts/mcp/agentic_tools_server.py --transport sse --port 8081
```


## Configuration

The server reuses the same YAML config as `deepscholar_base/main.py`. The default is `configs/deepscholar_base.yaml` in the project root. Override any setting there (model, search mode, filters, etc.).

```yaml
# configs/deepscholar_base.yaml
lm:
  model: gpt-4o
  temperature: 1.0
  max_tokens: 10000

search_mode: agentic
enable_web_search: true
final_max_results_count: 30
```

## Tool: `run_deepscholar_base`

Runs the full DeepScholar-Base pipeline (search → filter → taxonomize → generate report).

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `topic` | string | yes | Research topic, question, or paper abstract |
| `end_date` | string | no | Paper cutoff date in `YYYY-MM-DD` format |

**Returns:** JSON string with three keys:

```json
{
  "final_report": "# Related Works\n...",
  "papers": [
    {"title": "...", "url": "...", "snippet": "...", ...}
  ],
  "stats": {"search_time": 12.3, "num_papers_found": 47, ...}
}
```

## Agentic Tools and Modes

`scripts/mcp/agentic_tools_server.py` exposes only the function-level agentic search tools from `deepscholar_base/search/agentic_search.py`.

Tool families:
- `arxiv`: `search_arxiv`, `read_arxiv_abstracts`
- `web`: `search_web`, `read_webpage_full_text`

Mode controls:
- `--tool-mode both` (default): all 4 tools enabled
- `--tool-mode arxiv`: only arXiv tools enabled
- `--tool-mode web`: only web tools enabled

Calls to a disabled family return a clear error.

### Using with MassGen MCP config

Add a stdio MCP server entry to your MassGen config:

```yaml
agents:
  - id: agent_a
    backend:
      type: openai
      model: gpt-5-mini
      mcp_servers:
        deepscholar_agentic:
          type: stdio
          command: python
          args:
            - scripts/mcp/agentic_tools_server.py
            - --tool-mode
            - both
```

## Testing the Server and Clients

From the project root, with dependencies installed:

1. **Server only** — verify the server starts:
   ```bash
   python scripts/mcp/server.py --help
   ```

2. **Stdio client** — spawns the server and calls the tool (needs `mcp` from `scripts/mcp/requirements.txt`):
   ```bash
   python scripts/mcp/example_clients/client_stdio.py
   ```
   This runs the full pipeline once; ensure `.env` has `OPENAI_API_KEY` and `TAVILY_API_KEY`.

2a. **Agentic arXiv tool isolation (stdio)** — spawns `agentic_tools_server.py` and calls `search_arxiv` directly:
   ```bash
   python scripts/mcp/example_clients/client_agentic_search_arxiv_stdio.py \
     --query "agent-based modeling taxation economic policy economic inequality" \
     --query "optimal income tax saez model heterogenous agents" \
     --end-date 2025-06-03
   ```
   Use this to debug arXiv search behavior outside MassGen orchestration.

3. **SSE client** — start the server in another terminal, then run the client:
   ```bash
   # Terminal 1
   python scripts/mcp/server.py --transport sse --port 8080
   # Terminal 2
   python scripts/mcp/example_clients/client_sse.py
   ```
