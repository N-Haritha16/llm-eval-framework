from llm_eval.metrics.bleu import BleuMetric

def test_bleu_metric():
    sample = {
        "expected_answer": "hello",
        "model_answer": "hello"
    }
    assert BleuMetric().compute(sample) > 0
