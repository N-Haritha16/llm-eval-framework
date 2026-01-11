import os
import typer

from llm_eval.utils import load_config, load_benchmark
from llm_eval.evaluator import evaluate
from llm_eval.reports import generate_json_report, generate_markdown_report
from llm_eval.plots import generate_plots

app = typer.Typer()


@app.command()
def run(config: str, output: str):
    # Load config + dataset
    cfg = load_config(config)
    data = load_benchmark(cfg["dataset"])

    # Extract predictions & references
    predictions = [item["model_answer"] for item in data]
    references = [item["expected_answer"] for item in data]

    # Evaluate
    results = evaluate(predictions, references)

    # Ensure output folder exists
    os.makedirs(output, exist_ok=True)

    # File paths
    json_path = f"{output}/report.json"
    md_path = f"{output}/report.md"

    # Save reports
    generate_json_report(results, json_path)
    generate_markdown_report(results, md_path)

    # Generate plots
    generate_plots(results, f"{output}/plots")

    print("Evaluation completed successfully!")
    print(f"JSON report: {json_path}")
    print(f"Markdown report: {md_path}")


if __name__ == "__main__":
    app()
