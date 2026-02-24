from __future__ import annotations

import logging
import statistics
from typing import Any, Dict, List

from llm_eval.metrics.bleu import BleuMetric
from llm_eval.metrics.rouge import RougeLMetric
from llm_eval.metrics.bertscore import BertScoreMetric
from llm_eval.metrics.context_relevance import ContextRelevanceMetric
from llm_eval.metrics.answer_relevance import AnswerRelevanceMetric
from llm_eval.metrics.faithfulness import FaithfulnessMetric
from llm_eval.metrics.llm_judge import LLMJudgeMetric
from llm_eval.utils import load_benchmark

logger = logging.getLogger(__name__)

METRIC_REGISTRY = {
    "bleu": BleuMetric,
    "rougeL": RougeLMetric,
    "bertscore": BertScoreMetric,
    "faithfulness": FaithfulnessMetric,
    "context_relevance": ContextRelevanceMetric,
    "answer_relevance": AnswerRelevanceMetric,
    "llm_judge": LLMJudgeMetric,
}


def _evaluate_internal(
    samples: List[Dict[str, Any]],
    metric_names: List[str],
) -> Dict[str, Any]:
    """
    Core evaluation: operates on loaded samples and chosen metric names.
    """
    logger.info("Evaluating metrics: %s", metric_names)

    metrics = []
    for name in metric_names:
        cls = METRIC_REGISTRY.get(name)
        if cls is None:
            logger.warning("Unknown metric %s, skipping", name)
            continue
        metrics.append(cls())

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


def evaluate(cfg) -> Dict[str, Any]:
    """
    Config-based entrypoint used by tests/test_evaluator.py.

    Expects cfg to have:
      - cfg.dataset: DatasetConfig with .path
      - cfg.metrics: MetricsConfig with .metrics (list of metric names)
    """
    dataset_path = cfg.dataset.path
    metric_names = getattr(cfg.metrics, "metrics", ["bleu", "rougeL", "bertscore"])

    samples = load_benchmark(dataset_path)
    return _evaluate_internal(samples, metric_names)
