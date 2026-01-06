from llm_eval.metrics.bleu import BleuMetric


def test_bleu_metric():
    sample = {
        "expected_answer": "hello world",
        "model_answer": "hello world"
    }

    score = BleuMetric().compute(sample, sample["expected_answer"])
    assert score > 0
