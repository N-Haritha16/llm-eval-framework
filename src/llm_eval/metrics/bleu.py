from __future__ import annotations

from typing import Any, Dict, List

from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

from .base import Metric  # <- changed

class BleuMetric(Metric):  # <- changed
    def __init__(self, max_ngram: int = 4) -> None:
        self.name = "bleu"
        self.max_ngram = max_ngram
        self._smooth = SmoothingFunction().method1

    def _weights(self) -> List[float]:
        return [1.0 / self.max_ngram] * self.max_ngram

    def compute(self, sample: Dict[str, Any]) -> float:
        reference = sample.get("expected_answer", "") or ""
        prediction = sample.get("model_answer", "") or ""
        if not reference or not prediction:
            return 0.0

        ref_tokens = reference.split()
        pred_tokens = prediction.split()
        return float(
            sentence_bleu(
                [ref_tokens],
                pred_tokens,
                weights=tuple(self._weights()),
                smoothing_function=self._smooth,
            )
        )
