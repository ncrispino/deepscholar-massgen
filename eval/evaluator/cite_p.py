import pandas as pd
import re
from nltk.tokenize import sent_tokenize
import numpy as np

try:
    from evaluator import Evaluator
    from parsers import Parser
    from evaluator import EvaluationFunction
    from prompts.support import get_support
except ImportError:
    from .evaluator import Evaluator
    from ..parsers import Parser
    from .enum import EvaluationFunction
    from ..prompts.support import get_support


class CitePEvaluator(Evaluator):
    evaluation_function = EvaluationFunction.CITE_P

    def _calculate(self, parser: Parser) -> pd.DataFrame:
        sentences = custom_sent_tokenize(parser.clean_text)
        docs = parser.docs or []
        cite_quality_docs = parser.citations_for_cite_quality or []
        max_citable_idx = min(len(docs), len(cite_quality_docs)) - 1
        if max_citable_idx < 0:
            return 0.0

        citation_precision = []
        for sent in sentences:
            if len(sent) < 50:
                continue
            correct_citations = []
            target = _remove_citations(sent)
            ref = [int(x[1:]) - 1 for x in re.findall(r"\[\d+", sent)]
            for r in ref:
                if r > max_citable_idx or r < 0:
                    continue
                current_doc = _format_document(cite_quality_docs[r])
                single_entail = get_support(current_doc, target)
                correct_citations.append(single_entail)
            precision = (
                sum(correct_citations) / len(correct_citations)
                if correct_citations
                else 0
            )
            citation_precision.append(precision)
        if not citation_precision:
            return 0.0
        return float(np.mean(citation_precision))

    def calculate(self, parsers: list[Parser]) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "folder_path": [parser.folder_path for parser in parsers],
                self.evaluation_function.value: [
                    self._calculate(parser) for parser in parsers
                ],
            }
        )


def custom_sent_tokenize(text):
    if text is None:
        return []
    protected_text = str(text)
    protected_text = re.sub(r"\bet al\.", "ET_AL_PLACEHOLDER", protected_text)
    sentences = sent_tokenize(protected_text)
    sentences = [s.replace("ET_AL_PLACEHOLDER", "et al.") for s in sentences]
    return sentences


def _remove_citations(text: str) -> str:
    return re.sub(r"\s*\[\d+\]", "", text).replace(" |", "").strip()


def _format_document(doc: tuple[str, str]) -> str:
    return f"Title: {doc[0]}\n{doc[1]}"
