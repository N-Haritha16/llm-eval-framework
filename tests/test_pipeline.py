from llm_eval.dataset import load_benchmark
from llm_eval.evaluator import evaluate

def test_full_pipeline():
    dataset = load_benchmark("benchmarks/rag_benchmark.jsonl")
    results = evaluate(dataset)

    assert isinstance(results, dict)
    assert "bleu" in results
    assert results["bleu"]["mean"] >= 0.0
