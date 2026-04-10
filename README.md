<h1 align="center"> 
    🌐🔍DeepScholar-Bench: Build and Benchmark Generative Research Synthesis
</h1>


<!-- [![Dataset](https://img.shields.io/badge/Dataset-deepscholar--bench%2FDeepScholarBench-blue)](https://huggingface.co/datasets/deepscholar-bench/DeepScholarBench)
[![GitHub](https://img.shields.io/badge/GitHub-deepscholar--bench-green)](https://github.com/guestrin-lab/deepscholar-bench)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://github.com/guestrin-lab/deepscholar-bench/blob/main/LICENSE)
[![Leaderboard](https://img.shields.io/badge/Leaderboard-DeepScholar%20Bench-orange)](https://guestrin-lab.github.io/deepscholar-leaderboard/leaderboard/deepscholar_bench_leaderboard.html)
-->

<!-- **📊 Dataset**: [deepscholar-bench/DeepScholarBench](https://huggingface.co/datasets/deepscholar-bench/DeepScholarBench)  
**🔗 GitHub**: [guestrin-lab/deepscholar-bench](https://github.com/guestrin-lab/deepscholar-bench)
**🏆 Leaderboard**: [DeepScholar Bench Leaderboard](https://guestrin-lab.github.io/deepscholar-leaderboard/leaderboard/deepscholar_bench_leaderboard.html) -->


<p align="center">
<a href="https://guestrin-lab.github.io/deepscholar-leaderboard/leaderboard/deepscholar_bench_leaderboard.html"><b> 🏆 Live Leaderboard</b></a> | <a href="https://deep-scholar.vercel.app"><b> 🤖 DeepScholar Live Preview </b></a> 
</p>

<p align="center">
<a href="https://huggingface.co/datasets/deepscholar-bench/DeepScholarBench"><b> 📊 Dataset </b></a> | <a href="https://arxiv.org/abs/2508.20033"><b>📄 Paper</b></a> | <a href="https://discord.gg/ZWQBurm5bt"><b> 🎮Discord </b></a>
</p>

---

DeepScholar-Bench provides a live benchmark dataset and holistic evaluation of generative research synthesis, an emerging capability among AI systems designed for DeepResearch. We also developed DeepScholar-base, a strong open-source reference pipeline/

This repository provides:
1. **[Dataset Scripts](data_pipeline/README.md)** - which allow you to collect new datasets from recent, high-quality Arxiv papers using our automated data-collection pipeline. You can set your own configurations (e.g., choice of valid date ranges and valid Arxiv domains) to customize your dataset
2. **[An Evaluation Suite](eval/README.md)** - for measuring performance of long-form research synthesis answers. Our evaluation framework supports a holistic set of metrics, which demonstrate high agreement with human annotations. Our eval suite is built using the [LOTUS framework for LLM-based data processing](https://github.com/lotus-data/lotus), which  provides a library for LLM-based evaluations and can be used directly to instantiate [your custom LLM-judges](https://lotus-ai.readthedocs.io/en/latest/evals.html#).
3. **[DeepScholar-base](deepscholar_base/README.md)** - our open-source reference pipeline for generative research synthesis. It is built on top of the [LOTUS framework](https://github.com/lotus-data/lotus), which introduces and serves semantic operators for LLM-powered data processing. LOTUS' semantic operators provide a rich-set of primitives, providing a superset of RAG that goes beyond search() and LM() calls. On DeepScholar-bench, our reference pipeline achieves competitive performance with OpenAI's DeepResearch, while running 2x faster.

If you run into any problems with the code in this repo, leaderboard, or dataset, please feel free to raise an issue and we will address it promptly. If you would like to add your AI system to the DeepScholar-bench leaderboard, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeug4igDHhVUU3XnrUSeMVRUJFKlHP28i8fcBAu_LHCkqdV1g/viewform).



## 🚀 Quick Start

To get started, make sure you are using Python 3.10, simply clone the repository and install dependencies as follows:

```bash
# Clone the repository
git clone https://github.com/ncrispino/deepscholar-massgen.git
cd deepscholar-massgen

# Install dependencies with uv (recommended)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt --overrides requirements-overrides.txt
uv pip install -r scripts/mcp/requirements.txt  # if using MCP tools

# Set up API keys
cp .env.example .env
# Edit .env and fill in OPENAI_API_KEY, TAVILY_API_KEY, OPENROUTER_API_KEY, etc.
```

Once you have a dataset (can use the dataset in `./dataset/` for testing or generate your own as in [Benchmark Usage](#-benchmark-usage)), you can first test MassGen with
```bash
./scripts/run_massgen.sh --tui --instances 1
```

Then, run the full pipeline—report generation and evaluation—with:

```bash
./scripts/run_massgen.sh
```
Generation results are written to `./outputs/results/` and evaluation results to `./outputs/evaluation/`.

#### Running a Subset with Parallel Workers

To run a specific range of queries (e.g., 0–65) with parallel workers, use `python -m massgen_runner.main` directly with `--start-idx` and `--end-idx`. Each shard writes to a separate subdirectory (`<output-folder>/<file_id>/`), so there's no overlap:

```bash
# 2 parallel shards covering queries 0-65
python -m massgen_runner.main --queries-file dataset/queries.csv --output-folder outputs/results_minimax --massgen-config configs/massgen.config.yaml --start-idx 0 --end-idx 33 &
python -m massgen_runner.main --queries-file dataset/queries.csv --output-folder outputs/results_minimax --massgen-config configs/massgen.config.yaml --start-idx 33 --end-idx 66 &
wait
```

`./scripts/run_all.sh` remains available as a compatibility entrypoint.

Useful options:

```bash
# For TUI example run.
./scripts/run_massgen.sh --dry-run --tui --instances 1

# Preview commands and query shards without running anything
./scripts/run_massgen.sh --engine massgen --dry-run --instances 4

# Run MassGen generation with 4 parallel workers, then run eval
./scripts/run_massgen.sh --engine massgen --instances 4

# Use a custom MassGen config (including MCP servers/tools)
./scripts/run_massgen.sh --engine massgen --massgen-config /path/to/massgen_config.yaml --instances 2

# Compatibility mode: use legacy DeepScholar-Base generation
./scripts/run_massgen.sh --engine deepscholar --instances 4

# Run generation only
./scripts/run_massgen.sh --engine massgen --instances 4 --skip-eval

# Launch MassGen interactive TUI with a custom prompt (debug mode)
./scripts/run_massgen.sh --tui --prompt "Debug this prompt in interactive mode"

# Launch TUI using query row 0 from dataset/queries.csv (or synthesize from papers csv in dry-run)
./scripts/run_massgen.sh --tui --query-idx 0

# Disable automatic export of TUI logs to eval-ready outputs/results/<file_id>
./scripts/run_massgen.sh --tui --query-idx 0 --no-tui-export
```

The default engine is `massgen`, which runs `python -m massgen_runner.main` and calls `massgen.run(...)` directly.
In `--tui` mode, the script runs `massgen --config ... "<prompt>"` and forces `--skip-eval`. If `--instances > 1`, TUI sessions run sequentially.
After each TUI session, `run_massgen.sh` now automatically converts the generated `.massgen/massgen_logs/log_*` run into eval-compatible files under `outputs/results/<file_id>/` (including `intro.md`, `paper.csv`, `stats.json`) so you can run `python -m eval.main` later without rerunning generation.
For eval parsing, `eval/parsers/massgen.py` reads `intro.md` (same convention as DeepScholar-Base).

### 📊 Benchmark Usage
You can start scraping your own datasets and running our holistic, automated evaluation suite using the commands below. For more details and a full introduction, please continue to our **[Dataset Scripts Description](data_pipeline/README.md)** and/or our **[Evaluation library Description](eval/README.md)**.


#### 1. Scraping Data

```bash
# Collect recent AI papers since May 1, 2025
python -m data_pipeline.main \
    --categories cs.AI \
    --start-date 2025-05-01

# Collect by field shorthand (cs, bio, econ, phy, stat)
python -m data_pipeline.main --field cs --field bio --start-date 2025-01-01
```

#### 2. Evaluate Research Generation Systems

##### 2A. TUI Run → Evaluate → Compare With Provided Baselines

Use this path when you want to debug one query interactively, then score it against dataset ground truth and baseline examples in `tests/baselines_results/`.

```bash
# 1) Run a single interactive TUI session on dataset row 0
./scripts/run_massgen.sh --tui --query-idx 0 --instances 1

# TUI note:
# - this skips automatic eval
# - it now auto-exports eval-ready files to outputs/results/0/
#   (intro.md, final_report.md, paper.csv, stats.json)

# 2) Evaluate only this one result (file_id 0)
python -m eval.main \
  --modes massgen \
  --evals all \
  --input-folder outputs/results \
  --file-id 0 \
  --output-folder outputs/evaluation_tui_0 \
  --dataset-path dataset/papers_with_related_works.csv \
  --important-citations-path dataset/important_citations.csv \
  --nugget-groundtruth-dir-path dataset/gt_nuggets_outputs \
  --config-yaml configs/eval.yaml

# 3) Compare the same file_id against the packaged DeepScholar-base example
python -m eval.main \
  --modes massgen deepscholar_base \
  --evals all \
  --input-folder outputs/results tests/baselines_results/deepscholar-base \
  --file-id 0 \
  --output-folder outputs/evaluation_tui_vs_deepscholar_base_0 \
  --dataset-path dataset/papers_with_related_works.csv \
  --important-citations-path dataset/important_citations.csv \
  --nugget-groundtruth-dir-path dataset/gt_nuggets_outputs \
  --config-yaml configs/eval.yaml
```

`file_id` alignment note: in TUI mode, exported outputs are keyed by `--query-idx` (for example, `--query-idx 0` writes `outputs/results/0/`). For apples-to-apples comparison against `tests/baselines_results/*`, use the same `--file-id` in eval commands.

You can also compare against multiple provided baselines (same `file_id`):
```bash
python -m eval.main \
  --modes massgen deepscholar_base openscholar deepresearcher storm SearchAI \
  --evals all \
  --input-folder \
    outputs/results \
    tests/baselines_results/deepscholar-base \
    tests/baselines_results/openscholar \
    tests/baselines_results/deepresearcher \
    tests/baselines_results/storm \
    tests/baselines_results/search_ai_gpt_4.1 \
  --file-id 0 \
  --output-folder outputs/evaluation_tui_vs_all_baselines_0 \
  --dataset-path dataset/papers_with_related_works.csv \
  --important-citations-path dataset/important_citations.csv \
  --nugget-groundtruth-dir-path dataset/gt_nuggets_outputs \
  --config-yaml configs/eval.yaml
```

##### 2B. Headless Automatic Runs (More Queries / More Workers)

Use this path for non-interactive generation and automatic eval over many queries.

```bash
# Full automatic pipeline: generate + eval
./scripts/run_massgen.sh --engine massgen --instances 4

# Generation only (skip eval), useful when planning a combined comparison later
./scripts/run_massgen.sh --engine massgen --instances 4 --skip-eval

# Example: generate MassGen + DeepScholar-base separately, then compare together
RESULTS_DIR=./outputs/results_massgen \
SKIP_EVAL=true \
./scripts/run_massgen.sh --engine massgen --instances 1 --massgen-config configs/massgen.config.yaml

RESULTS_DIR=./outputs/results_deepscholar_base \
SKIP_EVAL=true \
./scripts/run_massgen.sh --engine deepscholar --instances 1

python -m eval.main \
  --modes massgen deepscholar_base \
  --evals all \
  --input-folder ./outputs/results_massgen ./outputs/results_deepscholar_base \
  --output-folder ./outputs/evaluation_compare \
  --dataset-path ./dataset/papers_with_related_works.csv \
  --important-citations-path ./dataset/important_citations.csv \
  --nugget-groundtruth-dir-path ./dataset/gt_nuggets_outputs \
  --config-yaml configs/eval.yaml
```



### 📚 DeepScholar-Base

DeepScholar-Base is our reference pipeline research synthesis pipeline that generates comprehensive literature reviews from a research query. It serves as a strong, open-source baseline and is built on [LOTUS](https://github.com/lotus-data/lotus) for efficient LLM-based data processing. For detailed documentation see the **[DeepScholar Base README](deepscholar_base/README.md)**.

```python
from deepscholar_base import deepscholar_base
from deepscholar_base.configs import Configs
from lotus.models import LM
from datetime import datetime
import asyncio

configs = Configs(lm=LM(model="gpt-4o", temperature=1.0, max_tokens=10000))

async def main():
    final_report, docs_df, stats = await deepscholar_base(
        topic="What are the latest developments in retrieval-augmented generation?",
        end_date=datetime(2025, 1, 1),  # Only papers before this date
        configs=configs,
    )
    print(final_report)

asyncio.run(main())
```


## 🔌 MCP Integration

MassGen consumes MCP tools when they are configured in a MassGen config file and passed to the runner via `--massgen-config`.

```yaml
agents:
  - id: "agent_a"
    backend:
      type: "openai"
      model: "gpt-5-mini"
      mcp_servers:
        weather:
          type: "stdio"
          command: "npx"
          args: ["-y", "@modelcontextprotocol/server-weather"]
    allowed_tools:
      - "mcp__weather__get_current_weather"
    exclude_tools: []
```

Then run:

```bash
./scripts/run_massgen.sh --engine massgen --massgen-config /path/to/massgen_config.yaml
```

DeepScholar-Base can also be exposed as an [MCP (Model Context Protocol)](https://spec.modelcontextprotocol.io/) server for external clients (separate from MassGen runtime tool use). See [scripts/mcp/README.md](scripts/mcp/README.md) for full setup.

```bash
# Start the MCP server (from project root)
python scripts/mcp/server.py

# Search/read tools only (no full pipeline), with mode control:
# --tool-mode both|arxiv|web
python scripts/mcp/agentic_tools_server.py --tool-mode both
```

## 🤝 Contributing

We welcome contributions to DeepScholarBench! Please feel free to submit a PR for code contributions. If you would like to add your AI system to the DeepScholar-bench leaderboard, please fill out this [this form](https://docs.google.com/forms/d/e/1FAIpQLSeug4igDHhVUU3XnrUSeMVRUJFKlHP28i8fcBAu_LHCkqdV1g/viewform).


## Citation
If you use DeepScholar-Bench in an academic work, we would greatly appreciate it if you can cite this work as follows:
```bibtex
@article{patel2025deepscholarbench,
      title={DeepScholar-Bench: A Live Benchmark and Automated Evaluation for Generative Research Synthesis}, 
      author={Liana Patel and Negar Arabzadeh and Harshit Gupta and Ankita Sundar and Ion Stoica and Matei Zaharia and Carlos Guestrin},
      year={2025},
      url={https://arxiv.org/abs/2508.20033}, 
}
```
