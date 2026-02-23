from llm_eval.utils import load_config


def test_load_config():
    config = load_config("examples/config.yaml")
    # load_config returns a plain dict
    assert "dataset" in config
    assert config["dataset"]["path"].endswith("benchmarks/rag_benchmark.jsonl")
