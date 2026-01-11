from .base import Metric

class AnswerRelevance(Metric):
    name = "answer_relevance"

    def compute(self, sample, references=None):
        return 1.0 if len(sample["model_answer"]) > 15 else 0.4
