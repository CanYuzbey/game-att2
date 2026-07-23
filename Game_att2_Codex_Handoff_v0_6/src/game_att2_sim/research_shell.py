"""Minimal deterministic free-choice research shell for the approved simulator sequence."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, replace
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Iterable

from .config_loader import SimulatorConfig, load_config
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

INTERFACE_VERSION = "0.1"
APPROVED_SEQUENCE = "S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table"


class EvidenceClass(str, Enum):
    OWNER_DIAGNOSTIC = "OWNER_DIAGNOSTIC"
    EXTERNAL_PILOT = "EXTERNAL_PILOT"
    AUTOMATED_REGRESSION = "AUTOMATED_REGRESSION"


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
            if code.startswith(("OWNER-", "SELF-", "AUTO-")):
                raise ValueError("owner/automated codes cannot be labeled EXTERNAL_PILOT")
        elif not code.startswith("AUTO-"):
            raise ValueError("AUTOMATED_REGRESSION requires an AUTO- code")
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
            source = self._first_usable_enemy_arm()
            self.current_intent = (
                f"Desperate Swing from {source.value} against torso"
                if source is not None
                else "No valid Desperate Swing source"
            )
        elif self.encounter == "Anna":
            self.current_intent = "Surgical Jab from right_arm against torso"
        else:
            self.current_intent = ""

    def _first_usable_enemy_arm(self) -> Slot | None:
        if self.enemy is None:
            return None
        for slot in (Slot.LEFT_ARM, Slot.RIGHT_ARM):
            if is_usable(self.enemy.body.slots[slot]):
                return slot
        return None

    def _statuses(self) -> list[str]:
        statuses: list[str] = []
        if self.player.downed:
            statuses.append("Downed")
        if self.player.guard_active:
            statuses.append("Guard Flesh active")
        if self.player.debt:
            statuses.append(f"Debt {self.player.debt}")
        for slot, limb in self.player.body.slots.items():
            for tag in sorted(limb.tags, key=lambda value: value.value):
                statuses.append(f"{slot.value}:{tag.value}")
        return statuses

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
            self.engine.focus(self.player, self.current_intent)
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
                self._finish_jeff()
                return True
            if both_unusable:
                self.log.emit(
                    "jeff_incapacity_surrender",
                    self.enemy.id,
                    reason="both arm sources unusable",
                )
                self._finish_jeff()
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

    def _finish_jeff(self) -> None:
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
        self.current_intent = ""

    def _resolve_enemy_action(self) -> None:
        assert self.enemy is not None
        if self.encounter == "Jeff":
            source = self._first_usable_enemy_arm()
            if source is None:
                return
            self.engine.enemy_attack(
                self.enemy, self.player, source, Slot.TORSO, 10
            )
        elif self.encounter == "Anna":
            self.engine.enemy_attack(
                self.enemy,
                self.player,
                Slot.RIGHT_ARM,
                Slot.TORSO,
                8,
                can_bleed=True,
            )
        if self.player.collapsed:
            self.outcome = "PLAYER_COLLAPSE"
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
