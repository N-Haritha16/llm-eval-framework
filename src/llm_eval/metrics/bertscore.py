from __future__ import annotations

from typing import Any, Dict

import bert_score

from .base import MetricBase


class BERTScoreMetric(MetricBase):
    def __init__(self) -> None:
        self.name = "bertscore"

    def compute(self, sample: Dict[str, Any]) -> float:
        reference = sample.get("expected_answer", "") or ""
        prediction = sample.get("model_answer", "") or ""
        if not reference or not prediction:
            return 0.0

        P, R, F1 = bert_score.score(
            [prediction],
            [reference],
            lang="en",
            verbose=False,
        )
        return float(F1[0])
