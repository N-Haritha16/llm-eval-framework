from bert_score import score


class BertScoreMetric:
    """
    Computes BERTScore F1
    """

    def compute(self, predictions, references):
        _, _, f1 = score(predictions, references, lang="en", verbose=False)
        return float(f1.mean())
