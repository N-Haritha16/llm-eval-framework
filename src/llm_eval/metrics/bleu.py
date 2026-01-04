from nltk.translate.bleu_score import sentence_bleu
from .base import Metric

class BleuMetric(Metric):
    name = "bleu"

    def compute(self, sample):
        reference = sample["expected_answer"].split()
        hypothesis = sample["model_answer"].split()
        return sentence_bleu([reference], hypothesis)
