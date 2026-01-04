from abc import ABC, abstractmethod

class Metric(ABC):
    name: str

    @abstractmethod
    def compute(self, sample: dict) -> float:
        ...
