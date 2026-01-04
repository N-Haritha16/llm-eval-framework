import statistics
from llm_eval.metrics.bleu import BleuMetric
from llm_eval.metrics.rouge import RougeLMetric
from llm_eval.metrics.bertscore import BertScoreMetric
from llm_eval.metrics.faithfulness import FaithfulnessMetric
from llm_eval.metrics.context_relevance import ContextRelevanceMetric
from llm_eval.metrics.answer_relevance import AnswerRelevanceMetric
from llm_eval.metrics.llm_judge import LLMJudgeMetric

METRICS = [
    BleuMetric(),
    RougeLMetric(),
    BertScoreMetric(),
    FaithfulnessMetric(),
    ContextRelevanceMetric(),
    AnswerRelevanceMetric(),
    LLMJudgeMetric()
]

def evaluate(dataset):
    results = {m.name: [] for m in METRICS}

    for sample in dataset:
        for metric in METRICS:
            results[metric.name].append(metric.compute(sample))

    return {
        name: {
            "mean": statistics.mean(scores),
            "min": min(scores),
            "max": max(scores)
        }
        for name, scores in results.items()
    }
