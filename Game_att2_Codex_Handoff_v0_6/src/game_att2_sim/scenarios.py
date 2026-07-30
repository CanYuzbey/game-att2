"""The seven required scripts and small strategy observations for v0.1."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, replace
from statistics import mean, median

from .config_loader import SimulatorConfig, load_config
from .enums import HarvestQuality, LimbState, LimbTag, Slot
from .errors import InsufficientBloodError, ScenarioDefinitionError
from .events import EventLog
from .factory import body_summary, enemy_from_config, player_from_start, refresh_fight_tools
from .models import CombatantRuntime, HarvestedLimb, ScenarioMetrics, ScenarioResult
from .rng import RNGService, ScriptedRNG, SeededRNG
from .rules import RuleEngine, is_usable

STRATEGIES = {
    "balanced",
    "blood_hoarder",
    "limb_greed",
    "survival_first",
    "reckless_sever",
    "random_legal",
}


@dataclass
class ScenarioSession:
    config: SimulatorConfig
    name: str
    seed: int
    strategy: str
    rng: RNGService
    player: CombatantRuntime
    log: EventLog
    metrics: ScenarioMetrics
    engine: RuleEngine


def _session(name: str, seed: int, strategy: str, config: SimulatorConfig, rng: RNGService | None = None) -> ScenarioSession:
    if name not in config.scenarios:
        raise ScenarioDefinitionError(f"unknown scenario: {name}")
    if strategy not in STRATEGIES:
        raise ScenarioDefinitionError(f"unknown strategy: {strategy}")
    player = player_from_start(config)
    log = EventLog()
    metrics = ScenarioMetrics(scenario=name, seed=seed, strategy=strategy)
    service = rng or SeededRNG(seed)
    engine = RuleEngine(config, service, log, metrics, tutorial=True)
    return ScenarioSession(config, name, seed, strategy, service, player, log, metrics, engine)


def _close(session: ScenarioSession, notes: list[str] | None = None) -> ScenarioResult:
    player = session.player
    session.engine.end_round(player)
    session.metrics.final_blood = player.blood
    session.metrics.panic_pulse_used = player.panic_pulse_used
    session.metrics.soft_collapse_used = player.soft_collapse_used
    if player.collapsed:
        session.metrics.result = "collapsed"
    summary = body_summary(player)
    session.metrics.final_body_summary = "; ".join(f"{slot}: {value}" for slot, value in summary.items())
    return ScenarioResult(session.metrics, session.log.events, summary, notes or [])


def _jeff_baseline(session: ScenarioSession, graft: bool = True) -> HarvestedLimb | None:
    player = session.player
    jeff = enemy_from_config(session.config, "jeff")
    refresh_fight_tools(player)
    right = jeff.body.slots[Slot.RIGHT_ARM]
    left = jeff.body.slots[Slot.LEFT_ARM]
    session.engine.start_round(player)
    if session.strategy == "blood_hoarder":
        session.engine.grip(player, jeff, right)
        session.engine.start_round(player)
        session.engine.grip(player, jeff, right)
        session.engine.start_round(player)
        session.engine.grip(player, jeff, left)
        session.engine.start_round(player)
        session.engine.grip(player, jeff, left)
        session.metrics.plea_triggered = True
        session.log.emit("jeff_incapacity_surrender", jeff.id, reason="both arms ruined")
        return None
    if session.strategy != "reckless_sever":
        session.engine.claim(player, right)
    session.engine.start_round(player)
    session.engine.grip(player, jeff, right)
    session.engine.start_round(player)
    quality = session.engine.saw(player, jeff, right)
    if quality is None:
        session.metrics.result = "incomplete"
        session.log.emit("jeff_saw_failed", player.id, reason="no valid harvest after failed saw")
        return None
    if session.strategy != "reckless_sever" and quality is not HarvestQuality.CLEAN:
        raise ScenarioDefinitionError("Jeff baseline requires a marked Hell Saw Clean harvest")
    session.metrics.plea_triggered = quality is HarvestQuality.CLEAN
    session.log.emit("jeff_bargain", jeff.id, reward="right arm harvest", quality=quality.value)
    harvested = session.engine.harvest(right, quality)
    if graft:
        session.engine.emergency_graft(player, harvested, Slot.RIGHT_ARM)
    # A free destruction still creates surrender but never a premium second harvest.
    session.engine.start_round(player)
    session.engine.grip(player, jeff, left)
    session.engine.start_round(player)
    session.engine.grip(player, jeff, left)
    session.log.emit("jeff_incapacity_surrender", jeff.id, reason="both arm paths compromised")
    return harvested


def _anna_stabilization(session: ScenarioSession) -> None:
    player = session.player
    anna = enemy_from_config(session.config, "anna")
    refresh_fight_tools(player)
    arm = player.body.slots[Slot.RIGHT_ARM]
    if arm.state is LimbState.MISSING:
        acquired = enemy_from_config(session.config, "jeff").body.slots[Slot.RIGHT_ARM]
        harvested = HarvestedLimb(acquired, HarvestQuality.CLEAN, force_unstable=True)
        session.engine.emergency_graft(player, harvested, Slot.RIGHT_ARM)
        arm = player.body.slots[Slot.RIGHT_ARM]
    session.engine.force_unstable(player, arm, "Anna stabilization scenario setup")
    session.engine.start_round(player)
    session.engine.focus(player, "Surgical Jab from right arm against torso")
    if session.strategy != "blood_hoarder":
        session.engine.guard_flesh(player)
    session.engine.enemy_attack(anna, player, Slot.RIGHT_ARM, Slot.TORSO, 8, can_bleed=True)
    # The explicit trade ends this encounter without requiring Anna's death.
    session.engine.anna_trade(anna, player, arm)


def _anna_greed(session: ScenarioSession) -> None:
    player = session.player
    anna = enemy_from_config(session.config, "anna")
    refresh_fight_tools(player)
    target = anna.body.slots[Slot.RIGHT_ARM]
    session.metrics.anna_greed_attempted = True
    session.engine.apply_stabilized(anna, target, "Anna greed scenario setup")
    session.engine.start_round(player)
    session.engine.grip(player, anna, target)
    session.engine.start_round(player)
    session.engine.grip(player, anna, target)
    session.engine.start_round(player)
    quality = session.engine.scissors(player, anna, target)
    if quality is HarvestQuality.CLEAN:
        session.engine.harvest(target, quality)
        session.metrics.anna_greed_succeeded = True
    else:
        session.log.emit("anna_greed_failed", player.id, reason="Stabilized limb resisted sever")
        session.engine.enemy_attack(anna, player, Slot.RIGHT_ARM, Slot.LEFT_ARM, 8, can_bleed=True)


def _random_legal_campaign(session: ScenarioSession) -> None:
    """Diagnostic fuzz policy that chooses only legal existing actions through the engine."""
    player = session.player
    jeff = enemy_from_config(session.config, "jeff")
    refresh_fight_tools(player)
    right = jeff.body.slots[Slot.RIGHT_ARM]
    harvested: HarvestedLimb | None = None
    for _ in range(6):
        session.engine.start_round(player)
        if player.collapsed or not is_usable(right):
            break
        choices: list[str] = ["grip_right", "grip_left"]
        if LimbTag.MARKED not in right.tags and player.inventory.get("claim_the_cut", 0):
            choices.append("claim")
        if (
            right.definition.size == "large"
            and right.state in {LimbState.DAMAGED, LimbState.CRITICAL}
            and player.inventory.get("hell_saw", 0)
        ):
            choices.append("saw")
        choice = session.rng.choice(choices)
        if (
            player.blood <= 50
            and player.inventory.get("blood_bag", 0)
            and session.config.items["blood_bag"].get("available", True)
            and session.rng.randint(0, 1)
        ):
            session.engine.fast_item(player, "blood_bag")
        if choice == "claim":
            session.engine.claim(player, right)
        elif choice == "grip_right":
            session.engine.grip(player, jeff, right)
        elif choice == "grip_left":
            session.engine.grip(player, jeff, jeff.body.slots[Slot.LEFT_ARM])
        else:
            quality = session.engine.saw(player, jeff, right)
            if quality is not None:
                harvested = session.engine.harvest(right, quality)
                session.engine.emergency_graft(player, harvested, Slot.RIGHT_ARM)
                break
        if is_usable(jeff.body.slots[Slot.LEFT_ARM]):
            session.engine.enemy_attack(jeff, player, Slot.LEFT_ARM, Slot.TORSO, 10)
    if harvested is None:
        session.metrics.result = "incomplete"
        session.log.emit("diagnostic_incomplete", player.id, reason="random legal policy did not acquire a graft")
        return
    if (
        player.blood <= 50
        and player.inventory.get("blood_bag", 0)
        and session.config.items["blood_bag"].get("available", True)
        and session.rng.randint(0, 1)
    ):
        session.engine.start_round(player)
        session.engine.fast_item(player, "blood_bag")
    if session.rng.randint(0, 1):
        _anna_stabilization(session)
    else:
        _anna_greed(session)
    choices = ["leave", "table_loan"]
    arm = player.body.slots[Slot.RIGHT_ARM]
    if LimbTag.GRAFTED in arm.tags and player.blood >= session.config.table_options["integrate_arm"]["cost"]:
        choices.append("integrate_arm")
    if player.blood >= session.config.table_options["repair_torso"]["cost"]:
        choices.append("repair_torso")
    if player.blood >= session.config.table_options["strengthen_legs"]["cost"]:
        choices.append("strengthen_legs")
    session.engine.integrate(player, session.rng.choice(choices))


def _failed_hell_saw(session: ScenarioSession) -> None:
    player = session.player
    jeff = enemy_from_config(session.config, "jeff")
    refresh_fight_tools(player)
    torso = jeff.body.slots[Slot.TORSO]
    session.engine.start_round(player)
    session.engine.grip(player, jeff, torso)
    session.engine.start_round(player)
    # The scenario uses a scripted failure in its configured first roll.
    session.engine.saw(player, jeff, torso)
    from .rules import spend_blood
    spend_blood(
        player,
        player.blood - 24,
        "failed-saw scenario pressure",
        session.config,
        session.log,
        session.metrics,
        True,
        session.rng,
    )
    session.engine.apply_bleeding(player, player.body.slots[Slot.TORSO], source="failed_hell_saw")
    session.log.emit("critical_warning", player.id, projected_next_round=player.blood - 5)
    session.engine.enemy_attack(jeff, player, Slot.LEFT_ARM, Slot.TORSO, 10)
    session.engine.start_round(player)


def _campaign(session: ScenarioSession) -> None:
    if session.strategy == "random_legal":
        _random_legal_campaign(session)
        return
    harvested = _jeff_baseline(session, graft=True)
    if harvested is None:
        session.metrics.result = "incomplete"
        session.log.emit("campaign_incomplete", session.player.id, reason="Jeff did not yield a graftable right arm")
        return
    if session.strategy == "blood_hoarder":
        session.metrics.table_choice = "leave"
        session.engine.integrate(session.player, "leave")
        return
    if session.strategy == "limb_greed":
        _anna_greed(session)
        choice = "strengthen_legs"
    else:
        _anna_stabilization(session)
        choice = "repair_torso" if session.strategy == "survival_first" else "integrate_arm"
    try:
        session.engine.integrate(session.player, choice)
    except InsufficientBloodError as error:
        session.log.emit("table_choice_unaffordable", session.player.id, choice=choice, reason=str(error))
        session.engine.integrate(session.player, "leave")


def _blood_bag_balance(session: ScenarioSession) -> list[str]:
    player = session.player
    notes: list[str] = []
    for gain, bleeding_gain, label in ((25, 15, "baseline"), (20, 12, "variant_b"), (25, 15, "variant_c")):
        before = player.blood
        player.inventory["blood_bag"] = 1
        player.inventory.pop("_fast_round", None)
        session.engine.start_round(player)
        session.engine.apply_bleeding(player, player.body.slots[Slot.TORSO], source="blood_bag_balance")
        items = deepcopy(session.config.items)
        items["blood_bag"]["gain"] = gain
        items["blood_bag"]["gain_if_bleeding"] = bleeding_gain
        session.engine.config = replace(session.config, items=items)
        session.engine.fast_item(player, "blood_bag")
        session.engine.config = session.config
        notes.append(f"{label}: blood {before}->{player.blood}; bleeding recovery {bleeding_gain}")
    return notes


def run_scenario(
    name: str,
    seed: int = 42,
    strategy: str | None = None,
    config: SimulatorConfig | None = None,
    rng: RNGService | None = None,
    table_choice: str = "integrate_arm",
    threat_profile: str = "graft_pressure",
    fixture: str = "campaign_pretable",
) -> ScenarioResult:
    config = config or load_config()
    if name == "post_table_probe":
        from .probe import run_post_table_probe

        return run_post_table_probe(config, seed, table_choice, threat_profile, fixture)
    declared = config.scenarios.get(name)
    if declared is None:
        raise ScenarioDefinitionError(f"unknown scenario: {name}")
    chosen = strategy or str(declared["default_strategy"])
    if name == "failed_hell_saw" and rng is None:
        rolls = declared.get("scripted_rolls", [])
        rng = ScriptedRNG([int(value) for value in rolls])
    session = _session(name, seed, chosen, config, rng)
    notes: list[str] = []
    if name == "jeff_baseline":
        _jeff_baseline(session)
    elif name == "jeff_no_spend":
        _jeff_baseline(session, graft=False)
    elif name == "failed_hell_saw":
        _failed_hell_saw(session)
    elif name == "anna_stabilization":
        _anna_stabilization(session)
    elif name == "anna_greed":
        _anna_greed(session)
    elif name == "mini_campaign":
        _campaign(session)
    elif name == "blood_bag_balance":
        notes = _blood_bag_balance(session)
    else:
        raise ScenarioDefinitionError(f"scenario is not implemented: {name}")
    return _close(session, notes)


def run_all(seed: int = 42, config: SimulatorConfig | None = None) -> list[ScenarioResult]:
    config = config or load_config()
    return [run_scenario(name, seed=seed, config=config) for name in config.scenarios if name != "post_table_probe"]


def run_batch(
    strategy: str,
    count: int = 100,
    seed: int = 42,
    scenario: str = "mini_campaign",
    config: SimulatorConfig | None = None,
) -> dict[str, object]:
    if count < 1:
        raise ScenarioDefinitionError("batch count must be positive")
    config = config or load_config()
    results = [run_scenario(scenario, seed=seed + index, strategy=strategy, config=config) for index in range(count)]
    blood = [result.metrics.final_blood for result in results]
    bodies = [result.metrics.final_body_summary for result in results]
    body_counts = _counts(bodies)
    graft_events = [
        event
        for result in results
        for event in result.events
        if event.event_type == "emergency_graft"
    ]
    blood_bag_rounds = [
        event.round_number
        for result in results
        for event in result.events
        if event.event_type == "fast_item_used" and event.payload.get("item") == "blood_bag"
    ]
    bailout_events = [
        event.event_type
        for result in results
        for event in result.events
        if event.event_type in {"collapse", "soft_collapse", "campaign_incomplete", "diagnostic_incomplete", "table_choice_unaffordable"}
    ]
    return {
        "scenario": scenario,
        "strategy": strategy,
        "count": count,
        "seed": seed,
        "completion_rate": sum(result.metrics.result == "completed" for result in results) / count,
        "incomplete_rate": sum(result.metrics.result == "incomplete" for result in results) / count,
        "collapse_rate": sum(result.metrics.result == "collapsed" for result in results) / count,
        "survival_without_soft_rescue_rate": sum(
            result.metrics.result == "completed" and not result.metrics.soft_collapse_used for result in results
        ) / count,
        "soft_collapse_rate": sum(result.metrics.soft_collapse_used for result in results) / count,
        "panic_pulse_rate": sum(result.metrics.panic_pulse_used for result in results) / count,
        "average_final_blood": mean(blood),
        "median_final_blood": median(blood),
        "minimum_final_blood": min(blood),
        "maximum_final_blood": max(blood),
        "final_blood_bands": _blood_bands(blood, config),
        "average_blood_spent": mean(result.metrics.blood_spent for result in results),
        "average_blood_gained": mean(result.metrics.blood_gained for result in results),
        "average_critical_rounds": mean(result.metrics.critical_rounds for result in results),
        "clean_harvests": sum(result.metrics.clean_harvests for result in results),
        "stressed_harvests": sum(result.metrics.stressed_harvests for result in results),
        "ruined_harvests": sum(result.metrics.ruined_harvests for result in results),
        "premium_graft_rate": sum(result.metrics.clean_harvests > 0 and result.metrics.grafts_attempted > 0 for result in results) / count,
        "emergency_graft_rate": sum(result.metrics.grafts_attempted > 0 for result in results) / count,
        "stable_graft_rate": sum(event.payload.get("unstable") is False for event in graft_events) / count,
        "unstable_graft_rate": sum(event.payload.get("unstable") is True for event in graft_events) / count,
        "action_frequency": _sum_actions(results),
        "table_choices": _counts([result.metrics.table_choice for result in results]),
        "trade_acceptance_rate": sum(result.metrics.trade_accepted for result in results) / count,
        "anna_greed_attempt_rate": sum(result.metrics.anna_greed_attempted for result in results) / count,
        "anna_greed_success_rate": sum(result.metrics.anna_greed_succeeded for result in results) / count,
        "blood_bag_use_rate": sum(result.metrics.blood_bag_uses > 0 for result in results) / count,
        "blood_bag_rounds": _counts([str(value) for value in blood_bag_rounds]),
        "final_body_distribution": body_counts,
        "identical_final_body_rate": max(body_counts.values()) / count,
        "average_actions": mean(sum(result.metrics.actions.values()) for result in results),
        "average_rounds": mean(result.metrics.rounds for result in results),
        "most_common_bailout": _most_common(bailout_events),
    }


def blood_bag_overlay(
    config: SimulatorConfig,
    *,
    gain: int | None = None,
    gain_if_bleeding: int | None = None,
    cap: int | None = None,
    available: bool = True,
) -> SimulatorConfig:
    """Return an isolated diagnostic config overlay without mutating baseline definitions."""
    items = deepcopy(config.items)
    bag = items["blood_bag"]
    if gain is not None:
        bag["gain"] = gain
    if gain_if_bleeding is not None:
        bag["gain_if_bleeding"] = gain_if_bleeding
    if cap is None:
        bag.pop("cap", None)
    else:
        bag["cap"] = cap
    bag["available"] = available
    return replace(config, items=items)


def run_blood_bag_counterfactuals(
    count: int = 500,
    seed: int = 42,
    strategy: str = "random_legal",
    config: SimulatorConfig | None = None,
) -> dict[str, dict[str, object]]:
    baseline = config or load_config()
    variants = {
        "baseline_a": baseline,
        "variant_b": blood_bag_overlay(baseline, gain=20, gain_if_bleeding=12),
        "variant_c": blood_bag_overlay(baseline, cap=60),
        "diagnostic_d_unavailable": blood_bag_overlay(baseline, available=False),
    }
    return {
        label: run_batch(strategy, count=count, seed=seed, config=overlay)
        for label, overlay in variants.items()
    }


def _sum_actions(results: list[ScenarioResult]) -> dict[str, int]:
    total: dict[str, int] = {}
    for result in results:
        for action, count in result.metrics.actions.items():
            total[action] = total.get(action, 0) + count
    return total


def _counts(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    return result


def _blood_bands(blood: list[int], config: SimulatorConfig) -> dict[str, int]:
    rules = config.rules["blood"]
    counts = {"collapsed": 0, "critical": 0, "dangerous": 0, "normal": 0, "strong": 0, "rich": 0}
    for value in blood:
        if value <= rules["collapse_at"]:
            counts["collapsed"] += 1
        elif value <= rules["critical_max"]:
            counts["critical"] += 1
        elif value <= rules["dangerous_max"]:
            counts["dangerous"] += 1
        elif value <= rules["normal_max"]:
            counts["normal"] += 1
        elif value <= rules["strong_max"]:
            counts["strong"] += 1
        else:
            counts["rich"] += 1
    return counts


def _most_common(values: list[str]) -> str | None:
    return max(_counts(values).items(), key=lambda item: item[1])[0] if values else None
