"""Injected randomness. Domain code never imports module-global random."""

from __future__ import annotations

import random
from collections.abc import Sequence
from typing import Protocol, TypeVar

T = TypeVar("T")


class RNGService(Protocol):
    def randint(self, lower: int, upper: int) -> int: ...

    def choice(self, values: Sequence[T]) -> T: ...

    def state_token(self) -> object: ...


class SeededRNG:
    def __init__(self, seed: int) -> None:
        self.seed = seed
        self._random = random.Random(seed)

    def randint(self, lower: int, upper: int) -> int:
        return self._random.randint(lower, upper)

    def choice(self, values: Sequence[T]) -> T:
        if not values:
            raise ValueError("choice requires at least one value")
        return self._random.choice(values)

    def state_token(self) -> object:
        return self._random.getstate()


class ScriptedRNG:
    """Test RNG which consumes supplied d6 outcomes before using a fallback."""

    def __init__(self, rolls: Sequence[int], fallback: int = 6) -> None:
        self._rolls = list(rolls)
        self._fallback = fallback

    def randint(self, lower: int, upper: int) -> int:
        value = self._rolls.pop(0) if self._rolls else self._fallback
        if not lower <= value <= upper:
            raise ValueError(f"scripted roll {value} outside [{lower}, {upper}]")
        return value

    def choice(self, values: Sequence[T]) -> T:
        if not values:
            raise ValueError("choice requires at least one value")
        index = self.randint(0, len(values) - 1)
        return values[index]

    def state_token(self) -> object:
        return tuple(self._rolls), self._fallback
