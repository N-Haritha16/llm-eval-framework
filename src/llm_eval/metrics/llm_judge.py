# src/llm_eval/metrics/llm_judge.py
import json
import os
import time
from typing import Dict, Any

from anthropic import Anthropic
from llm_eval.llm_judge_prompts import JUDGE_PROMPT  # your prompt file


class LLMJudgeMetric:
    def __init__(self, model: str = "claude-3-haiku-20240307", max_retries: int = 3):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY not set")
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.max_retries = max_retries

    def _call_api(self, prompt: str) -> Dict[str, float]:
        last_err = None
        for attempt in range(self.max_retries):
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=256,
                    temperature=0.0,
                    messages=[{"role": "user", "content": prompt}],
                )
                # Anthropic v1 returns content as a list of blocks
                content = resp.content[0].text
                return json.loads(content)
            except Exception as e:
                last_err = e
                time.sleep(2 ** attempt)
        raise RuntimeError(f"LLMJudge failed after retries: {last_err}")

    def compute(self, sample: Dict[str, Any]) -> Dict[str, float]:
        prompt = JUDGE_PROMPT.format(
            question=sample["query"],
            context="\n".join(sample.get("retrieved_contexts", [])),
            answer=sample["model_answer"],
        )
        scores = self._call_api(prompt)
        return {
            "coherence": scores["coherence"] / 5.0,
            "relevance": scores["relevance"] / 5.0,
            "safety": scores["safety"] / 5.0,
        }
