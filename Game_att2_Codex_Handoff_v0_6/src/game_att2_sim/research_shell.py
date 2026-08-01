"""Minimal deterministic free-choice research shell for the approved simulator sequence."""

from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass, field, replace
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

from .config_loader import SimulatorConfig, load_config
from .encounter_goals import (
    EncounterOutcome,
    ResolutionKind,
    evaluate_encounter_outcome,
)
from .enemy_behavior import IntentCandidate, select_intent
from .enums import HarvestQuality, LimbTag, Slot
from .errors import IllegalActionError
from .events import EventLog
from .factory import body_summary, enemy_from_config, player_from_start, refresh_fight_tools
from .models import (
    ActionAvailability,
    CombatantRuntime,
    HarvestedLimb,
    ScenarioMetrics,
)
from .rng import RNGService, SeededRNG
from .rules import RuleEngine, is_usable

INTERFACE_VERSION = "0.2"
APPROVED_SEQUENCE = "S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table"


class EvidenceClass(str, Enum):
    OWNER_DIAGNOSTIC = "OWNER_DIAGNOSTIC"
    EXTERNAL_PILOT = "EXTERNAL_PILOT"
    AUTOMATED_REGRESSION = "AUTOMATED_REGRESSION"
    UNCLASSIFIED_HUMAN_PLAY = "UNCLASSIFIED_HUMAN_PLAY"


@dataclass(frozen=True)
class SessionMetadata:
    session_id: str
    evidence_class: EvidenceClass
    timestamp: str
    seed: int
    participant_code: str
    information_condition: str = "NOT_APPLICABLE"
    strategy_intention: str | None = None

    @classmethod
    def create(
        cls,
        session_id: str,
        evidence_class: EvidenceClass,
        seed: int,
        participant_code: str,
        *,
        timestamp: str | None = None,
        information_condition: str = "NOT_APPLICABLE",
        strategy_intention: str | None = None,
    ) -> SessionMetadata:
        metadata = cls(
            session_id=session_id,
            evidence_class=evidence_class,
            timestamp=timestamp or datetime.now().astimezone().isoformat(),
            seed=seed,
            participant_code=participant_code,
            information_condition=information_condition,
            strategy_intention=strategy_intention,
        )
        metadata.validate()
        return metadata

    def validate(self) -> None:
        code = self.participant_code.upper()
        if not self.session_id.strip() or not self.participant_code.strip():
            raise ValueError("session_id and participant_code are required")
        if self.evidence_class is EvidenceClass.OWNER_DIAGNOSTIC:
            if not code.startswith(("OWNER-", "SELF-")):
                raise ValueError("OWNER_DIAGNOSTIC requires an OWNER- or SELF- code")
        elif self.evidence_class is EvidenceClass.EXTERNAL_PILOT:
            if code.startswith(("OWNER-", "SELF-", "AUTO-", "PLAY-")):
                raise ValueError(
                    "owner/automated/unclassified codes cannot be labeled EXTERNAL_PILOT"
                )
        elif self.evidence_class is EvidenceClass.AUTOMATED_REGRESSION and not code.startswith(
            "AUTO-"
        ):
            raise ValueError("AUTOMATED_REGRESSION requires an AUTO- code")
        elif self.evidence_class is EvidenceClass.UNCLASSIFIED_HUMAN_PLAY and not code.startswith(
            "PLAY-"
        ):
            raise ValueError("UNCLASSIFIED_HUMAN_PLAY requires a PLAY- code")
        if self.information_condition not in {"KNOWN", "UNKNOWN", "NOT_APPLICABLE"}:
            raise ValueError("information_condition must be KNOWN, UNKNOWN, or NOT_APPLICABLE")


@dataclass
class DecisionRecord:
    index: int
    encounter: str
    round_number: int
    blood: int
    body: dict[str, str]
    statuses: list[str]
    main_available: bool
    focus_available: bool
    fast_available: bool
    action_sources: dict[str, str]
    actions_presented: list[dict[str, Any]]
    selected_action: str
    disposition: str
    reason: str | None = None


@dataclass
class InteractiveResearchSession:
    metadata: SessionMetadata
    config: SimulatorConfig = field(default_factory=load_config)
    rng: RNGService | None = None
    player: CombatantRuntime = field(init=False)
    log: EventLog = field(init=False)
    metrics: ScenarioMetrics = field(init=False)
    engine: RuleEngine = field(init=False)
    encounter: str = field(init=False, default="Jeff")
    enemy: CombatantRuntime | None = field(init=False)
    current_intent: str = field(init=False, default="")
    exact_intent: str = field(init=False, default="")
    current_intent_source: Slot | None = field(init=False, default=None)
    current_intent_target: Slot | None = field(init=False, default=None)
    current_intent_action: str = field(init=False, default="")
    last_enemy_action: str | None = field(init=False, default=None)
    last_enemy_target: Slot | None = field(init=False, default=None)
    jeff_bargain_offered: bool = field(init=False, default=False)
    jeff_bargain_rejected: bool = field(init=False, default=False)
    jeff_bargain_accepted: bool = field(init=False, default=False)
    jeff_surrendered: bool = field(init=False, default=False)
    encounter_outcomes: list[EncounterOutcome] = field(init=False, default_factory=list)
    decisions: list[DecisionRecord] = field(init=False, default_factory=list)
    action_sequence: list[dict[str, Any]] = field(init=False, default_factory=list)
    harvested_jeff_arm: HarvestedLimb | None = field(init=False, default=None)
    anna_path: str = field(init=False, default="")
    outcome: str = field(init=False, default="IN_PROGRESS")
    transcript_lines: list[str] = field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        self.metadata.validate()
        self.rng = self.rng or SeededRNG(self.metadata.seed)
        self.player = player_from_start(self.config)
        self.log = EventLog()
        self.metrics = ScenarioMetrics(
            "interactive_research_shell",
            self.metadata.seed,
            self.metadata.strategy_intention or "free_choice",
        )
        self.engine = RuleEngine(
            self.config, self.rng, self.log, self.metrics, tutorial=True
        )
        self.enemy = enemy_from_config(self.config, "jeff")
        refresh_fight_tools(self.player)
        self._start_round()
        self.log.emit(
            "research_session_started",
            self.player.id,
            session_id=self.metadata.session_id,
            evidence_class=self.metadata.evidence_class.value,
            interface_version=INTERFACE_VERSION,
        )

    @property
    def complete(self) -> bool:
        return self.outcome != "IN_PROGRESS"

    def _start_round(self) -> None:
        self.engine.start_round(self.player)
        if self.encounter == "Jeff":
            self._select_jeff_intent()
        elif self.encounter == "Anna":
            self.current_intent_action = "surgical_jab"
            self.current_intent_source = Slot.RIGHT_ARM
            self.current_intent_target = Slot.TORSO
            self.exact_intent = "Surgical Jab from right_arm against torso"
            self.current_intent = "Anna prepares Surgical Jab (source and target unclear)"
        else:
            self.current_intent_action = ""
            self.current_intent_source = None
            self.current_intent_target = None
            self.exact_intent = ""
            self.current_intent = ""

    def _first_usable_enemy_arm(self) -> Slot | None:
        if self.enemy is None:
            return None
        for slot in (Slot.LEFT_ARM, Slot.RIGHT_ARM):
            if is_usable(self.enemy.body.slots[slot]):
                return slot
        return None

    def _choose_jeff_intent_source(self) -> Slot | None:
        assert self.enemy is not None
        for slot in (Slot.RIGHT_ARM, Slot.LEFT_ARM):
            limb = self.enemy.body.slots[slot]
            if LimbTag.MARKED in limb.tags and is_usable(limb):
                return slot
        return self._first_usable_enemy_arm()

    def _jeff_bargain_available(self) -> bool:
        assert self.enemy is not None
        design = self.config.encounter_designs["jeff"]
        asset_id = str(design.parameters["bargain_asset"])
        bargain_slot = Slot(str(design.parameters["bargain_limb"]))
        offered_limb = self.enemy.body.slots[bargain_slot]
        return (
            not self.jeff_bargain_rejected
            and not self.jeff_bargain_accepted
            and LimbTag.MARKED in offered_limb.tags
            and is_usable(offered_limb)
            and self.player.inventory.get(asset_id, 0) > 0
            and ResolutionKind.BARGAIN
            in self.config.motivation_profiles[
                design.actor_motivations["enemy"]
            ].acceptable_resolutions
        )

    def _jeff_int_parameter(self, name: str) -> int:
        value = self.config.encounter_designs["jeff"].parameters[name]
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"Jeff encounter parameter {name} must be an integer")
        return value

    def _select_jeff_intent(self) -> None:
        assert self.enemy is not None
        profile = self.config.motivation_profiles[
            self.config.encounter_designs["jeff"].actor_motivations["enemy"]
        ]
        parameters = self.config.encounter_designs["jeff"].parameters
        bargain_asset = str(parameters["bargain_asset"])
        bargain_slot = Slot(str(parameters["bargain_limb"]))
        offense_target = Slot(str(parameters["offense_target"]))
        pressure_target = Slot(str(parameters["pressure_target"]))
        asset_name = str(self.config.items[bargain_asset]["name"])
        candidates: list[IntentCandidate] = []
        if self._jeff_bargain_available():
            candidates.append(
                IntentCandidate(
                    action_id="jeff_bargain",
                    source_slot=None,
                    target_slot=bargain_slot,
                    score=self._jeff_int_parameter("bargain_score"),
                    reasons=("desired repair asset is available", "marked arm can be exchanged"),
                    public_text=(
                        "Jeff slows down, guarding the marked arm while watching your supplies."
                    ),
                    exact_text=(
                        f"Jeff offers his marked {bargain_slot.value} for your {asset_name}; "
                        "a hostile Main action rejects the offer."
                    ),
                )
            )
        source = self._choose_jeff_intent_source()
        if source is not None:
            candidates.extend(
                (
                    IntentCandidate(
                        action_id="desperate_swing",
                        source_slot=source,
                        target_slot=offense_target,
                        score=self._jeff_int_parameter("offense_target_score"),
                        reasons=(
                            "reduce the player's current offensive capability",
                            "preserve the desired repair item",
                        ),
                        public_text=(
                            "Jeff prepares a Desperate Swing (source and target unclear)."
                        ),
                        exact_text=(
                            f"Desperate Swing from {source.value} against {offense_target.value}"
                        ),
                        legal=is_usable(self.player.body.slots[offense_target]),
                        exclusion_reason=f"player {offense_target.value} is already unusable",
                    ),
                    IntentCandidate(
                        action_id="desperate_swing",
                        source_slot=source,
                        target_slot=pressure_target,
                        score=self._jeff_int_parameter("pressure_target_score"),
                        reasons=("create surrender pressure without consuming the desired item",),
                        public_text=(
                            "Jeff prepares a Desperate Swing (source and target unclear)."
                        ),
                        exact_text=(
                            f"Desperate Swing from {source.value} against {pressure_target.value}"
                        ),
                    ),
                )
            )
        selection = select_intent(
            tuple(candidates),
            last_action_id=self.last_enemy_action,
            last_target_slot=self.last_enemy_target,
            repetition_penalty=self._jeff_int_parameter("repetition_penalty"),
        )
        if selection is None:
            self.current_intent_action = ""
            self.current_intent_source = None
            self.current_intent_target = None
            self.exact_intent = "No legal Jeff action remains"
            self.current_intent = self.exact_intent
            return
        chosen = selection.candidate
        self.current_intent_action = chosen.action_id
        self.current_intent_source = chosen.source_slot
        self.current_intent_target = chosen.target_slot
        self.exact_intent = chosen.exact_text
        self.current_intent = chosen.public_text
        if chosen.action_id == "jeff_bargain":
            self.jeff_bargain_offered = True
        elif chosen.source_slot is not None and LimbTag.MARKED in self.enemy.body.slots[
            chosen.source_slot
        ].tags:
            self.log.emit(
                "jeff_marked_source_selected",
                self.enemy.id,
                source_slot=chosen.source_slot.value,
                response="aggressive_use",
            )
        self.log.emit(
            "enemy_intent_selected",
            self.enemy.id,
            action=chosen.action_id,
            source_slot=chosen.source_slot.value if chosen.source_slot is not None else None,
            target_slot=chosen.target_slot.value if chosen.target_slot is not None else None,
            motivation_id=profile.id,
            motivation_kind=profile.kind.value,
            lethality=profile.lethality,
            score=selection.final_score,
            reasons=list(chosen.reasons),
        )

    def _statuses(self) -> list[str]:
        statuses: list[str] = []
        if self.player.downed:
            statuses.append("Downed")
        if self.player.guard_active:
            statuses.append("Guard Flesh active")
        if self.player.brace_active:
            statuses.append("Brace manual stance active")
        if self.player.brace_charges:
            statuses.append(f"Braced Legs automatic charge {self.player.brace_charges}")
        if self.player.limb_for_life_used:
            statuses.append("Limb for Life used")
        if self.player.debt:
            statuses.append(f"Debt {self.player.debt}")
        for slot, limb in self.player.body.slots.items():
            for tag in sorted(limb.tags, key=lambda value: value.value):
                statuses.append(f"{slot.value}:{tag.value}")
        return statuses

    def statuses(self) -> list[str]:
        """Return the player-facing status list without exposing private helpers."""
        return self._statuses()

    def _action_sources(self) -> dict[str, str]:
        return {
            slot.value: (
                f"{limb.name} - {limb.state.value}"
                if is_usable(limb)
                else f"UNAVAILABLE - {limb.state.value}"
            )
            for slot, limb in self.player.body.slots.items()
        }

    def _targeted_offer(
        self, action_id: str, slot: Slot, target: CombatantRuntime
    ) -> ActionAvailability:
        limb = target.body.slots[slot]
        offer = self.engine.main_action_availability(self.player, action_id, limb)
        return replace(
            offer,
            action_id=f"{action_id}:{slot.value}",
            label=f"{offer.label} -> {limb.name} ({slot.value})",
        )

    def offers(self) -> list[ActionAvailability]:
        if self.complete:
            return []
        if self.encounter in {"Jeff", "Anna"}:
            assert self.enemy is not None
            offers: list[ActionAvailability] = [self.engine.focus_availability(self.player)]
            offers.append(self.engine.fast_item_availability(self.player, "blood_bag"))
            bleeding_target = next(
                (
                    limb
                    for limb in self.player.body.slots.values()
                    if LimbTag.BLEEDING in limb.tags
                ),
                self.player.body.slots[Slot.TORSO],
            )
            cream = self.engine.fast_item_availability(
                self.player, "clotting_cream", bleeding_target
            )
            offers.append(replace(cream, action_id=f"clotting_cream:{bleeding_target.slot.value}"))
            for action_id in ("grip_strike", "claim_the_cut", "bone_scissors", "hell_saw"):
                offers.extend(
                    self._targeted_offer(action_id, slot, self.enemy) for slot in Slot
                )
            offers.append(self.engine.main_action_availability(self.player, "guard_flesh"))
            offers.append(self.engine.main_action_availability(self.player, "brace"))
            offers.append(self.engine.main_action_availability(self.player, "stand"))
            if self.encounter == "Jeff" and self.current_intent_action == "jeff_bargain":
                parameters = self.config.encounter_designs["jeff"].parameters
                bargain_asset = str(parameters["bargain_asset"])
                bargain_slot = Slot(str(parameters["bargain_limb"]))
                asset_name = str(self.config.items[bargain_asset]["name"])
                offers.append(
                    ActionAvailability(
                        "accept_jeff_bargain",
                        f"Give {asset_name} for Jeff's marked {bargain_slot.value}",
                        "resolution",
                        self._jeff_bargain_available(),
                        None
                        if self._jeff_bargain_available()
                        else "The required marked arm or Clotting Cream is unavailable",
                        irreversible=True,
                        risk="Clotting Cream is transferred; the encounter ends by bargain",
                    )
                )
            if self.encounter == "Anna":
                enabled, reason = self.engine.anna_trade_available(self.player, self.enemy)
                offers.append(
                    ActionAvailability(
                        "accept_anna_trade",
                        "Accept Anna's stabilization trade",
                        "resolution",
                        enabled,
                        reason,
                        irreversible=True,
                    )
                )
            offers.append(
                ActionAvailability(
                    "end_session",
                    "End research session",
                    "resolution",
                    True,
                    irreversible=True,
                )
            )
            return offers
        if self.encounter == "Post-Jeff":
            return [
                ActionAvailability(
                    "emergency_graft",
                    "Emergency graft Jeff's Right Arm",
                    "post_fight",
                    self.harvested_jeff_arm is not None,
                    None if self.harvested_jeff_arm is not None else "No graftable Right Arm",
                    cost=int(self.config.rules["harvest"]["emergency_graft_cost"]),
                    irreversible=True,
                    risk="Configured stability roll applies",
                ),
                ActionAvailability(
                    "end_session",
                    "Decline graft and end session",
                    "resolution",
                    True,
                    irreversible=True,
                ),
            ]
        if self.encounter == "Grafting Table":
            return [
                self.engine.table_availability(self.player, choice)
                for choice in (
                    "integrate_arm",
                    "repair_torso",
                    "strengthen_legs",
                    "table_loan",
                    "leave",
                )
            ]
        return []

    def _decision_record(
        self,
        offers: list[ActionAvailability],
        selected: str,
        disposition: str,
        reason: str | None,
    ) -> None:
        self.decisions.append(
            DecisionRecord(
                index=len(self.decisions) + 1,
                encounter=self.encounter,
                round_number=self.log.round_number,
                blood=self.player.blood,
                body=body_summary(self.player),
                statuses=self._statuses(),
                main_available=not self.player.normal_action_consumed,
                focus_available=next(
                    (offer.enabled for offer in offers if offer.action_id == "focus"), False
                ),
                fast_available=any(
                    offer.enabled for offer in offers if offer.timing == "fast"
                ),
                action_sources=self._action_sources(),
                actions_presented=[asdict(offer) for offer in offers],
                selected_action=selected,
                disposition=disposition,
                reason=reason,
            )
        )

    def perform(self, selection: str, *, confirmed: bool | None = None) -> str:
        if self.complete:
            raise IllegalActionError("research session is already complete")
        offers = self.offers()
        offer = next((candidate for candidate in offers if candidate.action_id == selection), None)
        if offer is None:
            reason = "Action was not presented in the current state"
            self._decision_record(offers, selection, "INVALID_ATTEMPT", reason)
            self.log.emit("shell_invalid_attempt", self.player.id, action=selection, reason=reason)
            return reason
        if not offer.enabled:
            reason = offer.reason or "Action is disabled"
            self._decision_record(offers, selection, "DISABLED_ATTEMPT", reason)
            self.log.emit("shell_disabled_attempt", self.player.id, action=selection, reason=reason)
            return reason
        if offer.irreversible and confirmed is not True:
            reason = "Cancelled before commitment"
            self._decision_record(offers, selection, "CANCELLED", reason)
            self.action_sequence.append({"action": selection, "confirmed": False})
            self.log.emit("shell_action_cancelled", self.player.id, action=selection)
            return reason
        self._decision_record(offers, selection, "EXECUTED", None)
        self._execute(selection)
        self.action_sequence.append({"action": selection, "confirmed": confirmed})
        return "executed"

    def _execute(self, selection: str) -> None:
        if selection == "focus":
            self.engine.focus(self.player, self.exact_intent)
            self.current_intent = self.exact_intent
            return
        if selection == "blood_bag":
            self.engine.fast_item(self.player, "blood_bag")
            return
        if selection.startswith("clotting_cream:"):
            slot = Slot(selection.split(":", 1)[1])
            self.engine.fast_item(
                self.player, "clotting_cream", self.player.body.slots[slot]
            )
            return
        if selection == "emergency_graft":
            assert self.harvested_jeff_arm is not None
            self.engine.emergency_graft(
                self.player, self.harvested_jeff_arm, Slot.RIGHT_ARM
            )
            self._begin_anna()
            return
        if selection == "accept_anna_trade":
            assert self.enemy is not None
            self.engine.anna_trade(
                self.enemy, self.player, self.player.body.slots[Slot.RIGHT_ARM]
            )
            self.anna_path = "stabilization_trade"
            self._begin_table()
            return
        if selection == "accept_jeff_bargain":
            assert self.enemy is not None
            parameters = self.config.encounter_designs["jeff"].parameters
            bargain_slot = Slot(str(parameters["bargain_limb"]))
            offered_limb = self.enemy.body.slots[bargain_slot]
            self.harvested_jeff_arm = self.engine.negotiated_item_for_limb_exchange(
                self.player,
                self.enemy,
                str(parameters["bargain_asset"]),
                offered_limb,
                HarvestQuality(str(parameters["bargain_quality"])),
            )
            self.jeff_bargain_accepted = True
            self._finish_jeff(ResolutionKind.BARGAIN)
            return
        if selection.startswith("table:"):
            choice = selection.split(":", 1)[1]
            self.engine.integrate(self.player, choice)
            self.outcome = "COMPLETED"
            self.log.emit("research_session_completed", self.player.id, table_choice=choice)
            return
        if selection == "end_session":
            self.outcome = "ENDED_BY_PARTICIPANT"
            self.log.emit("research_session_ended", self.player.id, reason=self.outcome)
            return
        self._execute_main(selection)

    def _execute_main(self, selection: str) -> None:
        assert self.enemy is not None
        action_id, _, target_name = selection.partition(":")
        target = self.enemy.body.slots[Slot(target_name)] if target_name else None
        quality: HarvestQuality | None = None
        if action_id == "grip_strike":
            assert target is not None
            quality = self.engine.grip(self.player, self.enemy, target)
        elif action_id == "claim_the_cut":
            assert target is not None
            self.engine.claim(self.player, target)
        elif action_id == "bone_scissors":
            assert target is not None
            quality = self.engine.scissors(self.player, self.enemy, target)
        elif action_id == "hell_saw":
            assert target is not None
            quality = self.engine.saw(self.player, self.enemy, target)
        elif action_id == "guard_flesh":
            self.engine.guard_flesh(self.player)
        elif action_id == "brace":
            self.engine.brace(self.player)
        elif action_id == "stand":
            self.engine.stand(self.player)
        else:
            raise IllegalActionError(f"unsupported shell Main action: {selection}")
        if quality in {HarvestQuality.CLEAN, HarvestQuality.STRESSED} and target is not None:
            harvested = self.engine.harvest(target, quality)
            if self.encounter == "Jeff" and target.slot is Slot.RIGHT_ARM:
                self.harvested_jeff_arm = harvested
            if self.encounter == "Anna" and target.slot is Slot.RIGHT_ARM:
                self.anna_path = "greed_harvest"
                self._begin_table()
                return
        if self._resolve_encounter_after_player_action():
            return
        self._resolve_enemy_action()
        if not self.complete:
            self._start_round()

    def _resolve_encounter_after_player_action(self) -> bool:
        assert self.enemy is not None
        if self.encounter == "Jeff":
            arms = (self.enemy.body.slots[Slot.LEFT_ARM], self.enemy.body.slots[Slot.RIGHT_ARM])
            both_unusable = all(not is_usable(arm) for arm in arms)
            if both_unusable:
                self.engine.add_plead_pressure(self.enemy, "Jeff both arms lost")
            if self.enemy.plead_pressure >= int(self.config.rules["plead"]["basic_threshold"]):
                self.log.emit(
                    "generic_plead_resolved",
                    self.enemy.id,
                    pressure=self.enemy.plead_pressure,
                )
                self.jeff_surrendered = True
                self._finish_jeff(ResolutionKind.SURRENDER)
                return True
            if both_unusable:
                self.log.emit(
                    "jeff_incapacity_surrender",
                    self.enemy.id,
                    reason="both arm sources unusable",
                )
                self.jeff_surrendered = True
                self._finish_jeff(ResolutionKind.INCAPACITY)
                return True
        elif self.encounter == "Anna":
            arm = self.enemy.body.slots[Slot.RIGHT_ARM]
            if not is_usable(arm):
                self.anna_path = "greed_failed_or_disabled"
                self.log.emit(
                    "anna_encounter_resolved",
                    self.enemy.id,
                    reason="Surgical Jab source unusable",
                )
                self._begin_table()
                return True
        return False

    def _jeff_outcome_facts(self) -> dict[str, bool]:
        assert self.enemy is not None
        arms = (
            self.enemy.body.slots[Slot.LEFT_ARM],
            self.enemy.body.slots[Slot.RIGHT_ARM],
        )
        return {
            "player_has_graftable_jeff_right_arm": self.harvested_jeff_arm is not None,
            "jeff_offensive_sources_unusable": all(not is_usable(arm) for arm in arms),
            "jeff_surrendered": self.jeff_surrendered,
            "jeff_has_clotting_cream": self.enemy.inventory.get("clotting_cream", 0) > 0,
            "player_dead": self.player.dead,
            "jeff_survived_resolution": not self.enemy.collapsed,
        }

    def _record_jeff_outcome(self, resolution: ResolutionKind) -> None:
        if any(outcome.encounter_id == "jeff" for outcome in self.encounter_outcomes):
            return
        assert self.enemy is not None
        outcome = evaluate_encounter_outcome(
            self.config.encounter_designs["jeff"],
            self._jeff_outcome_facts(),
            resolution,
        )
        self.encounter_outcomes.append(outcome)
        self.log.emit(
            "encounter_outcome_evaluated",
            self.enemy.id,
            encounter_id="jeff",
            resolution=resolution.value,
            actor_outcomes=[asdict(actor) for actor in outcome.actors],
        )

    def _finish_jeff(self, resolution: ResolutionKind) -> None:
        self._record_jeff_outcome(resolution)
        if self.harvested_jeff_arm is None:
            self.outcome = "INCOMPLETE_NO_GRAFTABLE_RIGHT_ARM"
            self.log.emit(
                "research_session_ended",
                self.player.id,
                reason=self.outcome,
            )
            return
        self.encounter = "Post-Jeff"
        self.enemy = None
        self.current_intent_action = ""
        self.current_intent_source = None
        self.current_intent_target = None
        self.current_intent = ""

    def _resolve_enemy_action(self) -> None:
        assert self.enemy is not None
        if self.encounter == "Jeff":
            if self.current_intent_action == "jeff_bargain":
                bargain_slot = Slot(
                    str(self.config.encounter_designs["jeff"].parameters["bargain_limb"])
                )
                self.jeff_bargain_rejected = True
                self.last_enemy_action = "jeff_bargain"
                self.last_enemy_target = bargain_slot
                self.log.emit(
                    "jeff_bargain_rejected",
                    self.enemy.id,
                    reason="player continued with a hostile Main action",
                )
                profile = self.config.motivation_profiles[
                    self.config.encounter_designs["jeff"].actor_motivations["enemy"]
                ]
                self.log.emit(
                    "enemy_behavior_triggered",
                    self.enemy.id,
                    trigger="bargain_rejected",
                    response="resume_combat",
                    motivation_id=profile.id,
                    stat_modifier_applied=False,
                )
                return
            source = self.current_intent_source
            target = self.current_intent_target
            if (
                self.current_intent_action != "desperate_swing"
                or source is None
                or target is None
                or not is_usable(self.enemy.body.slots[source])
            ):
                self.log.emit(
                    "enemy_action_cancelled",
                    self.enemy.id,
                    source_slot=source.value if source is not None else None,
                    reason="declared source is unavailable",
                )
                return
            self.engine.enemy_attack(
                self.enemy,
                self.player,
                source,
                target,
                self.config.actions["desperate_swing"].damage,
            )
            self.last_enemy_action = self.current_intent_action
            self.last_enemy_target = target
        elif self.encounter == "Anna":
            self.engine.enemy_attack(
                self.enemy,
                self.player,
                Slot.RIGHT_ARM,
                Slot.TORSO,
                8,
                can_bleed=True,
            )
        if self.player.dead:
            self.outcome = "PLAYER_DEATH"
            if self.encounter == "Jeff":
                self._record_jeff_outcome(ResolutionKind.DEATH)
            self.log.emit("research_session_ended", self.player.id, reason=self.outcome)

    def _begin_anna(self) -> None:
        self.encounter = "Anna"
        self.enemy = enemy_from_config(self.config, "anna")
        refresh_fight_tools(self.player)
        self.engine.apply_stabilized(
            self.enemy,
            self.enemy.body.slots[Slot.RIGHT_ARM],
            "Approved Anna greed-path setup",
        )
        self._start_round()

    def _begin_table(self) -> None:
        self.engine.end_round(self.player)
        self.encounter = "Grafting Table"
        self.enemy = None
        self.current_intent_action = ""
        self.current_intent_source = None
        self.current_intent_target = None
        self.current_intent = ""

    def export_payload(self) -> dict[str, Any]:
        return {
            "metadata": {
                **asdict(self.metadata),
                "evidence_class": self.metadata.evidence_class.value,
                "rules_version": str(self.config.rules["rules_version"]),
                "schema_version": self.config.schema_version,
                "content_version": self.config.content_version,
                "scenario_version": self.config.scenario_version,
                "interface_version": INTERFACE_VERSION,
                "approved_sequence": APPROVED_SEQUENCE,
                "parent_baseline": "9b3f72b33e0c6b27f29e90e72f91841e5f0dbb81",
            },
            "decision_points": [asdict(decision) for decision in self.decisions],
            "action_sequence": self.action_sequence,
            "encounter_design": {
                "jeff": {
                    "actor_motivations": dict(
                        self.config.encounter_designs["jeff"].actor_motivations
                    ),
                    "victory_routes": [
                        asdict(route)
                        for route in self.config.encounter_designs["jeff"].victory_routes
                    ],
                }
            },
            "encounter_outcomes": [asdict(outcome) for outcome in self.encounter_outcomes],
            "jeff_test_signals": {
                "bargain_offered": self.jeff_bargain_offered,
                "bargain_rejected": self.jeff_bargain_rejected,
                "bargain_accepted": self.jeff_bargain_accepted,
            },
            "outcome": self.outcome,
            "anna_path": self.anna_path,
            "table_choice": self.metrics.table_choice,
            "final_blood": self.player.blood,
            "final_body": body_summary(self.player),
            "events": [asdict(event) for event in self.log.events],
        }

    def export_json(self) -> str:
        return json.dumps(self.export_payload(), indent=2, sort_keys=True, default=str)

    def human_summary(self) -> str:
        return "\n".join(
            [
                f"Session {self.metadata.session_id} ({self.metadata.evidence_class.value})",
                f"Seed: {self.metadata.seed}; interface: {INTERFACE_VERSION}",
                f"Outcome: {self.outcome}; Anna path: {self.anna_path or 'not reached'}",
                f"Table choice: {self.metrics.table_choice or 'none'}",
                f"Final Blood: {self.player.blood}",
                f"Decisions: {len(self.decisions)}; events: {len(self.log.events)}",
                "Final body:",
                *(
                    f"- {slot}: {description}"
                    for slot, description in body_summary(self.player).items()
                ),
            ]
        )

    def write_exports(self, json_path: Path, summary_path: Path) -> None:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(self.export_json() + "\n", encoding="utf-8")
        summary_path.write_text(self.human_summary() + "\n", encoding="utf-8")

    def write_transcript(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(self.transcript_lines) + "\n", encoding="utf-8")

    def render_state(self) -> str:
        offers = self.offers()
        lines = [
            f"Encounter: {self.encounter} | Round: {self.log.round_number}",
            f"Blood: {self.player.blood}",
            f"Statuses: {', '.join(self._statuses()) or 'none'}",
            f"Main available: {not self.player.normal_action_consumed}",
            f"Focus available: {any(o.action_id == 'focus' and o.enabled for o in offers)}",
            f"Fast available: {any(o.timing == 'fast' and o.enabled for o in offers)}",
            "Body:",
            *(f"  {slot}: {value}" for slot, value in body_summary(self.player).items()),
            f"Visible intent: {self.current_intent or 'none'}",
            "Actions:",
        ]
        for offer in offers:
            status = "LEGAL" if offer.enabled else f"DISABLED: {offer.reason}"
            details = f"cost={offer.cost}"
            if offer.risk:
                details += f"; risk={offer.risk}"
            lines.append(f"  {offer.action_id}: {offer.label} [{status}; {details}]")
        return "\n".join(lines)

    def run_console(
        self,
        input_fn: Callable[[str], str] = input,
        output_fn: Callable[[str], None] = print,
    ) -> None:
        def emit(value: str) -> None:
            self.transcript_lines.append(value)
            output_fn(value)

        while not self.complete:
            emit(self.render_state())
            selection = input_fn("Select action: ").strip()
            emit(f"Select action: {selection}")
            offer = next(
                (candidate for candidate in self.offers() if candidate.action_id == selection),
                None,
            )
            confirmed: bool | None = None
            if offer is not None and offer.enabled and offer.irreversible:
                response = input_fn("Confirm irreversible action? [y/N]: ").strip()
                emit(f"Confirm irreversible action? [y/N]: {response}")
                confirmed = response.lower() == "y"
            emit(self.perform(selection, confirmed=confirmed))
        emit(self.human_summary())


def replay_session(
    metadata: SessionMetadata,
    actions: Iterable[dict[str, Any]],
    config: SimulatorConfig | None = None,
) -> InteractiveResearchSession:
    session = InteractiveResearchSession(metadata, config or load_config())
    for item in actions:
        if session.complete:
            break
        session.perform(str(item["action"]), confirmed=item.get("confirmed"))
    return session
