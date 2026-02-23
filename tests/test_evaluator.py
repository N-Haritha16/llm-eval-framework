from pathlib import Path

from llm_eval.config import load_config
from llm_eval.evaluator import evaluate


def test_evaluator_small_dataset(tmp_path: Path):
    cfg = load_config("examples/config.yaml")
    cfg.output_dir = str(tmp_path)

    results = evaluate(cfg)

    assert isinstance(results, dict)
    assert "per_example" in results
    assert isinstance(results["per_example"], list)
    assert len(results["per_example"]) > 0
