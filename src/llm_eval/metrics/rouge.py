from rouge_score import rouge_scorer
from .base import Metric

class RougeLMetric(Metric):
    name = "rouge_l"

    def compute(self, sample):
        scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
        score = scorer.score(sample["expected_answer"], sample["model_answer"])
        return score["rougeL"].fmeasure
