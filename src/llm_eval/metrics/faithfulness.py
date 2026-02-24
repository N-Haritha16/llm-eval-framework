# src/llm_eval/metrics/faithfulness.py

from typing import List
import numpy as np

from .base import Metric
from .embeddings import embed_texts, cosine

class FaithfulnessMetric(Metric):
    name = "faithfulness"

    def compute(self, sample: dict) -> float:
        answer: str = sample["model_answer"]
        contexts: List[str] = sample.get("retrieved_contexts", [])

        if not contexts:
            return 0.0

        ans_emb = embed_texts([answer])[0]
        ctx_embs = embed_texts(contexts)
        sims = [cosine(ans_emb, ctx_emb) for ctx_emb in ctx_embs]
        # average similarity as proxy for faithfulness
        return float(np.mean(sims))
