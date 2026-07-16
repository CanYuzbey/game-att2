"""Construction of independent runtime state from immutable loaded data."""

from __future__ import annotations

from typing import cast

from .config_loader import SimulatorConfig
from .enums import LimbState, Slot
from .errors import ConfigValidationError
from .models import BodyRuntime, CombatantRuntime, LimbDefinition, LimbRuntime


def limb_runtime(definition: LimbDefinition) -> LimbRuntime:
    integrity = 0 if definition.initial_state is LimbState.MISSING else definition.max_integrity
    return LimbRuntime(definition=definition, integrity=integrity, state=definition.initial_state)


def player_from_start(config: SimulatorConfig, body_id: str = "s001") -> CombatantRuntime:
    raw = config.starting_bodies.get(body_id)
    if raw is None:
        raise ConfigValidationError(f"unknown starting body: {body_id}")
    slots = {Slot(slot): limb_runtime(config.limbs[limb_id]) for slot, limb_id in raw["slots"].items()}
    return CombatantRuntime(
        id=body_id,
        name=str(raw["name"]),
        body=BodyRuntime(slots),
        blood=int(cast(int, raw["blood"])),
        inventory={key: int(cast(int, value)) for key, value in raw.get("inventory", {}).items()},
        role="player",
    )


def _inline_limb(slot: Slot, raw: dict[str, object]) -> LimbRuntime:
    definition = LimbDefinition(
        id=f"inline_{slot.value}_{str(raw.get('name', 'limb')).lower().replace(' ', '_')}",
        name=str(raw.get("name", "Unnamed Limb")),
        slot=slot,
        max_integrity=int(cast(int, raw["max_integrity"])),
        size=str(raw["size"]),
    )
    return limb_runtime(definition)


def enemy_from_config(config: SimulatorConfig, enemy_id: str) -> CombatantRuntime:
    raw = config.enemies.get(enemy_id)
    if raw is None:
        raise ConfigValidationError(f"unknown enemy: {enemy_id}")
    slots: dict[Slot, LimbRuntime] = {}
    for slot_name, limb_raw in raw["limbs"].items():
        slot = Slot(slot_name)
        if "definition" in limb_raw:
            definition = config.limbs[str(limb_raw["definition"])]
            slots[slot] = limb_runtime(definition)
        else:
            slots[slot] = _inline_limb(slot, limb_raw)
    return CombatantRuntime(
        id=enemy_id,
        name=str(raw["name"]),
        body=BodyRuntime(slots),
        blood=int(cast(int, raw["blood"])),
        inventory={},
        role="enemy",
    )


def refresh_fight_tools(player: CombatantRuntime) -> None:
    """One-use tools refresh per fight; consumables deliberately do not."""
    player.inventory["bone_scissors"] = 1
    player.inventory["hell_saw"] = 1


def body_summary(actor: CombatantRuntime) -> dict[str, str]:
    return {
        slot.value: f"{limb.name} - {limb.state.value}"
        + (f" ({', '.join(sorted(tag.value for tag in limb.tags))})" if limb.tags else "")
        for slot, limb in actor.body.slots.items()
    }
