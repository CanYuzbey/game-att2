"""Structured event recording; rendering belongs to reporting.py."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .enums import Phase
from .models import Event


@dataclass
class EventLog:
    events: list[Event] = field(default_factory=list)
    round_number: int = 0
    phase: Phase = Phase.START

    def set_phase(self, phase: Phase) -> None:
        self.phase = phase

    def next_round(self) -> None:
        self.round_number += 1
        self.phase = Phase.START

    def emit(
        self,
        event_type: str,
        actor_id: str | None = None,
        target_id: str | None = None,
        **payload: Any,
    ) -> Event:
        event = Event(
            sequence=len(self.events) + 1,
            round_number=self.round_number,
            phase=self.phase.value,
            event_type=event_type,
            actor_id=actor_id,
            target_id=target_id,
            payload=payload,
        )
        self.events.append(event)
        return event
