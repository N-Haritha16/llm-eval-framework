from pathlib import Path
from llm_eval.reports import generate_json_report
from llm_eval.plots import generate_plots


def test_reports_and_plots(tmp_path: Path):
    results = {
        "per_example": [
            {
                "query": "Q1",
                "expected_answer": "A1",
                "model_answer": "A1",
                "bleu": 0.8,
                "rougeL": 0.9,
            },
            {
                "query": "Q2",
                "expected_answer": "A2",
                "model_answer": "A2",
                "bleu": 0.5,
                "rougeL": 0.6,
            },
        ],
        "aggregates": {
            "bleu": {"mean": 0.65, "median": 0.65, "std": 0.15},
            "rougeL": {"mean": 0.75, "median": 0.75, "std": 0.15},
        },
    }

    json_path = tmp_path / "report.json"
    generate_json_report(results, json_path)
    assert json_path.exists()

    generate_plots(results, tmp_path)
    # histograms + radar
    files = {p.name for p in tmp_path.iterdir()}
    assert any("bleu_histogram" in name for name in files)
    assert any("rougeL_histogram" in name for name in files)
    assert "metrics_radar.png" in files
