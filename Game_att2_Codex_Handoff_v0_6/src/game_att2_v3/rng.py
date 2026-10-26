from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class WeightedChoice:
    index: int
    roll: float
    total_weight: float


@dataclass
class SeededRNG:
    seed: int

    def __post_init__(self) -> None:
        self._random = random.Random(self.seed)

    def random(self) -> float:
        return self._random.random()

    def choice_weighted_with_trace(
        self, values: Sequence[T], weights: Sequence[float]
    ) -> tuple[T, WeightedChoice]:
        if len(values) != len(weights) or not values:
            raise ValueError("values/weights must have same non-zero length")
        total = sum(weights)
        if total <= 0:
            raise ValueError("weight total must be positive")
        roll = self.random() * total
        upto = 0.0
        for index, (value, weight) in enumerate(zip(values, weights, strict=True)):
            upto += weight
            if roll < upto:
                return value, WeightedChoice(index=index, roll=roll, total_weight=total)
        index = len(values) - 1
        return values[index], WeightedChoice(index=index, roll=roll, total_weight=total)

    def choice_weighted(self, values: Sequence[T], weights: Sequence[float]) -> T:
        value, _trace = self.choice_weighted_with_trace(values, weights)
        return value
