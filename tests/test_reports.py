from pathlib import Path
from llm_eval.reports import generate_json_report, generate_markdown_report


def test_generate_json(tmp_path: Path):
    results = {
        "bleu": {"mean": 0.5, "median": 0.5, "std": 0.1},
        "rougeL": {"mean": 0.7, "median": 0.7, "std": 0.05},
    }
    path = tmp_path / "report.json"
    generate_json_report(results, path)
    assert path.exists()


def test_generate_markdown(tmp_path: Path):
    aggregates = {
        "bleu": {"mean": 0.5, "median": 0.5, "std": 0.1},
        "rougeL": {"mean": 0.7, "median": 0.7, "std": 0.05},
    }
    path = tmp_path / "report.md"
    generate_markdown_report(aggregates, path)
    text = path.read_text(encoding="utf-8")
    assert "# LLM Evaluation Report" in text
    assert "| Metric | Mean | Median | Std Dev |" in text
    assert "bleu" in text
    assert "rougeL" in text
