from .base import Metric

class FaithfulnessMetric(Metric):
    name = "faithfulness"

    def compute(self, sample):
        context = " ".join(sample["retrieved_contexts"])
        return 1.0 if sample["model_answer"] in context else 0.0
