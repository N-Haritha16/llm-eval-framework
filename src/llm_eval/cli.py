from pathlib import Path

from llm_eval.config import load_config
from llm_eval.evaluator import evaluate
from llm_eval.reports import generate_json_report, generate_markdown_report


def main(config_path: str, output_dir: str | None = None):
    cfg = load_config(config_path)
    if output_dir is not None:
        cfg.output_dir = output_dir

    results = evaluate(cfg)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "report.json"
    md_path = out_dir / "report.md"

    generate_json_report(results, str(json_path))
    generate_markdown_report(results["aggregates"], str(md_path))
