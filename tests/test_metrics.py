from llm_eval.metrics.bleu import BLEUMetric as BleuMetric
from llm_eval.metrics.rouge import RougeMetric
from llm_eval.metrics.bertscore import BERTScoreMetric
from llm_eval.metrics.faithfulness import FaithfulnessMetric
from llm_eval.metrics.context_relevance import ContextRelevanceMetric
from llm_eval.metrics.answer_relevance import AnswerRelevanceMetric


def test_bleu_metric():
    sample = {
        "query": "hi",
        "expected_answer": "hello world",
        "model_answer": "hello world",
        "retrieved_contexts": ["hello world"],
    }
    score = BleuMetric().compute(sample)
    assert 0.0 <= score <= 1.0


def test_other_metrics():
    sample = {
        "query": "What is AI?",
        "expected_answer": "Artificial intelligence is the field of creating intelligent machines.",
        "model_answer": "Artificial intelligence is the study of intelligent machines.",
        "retrieved_contexts": [
            "Artificial intelligence is the field of creating intelligent machines."
        ],
    }

    assert 0.0 <= RougeMetric().compute(sample) <= 1.0
    assert 0.0 <= BERTScoreMetric().compute(sample) <= 1.0
    assert 0.0 <= FaithfulnessMetric().compute(sample) <= 1.0
    assert 0.0 <= ContextRelevanceMetric().compute(sample) <= 1.0
    assert 0.0 <= AnswerRelevanceMetric().compute(sample) <= 1.0
