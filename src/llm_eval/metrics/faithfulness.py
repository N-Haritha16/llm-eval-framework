# src/llm_eval/metrics/faithfulness.py
class FaithfulnessMetric:
    def __init__(self):
        self.model = get_embedding_model()

    def compute(self, answer: str, contexts: list[str]) -> float:
        if not contexts:
            return 0.0
        ctx_text = " ".join(contexts)
        ctx_emb = self.model.encode([ctx_text])
        a_emb = self.model.encode([answer])
        sim = cosine_similarity(ctx_emb, a_emb)[0][0]
        return float(sim)
