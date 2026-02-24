from llm_eval.metrics.base import Metric
from llm_eval.metrics.answer_relevance import AnswerRelevanceMetric
from llm_eval.metrics.context_relevance import ContextRelevanceMetric
from llm_eval.metrics.faithfulness import FaithfulnessMetric
from llm_eval.metrics.llm_judge import LLMJudgeMetric


def test_extra_metrics_import():
    assert Metric is not None
    assert AnswerRelevanceMetric() is not None
    assert ContextRelevanceMetric() is not None
    assert FaithfulnessMetric() is not None
    assert LLMJudgeMetric() is not None
