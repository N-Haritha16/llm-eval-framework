from __future__ import annotations

from pathlib import Path

import typer

from llm_eval.config import load_config as _load_config
from llm_eval.evaluator import evaluate as _evaluate
from llm_eval.reports import (
    generate_json_report as _generate_json_report,
    generate_markdown_report as _generate_markdown_report,
)

# Re-export for tests to patch
load_config = _load_config
evaluate = _evaluate
generate_json_report = _generate_json_report
generate_markdown_report = _generate_markdown_report

app = typer.Typer(help="LLM evaluation CLI")


@app.command()
def main(
    config: str = typer.Argument(..., help="Path to config YAML/JSON"),
    output: str | None = typer.Option(
        None, "--output", "-o", help="Override output directory"
    ),
) -> None:
    """
    Run the evaluation pipeline.
    """
    cfg = load_config(config)

    if output is not None:
        cfg.output_dir = output

    results = evaluate(cfg)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "report.json"
    md_path = out_dir / "report.md"

    generate_json_report(results, str(json_path))
    generate_markdown_report(results["aggregates"], str(md_path))


# Plain function version for tests that import llm_eval.cli.main(config_path, output_dir)
def main_entry(config_path: str, output_dir: str | None = None) -> None:
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


if __name__ == "__main__":
    app()
