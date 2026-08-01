"""Reusable deterministic selection among state-derived legal enemy intents."""

from __future__ import annotations

from dataclasses import dataclass, replace

from .enums import Slot


@dataclass(frozen=True)
class IntentCandidate:
    action_id: str
    source_slot: Slot | None
    target_slot: Slot | None
    score: int
    reasons: tuple[str, ...]
    public_text: str
    exact_text: str
    legal: bool = True
    exclusion_reason: str | None = None


@dataclass(frozen=True)
class IntentSelection:
    candidate: IntentCandidate
    final_score: int


def select_intent(
    candidates: tuple[IntentCandidate, ...],
    *,
    last_action_id: str | None,
    last_target_slot: Slot | None,
    repetition_penalty: int,
) -> IntentSelection | None:
    """Choose the highest utility legal intent with stable deterministic ties."""
    if repetition_penalty < 0:
        raise ValueError("repetition_penalty must not be negative")
    scored: list[IntentSelection] = []
    for candidate in candidates:
        if not candidate.legal:
            continue
        repeated = (
            candidate.action_id == last_action_id
            and candidate.target_slot == last_target_slot
        )
        penalty = repetition_penalty if repeated else 0
        adjusted = replace(
            candidate,
            reasons=(
                *candidate.reasons,
                *(("repeat penalty applied",) if repeated else ()),
            ),
        )
        scored.append(IntentSelection(adjusted, candidate.score - penalty))
    if not scored:
        return None
    return min(
        scored,
        key=lambda selection: (
            -selection.final_score,
            selection.candidate.action_id,
            selection.candidate.source_slot.value
            if selection.candidate.source_slot is not None
            else "",
            selection.candidate.target_slot.value
            if selection.candidate.target_slot is not None
            else "",
        ),
    )
