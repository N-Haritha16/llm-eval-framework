from llm_eval.plots import generate_plots
from llm_eval.reports import generate_json_report, generate_markdown_report

def test_reports_and_plots(tmp_path):
    results = {
        "bleu": 0.3,
        "rougeL": 1.0,
        "bertscore": 1.0
    }

    generate_json_report(results, tmp_path)
    generate_markdown_report(results, tmp_path)
    generate_plots(results, tmp_path)

    assert tmp_path.exists()
