from __future__ import annotations

import logging
import statistics
from typing import Any, Dict, List

from .config import EvalConfig
from .dataset import load_dataset
from .metrics.base import MetricBase
from .metrics.bleu import BLEUMetric
from .metrics.rouge import RougeMetric
from .metrics.bertscore import BERTScoreMetric
from .metrics.context_relevance import ContextRelevanceMetric
from .metrics.answer_relevance import AnswerRelevanceMetric
from .metrics.faithfulness import FaithfulnessMetric
from .metrics.llm_judge import LLMJudgeMetric

logger = logging.getLogger(__name__)


def _build_metric(name: str, cfg: EvalConfig) -> MetricBase:
    n = name.lower()
    if n == "bleu":
        return BLEUMetric(max_ngram=cfg.metrics.bleu_max_ngram)
    if n in {"rouge", "rouge_l"}:
        return RougeMetric()
    if n == "bertscore":
        return BERTScoreMetric()
    if n == "faithfulness":
        return FaithfulnessMetric()
    if n in {"context_relevance", "context_rel"}:
        return ContextRelevanceMetric()
    if n in {"answer_relevance", "answer_rel"}:
        return AnswerRelevanceMetric()
    if n == "llm_judge":
        if not cfg.llm_judge:
            raise ValueError("llm_judge metric requested but llm_judge config missing")
        return LLMJudgeMetric(cfg.llm_judge)
    raise ValueError(f"Unknown metric: {name}")


def evaluate(cfg: EvalConfig) -> Dict[str, Any]:
    # Debug: see what metrics config actually has
    logger.info("ACTIVE CONFIG METRICS: %s", cfg.metrics.metrics)

    samples = load_dataset(cfg.dataset)

    metrics: List[MetricBase] = []
    for mname in cfg.metrics.metrics:
        try:
            metric = _build_metric(mname, cfg)
            metrics.append(metric)
        except Exception as exc:
            logger.warning("Skipping metric %s: %s", mname, exc)

    per_example: List[Dict[str, Any]] = []
    metric_scores: Dict[str, List[float]] = {m.name: [] for m in metrics}

    for sample in samples:
        row: Dict[str, Any] = {
            "query": sample["query"],
            "expected_answer": sample["expected_answer"],
            "model_answer": sample["model_answer"],
        }
        for metric in metrics:
            score = metric.compute(sample)
            metric_scores[metric.name].append(score)
            row[metric.name] = score
        per_example.append(row)

    aggregates: Dict[str, Dict[str, float]] = {}
    for name, scores in metric_scores.items():
        if not scores:
            continue
        aggregates[name] = {
            "mean": float(statistics.fmean(scores)),
            "median": float(statistics.median(scores)),
            "std": float(statistics.pstdev(scores)),
            "min": float(min(scores)),
            "max": float(max(scores)),
        }

    return {"per_example": per_example, "aggregates": aggregates}
