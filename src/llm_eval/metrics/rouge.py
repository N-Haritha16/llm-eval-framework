from __future__ import annotations

from typing import Any, Dict

from rouge_score import rouge_scorer

from .base import MetricBase


class RougeMetric(MetricBase):
    def __init__(self) -> None:
        self.name = "rouge_l"
        self._scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

    def compute(self, sample: Dict[str, Any]) -> float:
        reference = sample.get("expected_answer", "") or ""
        prediction = sample.get("model_answer", "") or ""
        if not reference or not prediction:
            return 0.0

        scores = self._scorer.score(reference, prediction)
        return float(scores["rougeL"].fmeasure)
