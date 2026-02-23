from llm_eval.dataset import load_dataset
from llm_eval.config import DatasetConfig

def test_load_benchmark():
    cfg = DatasetConfig(path="benchmarks/rag_benchmark.jsonl", format="jsonl")
    data = load_dataset(cfg)
    assert len(data) > 0
    assert "query" in data[0]
    assert "expected_answer" in data[0]
