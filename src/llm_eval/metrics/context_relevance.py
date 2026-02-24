# src/llm_eval/metrics/context_relevance.py

from typing import List
import numpy as np

from .base import Metric
from .embeddings import embed_texts, cosine

class ContextRelevanceMetric(Metric):
    name = "context_relevance"

    def compute(self, sample: dict) -> float:
        query: str = sample["query"]
        contexts: List[str] = sample.get("retrieved_contexts", [])

        if not contexts:
            return 0.0

        # encode query and contexts using shared model
        q_emb = embed_texts([query])[0]
        ctx_embs = embed_texts(contexts)

        sims = [cosine(q_emb, ctx_emb) for ctx_emb in ctx_embs]
        return float(np.mean(sims))
