## LLM Evaluation Framework

A lightweight, modular LLM evaluation framework for benchmarking language model outputs using automatic metrics, generating reports, visualizations, and supporting CLI + Docker-based execution.

This project focuses on correctness, reproducibility, and extensibility rather than optimizing metric values.

## 📌 Features

1. End-to-end evaluation pipeline

2. Multiple evaluation metrics:

       BLEU

       ROUGE-L

       BERTScore

3. CLI-based execution

4. JSON & Markdown reporting

5. Visualizations (bar charts, histograms, radar plots)

6. Pytest-based test coverage

7. Docker support for reproducibility

## 📁 Project Structure

llm_eval_framework/
├── src/llm_eval/
│   ├── cli.py
│   ├── config.py
│   ├── evaluator.py
│   ├── dataset.py
│   ├── logger.py
│   ├── utils.py
│   │
│   ├── metrics/
│   │   ├── bleu.py
│   │   ├── rouge.py
│   │   ├── bertscore.py
│   │   ├── faithfulness.py
│   │   ├── context_relevance.py
│   │   ├── answer_relevance.py
│   │   └── llm_judge.py
│   │
│   ├── reporting/
│   │   ├── json_report.py
│   │   └── markdown_report.py
│   │
│   └── visualization/
│       ├── histograms.py
│       └── radar.py
│
├── benchmarks/
│   └── rag_benchmark.jsonl
├── examples/
│   ├── config.yaml
│   └── model_outputs/
│       └── model_a.jsonl
├── results/                # generated at runtime
│   ├── report.json
│   ├── report.md
│   └── plots/
├── tests/
│   ├── test_metrics.py
│   ├── test_pipeline.py
│   └── test_reports.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── .env.example

## ⚙️ Installation
1️⃣ Create virtual environment (recommended)

python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install project in editable mode

pip install -e .

# Verify installation:

python -c "import llm_eval; print('llm_eval imported successfully')"

## 📄 Dataset Format

Each dataset entry must be a JSON line with:

{
  "query": "What is AI?",
  "expected_answer": "Artificial Intelligence",
  "retrieved_contexts": ["Artificial Intelligence is called AI"],
  "model_answer": "Artificial Intelligence"
}

## 🚀 Running Evaluation (CLI)

python -m llm_eval.cli examples/config.yaml results

This command:

1. Loads dataset

2. Computes metrics

3. Generates reports

4. Saves plots

## 📊 Output Artifacts

# 📁 results/

report.json
{
  "bleu": 0.316227766016838,
  "rougeL": 1.0,
  "bertscore": 1.0000001192092896
}

report.md

# LLM Evaluation Report

## bleu
- Score: 0.316227766016838

## rougeL
- Score: 1.0

## bertscore
- Score: 1.0000001192092896

# 📈 results/plots/

Generated visualizations:

1. metrics.png

2. bleu_hist.png

3. rougeL_hist.png

4. bertscore_hist.png

5. metrics_radar.png

These visualize metric distributions and comparisons.

## 🧪 Running Tests

python -m pytest


Expected result:

================= 3 passed in X.XXs =================


Metric values are not hard-coded — tests validate logic correctness, not numeric thresholds.

## 🐳 Docker Support

Build image
docker build -t llm-eval .

Run container
docker run -v $(pwd)/results:/app/results llm-eval


Or using docker-compose:

docker-compose up --build

## ⚠️ Notes on Metric Values

BLEU, ROUGE, and BERTScore depend on:

1. Dataset size

2. Sentence length

3. Tokenization

4. Smoothing methods

## ⚠️ Low BLEU scores do NOT indicate an error.
This framework evaluates correctly and dynamically, which is the goal.

## 🎯 Project Goals

✔ Build a working LLM evaluation pipeline
✔ Support multiple metrics
✔ Provide reports and plots
✔ Enable CLI & Docker execution
✔ Ensure reproducibility and testability

❌ The goal is not to optimize or hardcode metric values.

## 📌 Conclusion

This project delivers a functional, extensible, and reproducible LLM evaluation framework suitable for:

1. Academic assignments

2. Benchmarking experiments

3. RAG evaluation pipelines

4. MLOps workflows

## 🧠 Future Extensions

Add human evaluation hooks

Support multiple models

Integrate LLM-as-judge

Add confidence intervals

Support larger benchmarks
