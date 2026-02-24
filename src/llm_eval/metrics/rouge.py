from __future__ import annotations

from typing import Any, Dict

from rouge_score import rouge_scorer

from .base import Metric  # <- changed

class RougeLMetric(Metric):  # <- changed
    name = "rougeL"

    def __init__(self) -> None:
        self.scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

    def compute(self, sample: Dict[str, Any]) -> float:
        reference = sample.get("expected_answer", "") or ""
        prediction = sample.get("model_answer", "") or ""
        if not reference or not prediction:
            return 0.0

        score = self.scorer.score(reference, prediction)
        return float(score["rougeL"].fmeasure)
