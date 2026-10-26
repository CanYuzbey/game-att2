from __future__ import annotations

from dataclasses import dataclass

from .model import DefenceResponse, RoundBudget, ThreatClass


@dataclass(frozen=True)
class DefenceResult:
    legal: bool
    response: DefenceResponse
    consequence_prevented: bool
    reason: str


def resolve_defence(
    threat: ThreatClass,
    response: DefenceResponse,
    success: bool,
) -> DefenceResult:
    if threat is ThreatClass.YELLOW:
        if response not in (DefenceResponse.BLOCK, DefenceResponse.PARRY):
            return DefenceResult(False, response, False, "yellow_requires_block_or_parry")
        if response is DefenceResponse.BLOCK:
            return DefenceResult(True, response, False, "block_redirects_consequence_to_guard_source")
        return DefenceResult(
            True,
            response,
            success,
            "parry_success" if success else "parry_miss_original_consequence",
        )

    if response is not DefenceResponse.EVADE:
        return DefenceResult(False, response, False, "red_requires_evade")
    return DefenceResult(
        True,
        response,
        success,
        "evade_success" if success else "evade_miss_original_consequence",
    )


def commit_preparation(budget: RoundBudget, inventory_origin: bool = False) -> None:
    budget.spend_preparation()
    if inventory_origin:
        budget.spend_inventory_action()


def commit_main(budget: RoundBudget, inventory_origin: bool = False) -> None:
    budget.spend_main()
    if inventory_origin:
        budget.spend_inventory_action()
