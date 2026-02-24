# LLM Evaluation Framework

A lightweight, modular LLM evaluation framework for benchmarking language model outputs using automatic metrics, generating reports, visualizations, and supporting CLI + Docker-based execution.

This project focuses on **correctness**, reproducibility, and extensibility rather than optimizing metric values.


## 📌 Features

1. End-to-end evaluation pipeline (load data → run metrics → aggregate → report → plots).
2. Multiple evaluation metrics:
   - BLEU
   - ROUGE-L
   - BERTScore
   - Basic RAG-style metrics: faithfulness, context relevance, answer relevance
   - Skeleton LLM-as-a-judge metric (currently minimal logic)
3. Typer-based CLI.
4. JSON & Markdown reporting with both per-example and aggregate statistics.
5. Visualizations (histograms, radar plots) for metric distributions.
6. Pytest-based tests for core components.
7. Optional Docker support for reproducibility.

> Note: RAG-specific metrics and LLM-as-a-judge are intentionally simple and can be extended with real LLM/embedding calls as a future improvement.

## ⚙️ Installation
1️⃣ Create virtual environment (recommended)
bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
2️⃣ Install project in editable mode
bash
pip install -e .
Verify installation:

bash
python -c "import llm_eval; print('llm_eval imported successfully')"


## 📄 Dataset & Model Output Format
The framework expects JSONL files for both the benchmark dataset and model outputs.

Dataset (benchmarks/rag_benchmark.jsonl)
Each line:

json
{
  "query": "What is AI?",
  "expected_answer": "Artificial Intelligence",
  "retrieved_contexts": ["Artificial Intelligence is called AI"]
}
Model outputs (examples/model_outputs/model_a.jsonl)
Each line should align with the dataset (same order), for example:

json
{
  "query": "What is AI?",
  "model_answer": "Artificial Intelligence"
}
The evaluator joins dataset and predictions internally and passes unified samples to the metrics.

## 🧾 Configuration
Example examples/config.yaml:

text
dataset_path: benchmarks/rag_benchmark.jsonl
predictions_path: examples/model_outputs/model_a.jsonl
output_dir: results

metrics:
  - bleu
  - rougeL
  - bertscore
  - faithfulness
  - context_relevance
  - answer_relevance
  # - llm_judge  # enable once you implement a real judge

# Optional: additional metric/model settings can be added here
Config can be YAML or JSON.

Basic validation is handled via Pydantic models in config.py (with a deprecation warning for V1-style validators).

## 🚀 Running Evaluation (CLI)
From the project root:

bash
python -m llm_eval.cli examples/config.yaml --output results
This command:

Loads configuration.

Loads dataset and model outputs.

Runs all configured metrics.

Computes per-example scores and aggregates (mean, etc.).

Writes JSON + Markdown reports.

Saves plots in results.

You can override the output directory from the config using --output:

bash
python -m llm_eval.cli examples/config.yaml --output custom_results

## 📊 Output Artifacts
All outputs are written under the configured output_dir (default results/).

1. JSON report – results/report.json
Structure:

json
{
  "per_example": [
    {
      "query": "What is AI?",
      "expected_answer": "Artificial Intelligence",
      "model_answer": "Artificial Intelligence",
      "bleu": 1.0,
      "rouge": 1.0,
      "bertscore": 1.0,
      "faithfulness": 1.0,
      "context_relevance": 1.0,
      "answer_relevance": 1.0
    },
    ...
  ],
  "aggregates": {
    "bleu": 0.31,
    "rouge": 0.85,
    "bertscore": 0.92,
    "faithfulness": 0.78,
    "context_relevance": 0.81,
    "answer_relevance": 0.80
  }
}
Field names may vary slightly (for example rougeL vs rouge) depending on metric implementation, but the structure is per_example + aggregates.

2. Markdown report – results/report.md
Human-readable summary, for example:

text
# LLM Evaluation Report

## BLEU
- Mean: 0.31

## ROUGE-L
- Mean: 0.85

## BERTScore
- Mean: 0.92

## Faithfulness
- Mean: 0.78

## Context Relevance
- Mean: 0.81

## Answer Relevance
- Mean: 0.80
You can extend Markdown generation to include tables and additional statistics (median, std, etc.).

3. Plots – results/plots/
Typical files:

bleu_hist.png

rougeL_hist.png

bertscore_hist.png

metrics_radar.png (radar comparison of metrics)

These visualize score distributions and relative performance across metrics.

## 🧪 Running Tests
Run from the project root:

bash
python -m pytest
You should see tests for metrics, pipeline, and reporting modules passing (some tests may be skipped depending on optional deps). The tests validate logic and wiring; they do not enforce specific metric values.

## 🐳 Docker Support
Build the image:

bash
docker build -t llm-eval .
Run evaluation inside a container (mount local results):

bash
docker run --rm -v "$(pwd)/results:/app/results" llm-eval \
  python -m llm_eval.cli examples/config.yaml --output /app/results
Using docker-compose:

bash
docker-compose up --build
This is useful for reproducible runs and CI.

⚠️ Notes on Metric Values
BLEU, ROUGE, and BERTScore are sensitive to:

Dataset size.

Sentence length.

Tokenization and casing.

Smoothing and metric configuration.

Therefore:

Low BLEU does not necessarily indicate a bug.

RAG-related metrics (faithfulness, context relevance, answer relevance) are simple heuristics in this baseline and can be replaced with embedding or LLM-based evaluators for higher fidelity.

## 🎯 Project Goals
Build a working LLM evaluation pipeline.

Support multiple automatic metrics.

Provide machine-readable (JSON) and human-readable (Markdown) reports.

Generate basic visualizations.

Enable CLI & Docker execution.

Keep the codebase extensible for new metrics and judges.

## 🧠 Future Extensions

Replace placeholder RAG metrics with embedding/LLM-based implementations.

Implement a real LLM-as-a-judge with prompt templates, rubrics, and robust error handling.

Add configurable metric registry / plugin system via config.

Support more dataset formats (e.g., CSV) and richer benchmarks.

Add more aggregate statistics (median, std dev, confidence intervals).

Generate richer HTML dashboards for interactive exploration.

text

Do not commit or share any real API keys (like Anthropic/OpenAI) in your repo or README; keep them only in `.env` and environment variables and reference them generically in docs (for example “set `ANTHROPIC_API_KEY` in your environment”).
