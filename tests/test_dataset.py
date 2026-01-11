from llm_eval.dataset import load_benchmark

def test_load_benchmark():
    data = load_benchmark("benchmarks/rag_benchmark.jsonl")
    assert len(data) > 0
