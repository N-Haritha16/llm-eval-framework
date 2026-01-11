from .base import Metric

class Faithfulness(Metric):   
    name = "faithfulness"

    def compute(self, predictions, references):
        return [1.0 if p in r else 0.0 for p, r in zip(predictions, references)]
