from .base import Metric

class AnswerRelevanceMetric(Metric):
    name = "answer_relevance"

    def compute(self, sample):
        return 1.0 if len(sample["model_answer"]) > 15 else 0.4
