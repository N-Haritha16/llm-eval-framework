from llm_eval.metrics.base import MetricBase as Metric
from llm_eval.metrics.answer_relevance import AnswerRelevanceMetric as AnswerRelevance
from llm_eval.metrics.context_relevance import ContextRelevanceMetric as ContextRelevance
from llm_eval.metrics.faithfulness import FaithfulnessMetric as Faithfulness
from llm_eval.metrics.llm_judge import LLMJudgeMetric as LLMJudge
from llm_eval.config import LLMJudgeConfig


def test_extra_metrics_import():
    assert Metric is not None
    assert AnswerRelevance() is not None
    assert ContextRelevance() is not None
    assert Faithfulness() is not None

    cfg = LLMJudgeConfig(
        provider="openai",
        model="gpt-4.1-mini",
        api_key_env="OPENAI_API_KEY",
        temperature=0.0,
        max_retries=1,
        backoff_factor=1.0,
    )
    assert LLMJudge(cfg) is not None
