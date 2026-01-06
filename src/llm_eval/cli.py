import typer
from llm_eval.utils import load_config, load_benchmark
from llm_eval.evaluator import evaluate
from llm_eval.reports import generate_json, generate_markdown
from llm_eval.plots import generate_plots

app = typer.Typer()


@app.command()
def run(config: str, output: str):
    cfg = load_config(config)
    data = load_benchmark(cfg["dataset"])

    predictions = [item["model_answer"] for item in data]
    references = [item["expected_answer"] for item in data]

    results = evaluate(predictions, references)

    generate_json(results, f"{output}/report.json")
    generate_markdown(results, f"{output}/report.md")
    generate_plots(results, f"{output}/plots")


if __name__ == "__main__":
    app()
