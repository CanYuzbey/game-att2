from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass
class SeededRNG:
    seed: int

    def __post_init__(self) -> None:
        self._random = random.Random(self.seed)

    def random(self) -> float:
        return self._random.random()

    def choice_weighted(self, values: Sequence[T], weights: Sequence[float]) -> T:
        if len(values) != len(weights) or not values:
            raise ValueError("values/weights must have same non-zero length")
        total = sum(weights)
        if total <= 0:
            raise ValueError("weight total must be positive")
        roll = self.random() * total
        upto = 0.0
        for value, weight in zip(values, weights, strict=True):
            upto += weight
            if roll < upto:
                return value
        return values[-1]
