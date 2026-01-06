from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


class BleuMetric:
    name = "bleu"

    def compute(self, predictions, references):
        """
        Supports:
        - single sample dict (unit tests)
        - list[str] predictions + list[str] references (pipeline)
        """
        smoothie = SmoothingFunction().method1

        # ---- Case 1: unit test (single sample dict) ----
        if isinstance(predictions, dict):
            return sentence_bleu(
                [references.split()],
                predictions["model_answer"].split(),
                smoothing_function=smoothie
            )

        # ---- Case 2: pipeline (list inputs) ----
        scores = []
        for pred, ref in zip(predictions, references):
            score = sentence_bleu(
                [ref.split()],
                pred.split(),
                smoothing_function=smoothie
            )
            scores.append(score)

        return sum(scores) / len(scores)
