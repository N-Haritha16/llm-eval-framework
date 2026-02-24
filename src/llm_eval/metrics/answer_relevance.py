# src/llm_eval/metrics/answer_relevance.py

import numpy as np

from .base import Metric
from .embeddings import embed_texts, cosine

class AnswerRelevanceMetric(Metric):
    name = "answer_relevance"

    def compute(self, sample: dict) -> float:
        query: str = sample["query"]
        answer: str = sample["model_answer"]

        q_emb, a_emb = embed_texts([query, answer])
        sim = cosine(q_emb, a_emb)
        return float(sim)
