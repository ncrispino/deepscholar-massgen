# evaluation_suite.py - Combined Citation Stats Evaluation Version
import os
import pandas as pd
import argparse
import logging
from pathlib import Path
from tabulate import tabulate  # type: ignore
import lotus
from lotus.models import LM
import traceback
try:
    from parsers import get_parser, Parser, ParserType
    from argument_parser import parse_args
except ImportError:
    from .parsers import get_parser, Parser, ParserType
    from .argument_parser import parse_args

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

_NLTK_SENTENCE_TOKENIZER_EVALS = {"cite_p", "claim_coverage"}


def _nltk_data_dir() -> Path:
    env_nltk_data = os.environ.get("NLTK_DATA", "").strip()
    if env_nltk_data:
        return Path(env_nltk_data).expanduser()

    virtual_env = os.environ.get("VIRTUAL_ENV", "").strip()
    if virtual_env:
        return Path(virtual_env) / "nltk_data"

    return Path.cwd() / ".nltk_data"


def _ensure_nltk_sentence_tokenizers(args: argparse.Namespace) -> None:
    selected_evals = {str(eval_fn.value) for eval_fn in args.evals}
    if not selected_evals.intersection(_NLTK_SENTENCE_TOKENIZER_EVALS):
        return

    try:
        import nltk
        from nltk import data as nltk_data
    except Exception as e:
        raise RuntimeError(
            "NLTK is required for cite_p/claim_coverage evals. "
            "Install requirements and retry."
        ) from e

    download_dir = _nltk_data_dir()
    download_dir.mkdir(parents=True, exist_ok=True)
    download_dir_str = str(download_dir)
    os.environ["NLTK_DATA"] = download_dir_str

    if download_dir_str not in nltk_data.path:
        nltk_data.path.insert(0, download_dir_str)

    required_resources = (
        ("punkt_tab", "tokenizers/punkt_tab/english/"),
        ("punkt", "tokenizers/punkt"),
    )

    for resource_name, resource_path in required_resources:
        try:
            nltk_data.find(resource_path)
            continue
        except LookupError:
            logger.info(
                "Downloading NLTK resource '%s' into %s ...",
                resource_name,
                download_dir_str,
            )

        downloaded = nltk.download(
            resource_name,
            download_dir=download_dir_str,
            quiet=True,
        )
        if not downloaded:
            raise RuntimeError(
                f"Failed to download NLTK resource '{resource_name}' "
                f"to {download_dir_str}. "
                "Try running: python -m nltk.downloader punkt_tab punkt"
            )

        try:
            nltk_data.find(resource_path)
        except LookupError as e:
            raise RuntimeError(
                f"NLTK resource '{resource_name}' still not found after download. "
                f"Searched path includes: {nltk_data.path}"
            ) from e


def process_mode(
    args: argparse.Namespace,
    mode: ParserType,
    input_folder: str,
    dataset: pd.DataFrame,
) -> list[Parser]:
    mode_results: list[Parser] = []

    if not os.path.exists(input_folder) and mode != ParserType.GROUNDTRUTH:
        logger.warning(f"Warning: Mode folder {input_folder} not found, skipping")
        return []

    if args.file_id:
        files_to_process: list[str] = [
            fid
            for fid in args.file_id
            if os.path.exists(os.path.join(input_folder, fid))
        ]
    else:
        if mode == ParserType.GROUNDTRUTH:
            try:
                files_to_process = sorted(os.listdir(args.reference_folder))
            except FileNotFoundError:
                logger.warning(
                    f"Warning: Reference folder {args.reference_folder} not found, skipping"
                )
                return []
        else:
            files_to_process = sorted(os.listdir(input_folder))

    for file_id in files_to_process:
        folder_path = os.path.join(input_folder, file_id)

        try:
            parser = get_parser(
                {
                    "mode": mode,
                    "file_id": file_id.replace(".json", ""),
                    "dataset": dataset,
                },
                folder_path,
            )
        except Exception as e:
            logger.warning(f"❌ Error processing {mode.value} / {file_id}: {traceback.format_exc()}")
            continue

        if parser.docs:
            mode_results.append(parser)
            logger.info(f"✅ {mode.value} / {file_id} processed")
        else:
            logger.warning(
                f"❌ Error processing {mode.value} / {file_id}: No docs found"
            )

    if mode_results:
        logger.info(f"Processed {len(mode_results)} results for mode: {mode.value}")
    else:
        logger.warning(f"No  results to save for mode: {mode.value}")

    return mode_results


def pretty_print_results(results: pd.DataFrame) -> None:
    print(tabulate(results, headers="keys", tablefmt="grid"))


def main() -> None:
    """Main function to run the citation statistics evaluation"""
    args = parse_args()
    _ensure_nltk_sentence_tokenizers(args)

    lotus.settings.configure(
        lm=LM(
            model=args.model_name,
        )
    )

    # Load dataset and setup mappings
    dataset = pd.read_csv(args.dataset_path)

    mode_results = {
        mode.value: process_mode(args, mode, input_folder, dataset)
        for mode, input_folder in zip(args.modes, args.input_folder)

    }

    os.makedirs(args.output_folder, exist_ok=True)

    results: pd.DataFrame | None = None
    for eval in args.evals:
        new_results = eval.evaluate_all(
            mode_results,
            output_dir=os.path.join(args.output_folder, eval.value),
            important_citations_path=args.important_citations_path,
            nugget_groundtruth_dir_path=args.nugget_groundtruth_dir_path,
        )
        if results is None:
            results = new_results
        else:
            results = results.merge(new_results, on="baseline_name", how="outer")

    if results is not None:
        results.to_csv(os.path.join(args.output_folder, "results.csv"), index=False)

    pretty_print_results(results)
    logger.info(f"Results saved to: {args.output_folder}")


if __name__ == "__main__":
    main()
