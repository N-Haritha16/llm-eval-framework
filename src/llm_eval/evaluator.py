from llm_eval.metrics.bleu import BleuMetric
from llm_eval.metrics.rouge import RougeLMetric
from llm_eval.metrics.bertscore import BertScoreMetric


def evaluate(predictions, references):
    metrics = {
        "bleu": BleuMetric(),
        "rougeL": RougeLMetric(),
        "bertscore": BertScoreMetric(),
    }

    results = {}
    for name, metric in metrics.items():
        results[name] = metric.compute(predictions, references)

    return results
