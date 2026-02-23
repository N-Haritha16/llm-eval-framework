# tests/test_utils.py
from pathlib import Path
import pytest

from llm_eval.utils import load_config, load_benchmark


def test_load_config_valid():
    cfg = load_config("examples/config.yaml")
    assert cfg is not None


def test_load_config_invalid(tmp_path: Path):
    bad = tmp_path / "bad.yaml"
    bad.write_text("not: valid: yaml:", encoding="utf-8")
    with pytest.raises(Exception):
        load_config(str(bad))


def test_load_benchmark_valid():
    data = load_benchmark("benchmarks/rag_benchmark.jsonl")
    assert len(data) > 0
    first = data[0]
    assert "query" in first
    assert "expected_answer" in first
    assert "retrieved_contexts" in first


def test_load_benchmark_missing():
    with pytest.raises(Exception):
        load_benchmark("benchmarks/does_not_exist.jsonl")
