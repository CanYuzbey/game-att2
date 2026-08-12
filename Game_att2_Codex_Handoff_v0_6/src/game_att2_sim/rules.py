"""Rule systems with narrow, event-only side effects."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

from .config_loader import SimulatorConfig
from .enums import HarvestQuality, LimbState, LimbTag, Phase, Slot, UnstableResult
from .errors import IllegalActionError, InsufficientBloodError, InvalidTargetError
from .events import EventLog
from .models import (
    ActionAvailability,
    CombatantRuntime,
    HarvestedLimb,
    LimbRuntime,
    ScenarioMetrics,
)
from .reflex import AttackModifier
from .rng import RNGService


def is_usable(limb: LimbRuntime) -> bool:
    return limb.state in {LimbState.INTACT, LimbState.DAMAGED, LimbState.CRITICAL}


def effectiveness(limb: LimbRuntime) -> Decimal:
    if limb.state is LimbState.INTACT:
        return Decimal(1)
    if limb.state is LimbState.DAMAGED:
        return Decimal("0.75")
    if limb.state is LimbState.CRITICAL:
        return Decimal("0.5")
    return Decimal(0)


def round_half_up(value: Decimal) -> int:
    return int(value.quantize(Decimal(1), rounding=ROUND_HALF_UP))


def recalculate_state(limb: LimbRuntime) -> LimbState:
    if limb.integrity <= 0:
        return limb.state
    ratio = limb.integrity / limb.definition.max_integrity
    if ratio > 0.70:
        return LimbState.INTACT
    if ratio > 0.35:
        return LimbState.DAMAGED
    return LimbState.CRITICAL


def _record_state(
    limb: LimbRuntime, old: LimbState, log: EventLog, actor: CombatantRuntime, reason: str
) -> None:
    if old is not limb.state:
        log.emit(
            "limb_state_changed",
            actor.id,
            slot=limb.slot.value,
            limb=limb.name,
            old=old.value,
            new=limb.state.value,
            reason=reason,
        )


def spend_blood(
    actor: CombatantRuntime,
    amount: int,
    reason: str,
    config: SimulatorConfig,
    log: EventLog,
    metrics: ScenarioMetrics,
    tutorial: bool = False,
    rng: RNGService | None = None,
) -> None:
    if amount < 0:
        raise ValueError("spend amount cannot be negative")
    if actor.blood < amount:
        raise InsufficientBloodError(f"{actor.name} needs {amount} blood for {reason}")
    before = actor.blood
    actor.blood -= amount
    metrics.blood_spent += amount
    log.emit("blood_changed", actor.id, reason=reason, before=before, delta=-amount, after=actor.blood)
    _thresholds(actor, before, config, log, metrics, tutorial, rng)


def lose_blood(actor: CombatantRuntime, amount: int, reason: str, config: SimulatorConfig, log: EventLog, metrics: ScenarioMetrics, tutorial: bool, rng: RNGService) -> None:
    """Involuntary loss may reduce Blood to zero; voluntary spends remain affordability-checked."""
    before = actor.blood
    actor.blood = max(0, actor.blood - amount)
    metrics.blood_spent += before - actor.blood
    log.emit("blood_changed", actor.id, reason=reason, before=before, delta=actor.blood - before, after=actor.blood)
    _thresholds(actor, before, config, log, metrics, tutorial, rng)


def gain_blood(
    actor: CombatantRuntime,
    amount: int,
    reason: str,
    config: SimulatorConfig,
    log: EventLog,
    metrics: ScenarioMetrics,
) -> None:
    if amount < 0:
        raise ValueError("gain amount cannot be negative")
    before = actor.blood
    actor.blood += amount
    metrics.blood_gained += amount
    log.emit("blood_changed", actor.id, reason=reason, before=before, delta=amount, after=actor.blood)


def _thresholds(
    actor: CombatantRuntime,
    before: int,
    config: SimulatorConfig,
    log: EventLog,
    metrics: ScenarioMetrics,
    tutorial: bool,
    rng: RNGService | None,
) -> None:
    pulse = config.rules["panic_pulse"]
    if (
        actor.role == "player"
        and not actor.panic_pulse_used
        and before >= pulse["trigger_below"]
        and actor.blood < pulse["trigger_below"]
    ):
        actor.panic_pulse_used = True
        gained = min(pulse["gain"], pulse["cap"] - actor.blood)
        gain_blood(actor, gained, "Panic Pulse", config, log, metrics)
        log.emit("panic_pulse", actor.id, gained=gained)
    if actor.blood <= config.rules["blood"]["death_at"]:
        _resolve_zero_blood(actor, config, log, metrics, tutorial, rng)


def _resolve_zero_blood(
    actor: CombatantRuntime,
    config: SimulatorConfig,
    log: EventLog,
    metrics: ScenarioMetrics,
    tutorial: bool,
    rng: RNGService | None,
) -> None:
    if (
        tutorial
        and bool(config.rules["limb_for_life"]["enabled"])
        and actor.role == "player"
        and not actor.limb_for_life_used
        and rng is not None
    ):
        candidates = [
            limb
            for slot, limb in actor.body.slots.items()
            if slot is not Slot.CORE and is_usable(limb)
        ]
        if candidates:
            limb = rng.choice(candidates)
            old = limb.state
            limb.integrity = 0
            limb.state = LimbState.SEVERED
            actor.limb_for_life_used = True
            actor.blood = config.rules["limb_for_life"]["restore_blood"]
            _record_state(limb, old, log, actor, "Limb for Life")
            log.emit(
                "limb_for_life",
                actor.id,
                slot=limb.slot.value,
                restored_blood=actor.blood,
                death_prevented=True,
                selection=str(config.rules["limb_for_life"]["sacrifice_selection"]),
            )
            return
    actor.collapsed = True
    actor.dead = True
    log.emit("death", actor.id, blood=actor.blood, reason="Blood reached zero")


def apply_damage(
    owner: CombatantRuntime,
    target: LimbRuntime,
    amount: int,
    reason: str,
    log: EventLog,
    clean: bool = False,
) -> HarvestQuality | None:
    if amount < 0:
        raise ValueError("damage cannot be negative")
    old_state = target.state
    before = target.integrity
    target.integrity = max(0, target.integrity - amount)
    quality: HarvestQuality | None = None
    if target.integrity == 0:
        if clean:
            target.state = LimbState.SEVERED
            quality = HarvestQuality.CLEAN
        else:
            target.state = LimbState.RUINED
            quality = HarvestQuality.RUINED
    else:
        target.state = recalculate_state(target)
    log.emit(
        "limb_damaged",
        owner.id,
        slot=target.slot.value,
        limb=target.name,
        reason=reason,
        before=before,
        damage=amount,
        after=target.integrity,
    )
    _record_state(target, old_state, log, owner, reason)
    return quality


def require_source(actor: CombatantRuntime, slot: Slot) -> LimbRuntime:
    limb = actor.body.slots[slot]
    if not is_usable(limb):
        raise IllegalActionError(f"{actor.name}'s {slot.value} cannot source an action")
    return limb


def action_damage(actor: CombatantRuntime, source: LimbRuntime, base: int) -> int:
    return round_half_up(Decimal(base) * effectiveness(source))


@dataclass
class RuleEngine:
    config: SimulatorConfig
    rng: RNGService
    log: EventLog
    metrics: ScenarioMetrics
    tutorial: bool = False

    def main_action_availability(
        self,
        actor: CombatantRuntime,
        action_id: str,
        target: LimbRuntime | None = None,
    ) -> ActionAvailability:
        """Return the rules-owned affordance for one approved Main action."""
        label = action_id.replace("_", " ").title()
        source_slot: Slot | None = None
        cost = 0
        reason: str | None = None
        risk: str | None = None
        allow_downed = action_id == "stand"
        if actor.normal_action_consumed:
            reason = "Main action already consumed this round"
        elif actor.downed and not allow_downed:
            reason = "Downed requires Stand"
        elif action_id == "stand":
            if not actor.downed:
                reason = "Stand requires Downed"
        elif action_id == "grip_strike":
            source_slot = Slot.LEFT_ARM
            if not is_usable(actor.body.slots[source_slot]):
                reason = "Left Arm source is unavailable"
        elif action_id == "claim_the_cut":
            cost = int(self.config.items["claim_the_cut"]["cost"])
            if actor.inventory.get("claim_the_cut", 0) <= 0:
                reason = "Claim the Cut is unavailable"
            elif actor.blood < cost:
                reason = f"Requires {cost} Blood"
        elif action_id == "bone_scissors":
            cost = int(self.config.items["bone_scissors"]["cost"])
            if actor.inventory.get("bone_scissors", 0) <= 0:
                reason = "Bone Scissors already used this fight"
            elif target is None:
                reason = "A target limb is required"
            elif target.definition.size not in self.config.items["bone_scissors"]["valid_sizes"]:
                reason = "Target is too large for Bone Scissors"
            elif target.state not in {LimbState.DAMAGED, LimbState.CRITICAL}:
                reason = "Target must be Damaged or Critical"
            elif actor.blood < cost:
                reason = f"Requires {cost} Blood"
            risk = "Stabilized targets may resist severing"
        elif action_id == "hell_saw":
            cost = int(self.config.items["hell_saw"]["cost"])
            if actor.inventory.get("hell_saw", 0) <= 0:
                reason = "Hell Saw already used this fight"
            elif target is None:
                reason = "A target limb is required"
            elif target.definition.size != "large":
                reason = "Hell Saw requires a Large target"
            elif actor.blood < cost:
                reason = f"Requires {cost} Blood"
            risk = "Damaged/Critical Large targets use the configured sever roll"
        elif action_id == "guard_flesh":
            source_slot = Slot.RIGHT_ARM
            arm = actor.body.slots[source_slot]
            if not is_usable(arm):
                reason = "Right Arm source is unavailable"
            else:
                cost = self._limb_action_cost_amount(
                    arm, self.config.actions["guard_flesh"].cost
                )
                if actor.blood < cost:
                    reason = f"Requires {cost} Blood"
        elif action_id == "brace":
            source_slot = Slot.LEGS
            if not is_usable(actor.body.slots[source_slot]):
                reason = "Legs source is unavailable"
            elif actor.brace_used:
                reason = "Brace already used this encounter"
        else:
            reason = "Action is not an approved Main action"
        return ActionAvailability(
            action_id=action_id,
            label=label,
            timing="main",
            enabled=reason is None,
            reason=reason,
            cost=cost,
            source_slot=source_slot,
            target_slot=target.slot if target is not None else None,
            irreversible=True,
            risk=risk,
        )

    def focus_availability(self, actor: CombatantRuntime) -> ActionAvailability:
        reason: str | None = None
        cost = int(self.config.rules["focus"]["base_cost"])
        head = actor.body.slots[Slot.HEAD]
        if actor.downed:
            reason = "Focus is unavailable while Downed"
        elif actor.normal_action_consumed:
            reason = "Focus must occur before the Main action"
        elif not is_usable(head):
            reason = "Head source is unavailable"
        elif head.focused_round == self.log.round_number:
            reason = "Focus already used this round"
        else:
            if head.state is LimbState.DAMAGED:
                cost += int(self.config.rules["focus"]["damaged_head_extra_cost"])
            if actor.blood < cost:
                reason = f"Requires {cost} Blood"
        return ActionAvailability(
            "focus",
            "Focus",
            "focus",
            reason is None,
            reason,
            cost,
            Slot.HEAD,
            irreversible=False,
            risk="Critical Head may reveal incomplete information",
        )

    def fast_item_availability(
        self, actor: CombatantRuntime, item_id: str, target: LimbRuntime | None = None
    ) -> ActionAvailability:
        item = self.config.items[item_id]
        reason: str | None = None
        cost = int(item.get("cost", 0))
        if actor.normal_action_consumed:
            reason = "Fast item must occur before the Main action"
        elif actor.inventory.get("_fast_round", -1) == self.log.round_number:
            reason = "Fast item already used this round"
        elif actor.inventory.get(item_id, 0) <= 0 or not item.get("available", True):
            reason = f"{item['name']} is unavailable"
        elif item_id == "clotting_cream" and (
            target is None or LimbTag.BLEEDING not in target.tags
        ):
            reason = "Requires a Bleeding target"
        elif actor.blood < cost:
            reason = f"Requires {cost} Blood"
        return ActionAvailability(
            item_id,
            str(item["name"]),
            "fast",
            reason is None,
            reason,
            cost,
            target_slot=target.slot if target is not None else None,
            irreversible=False,
        )

    def table_availability(
        self, actor: CombatantRuntime, choice: str
    ) -> ActionAvailability:
        option = self.config.table_options[choice]
        cost = int(option.get("cost", 0))
        reason: str | None = None
        if choice == "integrate_arm" and LimbTag.GRAFTED not in actor.body.slots[
            Slot.RIGHT_ARM
        ].tags:
            reason = "Requires a Grafted Right Arm"
        elif actor.blood < cost:
            reason = f"Requires {cost} Blood"
        return ActionAvailability(
            f"table:{choice}",
            str(option["name"]),
            "table",
            reason is None,
            reason,
            cost,
            irreversible=True,
        )

    def anna_trade_available(
        self, player: CombatantRuntime, anna: CombatantRuntime
    ) -> tuple[bool, str | None]:
        graft = player.body.slots[Slot.RIGHT_ARM]
        bleeding = any(LimbTag.BLEEDING in limb.tags for limb in player.body.slots.values())
        threatened = (
            anna.body.slots[Slot.RIGHT_ARM].state in {LimbState.DAMAGED, LimbState.CRITICAL}
            or LimbTag.MARKED in anna.body.slots[Slot.RIGHT_ARM].tags
        )
        if LimbTag.UNSTABLE in graft.tags or bleeding or threatened:
            return True, None
        return False, "Requires an Unstable graft, Bleeding, or threatened Crude Graft Arm"

    def start_round(self, player: CombatantRuntime) -> None:
        self.end_round(player)
        self.log.next_round()
        self.metrics.rounds = self.log.round_number
        self.log.set_phase(Phase.START)
        player.normal_action_consumed = False
        if player.blood <= self.config.rules["blood"]["critical_max"]:
            self.metrics.critical_rounds += 1
        for limb in player.body.slots.values():
            if limb.disabled_rounds:
                limb.disabled_rounds -= 1
                if limb.disabled_rounds == 0 and limb.state is LimbState.DISABLED:
                    old = limb.state
                    limb.state = recalculate_state(limb)
                    _record_state(limb, old, self.log, player, "temporary disable expired")
            if LimbTag.BLEEDING in limb.tags:
                lose_blood(player, self.config.rules["bleeding"]["basic_loss"], "Bleeding", self.config, self.log, self.metrics, self.tutorial, self.rng)
        self.unstable_checks(player)

    def start_encounter(self, player: CombatantRuntime) -> None:
        legs = player.body.slots[Slot.LEGS]
        player.brace_charges = int(legs.definition.id == "braced_human_legs" and is_usable(legs))
        player.brace_used = False
        player.brace_active = False
        self.log.emit("brace_reset", player.id, before=player.brace_charges, after=player.brace_charges)

    def resolve_knockdown(self, player: CombatantRuntime, source: str, roll: int, threshold: int = 4) -> bool:
        before = player.brace_charges
        self.log.emit("knockdown_attempted", source, target_id=player.id, roll=roll, threshold=threshold, brace_before=before, downed_before=player.downed)
        if roll < threshold:
            self.log.emit("knockdown_failed", source, target_id=player.id, roll=roll, threshold=threshold, brace_after=player.brace_charges)
            return False
        if not player.downed and player.brace_active:
            player.brace_active = False
            self.log.emit(
                "knockdown_prevented_by_active_brace",
                source,
                target_id=player.id,
                downed_after=False,
            )
            return False
        legs = player.body.slots[Slot.LEGS]
        if not player.downed and player.brace_charges and is_usable(legs):
            player.brace_charges -= 1
            self.log.emit("knockdown_prevented_by_brace", source, target_id=player.id, brace_before=before, brace_after=player.brace_charges, downed_after=False)
            return False
        if player.downed:
            self.log.emit("knockdown_failed", source, target_id=player.id, reason="already_downed", brace_after=player.brace_charges)
            return False
        player.downed = True
        self.log.emit("downed_applied", source, target_id=player.id, downed_before=False, downed_after=True)
        return True

    def stand(self, player: CombatantRuntime) -> None:
        self._require_main_action(player, "Stand", allow_downed=True)
        if not player.downed:
            raise IllegalActionError("Stand requires Downed")
        self._commit_main_action(player, "stand", allow_downed=True)
        player.downed = False
        self.log.emit("stand_performed", player.id, action_consumed=True, downed_after=False)

    def _require_main_action(
        self, actor: CombatantRuntime, action: str, *, allow_downed: bool = False
    ) -> None:
        if actor.downed and not allow_downed:
            self.log.emit(
                "main_action_rejected",
                actor.id,
                action=action,
                reason="downed",
                action_consumed=actor.normal_action_consumed,
            )
            raise IllegalActionError(f"{action} is unavailable while Downed")
        if actor.normal_action_consumed:
            self.log.emit(
                "main_action_rejected",
                actor.id,
                action=action,
                reason="main_action_already_consumed",
                action_consumed=True,
            )
            raise IllegalActionError(f"{action} is unavailable after the Main action was consumed")

    def _require_pre_main_window(self, actor: CombatantRuntime, action: str) -> None:
        if actor.downed or actor.normal_action_consumed:
            reason = "downed" if actor.downed else "main_action_already_consumed"
            self.log.emit(
                "pre_main_action_rejected",
                actor.id,
                action=action,
                reason=reason,
                action_consumed=actor.normal_action_consumed,
            )
            raise IllegalActionError(f"{action} is only available before the Main action")

    def _require_affordable(self, actor: CombatantRuntime, amount: int, reason: str) -> None:
        if actor.blood < amount:
            raise InsufficientBloodError(f"{actor.name} needs {amount} blood for {reason}")

    def _commit_main_action(
        self, actor: CombatantRuntime, action_id: str, *, allow_downed: bool = False
    ) -> None:
        """Commit one validated Main action before applying its approved effects."""
        self._require_main_action(actor, action_id, allow_downed=allow_downed)
        actor.normal_action_consumed = True
        self.log.set_phase(Phase.MAIN)
        self.log.emit("main_action_committed", actor.id, action=action_id)
        self._action(action_id)

    def end_round(self, player: CombatantRuntime) -> None:
        """Own expiry and benefits that resolve at the round boundary."""
        self.log.set_phase(Phase.END)
        if player.guard_active:
            player.guard_active = False
            self.log.emit("guard_expired", player.id, reason="unused_at_end_of_round")
        if player.brace_active:
            player.brace_active = False
            self.log.emit("brace_expired", player.id, reason="unused_at_end_of_round")
        for limb in player.body.slots.values():
            if limb.surge_unused:
                limb.surge_unused = False
                gain_blood(
                    player,
                    self.config.rules["unstable_graft"]["surge_unused_blood_gain"],
                    "Unstable Surge fallback",
                    self.config,
                    self.log,
                    self.metrics,
                )

    def unstable_checks(self, player: CombatantRuntime) -> None:
        for limb in player.body.slots.values():
            if LimbTag.UNSTABLE not in limb.tags or LimbTag.INTEGRATED in limb.tags:
                continue
            roll = self.rng.randint(1, 6)
            rules = self.config.rules["unstable_graft"]
            if roll in rules["twitch_rolls"]:
                limb.unstable_result = UnstableResult.TWITCH.value
            elif roll in rules["ache_rolls"]:
                limb.unstable_result = UnstableResult.ACHE.value
            elif roll in rules["surge_rolls"]:
                limb.unstable_result = UnstableResult.SURGE.value
                limb.surge_unused = True
            else:
                limb.unstable_result = UnstableResult.WORKS.value
            self.metrics.unstable_results += 1
            self.log.emit("unstable_check", player.id, slot=limb.slot.value, roll=roll, result=limb.unstable_result)

    def focus(self, player: CombatantRuntime, intent: str, exact: bool = True) -> str:
        self._require_pre_main_window(player, "Focus")
        self.log.set_phase(Phase.FOCUS)
        head = require_source(player, Slot.HEAD)
        if getattr(head, "focused_round", None) == self.log.round_number:
            raise IllegalActionError("Focus is limited to once per round")
        cost = self.config.rules["focus"]["base_cost"]
        if head.state is LimbState.DAMAGED:
            cost += self.config.rules["focus"]["damaged_head_extra_cost"]
        if head.state is LimbState.CRITICAL and self.rng.randint(1, 2) == 1:
            exact = False
        spend_blood(player, cost, "Focus", self.config, self.log, self.metrics, self.tutorial, self.rng)
        head.focused_round = self.log.round_number
        self.metrics.focus_used += 1
        revealed = intent if exact else "enemy intent is incomplete"
        self.log.emit("focus_resolved", player.id, cost=cost, intent=revealed, exact=exact)
        return revealed

    def fast_item(self, player: CombatantRuntime, item_id: str, target: LimbRuntime | None = None) -> None:
        if player.normal_action_consumed:
            self.log.emit(
                "pre_main_action_rejected",
                player.id,
                action=item_id,
                reason="main_action_already_consumed",
                action_consumed=True,
            )
            raise IllegalActionError(f"{item_id} is only available before the Main action")
        self.log.set_phase(Phase.FAST)
        if player.inventory.get("_fast_round", -1) == self.log.round_number:
            raise IllegalActionError("only one Fast item is allowed each round")
        if player.inventory.get(item_id, 0) <= 0:
            raise IllegalActionError(f"{item_id} is unavailable")
        item = self.config.items[item_id]
        if not item.get("available", True):
            raise IllegalActionError(f"{item_id} is unavailable in this configuration")
        if item_id == "clotting_cream":
            if target is None or LimbTag.BLEEDING not in target.tags:
                raise InvalidTargetError("Clotting Cream needs a Bleeding limb")
            self._require_affordable(player, item["cost"], "Clotting Cream")
        elif item_id != "blood_bag":
            raise IllegalActionError(f"{item_id} is not a Fast item")
        player.inventory[item_id] -= 1
        player.inventory["_fast_round"] = self.log.round_number
        self.metrics.fast_items_used += 1
        if item_id == "blood_bag":
            bleeding = any(LimbTag.BLEEDING in limb.tags for limb in player.body.slots.values())
            amount = item["gain_if_bleeding"] if bleeding else item["gain"]
            if "cap" in item:
                amount = min(amount, max(0, item["cap"] - player.blood))
            gain_blood(
                player,
                amount,
                "Blood Bag",
                self.config,
                self.log,
                self.metrics,
            )
            self.metrics.blood_bag_uses += 1
        elif item_id == "clotting_cream":
            assert target is not None
            spend_blood(player, item["cost"], "Clotting Cream", self.config, self.log, self.metrics, self.tutorial, self.rng)
            target.tags.remove(LimbTag.BLEEDING)
            self.log.emit("bleeding_removed", player.id, slot=target.slot.value)
        self.log.emit("fast_item_used", player.id, item=item_id)

    def claim(self, player: CombatantRuntime, target: LimbRuntime) -> None:
        self._require_main_action(player, "Claim the Cut")
        if player.inventory.get("claim_the_cut", 0) <= 0:
            raise IllegalActionError("Claim the Cut is unavailable")
        cost = self.config.items["claim_the_cut"]["cost"]
        self._require_affordable(player, cost, "Claim the Cut")
        self._commit_main_action(player, "claim_the_cut")
        spend_blood(player, cost, "Claim the Cut", self.config, self.log, self.metrics, self.tutorial, self.rng)
        player.inventory["claim_the_cut"] -= 1
        target.tags.add(LimbTag.MARKED)
        self.log.emit("limb_marked", player.id, slot=target.slot.value, target=target.name)

    def grip(self, player: CombatantRuntime, target_owner: CombatantRuntime, target: LimbRuntime) -> HarvestQuality | None:
        self._require_main_action(player, "Grip Strike")
        source = require_source(player, Slot.LEFT_ARM)
        damage = action_damage(player, source, self.config.actions["grip_strike"].damage)
        self._commit_main_action(player, "grip_strike")
        return apply_damage(target_owner, target, damage, "Grip Strike", self.log, clean=False)

    def scissors(self, player: CombatantRuntime, target_owner: CombatantRuntime, target: LimbRuntime) -> HarvestQuality | None:
        self._require_main_action(player, "Bone Scissors")
        if player.inventory.get("bone_scissors", 0) <= 0:
            raise IllegalActionError("Bone Scissors already used this fight")
        item = self.config.items["bone_scissors"]
        if target.definition.size not in item["valid_sizes"]:
            raise InvalidTargetError("Bone Scissors are invalid against this limb size")
        if target.state not in {LimbState.DAMAGED, LimbState.CRITICAL}:
            raise InvalidTargetError("Bone Scissors require a Damaged or Critical limb")
        self._require_affordable(player, item["cost"], "Bone Scissors")
        self._commit_main_action(player, "bone_scissors")
        spend_blood(player, item["cost"], "Bone Scissors", self.config, self.log, self.metrics, self.tutorial, self.rng)
        player.inventory["bone_scissors"] -= 1
        if LimbTag.STABILIZED in target.tags:
            roll = self.rng.randint(1, 6)
            self.log.emit("stabilized_sever_roll", player.id, slot=target.slot.value, roll=roll, success=roll in self.config.rules["stabilized"]["sever_success_rolls"])
            target.tags.remove(LimbTag.STABILIZED)
            if roll not in self.config.rules["stabilized"]["sever_success_rolls"]:
                old = target.state
                target.state = LimbState.DISABLED
                target.tags.add(LimbTag.HANGING)
                _record_state(target, old, self.log, target_owner, "Stabilized sever failed")
                return None
        if target.state is LimbState.CRITICAL:
            quality = apply_damage(target_owner, target, target.integrity, "Bone Scissors", self.log, clean=True)
            if quality is HarvestQuality.CLEAN and target.slot is not Slot.CORE:
                self.add_plead_pressure(target_owner, "major limb cleanly severed")
            return quality
        if target.state is LimbState.DAMAGED:
            return apply_damage(target_owner, target, item["damaged_damage"], "Bone Scissors", self.log, clean=False)
        raise AssertionError("validated Bone Scissors target changed before resolution")

    def saw(self, player: CombatantRuntime, target_owner: CombatantRuntime, target: LimbRuntime) -> HarvestQuality | None:
        self._require_main_action(player, "Hell Saw")
        if player.inventory.get("hell_saw", 0) <= 0:
            raise IllegalActionError("Hell Saw already used this fight")
        item = self.config.items["hell_saw"]
        if target.definition.size != "large":
            raise InvalidTargetError("Hell Saw only targets large limbs in v0.1")
        self._require_affordable(player, item["cost"], "Hell Saw")
        self._commit_main_action(player, "hell_saw")
        spend_blood(player, item["cost"], "Hell Saw", self.config, self.log, self.metrics, self.tutorial, self.rng)
        player.inventory["hell_saw"] -= 1
        valid = target.state in {LimbState.DAMAGED, LimbState.CRITICAL}
        roll = self.rng.randint(1, 6) if valid else 0
        self.log.emit("hell_saw_roll", player.id, slot=target.slot.value, roll=roll, valid=valid)
        if valid and roll in item["sever_success_rolls"]:
            apply_damage(target_owner, target, target.integrity, "Hell Saw", self.log, clean=True)
            quality = HarvestQuality.CLEAN if LimbTag.MARKED in target.tags else HarvestQuality.STRESSED
            if quality is HarvestQuality.CLEAN and target.slot is not Slot.CORE:
                self.add_plead_pressure(target_owner, "major limb cleanly severed")
            return quality
        apply_damage(target_owner, target, item["damage"], "Hell Saw", self.log, clean=False)
        target_owner.rage = True
        self.log.emit("rage_gained", target_owner.id, bonus=item["rage_bonus"])
        return None

    def salvage(self, player: CombatantRuntime, target: LimbRuntime) -> HarvestedLimb | None:
        """Recover a compromised limb using the configured emergency salvage tables."""
        if target.state not in {LimbState.RUINED, LimbState.DISABLED} and LimbTag.HANGING not in target.tags:
            raise InvalidTargetError("salvage requires a Ruined, Disabled, or Hanging limb")
        marked = LimbTag.MARKED in target.tags
        rules = self.config.rules["harvest"]
        cost_key = "marked_salvage_cost" if marked else "unmarked_salvage_cost"
        spend_blood(player, rules[cost_key], "Emergency Salvage", self.config, self.log, self.metrics, self.tutorial, self.rng)
        roll = self.rng.randint(1, 6)
        prefix = "marked_salvage" if marked else "unmarked_salvage"
        if roll in rules[f"{prefix}_unusable_rolls"]:
            self.log.emit("salvage_failed", player.id, slot=target.slot.value, roll=roll, marked=marked)
            return None
        if marked and roll in rules["marked_salvage_clean_unstable_rolls"]:
            quality = HarvestQuality.CLEAN
            force_unstable = True
        else:
            quality = HarvestQuality.STRESSED
            force_unstable = not marked and roll in rules["unmarked_salvage_unstable_rolls"]
        harvested = self.harvest(target, quality)
        self.log.emit(
            "salvage_succeeded",
            player.id,
            slot=target.slot.value,
            roll=roll,
            quality=quality.value,
            force_unstable=force_unstable,
        )
        return HarvestedLimb(harvested.limb, quality, force_unstable)

    def enemy_attack(
        self,
        enemy: CombatantRuntime,
        player: CombatantRuntime,
        source_slot: Slot,
        target_slot: Slot,
        base_damage: int,
        can_bleed: bool = False,
        modifier: AttackModifier | None = None,
    ) -> None:
        resolved_modifier = modifier or AttackModifier.neutral()
        if not 0 <= resolved_modifier.damage_reduction_basis_points <= 10000:
            raise ValueError("attack modifier reduction must be between 0 and 10000")
        if resolved_modifier.source_exposure_damage < 0:
            raise ValueError("attack modifier exposure cannot be negative")
        if resolved_modifier.source_exposure_damage and resolved_modifier.exposed_source is None:
            raise ValueError("attack modifier exposure requires a declared source")
        if resolved_modifier.source_exposure_damage and (
            resolved_modifier.required_source is None
            or resolved_modifier.exposed_source is not resolved_modifier.required_source
        ):
            raise ValueError("attack modifier exposure must derive from its required source")
        if (
            resolved_modifier.damage_reduction_basis_points
            and resolved_modifier.required_source is None
        ):
            raise ValueError("non-neutral attack modifier requires a physical source")
        self.log.set_phase(Phase.ENEMY)
        source = enemy.body.slots[source_slot]
        if not is_usable(source):
            self.log.emit("enemy_action_cancelled", enemy.id, reason="unusable source", slot=source_slot.value)
            return
        if resolved_modifier.required_source is not None and not is_usable(
            player.body.slots[resolved_modifier.required_source]
        ):
            self.log.emit(
                "reflex_opportunity_cancelled",
                player.id,
                target_id=enemy.id,
                reason="blocking_source_unusable_at_revalidation",
                source=resolved_modifier.required_source.value,
            )
            if player.guard_active:
                player.guard_active = False
                self.log.emit(
                    "guard_cancelled_source_unusable",
                    player.id,
                    target_id=enemy.id,
                    source=resolved_modifier.required_source.value,
                )
            resolved_modifier = AttackModifier.neutral()
        target = player.body.slots[target_slot]
        damage = action_damage(enemy, source, base_damage + (5 if enemy.rage else 0))
        enemy.rage = False
        damage = self.apply_guard_reduction(player, damage, source=enemy.id)
        if resolved_modifier.damage_reduction_basis_points:
            before_modifier = damage
            damage = round_half_up(
                Decimal(damage)
                * (
                    Decimal(1)
                    - Decimal(resolved_modifier.damage_reduction_basis_points) / Decimal(10000)
                )
            )
            self.log.emit(
                "reflex_modifier_applied",
                player.id,
                target_id=enemy.id,
                before=before_modifier,
                after=damage,
                reduction_basis_points=resolved_modifier.damage_reduction_basis_points,
                grade=(resolved_modifier.grade.value if resolved_modifier.grade else None),
                profile_id=resolved_modifier.profile_id,
                risk_class=(
                    resolved_modifier.risk_class.value if resolved_modifier.risk_class else None
                ),
            )
        apply_damage(player, target, damage, "Enemy attack", self.log)
        if resolved_modifier.source_exposure_damage:
            if resolved_modifier.exposed_source is None:
                raise AssertionError("validated exposure lost its source")
            exposed = player.body.slots[resolved_modifier.exposed_source]
            apply_damage(
                player,
                exposed,
                resolved_modifier.source_exposure_damage,
                "Disclosed high-risk Block exposure",
                self.log,
            )
            self.log.emit(
                "reflex_source_exposed",
                player.id,
                target_id=enemy.id,
                source=resolved_modifier.exposed_source.value,
                damage=resolved_modifier.source_exposure_damage,
            )
        if can_bleed:
            roll = self.rng.randint(1, 6)
            threshold = 4 if target.state in {LimbState.DAMAGED, LimbState.CRITICAL} else 5
            if roll >= threshold:
                self.apply_bleeding(player, target, source=enemy.id, roll=roll)

    def apply_bleeding(
        self, owner: CombatantRuntime, limb: LimbRuntime, *, source: str, roll: int | None = None
    ) -> None:
        limb.tags.add(LimbTag.BLEEDING)
        self.log.emit("bleeding_applied", source, target_id=owner.id, slot=limb.slot.value, roll=roll)

    def force_unstable(self, player: CombatantRuntime, limb: LimbRuntime, reason: str) -> None:
        limb.tags.add(LimbTag.UNSTABLE)
        self.log.emit("unstable_applied", player.id, slot=limb.slot.value, reason=reason)

    def apply_stabilized(self, target_owner: CombatantRuntime, limb: LimbRuntime, reason: str) -> None:
        limb.tags.add(LimbTag.STABILIZED)
        self.log.emit("stabilized_applied", target_owner.id, slot=limb.slot.value, reason=reason)

    def anna_trade(self, anna: CombatantRuntime, player: CombatantRuntime, limb: LimbRuntime) -> None:
        limb.tags.discard(LimbTag.UNSTABLE)
        limb.tags.discard(LimbTag.BLEEDING)
        self.metrics.trade_accepted = True
        self.log.emit(
            "anna_trade_accepted",
            anna.id,
            target_id=player.id,
            effect="Black Stitch removed Unstable/Bleeding",
        )

    def guard_flesh(self, player: CombatantRuntime) -> None:
        self._require_main_action(player, "Guard Flesh")
        arm = require_source(player, Slot.RIGHT_ARM)
        cost = self._limb_action_cost_amount(arm, self.config.actions["guard_flesh"].cost)
        self._require_affordable(player, cost, "Guard Flesh")
        self._commit_main_action(player, "guard_flesh")
        self.limb_action_cost(player, arm, self.config.actions["guard_flesh"].cost, "Guard Flesh")
        player.guard_active = True
        self.log.emit("guard_flesh", player.id, reduction=self.config.actions["guard_flesh"].reduction)

    def brace(self, player: CombatantRuntime) -> None:
        self._require_main_action(player, "Brace")
        require_source(player, Slot.LEGS)
        if player.brace_used:
            raise IllegalActionError("Brace is limited to once per encounter")
        self._commit_main_action(player, "brace")
        player.brace_used = True
        player.brace_active = True
        self.log.emit("brace_activated", player.id)

    def apply_guard_reduction(
        self, player: CombatantRuntime, damage: int, *, source: str | None
    ) -> int:
        if not player.guard_active:
            return damage
        reduced = round_half_up(
            Decimal(damage)
            * (Decimal(1) - Decimal(str(self.config.actions["guard_flesh"].reduction)))
        )
        player.guard_active = False
        self.log.emit(
            "guard_consumed",
            player.id,
            target_id=source,
            before=damage,
            after=reduced,
        )
        return reduced

    def _limb_action_cost_amount(self, limb: LimbRuntime, base_cost: int) -> int:
        cost = base_cost
        if limb.unstable_result == UnstableResult.TWITCH.value:
            cost += self.config.rules["unstable_graft"]["twitch_extra_cost"]
        elif limb.unstable_result == UnstableResult.SURGE.value:
            cost = max(0, cost - self.config.rules["unstable_graft"]["surge_cost_discount"])
        return cost

    def limb_action_cost(self, player: CombatantRuntime, limb: LimbRuntime, base_cost: int, reason: str) -> int:
        """Apply the current Unstable outcome to one blood-cost limb action."""
        require_source(player, limb.slot)
        cost = self._limb_action_cost_amount(limb, base_cost)
        self._require_affordable(player, cost, reason)
        if limb.unstable_result == UnstableResult.SURGE.value:
            limb.surge_unused = False
        spend_blood(player, cost, reason, self.config, self.log, self.metrics, self.tutorial, self.rng)
        if limb.unstable_result == UnstableResult.ACHE.value and cost > 0:
            roll = self.rng.randint(1, 6)
            disabled = roll in self.config.rules["unstable_graft"]["ache_stress_disable_rolls"]
            self.log.emit("ache_stress_roll", player.id, slot=limb.slot.value, roll=roll, disabled_next_round=disabled)
            if disabled:
                limb.disabled_rounds = 1
        return cost

    def decline_twitch(self, player: CombatantRuntime, limb: LimbRuntime) -> None:
        if limb.unstable_result != UnstableResult.TWITCH.value:
            raise IllegalActionError("only a Twitching limb can be declined")
        old = limb.state
        limb.state = LimbState.DISABLED
        limb.disabled_rounds = 1
        _record_state(limb, old, self.log, player, "Twitch declined")

    def add_plead_pressure(self, enemy: CombatantRuntime, trigger: str) -> bool:
        if trigger in enemy.plead_triggers:
            return enemy.plead_pressure >= int(self.config.rules["plead"]["basic_threshold"])
        enemy.plead_triggers.add(trigger)
        enemy.plead_pressure += 1
        threshold = int(self.config.rules["plead"]["basic_threshold"])
        pleading = enemy.plead_pressure >= threshold
        self.log.emit(
            "plead_pressure_changed",
            enemy.id,
            trigger=trigger,
            pressure=enemy.plead_pressure,
            threshold=threshold,
            pleading=pleading,
        )
        return pleading

    def harvest(self, target: LimbRuntime, quality: HarvestQuality) -> HarvestedLimb:
        if quality is HarvestQuality.RUINED:
            self.metrics.ruined_harvests += 1
        elif quality is HarvestQuality.CLEAN:
            self.metrics.clean_harvests += 1
        else:
            self.metrics.stressed_harvests += 1
        clone = LimbRuntime(target.definition, target.definition.max_integrity, LimbState.INTACT)
        self.log.emit("harvest_created", target_id=None, slot=target.slot.value, quality=quality.value, limb=target.name)
        return HarvestedLimb(clone, quality)

    def negotiated_item_for_limb_exchange(
        self,
        buyer: CombatantRuntime,
        seller: CombatantRuntime,
        item_id: str,
        target: LimbRuntime,
        quality: HarvestQuality,
    ) -> HarvestedLimb:
        """Exchange an owned item for a non-Core limb through explicit state changes."""
        if buyer.inventory.get(item_id, 0) <= 0:
            raise IllegalActionError(f"{buyer.name} does not have {item_id}")
        if target.slot is Slot.CORE:
            raise InvalidTargetError("Core cannot be exchanged as a harvested limb")
        if not is_usable(target):
            raise InvalidTargetError("negotiated limb must still be usable")
        if quality is not HarvestQuality.CLEAN:
            raise InvalidTargetError("controlled negotiated exchange requires Clean quality")
        buyer.inventory[item_id] -= 1
        seller.inventory[item_id] = seller.inventory.get(item_id, 0) + 1
        self.log.emit(
            "asset_transferred",
            buyer.id,
            target_id=seller.id,
            asset=item_id,
            amount=1,
            reason="negotiated limb exchange",
        )
        sever_quality = apply_damage(
            seller,
            target,
            target.integrity,
            "Negotiated limb exchange",
            self.log,
            clean=True,
        )
        if sever_quality is not HarvestQuality.CLEAN:
            raise AssertionError("validated negotiated sever did not produce a Clean state")
        harvested = self.harvest(target, quality)
        self.log.emit(
            "negotiated_exchange_completed",
            buyer.id,
            target_id=seller.id,
            asset_given=item_id,
            limb_received=target.name,
            slot=target.slot.value,
            quality=quality.value,
        )
        return harvested

    def emergency_graft(self, player: CombatantRuntime, harvested: HarvestedLimb, target_slot: Slot) -> None:
        if harvested.quality is HarvestQuality.RUINED:
            raise IllegalActionError("Ruined harvest cannot be emergency grafted")
        limb = harvested.limb
        if limb.slot is not target_slot:
            raise InvalidTargetError("harvest cannot be grafted into another slot")
        cost = self.config.rules["harvest"]["emergency_graft_cost"]
        spend_blood(player, cost, "Emergency graft", self.config, self.log, self.metrics, self.tutorial, self.rng)
        if limb.definition.id == "jeff_right_arm":
            player_definition = self.config.limbs["human_right_arm"]
            limb = LimbRuntime(player_definition, player_definition.max_integrity, LimbState.INTACT)
        limb.tags.add(LimbTag.GRAFTED)
        roll = self.rng.randint(1, 6)
        unstable = harvested.force_unstable or roll in self.config.rules["harvest"][f"{harvested.quality.value}_unstable_rolls"]
        if unstable:
            self.force_unstable(player, limb, "Emergency graft stability roll")
            self.metrics.unstable_grafts += 1
        else:
            self.metrics.stable_grafts += 1
        player.body.slots[target_slot] = limb
        self.metrics.grafts_attempted += 1
        self.metrics.body_changes.append(f"{target_slot.value} gained {limb.name} ({'Unstable' if unstable else 'Stable'})")
        self.log.emit("emergency_graft", player.id, slot=target_slot.value, quality=harvested.quality.value, roll=roll, unstable=unstable)

    def integrate(self, player: CombatantRuntime, choice: str) -> None:
        self.log.set_phase(Phase.TABLE)
        option = self.config.table_options.get(choice)
        if option is None:
            raise IllegalActionError(f"unknown table choice: {choice}")
        if choice == "integrate_arm":
            arm = player.body.slots[Slot.RIGHT_ARM]
            if LimbTag.GRAFTED not in arm.tags:
                raise IllegalActionError("cannot integrate a missing or non-grafted arm")
            spend_blood(player, option["cost"], option["name"], self.config, self.log, self.metrics, self.tutorial, self.rng)
            arm.tags.discard(LimbTag.UNSTABLE)
            arm.tags.add(LimbTag.INTEGRATED)
        elif choice == "repair_torso":
            torso = player.body.slots[Slot.TORSO]
            spend_blood(player, option["cost"], option["name"], self.config, self.log, self.metrics, self.tutorial, self.rng)
            torso.tags.discard(LimbTag.BLEEDING)
            torso.integrity = torso.definition.max_integrity
            torso.state = LimbState.INTACT
        elif choice == "strengthen_legs":
            legs = player.body.slots[Slot.LEGS]
            spend_blood(player, option["cost"], option["name"], self.config, self.log, self.metrics, self.tutorial, self.rng)
            legs.definition = legs.definition.__class__(
                id="braced_human_legs", name="Braced Human Legs", slot=Slot.LEGS,
                max_integrity=legs.definition.max_integrity, size=legs.definition.size,
                actions=legs.definition.actions, passives=legs.definition.passives,
            )
        elif choice == "table_loan":
            gain_blood(player, option["gain"], option["name"], self.config, self.log, self.metrics)
            player.debt += option["debt"]
        elif choice != "leave":
            raise IllegalActionError(f"unsupported table choice: {choice}")
        self.metrics.table_choice = choice
        self.log.emit("table_choice", player.id, choice=choice, debt=player.debt)

    def _action(self, action_id: str) -> None:
        self.metrics.actions[action_id] = self.metrics.actions.get(action_id, 0) + 1
