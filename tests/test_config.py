from llm_eval.config import load_config

def test_load_config():
    config = load_config("examples/config.yaml")
    assert "dataset" in config
