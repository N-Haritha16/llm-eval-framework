from .base import Metric

class ContextRelevanceMetric(Metric):
    name = "context_relevance"

    def compute(self, sample):
        return min(len(sample["retrieved_contexts"]) / 3, 1.0)
