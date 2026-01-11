from llm_eval.metrics.base import Metric
from llm_eval.metrics.answer_relevance import AnswerRelevance
from llm_eval.metrics.context_relevance import ContextRelevance
from llm_eval.metrics.faithfulness import Faithfulness
from llm_eval.metrics.llm_judge import LLMJudge

def test_extra_metrics_import():
    assert Metric is not None
    assert AnswerRelevance() is not None
    assert ContextRelevance() is not None
    assert Faithfulness() is not None
    assert LLMJudge() is not None
