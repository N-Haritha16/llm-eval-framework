from __future__ import annotations

from typing import Any, Dict

from bert_score import score as bert_score

from .base import Metric  # <- changed

class BertScoreMetric(Metric):  # <- changed
    name = "bertscore"

    def compute(self, sample: Dict[str, Any]) -> float:
        prediction = sample.get("model_answer", "") or ""
        reference = sample.get("expected_answer", "") or ""
        if not reference or not prediction:
            return 0.0

        preds = [prediction]
        refs = [reference]
        _, _, f1 = bert_score(preds, refs, lang="en", verbose=False)
        return float(f1.mean())
