from .base import Metric

class LLMJudge(Metric):
    name = "llm_judge"

    def compute(self, sample):
        # Mocked judge for CI/CD safety
        return 0.75
