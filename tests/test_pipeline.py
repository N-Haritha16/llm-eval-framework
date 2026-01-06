from llm_eval.evaluator import evaluate
from llm_eval.utils import load_benchmark


def test_full_pipeline():
    dataset = load_benchmark("benchmarks/rag_benchmark.jsonl")

    predictions = [item["model_answer"] for item in dataset]
    references = [item["expected_answer"] for item in dataset]

    results = evaluate(predictions, references)

    assert "bleu" in results
    assert "rougeL" in results
    assert "bertscore" in results
