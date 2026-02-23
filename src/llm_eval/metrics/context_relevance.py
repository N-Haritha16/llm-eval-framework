# src/llm_eval/metrics/context_relevance.py
from .embeddings import get_embedding_model
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ContextRelevanceMetric:
    def __init__(self):
        self.model = get_embedding_model()

    def compute(self, query: str, contexts: list[str]) -> float:
        if not contexts:
            return 0.0
        q_emb = self.model.encode([query])
        c_embs = self.model.encode(contexts)
        sims = cosine_similarity(q_emb, c_embs)[0]
        return float(np.mean(sims))
