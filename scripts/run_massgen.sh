#!/usr/bin/env bash

###############################################################################
# DeepScholar-Bench: MassGen End-to-End Runner
#
# This script runs the MassGen pipeline (generation + eval).
#
# It performs:
#   1. Related-works generation via MassGen direct import (default)
#      or deepscholar_base (compat mode)
#   2. Automated evaluation in eval mode "massgen"
#
# USAGE:
#   ./scripts/run_massgen.sh
#
# OPTIONAL ENV VARS:
#   SKIP_EVAL=true            # Skip evaluation step
#   AUTO_GENERATE_QUERIES=true  # Generate dataset/queries.csv if missing
#   DRY_RUN=true              # Print commands without executing
#   INSTANCES=4               # Parallel generation workers (query sharding)
#   ENGINE=massgen            # massgen | deepscholar
#   MASSGEN_CONFIG=path.yaml  # Optional MassGen config file
#   TUI=true                  # Launch MassGen CLI (interactive/TUI debug mode)
#   TUI_PROMPT="..."          # Prompt to run in TUI mode
#   TUI_QUERY_IDX=0           # Query row index to use when TUI_PROMPT is empty
#   EXPORT_TUI_FOR_EVAL=true  # Export TUI logs into eval-compatible outputs/results/<file_id>
#
# OPTIONAL FLAGS:
#   --dry-run
#   --instances N
#   --engine massgen|deepscholar
#   --massgen-config PATH
#   --tui
#   --prompt "..."
#   --query-idx N
#   --no-tui-export
#   --skip-eval
#   --auto-generate-queries
#   --help
###############################################################################

set -euo pipefail

DATASET_DIR="${DATASET_DIR:-./dataset}"
RESULTS_DIR="${RESULTS_DIR:-./outputs/results}"
EVAL_DIR="${EVAL_DIR:-./outputs/evaluation}"

DEEPSCHOLAR_CONFIG="${DEEPSCHOLAR_CONFIG:-configs/deepscholar_base.yaml}"
EVAL_CONFIG="${EVAL_CONFIG:-configs/eval.yaml}"
SKIP_EVAL="${SKIP_EVAL:-false}"
AUTO_GENERATE_QUERIES="${AUTO_GENERATE_QUERIES:-true}"
DRY_RUN="${DRY_RUN:-false}"
INSTANCES="${INSTANCES:-1}"
ENGINE="${ENGINE:-massgen}"
MASSGEN_CONFIG="${MASSGEN_CONFIG:-configs/massgen.config.yaml}"
TUI="${TUI:-false}"
TUI_PROMPT="${TUI_PROMPT:-}"
TUI_QUERY_IDX="${TUI_QUERY_IDX:-0}"
EXPORT_TUI_FOR_EVAL="${EXPORT_TUI_FOR_EVAL:-true}"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/run_massgen.sh [options]

Options:
  --instances N              Run generation with N parallel workers (query sharding)
  --engine NAME              Generation engine: massgen (default) or deepscholar
  --massgen-config PATH      Optional MassGen YAML config (used when --engine massgen)
  --tui                      Launch MassGen CLI in interactive/TUI debug mode
  --prompt "TEXT"            Prompt to use in TUI mode (defaults to query at --query-idx)
  --query-idx N              Query row index used for TUI mode when --prompt is omitted
  --no-tui-export            Do not export TUI logs into eval-compatible outputs/results/<file_id>
  --dry-run                  Print commands and planned shards without executing
  --skip-eval                Skip evaluation step
  --auto-generate-queries    Generate dataset/queries.csv if missing
  --help                     Show this help message

Environment overrides:
  DATASET_DIR, RESULTS_DIR, EVAL_DIR, DEEPSCHOLAR_CONFIG, EVAL_CONFIG, MASSGEN_CONFIG
  SKIP_EVAL, AUTO_GENERATE_QUERIES, DRY_RUN, INSTANCES, ENGINE, TUI, TUI_PROMPT, TUI_QUERY_IDX
  EXPORT_TUI_FOR_EVAL
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --instances)
      INSTANCES="${2:-}"
      shift 2
      ;;
    --engine)
      ENGINE="${2:-}"
      shift 2
      ;;
    --massgen-config)
      MASSGEN_CONFIG="${2:-}"
      shift 2
      ;;
    --tui)
      TUI=true
      shift
      ;;
    --prompt)
      TUI_PROMPT="${2:-}"
      shift 2
      ;;
    --query-idx)
      TUI_QUERY_IDX="${2:-}"
      shift 2
      ;;
    --no-tui-export)
      EXPORT_TUI_FOR_EVAL=false
      shift
      ;;
    --skip-eval)
      SKIP_EVAL=true
      shift
      ;;
    --auto-generate-queries)
      AUTO_GENERATE_QUERIES=true
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: Unknown option: $1"
      usage
      exit 1
      ;;
  esac
done

to_lower() {
  echo "$1" | tr '[:upper:]' '[:lower:]'
}

SKIP_EVAL="$(to_lower "$SKIP_EVAL")"
AUTO_GENERATE_QUERIES="$(to_lower "$AUTO_GENERATE_QUERIES")"
DRY_RUN="$(to_lower "$DRY_RUN")"
ENGINE="$(to_lower "$ENGINE")"
TUI="$(to_lower "$TUI")"
EXPORT_TUI_FOR_EVAL="$(to_lower "$EXPORT_TUI_FOR_EVAL")"

if [[ ! "$INSTANCES" =~ ^[1-9][0-9]*$ ]]; then
  echo "ERROR: INSTANCES must be a positive integer, got: $INSTANCES"
  exit 1
fi

if [[ ! "$TUI_QUERY_IDX" =~ ^[0-9]+$ ]]; then
  echo "ERROR: TUI_QUERY_IDX must be a non-negative integer, got: $TUI_QUERY_IDX"
  exit 1
fi

if [[ "$ENGINE" != "massgen" && "$ENGINE" != "deepscholar" ]]; then
  echo "ERROR: ENGINE must be one of: massgen, deepscholar (got: $ENGINE)"
  exit 1
fi

if [[ "$ENGINE" == "massgen" && -n "$MASSGEN_CONFIG" && ! -f "$MASSGEN_CONFIG" ]]; then
  echo "ERROR: MASSGEN_CONFIG file not found: $MASSGEN_CONFIG"
  exit 1
fi

print_cmd() {
  printf '+ '
  printf '%q ' "$@"
  echo
}

run_cmd() {
  if [[ "$DRY_RUN" == "true" ]]; then
    print_cmd "$@"
  else
    "$@"
  fi
}

lookup_query_by_index() {
  local csv_path="$1"
  local query_idx="$2"
  QUERY_CSV_PATH="$csv_path" QUERY_INDEX="$query_idx" python - <<'PY'
import csv
import os
import sys

path = os.environ["QUERY_CSV_PATH"]
idx = int(os.environ["QUERY_INDEX"])

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

if idx < 0 or idx >= len(rows):
    print(
        f"ERROR: --query-idx {idx} is out of range for {path} (rows: {len(rows)}).",
        file=sys.stderr,
    )
    sys.exit(2)

query = rows[idx].get("query", "")
if query:
    print(query)
    sys.exit(0)

row = rows[idx]
abstract = (row.get("abstract") or "").strip()
published_date = (row.get("published_date") or "").strip()
if abstract and published_date:
    template = (
        "Your task is to write a Related Works section for an academic paper given the paper's abstract. "
        "Your response should provide the Related Works section and references. "
        "Only include references from arXiv that are published before {cutoff_date}. "
        "Mention them in a separate, numbered reference list at the end and use the reference numbers to provide "
        "in-line citations in the Related Works section for all claims referring to a source (e.g., description of source [3]. "
        "Further details [6][7][8][9][10].) Each in-line citation must consist of a single reference number within a pair of brackets. "
        "Do not use any other citation format. Do not exceed 600 words for the related works section. "
        "Here is the paper abstract: {abstract}"
    )
    print(template.format(cutoff_date=published_date, abstract=abstract))
    sys.exit(0)

print(
    f"ERROR: Row {idx} in {path} has neither 'query' nor ('abstract' + 'published_date') fields.",
    file=sys.stderr,
)
sys.exit(3)

PY
}

list_massgen_log_dirs() {
  if [[ ! -d ".massgen/massgen_logs" ]]; then
    return 0
  fi
  find .massgen/massgen_logs -mindepth 1 -maxdepth 1 -type d -name "log_*" | sort
}

# TUI mode short-circuit:
# interactive debugging should not require full dataset/eval prerequisites.
if [[ "$TUI" == "true" ]]; then
  if [[ "$ENGINE" != "massgen" ]]; then
    echo "ERROR: --tui is only supported with --engine massgen."
    exit 1
  fi

  if [[ "$SKIP_EVAL" == "false" ]]; then
    echo "TUI mode note: forcing SKIP_EVAL=true because interactive runs do not emit eval-ready output folders."
    SKIP_EVAL="true"
  fi

  echo "Running MassGen generation..."
  echo "  Engine:             $ENGINE"
  echo "  MassGen config:     ${MASSGEN_CONFIG:-<none>}"
  echo "  TUI mode:           $TUI"
  echo "  Worker instances:   $INSTANCES"
  echo "  Dry run:            $DRY_RUN"
  echo "  Export for eval:    $EXPORT_TUI_FOR_EVAL"

  TUI_PROMPT_FROM_DATASET="false"
  if [[ -z "$TUI_PROMPT" ]]; then
    if [[ -f "$DATASET_DIR/queries.csv" ]]; then
      TUI_PROMPT_SOURCE="$DATASET_DIR/queries.csv"
    elif [[ -f "$DATASET_DIR/papers_with_related_works.csv" ]]; then
      TUI_PROMPT_SOURCE="$DATASET_DIR/papers_with_related_works.csv"
      echo "TUI mode note: dataset/queries.csv not found; synthesizing prompt from $TUI_PROMPT_SOURCE."
    else
      echo "ERROR: Could not find prompt source."
      echo "       Provide --prompt explicitly, or create dataset/queries.csv,"
      echo "       or ensure dataset/papers_with_related_works.csv exists."
      exit 1
    fi
    TUI_PROMPT="$(lookup_query_by_index "$TUI_PROMPT_SOURCE" "$TUI_QUERY_IDX")"
    echo "Using query index $TUI_QUERY_IDX from $TUI_PROMPT_SOURCE for TUI prompt."
    TUI_PROMPT_FROM_DATASET="true"
  else
    echo "Using prompt provided via --prompt for TUI run."
  fi

  if [[ "$INSTANCES" -gt 1 ]]; then
    echo "WARNING: TUI mode cannot run interactive instances in parallel."
    echo "         Running $INSTANCES TUI session(s) sequentially."
  fi

  for ((i = 1; i <= INSTANCES; i++)); do
    BEFORE_LOGS=""
    AFTER_LOGS=""
    if [[ "$DRY_RUN" != "true" ]]; then
      BEFORE_LOGS="$(list_massgen_log_dirs)"
    fi

    CMD=(uv run massgen --config "$MASSGEN_CONFIG" "$TUI_PROMPT")
    echo "  Launching TUI session $i/$INSTANCES"
    print_cmd "${CMD[@]}"
    if [[ "$DRY_RUN" != "true" ]]; then
      "${CMD[@]}"

      if [[ "$EXPORT_TUI_FOR_EVAL" == "true" ]]; then
        AFTER_LOGS="$(list_massgen_log_dirs)"

        NEW_LOG_DIR=""
        while IFS= read -r log_dir; do
          [[ -z "$log_dir" ]] && continue
          if ! grep -Fxq "$log_dir" <<<"$BEFORE_LOGS"; then
            NEW_LOG_DIR="$log_dir"
          fi
        done <<<"$AFTER_LOGS"

        if [[ -z "$NEW_LOG_DIR" ]]; then
          NEW_LOG_DIR="$(printf '%s\n' "$AFTER_LOGS" | tail -n 1)"
        fi

        if [[ -n "$NEW_LOG_DIR" ]]; then
          if [[ "$TUI_PROMPT_FROM_DATASET" == "true" ]]; then
            FILE_ID="$TUI_QUERY_IDX"
            if [[ "$INSTANCES" -gt 1 ]]; then
              FILE_ID=$((TUI_QUERY_IDX + i - 1))
              echo "TUI export note: using file_id=$FILE_ID for session $i/$INSTANCES."
            fi
          else
            FILE_ID="$TUI_QUERY_IDX"
            echo "TUI export note: prompt came from --prompt; writing eval files to file_id=$FILE_ID."
            echo "                 Ground-truth comparisons may be less meaningful unless file_id matches that prompt's dataset row."
          fi

          EXPORT_CMD=(
            python -m massgen_runner.export_tui_log
            --log-dir "$NEW_LOG_DIR"
            --output-folder "$RESULTS_DIR"
            --file-id "$FILE_ID"
          )
          print_cmd "${EXPORT_CMD[@]}"
          "${EXPORT_CMD[@]}"
        else
          echo "WARNING: Could not find a MassGen log directory for this TUI session; skipping eval export."
        fi
      fi
    fi
  done

  echo
  echo "=========================================="
  echo "MassGen Pipeline Complete"
  echo "=========================================="
  echo "Results:    $RESULTS_DIR/"
  echo "Evaluation: skipped (SKIP_EVAL=true)"
  echo "=========================================="
  exit 0
fi

if [[ ! -d "$DATASET_DIR" ]]; then
  echo "ERROR: Dataset directory does not exist: $DATASET_DIR"
  echo "       Generate it via data_pipeline first."
  exit 1
fi

if [[ ! -f "$DATASET_DIR/papers_with_related_works.csv" ]]; then
  echo "ERROR: $DATASET_DIR/papers_with_related_works.csv not found."
  exit 1
fi

if [[ ! -f "$DATASET_DIR/queries.csv" ]]; then
  if [[ "$AUTO_GENERATE_QUERIES" == "true" ]]; then
    echo "dataset/queries.csv not found. Auto-generating from papers_with_related_works.csv..."
    run_cmd python -m data_pipeline.generate_queries \
      --input "$DATASET_DIR/papers_with_related_works.csv" \
      --output "$DATASET_DIR/queries.csv"
  else
    echo "ERROR: $DATASET_DIR/queries.csv not found."
    echo "       Set AUTO_GENERATE_QUERIES=true or generate it manually."
    exit 1
  fi
fi

if [[ ! -f "$DATASET_DIR/important_citations.csv" ]]; then
  echo "ERROR: $DATASET_DIR/important_citations.csv not found."
  exit 1
fi

if [[ ! -d "$DATASET_DIR/gt_nuggets_outputs" ]]; then
  echo "ERROR: $DATASET_DIR/gt_nuggets_outputs directory not found."
  exit 1
fi

mkdir -p "$RESULTS_DIR"
mkdir -p "$EVAL_DIR"

QUERIES_CSV_PATH="$DATASET_DIR/queries.csv"
QUERY_COUNT_SOURCE="$QUERIES_CSV_PATH"
if [[ ! -f "$QUERIES_CSV_PATH" ]]; then
  if [[ "$DRY_RUN" == "true" && "$AUTO_GENERATE_QUERIES" == "true" ]]; then
    QUERY_COUNT_SOURCE="$DATASET_DIR/papers_with_related_works.csv"
    echo "DRY_RUN note: $QUERIES_CSV_PATH does not exist yet; estimating shard count from $QUERY_COUNT_SOURCE."
  else
    echo "ERROR: $QUERIES_CSV_PATH not found."
    exit 1
  fi
fi

TOTAL_QUERIES="$(
  QUERY_COUNT_SOURCE="$QUERY_COUNT_SOURCE" python - <<'PY'
import csv
import os

path = os.environ["QUERY_COUNT_SOURCE"]
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)  # header
    print(sum(1 for _ in reader))
PY
)"

if [[ "$TOTAL_QUERIES" -le 0 ]]; then
  echo "ERROR: No queries found in $QUERIES_CSV_PATH"
  exit 1
fi

ACTIVE_INSTANCES="$INSTANCES"
if [[ "$ACTIVE_INSTANCES" -gt "$TOTAL_QUERIES" ]]; then
  ACTIVE_INSTANCES="$TOTAL_QUERIES"
  echo "Reducing instances to $ACTIVE_INSTANCES (number of queries)."
fi

echo "Running MassGen generation..."
echo "  Engine:             $ENGINE"
if [[ "$ENGINE" == "massgen" ]]; then
  echo "  MassGen config:     ${MASSGEN_CONFIG:-<none>}"
fi
echo "  TUI mode:           $TUI"
echo "  Total queries:      $TOTAL_QUERIES"
echo "  Worker instances:   $ACTIVE_INSTANCES"
echo "  Dry run:            $DRY_RUN"

if [[ "$ACTIVE_INSTANCES" -eq 1 ]]; then
  if [[ "$ENGINE" == "massgen" ]]; then
    CMD=(
      python -m massgen_runner.main
      --queries-file "$DATASET_DIR/queries.csv"
      --output-folder "$RESULTS_DIR"
    )
    if [[ -n "$MASSGEN_CONFIG" ]]; then
      CMD+=(--massgen-config "$MASSGEN_CONFIG")
    fi
  else
    CMD=(
      python -m deepscholar_base.main
      --queries-file "$DATASET_DIR/queries.csv"
      --output-folder "$RESULTS_DIR"
      --config-yaml "$DEEPSCHOLAR_CONFIG"
    )
  fi
  run_cmd "${CMD[@]}"
else
  CHUNK_SIZE=$(( (TOTAL_QUERIES + ACTIVE_INSTANCES - 1) / ACTIVE_INSTANCES ))
  declare -a PIDS=()

  for ((i = 0; i < ACTIVE_INSTANCES; i++)); do
    START_IDX=$(( i * CHUNK_SIZE ))
    END_IDX=$(( START_IDX + CHUNK_SIZE ))
    if [[ "$START_IDX" -ge "$TOTAL_QUERIES" ]]; then
      break
    fi
    if [[ "$END_IDX" -gt "$TOTAL_QUERIES" ]]; then
      END_IDX="$TOTAL_QUERIES"
    fi

    if [[ "$ENGINE" == "massgen" ]]; then
      CMD=(
        python -m massgen_runner.main
        --queries-file "$DATASET_DIR/queries.csv"
        --output-folder "$RESULTS_DIR"
        --start-idx "$START_IDX"
        --end-idx "$END_IDX"
      )
      if [[ -n "$MASSGEN_CONFIG" ]]; then
        CMD+=(--massgen-config "$MASSGEN_CONFIG")
      fi
    else
      CMD=(
        python -m deepscholar_base.main
        --queries-file "$DATASET_DIR/queries.csv"
        --output-folder "$RESULTS_DIR"
        --config-yaml "$DEEPSCHOLAR_CONFIG"
        --start-idx "$START_IDX"
        --end-idx "$END_IDX"
      )
    fi

    echo "  Instance $((i + 1)) shard: [$START_IDX, $END_IDX)"
    if [[ "$DRY_RUN" == "true" ]]; then
      print_cmd "${CMD[@]}"
    else
      "${CMD[@]}" &
      PIDS+=("$!")
    fi
  done

  if [[ "$DRY_RUN" != "true" ]]; then
    FAILURES=0
    for pid in "${PIDS[@]}"; do
      if ! wait "$pid"; then
        FAILURES=$((FAILURES + 1))
      fi
    done
    if [[ "$FAILURES" -gt 0 ]]; then
      echo "ERROR: $FAILURES generation worker(s) failed."
      exit 1
    fi
  fi
fi

if [[ "$SKIP_EVAL" == "false" ]]; then
  echo "Running MassGen evaluation..."
  run_cmd python -m eval.main \
    --modes massgen \
    --evals all \
    --input-folder "$RESULTS_DIR" \
    --output-folder "$EVAL_DIR" \
    --dataset-path "$DATASET_DIR/papers_with_related_works.csv" \
    --important-citations-path "$DATASET_DIR/important_citations.csv" \
    --nugget-groundtruth-dir-path "$DATASET_DIR/gt_nuggets_outputs" \
    --config-yaml "$EVAL_CONFIG"
fi

echo
echo "=========================================="
echo "MassGen Pipeline Complete"
echo "=========================================="
echo "Results:    $RESULTS_DIR/"
if [[ "$SKIP_EVAL" == "false" ]]; then
  echo "Evaluation: $EVAL_DIR/"
else
  echo "Evaluation: skipped (SKIP_EVAL=true)"
fi
echo "=========================================="
