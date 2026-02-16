#!/usr/bin/env bash
#
# Minimal DeepScholar-Bench pipeline runner:
#   1. Data collection   -> python -m data_pipeline.main
#   2. Report generation -> python -m deepscholar_base.main
#   3. Evaluation        -> python -m eval.main
#
# Usage: ./run_all.sh [OPTIONS]
#   --output-base DIR
#   --dataset-dir DIR
#   --data-pipeline-config FILE
#   --deepscholar-config FILE
#   --eval-config FILE
#   --scrape-new-data
#   --skip-eval
#   -h | --help

set -e

# Default values
OUTPUT_BASE=""
DATASET_DIR="./dataset"
RESULTS_DIR=""
EVAL_DIR=""
DATA_PIPELINE_CONFIG=""
DEEPSCHOLAR_CONFIG=""
EVAL_CONFIG=""
SCRAPE_NEW_DATA=false
SKIP_EVAL=false

usage() {
  cat <<EOF
Usage: $0 [OPTIONS]

Minimal DeepScholar-Bench pipeline runner.

Options:
  --output-base DIR             Base output directory (required)
  --dataset-dir DIR             Dataset directory (default: ./dataset)
  --data-pipeline-config FILE   YAML config for data pipeline (default: configs/data_pipeline.yaml)
  --deepscholar-config FILE     YAML config for deepscholar_base (default: configs/deepscholar_base.yaml)
  --eval-config FILE            YAML config for evaluation (default: configs/eval.yaml)
  --scrape-new-data             Run data pipeline step; skipped by default
  --skip-eval                   Skip evaluation step
  -h, --help                    Show this help
EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --output-base)
      OUTPUT_BASE="$2"
      shift 2
      ;;
    --dataset-dir)
      DATASET_DIR="$2"
      shift 2
      ;;
    --data-pipeline-config)
      DATA_PIPELINE_CONFIG="$2"
      shift 2
      ;;
    --deepscholar-config)
      DEEPSCHOLAR_CONFIG="$2"
      shift 2
      ;;
    --eval-config)
      EVAL_CONFIG="$2"
      shift 2
      ;;
    --scrape-new-data)
      SCRAPE_NEW_DATA=true
      shift
      ;;
    --skip-eval)
      SKIP_EVAL=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$OUTPUT_BASE" ]]; then
  echo "ERROR: --output-base is required."
  usage
  exit 1
fi

# Derive default folders
if [[ -z "$DATASET_DIR" ]]; then
  DATASET_DIR="$OUTPUT_BASE/dataset"
fi
RESULTS_DIR="$OUTPUT_BASE/results"
EVAL_DIR="$OUTPUT_BASE/evaluation"

mkdir -p "$OUTPUT_BASE"
mkdir -p "$DATASET_DIR"
mkdir -p "$RESULTS_DIR"
mkdir -p "$EVAL_DIR"

echo "=========================================="
echo "DeepScholar-Bench Pipeline (Minimal)"
echo "=========================================="
echo "Output Base:           $OUTPUT_BASE"
echo "Dataset Directory:     $DATASET_DIR"
echo "Results Directory:     $RESULTS_DIR"
echo "Evaluation Directory:  $EVAL_DIR"
echo
echo "Steps:"
echo "  1. Data Pipeline:    $([ "$SCRAPE_NEW_DATA" = true ] && echo "RUN" || echo "SKIP")"
echo "  2. DeepScholar-Base: RUN"
echo "  3. Evaluation:       $([ "$SKIP_EVAL" = true ] && echo "SKIP" || echo "RUN")"
echo "=========================================="
echo

# Step 1: Data Pipeline
if [ "$SCRAPE_NEW_DATA" = true ]; then
  echo "=========================================="
  echo "Step 1/3: Running Data Pipeline"
  echo "=========================================="
  echo

  DATA_PIPELINE_CMD="python -m data_pipeline.main --output-dir \"$DATASET_DIR\""
  [[ -n "$DATA_PIPELINE_CONFIG" ]] && DATA_PIPELINE_CMD="$DATA_PIPELINE_CMD --config-yaml \"$DATA_PIPELINE_CONFIG\""

  echo "Running: $DATA_PIPELINE_CMD"
  eval "$DATA_PIPELINE_CMD"

  echo
  echo "Data pipeline completed"
  echo
else
  echo "Step 1/3: Data pipeline skipped (pass --scrape-new-data to enable)"
  echo "  Using existing dataset in: $DATASET_DIR"
  echo

  if [[ ! -d "$DATASET_DIR" ]]; then
    echo "ERROR: Dataset directory does not exist: $DATASET_DIR"
    echo "       Pass --scrape-new-data to generate it."
    exit 1
  fi
fi

# Step 2: DeepScholar-Base (cannot be skipped)
echo "=========================================="
echo "Step 2/3: Running DeepScholar-Base"
echo "=========================================="
echo

DEEPSCHOLAR_CMD="python -m deepscholar_base.main"
DEEPSCHOLAR_CMD="$DEEPSCHOLAR_CMD --queries-file \"$DATASET_DIR/queries.csv\""
DEEPSCHOLAR_CMD="$DEEPSCHOLAR_CMD --output-folder \"$RESULTS_DIR\""
[[ -n "$DEEPSCHOLAR_CONFIG" ]] && DEEPSCHOLAR_CMD="$DEEPSCHOLAR_CMD --config-yaml \"$DEEPSCHOLAR_CONFIG\""

echo "Running: $DEEPSCHOLAR_CMD"
eval "$DEEPSCHOLAR_CMD"

echo
echo "DeepScholar-Base completed"
echo

# Step 3: Evaluation
if [ "$SKIP_EVAL" = false ]; then
  echo "=========================================="
  echo "Step 3/3: Running Evaluation"
  echo "=========================================="
  echo

  EVAL_CMD="python -m eval.main \
    --modes deepscholar_base \
    --evals all \
    --input-folder \"$RESULTS_DIR\" \
    --output-folder \"$EVAL_DIR\" \
    --dataset-path \"$DATASET_DIR/papers_with_related_works.csv\""
    --important-citations-path \"$DATASET_DIR/important_citations.csv\" \
    --nugget-groundtruth-dir-path \"$DATASET_DIR/gt_nuggets_outputs\"


  [[ -n "$EVAL_CONFIG" ]] && EVAL_CMD="$EVAL_CMD --config-yaml \"$EVAL_CONFIG\""

  echo "Running: $EVAL_CMD"
  eval "$EVAL_CMD"

  echo
  echo "Evaluation completed"
  echo
else
  echo "Skipping evaluation step"
  echo
fi

# Summary
echo "=========================================="
echo "Pipeline Complete!"
echo "=========================================="
echo "Output Directory: $OUTPUT_BASE"
echo
echo "Generated Artifacts:"
[ "$SCRAPE_NEW_DATA" = true ] && echo "  Dataset:     $DATASET_DIR/"
echo "  Results:     $RESULTS_DIR/"
[ "$SKIP_EVAL" = false ]     && echo "  Evaluation:  $EVAL_DIR/"
echo
echo "=========================================="