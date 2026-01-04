import typer
import os
from llm_eval.config import load_config
from llm_eval.dataset import load_benchmark
from llm_eval.evaluator import evaluate
from llm_eval.reporting.json_report import generate_json
from llm_eval.reporting.markdown_report import generate_markdown
from llm_eval.visualization.histograms import plot_histograms
from llm_eval.visualization.radar import plot_radar

app = typer.Typer()

@app.command()
def run(config: str, output: str):
    os.makedirs(output + "/plots", exist_ok=True)

    cfg = load_config(config)
    data = load_benchmark(cfg["dataset"])
    results = evaluate(data)

    generate_json(results, f"{output}/report.json")
    generate_markdown(results, f"{output}/report.md")
    plot_histograms(results, f"{output}/plots")
    plot_radar(results, f"{output}/plots/radar.png")

if __name__ == "__main__":
    app()
