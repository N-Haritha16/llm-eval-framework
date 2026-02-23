from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class MetricBase(ABC):
    name: str

    @abstractmethod
    def compute(self, sample: Dict[str, Any]) -> float:
        raise NotImplementedError
