from rouge_score import rouge_scorer


class RougeLMetric:
    """
    Computes ROUGE-L score for generated text vs reference text
    """

    def __init__(self):
        self.scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

    def compute(self, predictions, references):
        scores = []
        for pred, ref in zip(predictions, references):
            score = self.scorer.score(ref, pred)
            scores.append(score["rougeL"].fmeasure)
        return sum(scores) / len(scores)
