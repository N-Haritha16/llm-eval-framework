# src/llm_eval/metrics/answer_relevance.py
class AnswerRelevanceMetric:
    def __init__(self):
        self.model = get_embedding_model()

    def compute(self, query: str, answer: str) -> float:
        q_emb = self.model.encode([query])
        a_emb = self.model.encode([answer])
        sim = cosine_similarity(q_emb, a_emb)[0][0]
        return float(sim)
