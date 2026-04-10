from pathlib import Path
from pydantic import BaseModel, model_validator
import logging
import json
from lotus.models import LM
from pydantic import Field
from lotus import WebSearchCorpus
from lotus.types import ReasoningStrategy
from typing import Any

logger = logging.getLogger("deepscholar_base")


def _normalize_mcp_servers(raw_servers: Any) -> list[dict[str, Any]]:
    """Normalize MCP server configs into a list of dict entries."""
    if raw_servers is None:
        return []
    if isinstance(raw_servers, list):
        out: list[dict[str, Any]] = []
        for idx, server in enumerate(raw_servers):
            if not isinstance(server, dict):
                raise ValueError(f"mcp_servers[{idx}] must be a mapping (dict).")
            out.append(_normalize_single_mcp_server(server))
        return out
    if isinstance(raw_servers, dict):
        # Accept quickstart-style shape:
        # { "server_name": { "command": "...", ... }, ... }
        out = []
        for name, server in raw_servers.items():
            if not isinstance(server, dict):
                raise ValueError(f"mcp_servers[{name!r}] must be a mapping (dict).")
            out.append(_normalize_single_mcp_server({"name": name, **server}))
        return out
    raise ValueError("mcp_servers must be a list or dict.")


def _normalize_single_mcp_server(server: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(server)

    transport = normalized.get("transport", normalized.get("type"))
    if isinstance(transport, str) and transport.strip():
        transport_normalized = transport.strip().lower().replace("_", "-")
    elif normalized.get("command"):
        transport_normalized = "stdio"
    elif normalized.get("url"):
        url = str(normalized.get("url", "")).rstrip("/")
        transport_normalized = "sse" if url.endswith("/sse") else "streamable-http"
    else:
        raise ValueError(
            "Each MCP server must include either `transport` or connection fields "
            "(`command` for stdio, `url` for sse/http)."
        )

    valid_transports = {"stdio", "sse", "streamable-http"}
    if transport_normalized not in valid_transports:
        raise ValueError(
            f"Invalid MCP transport {transport!r}. Expected one of: {sorted(valid_transports)}."
        )
    normalized["transport"] = transport_normalized
    return normalized


def _load_mcp_servers_from_path(path: str | Path) -> list[dict[str, Any]]:
    cfg_path = Path(path).expanduser()
    if not cfg_path.exists():
        raise FileNotFoundError(f"MCP config file not found: {cfg_path}")
    with open(cfg_path) as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"MCP config at {cfg_path} must be a JSON object.")

    # Preferred shape matches popular MCP quickstart configs:
    # { "mcpServers": { "name": { ... } } }
    if "mcpServers" in data:
        return _normalize_mcp_servers(data["mcpServers"])
    if "mcp_servers" in data:
        return _normalize_mcp_servers(data["mcp_servers"])
    # Fallback: treat top-level mapping as server map.
    return _normalize_mcp_servers(data)


class Configs(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    logger: logging.Logger

    use_agentic_search: bool = True
    max_search_retries: int = 3
    use_structured_output: bool = True

    # Common for both agentic and recursive search
    enable_web_search: bool = True
    per_query_max_search_results_count: int = 10

    # Only for agentic search
    use_responses_model: bool | None = None
    # External MCP tools consumed by the agentic search runtime.
    # Supports either inline YAML (mcp_servers) or quickstart JSON (mcp_config_path).
    mcp_servers: list[dict[str, Any]] = Field(default_factory=list)
    mcp_config_path: str | None = None
    allowed_tools: list[str] = Field(default_factory=list)
    exclude_tools: list[str] = Field(default_factory=list)

    # Only for recursive search
    num_search_steps: int = 3
    num_search_queries_per_step_per_corpus: int = 2
    web_corpuses: list[WebSearchCorpus] = Field(
        default_factory=lambda: [WebSearchCorpus.TAVILY]
    )
    
    # Filtering configs
    use_sem_filter: bool = True
    use_sem_topk: bool = True
    final_max_results_count: int = 30
    # Defaulted in initialize_sem_filter_kwargs and initialize_sem_topk_kwargs
    sem_filter_kwargs: dict[str, Any]
    sem_topk_kwargs: dict[str, Any]

    # Taxonomization configs
    categorize_references: bool = True
    generate_category_summary: bool = True

    # Generation configs
    generate_insights: bool = True

    # LM configs (defaulted in initialize_lms)
    filter_lm: LM
    search_lm: LM
    taxonomize_lm: LM
    generation_lm: LM

    @model_validator(mode="before")
    def initialize_logger(value: dict[str, Any]):
        if not value.get("logger"):
            value["logger"] = logger
        return value

    @model_validator(mode="before")
    def resolve_web_corpuses(value: dict[str, Any]):
        """Model validator for web_corpuses to ensure proper enum conversion."""
        raw = value.get("web_corpuses")
        if raw is None:
            value["web_corpuses"] = [WebSearchCorpus.TAVILY]
        elif isinstance(raw, list):
            out = []
            for item in raw:
                if isinstance(item, WebSearchCorpus):
                    out.append(item)
                else:
                    out.append(WebSearchCorpus[item.upper()] if isinstance(item, str) else item)
            value["web_corpuses"] = out
        else:
            value["web_corpuses"] = [WebSearchCorpus.TAVILY]
        return value

    @model_validator(mode="before")
    def resolve_mcp_servers(value: dict[str, Any]):
        if not isinstance(value, dict):
            return value
        raw_servers = value.get("mcp_servers")
        normalized_servers = _normalize_mcp_servers(raw_servers)

        config_path = value.get("mcp_config_path")
        if config_path:
            normalized_servers.extend(_load_mcp_servers_from_path(config_path))
        value["mcp_servers"] = normalized_servers
        return value

    @model_validator(mode="before")
    def initialize_sem_filter_kwargs(value: dict[str, Any]):
        # Default to COT reasoning and return explanations
        value["sem_filter_kwargs"] = {
            "strategy": ReasoningStrategy.COT,
            "return_explanations": True,
            **value.get("sem_filter_kwargs", {}),
        }
        return value

    @model_validator(mode="before")
    def initialize_sem_topk_kwargs(value: dict[str, Any]):
        # Default to COT reasoning and return explanations
        value["sem_topk_kwargs"] = {
            "strategy": ReasoningStrategy.COT,
            "return_explanations": True,
            **value.get("sem_topk_kwargs", {}),
        }
        return value

    @model_validator(mode="before")
    def initialize_lms(value: dict[str, Any]):
        raw_lm = value.get("lm")
        if raw_lm is None:
            configured_lm = LM(model="gpt-5-mini", temperature=1.0, reasoning_effort="low", max_tokens=10000)
        elif isinstance(raw_lm, dict):
            configured_lm = LM(**raw_lm)
            value["lm"] = configured_lm
        else:
            configured_lm = raw_lm
        assert isinstance(configured_lm, LM), "configured_lm must be a Lotus LM"
        configured_lm_kwargs = configured_lm.kwargs
        configured_lm_kwargs.pop("max_completion_tokens")
        for lm_key in ["filter_lm", "search_lm", "taxonomize_lm", "generation_lm"]:
            existing = value.get(lm_key)
            if existing is None:
                value[lm_key] = LM(
                    model=configured_lm.model,
                    max_ctx_len=configured_lm.max_ctx_len,
                    max_batch_size=configured_lm.max_batch_size,
                    rate_limit=configured_lm.rate_limit,
                    tokenizer=configured_lm.tokenizer,
                    cache=configured_lm.cache,
                    physical_usage_limit=configured_lm.physical_usage_limit,
                    virtual_usage_limit=configured_lm.virtual_usage_limit,
                    **configured_lm_kwargs,
                )
            elif isinstance(existing, dict):
                value[lm_key] = LM(**existing)
        return value

    @classmethod
    def from_yaml(cls, path: str | Path) -> "Configs":
        """Load Configs from a YAML file.

        LM may be given as a dict; all stage LMs (filter_lm, search_lm, etc.) are
        derived from it if not set. Example YAML:

          lm:
            model: gpt-4o
            temperature: 1.0
            max_tokens: 10000
          search_mode: agentic
          enable_web_search: true
          web_corpuses: [TAVILY, ARXIV]
          mcp_servers:
            - name: weather
              type: stdio
              command: npx
              args: ["-y", "@modelcontextprotocol/server-weather"]
        """
        try:
            import yaml
        except ImportError:
            raise ImportError("PyYAML is required for Configs.from_yaml(). Install with: pip install pyyaml")
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        with open(path) as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            raise ValueError("YAML config must be a mapping (dict).")

        mcp_config_path = data.get("mcp_config_path")
        if isinstance(mcp_config_path, str) and mcp_config_path:
            mcp_path = Path(mcp_config_path)
            if not mcp_path.is_absolute():
                data["mcp_config_path"] = str((path.parent / mcp_path).resolve())
        
        if data.get("search_mode") == "agentic":
            data["use_agentic_search"] = True
        elif data.get("search_mode") == "recursive":
            data["use_agentic_search"] = False
        elif data.get("search_mode") is None:
            data["use_agentic_search"] = True
        else:
            raise ValueError(f"Invalid search mode: {data.get('search_mode')}")
        return cls(**data)

    def log(self):
        model_dump = self.model_dump(
            mode="json",
            exclude={"logger", "search_lm", "taxonomize_lm", "generation_lm", "filter_lm"},
        )
        for lm in ["search_lm", "taxonomize_lm", "generation_lm", "filter_lm"]:
            lm_instance = getattr(self, lm)
            model_dump[lm] = {
                "model": lm_instance.model,
                "max_ctx_len": lm_instance.max_ctx_len,
                "kwargs": lm_instance.kwargs,
            }
        return model_dump
