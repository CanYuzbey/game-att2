"""Playable Jeff-locked combat loop for the Phase 1 interactive CLI.

Scope lock: starting body S-001 and the Jeff encounter only. Emergency
grafting, Anna, and the Grafting Table are deliberately outside this
interface; ``research_shell`` still owns the full approved sequence and its
evidence contract. This module owns no rules of its own -- it reuses
``RuleEngine`` and turns the emitted event stream into Pillar 5 readability
records. It never prints.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from .config_loader import SimulatorConfig, load_config
from .enums import HarvestQuality, LimbState, LimbTag, Slot
from .events import EventLog
from .factory import enemy_from_config, player_from_start, refresh_fight_tools
from .models import (
    ActionAvailability,
    CombatantRuntime,
    Event,
    LimbRuntime,
    ScenarioMetrics,
)
from .rng import RNGService, SeededRNG
from .rules import RuleEngine, is_usable

PLAY_INTERFACE_VERSION = "0.1"
LOCKED_START_BODY = "s001"
LOCKED_ENEMY = "jeff"
LOCKED_SCOPE = "S-001 -> Jeff (no graft, no Anna, no Grafting Table)"

#: Harness guard only. Not a game rule: the paper prototype has no round cap.
DEFAULT_ROUND_LIMIT = 50

ATTACK_ACTIONS = ("grip_strike", "claim_the_cut", "bone_scissors", "hell_saw")
DEFENCE_ACTIONS = ("guard_flesh", "brace", "stand")
FAST_ITEMS = ("blood_bag", "clotting_cream")

JEFF_SWING_DAMAGE = 10
ONE_USE_TOOLS = ("claim_the_cut", "bone_scissors", "hell_saw")

_BAND_ORDER = ("COLLAPSE", "CRITICAL", "DANGEROUS", "NORMAL", "STRONG", "OVERFULL")

_SLOT_LABELS = {
    Slot.HEAD: "Kafa",
    Slot.TORSO: "Gövde",
    Slot.LEFT_ARM: "Sol Kol",
    Slot.RIGHT_ARM: "Sağ Kol",
    Slot.LEGS: "Bacaklar",
    Slot.CORE: "Çekirdek",
}

_STATE_LABELS = {
    LimbState.INTACT: "sağlam",
    LimbState.DAMAGED: "hasarlı",
    LimbState.CRITICAL: "kritik",
    LimbState.DISABLED: "devre dışı",
    LimbState.SEVERED: "koparılmış",
    LimbState.MISSING: "yok",
    LimbState.RUINED: "harap",
}

_TAG_LABELS = {
    LimbTag.BLEEDING: "Bleeding (kanıyor)",
    LimbTag.GRAFTED: "Grafted (dikilmiş)",
    LimbTag.UNSTABLE: "Unstable (dengesiz)",
    LimbTag.INTEGRATED: "Integrated (oturmuş)",
    LimbTag.STABILIZED: "Stabilized (sabitlenmiş)",
    LimbTag.MARKED: "Marked (işaretli)",
    LimbTag.HANGING: "Hanging (sarkıyor)",
    LimbTag.PROTECTED: "Protected (korumalı)",
}


def slot_label(slot: Slot) -> str:
    return _SLOT_LABELS[slot]


def state_label(state: LimbState) -> str:
    return _STATE_LABELS[state]


def tag_label(tag: LimbTag) -> str:
    return _TAG_LABELS[tag]


class PlayOutcome(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    JEFF_YIELDED = "JEFF_YIELDED"
    PLAYER_COLLAPSE = "PLAYER_COLLAPSE"
    ENDED_BY_PLAYER = "ENDED_BY_PLAYER"
    ROUND_LIMIT_REACHED = "ROUND_LIMIT_REACHED"


class MenuCategory(str, Enum):
    ATTACK = "attack"
    FOCUS = "focus"
    ITEM = "item"
    DEFEND = "defend"
    SESSION = "session"


@dataclass(frozen=True)
class PlayOffer:
    """One selectable line, tagged with the menu branch that presents it."""

    availability: ActionAvailability
    category: MenuCategory
    target_slot: Slot | None = None
    target_name: str | None = None

    @property
    def action_id(self) -> str:
        return self.availability.action_id

    @property
    def enabled(self) -> bool:
        return self.availability.enabled

    @property
    def reason(self) -> str | None:
        return self.availability.reason

    @property
    def cost(self) -> int:
        return self.availability.cost

    @property
    def risk(self) -> str | None:
        return self.availability.risk

    @property
    def label(self) -> str:
        return self.availability.label

    @property
    def target_text(self) -> str:
        if self.target_slot is None:
            return "-"
        return f"{self.target_name} ({slot_label(self.target_slot)})"


@dataclass(frozen=True)
class ActionReport:
    """Pillar 5 record: every major action answers the same five questions."""

    round_number: int
    actor: str
    action_label: str
    targeted: str
    changed: tuple[str, ...]
    blood_cost: str
    gained: tuple[str, ...]
    new_risks: tuple[str, ...]

    def as_pairs(self) -> tuple[tuple[str, tuple[str, ...]], ...]:
        return (
            ("Ne hedeflendi?", (self.targeted,)),
            ("Ne değişti?", self.changed or ("kayda değer bir değişim yok",)),
            ("Kan maliyeti?", (self.blood_cost,)),
            ("Ne kazanıldı?", self.gained or ("bu eylem doğrudan bir kazanç vermedi",)),
            ("Hangi yeni risk doğdu?", self.new_risks or ("yeni bir risk doğmadı",)),
        )


@dataclass(frozen=True)
class HarvestRecord:
    slot: Slot
    limb_name: str
    quality: HarvestQuality


@dataclass(frozen=True)
class PerformResult:
    accepted: bool
    message: str
    reports: tuple[ActionReport, ...] = ()


@dataclass(frozen=True)
class _LimbSnapshot:
    owner: str
    slot: Slot
    name: str
    integrity: int
    state: LimbState
    tags: frozenset[LimbTag]


@dataclass(frozen=True)
class _Snapshot:
    blood: int
    band: str
    downed: bool
    guard_active: bool
    enemy_rage: bool
    plead_pressure: int
    tools: tuple[tuple[str, int], ...]
    limbs: tuple[_LimbSnapshot, ...]

    def limb(self, owner: str, slot: Slot) -> _LimbSnapshot | None:
        for entry in self.limbs:
            if entry.owner == owner and entry.slot is slot:
                return entry
        return None


def blood_band(blood: int, rules: dict[str, Any]) -> str:
    tiers = rules["blood"]
    if blood <= int(tiers["collapse_at"]):
        return "COLLAPSE"
    if blood <= int(tiers["critical_max"]):
        return "CRITICAL"
    if blood <= int(tiers["dangerous_max"]):
        return "DANGEROUS"
    if blood <= int(tiers["normal_max"]):
        return "NORMAL"
    if blood <= int(tiers["strong_max"]):
        return "STRONG"
    return "OVERFULL"


@dataclass
class PlaySession:
    """One playable Jeff fight driven by explicit player selections."""

    seed: int = 42
    config: SimulatorConfig = field(default_factory=load_config)
    rng: RNGService | None = None
    round_limit: int = DEFAULT_ROUND_LIMIT
    player: CombatantRuntime = field(init=False)
    enemy: CombatantRuntime = field(init=False)
    log: EventLog = field(init=False)
    metrics: ScenarioMetrics = field(init=False)
    engine: RuleEngine = field(init=False)
    outcome: PlayOutcome = field(init=False, default=PlayOutcome.IN_PROGRESS)
    reports: list[ActionReport] = field(init=False, default_factory=list)
    harvests: list[HarvestRecord] = field(init=False, default_factory=list)
    exact_intent: str = field(init=False, default="")
    public_intent: str = field(init=False, default="")
    revealed_intent: str | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        if self.round_limit < 1:
            raise ValueError("round_limit must be positive")
        self.rng = self.rng or SeededRNG(self.seed)
        self.player = player_from_start(self.config, LOCKED_START_BODY)
        self.enemy = enemy_from_config(self.config, LOCKED_ENEMY)
        self.log = EventLog()
        self.metrics = ScenarioMetrics("play_cli_jeff", self.seed, "free_choice")
        self.engine = RuleEngine(self.config, self.rng, self.log, self.metrics, tutorial=True)
        refresh_fight_tools(self.player)
        self.engine.start_encounter(self.player)
        self.log.emit(
            "play_session_started",
            self.player.id,
            interface_version=PLAY_INTERFACE_VERSION,
            scope=LOCKED_SCOPE,
            seed=self.seed,
        )
        self._start_round()

    # ---------------------------------------------------------------- state

    @property
    def complete(self) -> bool:
        return self.outcome is not PlayOutcome.IN_PROGRESS

    @property
    def rules(self) -> dict[str, Any]:
        return self.config.rules

    @property
    def graftable_right_arm(self) -> HarvestRecord | None:
        """The Phase 1 payoff signal: a Right Arm good enough to graft later."""
        for record in self.harvests:
            if record.slot is Slot.RIGHT_ARM and record.quality is not HarvestQuality.RUINED:
                return record
        return None

    def player_statuses(self) -> list[str]:
        statuses: list[str] = []
        if self.player.downed:
            statuses.append("Downed (yerde)")
        if self.player.guard_active:
            statuses.append("Guard Flesh aktif")
        if self.player.brace_active:
            statuses.append("Brace aktif")
        elif not self.player.brace_used and is_usable(self.player.body.slots[Slot.LEGS]):
            statuses.append("Brace hazır")
        if self.player.brace_charges:
            statuses.append(f"Brace yükü {self.player.brace_charges}")
        if self.player.panic_pulse_used:
            statuses.append("Panic Pulse tükendi")
        if self.player.soft_collapse_used:
            statuses.append("Limb for Life kullanıldı")
        if self.player.debt:
            statuses.append(f"Borç {self.player.debt}")
        return statuses

    def enemy_statuses(self) -> list[str]:
        threshold = int(self.rules["plead"]["basic_threshold"])
        statuses = [f"Plead baskısı {self.enemy.plead_pressure}/{threshold}"]
        if self.enemy.rage:
            statuses.append("Rage (sonraki vuruş güçlü)")
        return statuses

    def intent_text(self) -> str:
        """Public telegraph until Focus pays for the exact source and target."""
        if self.revealed_intent is not None:
            return self.revealed_intent
        return self.public_intent

    def intent_is_revealed(self) -> bool:
        return self.revealed_intent is not None

    def inventory_lines(self) -> list[str]:
        lines: list[str] = []
        for item_id in ("blood_bag", "clotting_cream", *ONE_USE_TOOLS):
            count = self.player.inventory.get(item_id, 0)
            name = str(self.config.items[item_id]["name"])
            lines.append(f"{name} x{count}")
        return lines

    # --------------------------------------------------------------- offers

    def offers(self) -> list[PlayOffer]:
        if self.complete:
            return []
        offers: list[PlayOffer] = []
        for action_id in ATTACK_ACTIONS:
            offers.extend(self._attack_target_offers(action_id))
        offers.append(
            PlayOffer(self.engine.focus_availability(self.player), MenuCategory.FOCUS)
        )
        offers.extend(self._item_offers())
        for action_id in DEFENCE_ACTIONS:
            offers.append(
                PlayOffer(
                    self.engine.main_action_availability(self.player, action_id),
                    MenuCategory.DEFEND,
                )
            )
        offers.append(
            PlayOffer(
                ActionAvailability(
                    "end_session",
                    "Dövüşü bırak ve oturumu bitir",
                    "resolution",
                    True,
                    irreversible=True,
                ),
                MenuCategory.SESSION,
            )
        )
        if not any(
            offer.enabled
            for offer in offers
            if offer.availability.timing == "main"
        ):
            offers.append(
                PlayOffer(
                    ActionAvailability(
                        "forfeit_main",
                        "Ana eylemi geç (yasal ana eylem kalmadı)",
                        "resolution",
                        True,
                        irreversible=True,
                    ),
                    MenuCategory.SESSION,
                )
            )
        return offers

    def _attack_target_offers(self, action_id: str) -> list[PlayOffer]:
        offers: list[PlayOffer] = []
        for slot in Slot:
            limb = self.enemy.body.slots[slot]
            availability = self.engine.main_action_availability(self.player, action_id, limb)
            offers.append(
                PlayOffer(
                    ActionAvailability(
                        action_id=f"{action_id}:{slot.value}",
                        label=availability.label,
                        timing=availability.timing,
                        enabled=availability.enabled,
                        reason=availability.reason,
                        cost=availability.cost,
                        source_slot=availability.source_slot,
                        target_slot=slot,
                        irreversible=availability.irreversible,
                        risk=availability.risk,
                    ),
                    MenuCategory.ATTACK,
                    target_slot=slot,
                    target_name=limb.name,
                )
            )
        return offers

    def _item_offers(self) -> list[PlayOffer]:
        offers: list[PlayOffer] = []
        offers.append(
            PlayOffer(
                self.engine.fast_item_availability(self.player, "blood_bag"),
                MenuCategory.ITEM,
            )
        )
        for slot, limb in self.player.body.slots.items():
            if LimbTag.BLEEDING not in limb.tags:
                continue
            availability = self.engine.fast_item_availability(
                self.player, "clotting_cream", limb
            )
            offers.append(
                PlayOffer(
                    ActionAvailability(
                        action_id=f"clotting_cream:{slot.value}",
                        label=availability.label,
                        timing=availability.timing,
                        enabled=availability.enabled,
                        reason=availability.reason,
                        cost=availability.cost,
                        target_slot=slot,
                    ),
                    MenuCategory.ITEM,
                    target_slot=slot,
                    target_name=limb.name,
                )
            )
        if not any(offer.action_id.startswith("clotting_cream") for offer in offers):
            torso = self.player.body.slots[Slot.TORSO]
            availability = self.engine.fast_item_availability(
                self.player, "clotting_cream", torso
            )
            offers.append(PlayOffer(availability, MenuCategory.ITEM))
        return offers

    def offers_in(self, category: MenuCategory) -> list[PlayOffer]:
        return [offer for offer in self.offers() if offer.category is category]

    def attack_action_summaries(self) -> list[tuple[str, bool, str | None]]:
        """Collapse the targeted attack matrix into one line per action."""
        summaries: list[tuple[str, bool, str | None]] = []
        for action_id in ATTACK_ACTIONS:
            targeted = self._attack_target_offers(action_id)
            enabled = any(offer.enabled for offer in targeted)
            reason = None if enabled else self._blocking_reason(targeted)
            summaries.append((action_id, enabled, reason))
        return summaries

    @staticmethod
    def _blocking_reason(targeted: list[PlayOffer]) -> str | None:
        reasons = [offer.reason for offer in targeted if offer.reason]
        if not reasons:
            return None
        shared = [reason for reason in reasons if reasons.count(reason) == len(reasons)]
        return shared[0] if shared else "Hiçbir hedef bu eylem için uygun değil"

    def find_offer(self, action_id: str) -> PlayOffer | None:
        return next(
            (offer for offer in self.offers() if offer.action_id == action_id), None
        )

    def action_display_name(self, action_id: str) -> str:
        base = action_id.split(":", 1)[0]
        if base in self.config.actions:
            return self.config.actions[base].name
        if base in self.config.items:
            return str(self.config.items[base]["name"])
        return base.replace("_", " ").title()

    # -------------------------------------------------------------- resolve

    def perform(self, selection: str) -> PerformResult:
        if self.complete:
            return PerformResult(False, "Oturum bitti; yeni eylem alınamaz.")
        offer = self.find_offer(selection)
        if offer is None:
            reason = "Bu eylem şu anda sunulmuyor."
            self.log.emit("play_invalid_attempt", self.player.id, action=selection, reason=reason)
            return PerformResult(False, reason)
        if not offer.enabled:
            reason = offer.reason or "Eylem şu anda kapalı."
            self.log.emit("play_disabled_attempt", self.player.id, action=selection, reason=reason)
            return PerformResult(False, reason)

        if selection == "end_session":
            self.outcome = PlayOutcome.ENDED_BY_PLAYER
            self.log.emit("play_session_ended", self.player.id, reason=self.outcome.value)
            return PerformResult(True, "Oturum oyuncu tarafından bitirildi.")

        targeted = self._targeted_text(offer)
        before = self._snapshot()
        start = len(self.log.events)
        reports: list[ActionReport] = []

        if selection == "forfeit_main":
            self.log.emit(
                "play_main_action_forfeited",
                self.player.id,
                reason="no legal Main action was available",
            )
            self.player.normal_action_consumed = True
        else:
            self._execute(selection, offer)

        pre_main = offer.availability.timing in {"focus", "fast"}
        # Resolve the encounter before closing the report window, so the action
        # that ends the fight is the action whose record says the fight ended.
        yielded = False if pre_main else self._resolve_jeff_after_player_action()

        reports.append(
            self._report(
                actor="Sen",
                action_label=self.action_display_name(selection),
                targeted=targeted,
                before=before,
                start=start,
            )
        )

        if pre_main:
            # Focus and Fast items still spend Blood, so they can collapse you
            # before the Main action is ever chosen.
            self._check_collapse()
            return PerformResult(True, "executed", tuple(reports))

        if yielded:
            return PerformResult(True, "executed", tuple(reports))

        enemy_before = self._snapshot()
        enemy_start = len(self.log.events)
        enemy_action = self._resolve_enemy_action()
        if enemy_action is not None:
            reports.append(
                self._report(
                    actor=self.enemy.name,
                    action_label=enemy_action[0],
                    targeted=enemy_action[1],
                    before=enemy_before,
                    start=enemy_start,
                )
            )
        if self._check_collapse():
            return PerformResult(True, "executed", tuple(reports))

        if self.log.round_number >= self.round_limit:
            self.outcome = PlayOutcome.ROUND_LIMIT_REACHED
            self.log.emit(
                "play_session_ended",
                self.player.id,
                reason=self.outcome.value,
                round_limit=self.round_limit,
            )
            return PerformResult(True, "executed", tuple(reports))

        self._start_round()
        # Start-of-round Bleeding is its own collapse route.
        self._check_collapse()
        return PerformResult(True, "executed", tuple(reports))

    def _check_collapse(self) -> bool:
        if not self.player.collapsed or self.complete:
            return False
        self.outcome = PlayOutcome.PLAYER_COLLAPSE
        self.log.emit("play_session_ended", self.player.id, reason=self.outcome.value)
        return True

    def _targeted_text(self, offer: PlayOffer) -> str:
        name = self.action_display_name(offer.action_id)
        if offer.category is MenuCategory.ATTACK:
            return f"{name} -> {self.enemy.name}: {offer.target_text}"
        if offer.target_slot is not None:
            return f"{name} -> kendi {offer.target_text}"
        if offer.category is MenuCategory.FOCUS:
            return f"{name} -> {self.enemy.name} niyeti"
        return f"{name} -> kendin"

    def _execute(self, selection: str, offer: PlayOffer) -> None:
        if selection == "focus":
            self.revealed_intent = self.engine.focus(self.player, self.exact_intent)
            return
        if selection == "blood_bag":
            self.engine.fast_item(self.player, "blood_bag")
            return
        if selection.startswith("clotting_cream"):
            assert offer.target_slot is not None
            self.engine.fast_item(
                self.player, "clotting_cream", self.player.body.slots[offer.target_slot]
            )
            return
        self._execute_main(selection, offer)

    def _execute_main(self, selection: str, offer: PlayOffer) -> None:
        action_id = selection.split(":", 1)[0]
        target: LimbRuntime | None = (
            self.enemy.body.slots[offer.target_slot] if offer.target_slot is not None else None
        )
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
        else:  # pragma: no cover - offers() cannot present anything else
            raise AssertionError(f"unsupported play Main action: {selection}")
        if target is not None and quality in {HarvestQuality.CLEAN, HarvestQuality.STRESSED}:
            harvested = self.engine.harvest(target, quality)
            self.harvests.append(
                HarvestRecord(target.slot, harvested.limb.name, quality)
            )

    def _resolve_jeff_after_player_action(self) -> bool:
        arms = (
            self.enemy.body.slots[Slot.LEFT_ARM],
            self.enemy.body.slots[Slot.RIGHT_ARM],
        )
        both_unusable = all(not is_usable(arm) for arm in arms)
        if both_unusable:
            self.engine.add_plead_pressure(self.enemy, "Jeff both arms lost")
        if self.enemy.plead_pressure >= int(self.rules["plead"]["basic_threshold"]):
            self.log.emit(
                "generic_plead_resolved", self.enemy.id, pressure=self.enemy.plead_pressure
            )
            self._finish_jeff("plead pressure reached the threshold")
            return True
        if both_unusable:
            self.log.emit(
                "jeff_incapacity_surrender",
                self.enemy.id,
                reason="both arm sources unusable",
            )
            self._finish_jeff("both arm sources unusable")
            return True
        return False

    def _finish_jeff(self, reason: str) -> None:
        self.engine.end_round(self.player)
        self.outcome = PlayOutcome.JEFF_YIELDED
        self.log.emit(
            "play_session_ended",
            self.player.id,
            reason=self.outcome.value,
            detail=reason,
        )

    def _resolve_enemy_action(self) -> tuple[str, str] | None:
        source = self._first_usable_enemy_arm()
        if source is None:
            self.log.emit(
                "enemy_action_cancelled",
                self.enemy.id,
                reason="no usable arm source",
            )
            return None
        torso = self.player.body.slots[Slot.TORSO]
        label = self.config.actions["desperate_swing"].name
        targeted = (
            f"{label} ({self.enemy.name}: {slot_label(source)}) -> senin "
            f"{torso.name} ({slot_label(Slot.TORSO)})"
        )
        self.engine.enemy_attack(
            self.enemy, self.player, source, Slot.TORSO, JEFF_SWING_DAMAGE
        )
        return label, targeted

    def _first_usable_enemy_arm(self) -> Slot | None:
        for slot in (Slot.LEFT_ARM, Slot.RIGHT_ARM):
            if is_usable(self.enemy.body.slots[slot]):
                return slot
        return None

    def _start_round(self) -> None:
        self.engine.start_round(self.player)
        self.revealed_intent = None
        source = self._first_usable_enemy_arm()
        swing = self.config.actions["desperate_swing"].name
        if source is None:
            self.exact_intent = f"{self.enemy.name} saldırabilecek durumda değil"
            self.public_intent = self.exact_intent
            return
        self.exact_intent = (
            f"{swing}: {slot_label(source)} kaynağından {slot_label(Slot.TORSO)} hedefine"
        )
        self.public_intent = (
            f"{self.enemy.name} bir {swing} için geriliyor "
            "(kaynak ve hedef yuva belirsiz)"
        )

    # ------------------------------------------------------------ reporting

    def _snapshot(self) -> _Snapshot:
        limbs: list[_LimbSnapshot] = []
        for owner_label, actor in (("Sen", self.player), (self.enemy.name, self.enemy)):
            for slot, limb in actor.body.slots.items():
                limbs.append(
                    _LimbSnapshot(
                        owner=owner_label,
                        slot=slot,
                        name=limb.name,
                        integrity=limb.integrity,
                        state=limb.state,
                        tags=frozenset(limb.tags),
                    )
                )
        return _Snapshot(
            blood=self.player.blood,
            band=blood_band(self.player.blood, self.rules),
            downed=self.player.downed,
            guard_active=self.player.guard_active,
            enemy_rage=self.enemy.rage,
            plead_pressure=self.enemy.plead_pressure,
            tools=tuple(
                (item, self.player.inventory.get(item, 0))
                for item in ("blood_bag", "clotting_cream", *ONE_USE_TOOLS)
            ),
            limbs=tuple(limbs),
        )

    def _report(
        self,
        *,
        actor: str,
        action_label: str,
        targeted: str,
        before: _Snapshot,
        start: int,
    ) -> ActionReport:
        after = self._snapshot()
        events = self.log.events[start:]
        report = ActionReport(
            round_number=self.log.round_number,
            actor=actor,
            action_label=action_label,
            targeted=targeted,
            changed=tuple(self._changes(before, after, events)),
            blood_cost=self._blood_cost(before, after, events),
            gained=tuple(self._gains(before, after, events)),
            new_risks=tuple(self._risks(before, after, events)),
        )
        self.reports.append(report)
        return report

    def _changes(
        self, before: _Snapshot, after: _Snapshot, events: list[Event]
    ) -> list[str]:
        lines: list[str] = []
        for entry in after.limbs:
            old = before.limb(entry.owner, entry.slot)
            if old is None:
                continue
            if old.integrity != entry.integrity:
                delta = entry.integrity - old.integrity
                lines.append(
                    f"{entry.owner} / {entry.name}: bütünlük {old.integrity} -> "
                    f"{entry.integrity} ({delta:+d})"
                )
            if old.state is not entry.state:
                lines.append(
                    f"{entry.owner} / {entry.name}: {state_label(old.state)} -> "
                    f"{state_label(entry.state)}"
                )
            removed = old.tags - entry.tags
            for tag in sorted(removed, key=lambda value: value.value):
                lines.append(f"{entry.owner} / {entry.name}: {tag_label(tag)} kalktı")
        if before.downed != after.downed:
            lines.append("Yerdesin" if after.downed else "Ayağa kalktın")
        if before.guard_active and not after.guard_active:
            lines.append("Guard Flesh koruması harcandı")
        for event in events:
            if event.event_type == "focus_resolved":
                lines.append(f"Niyet okundu: {event.payload['intent']}")
            elif event.event_type == "limb_marked":
                lines.append(f"{self.enemy.name} / {event.payload['target']} işaretlendi")
        return lines

    def _blood_cost(
        self, before: _Snapshot, after: _Snapshot, events: list[Event]
    ) -> str:
        spends: list[str] = []
        total = 0
        for event in events:
            if event.event_type != "blood_changed" or event.actor_id != self.player.id:
                continue
            delta = int(str(event.payload["delta"]))
            if delta < 0:
                total += -delta
                spends.append(f"{event.payload['reason']} {-delta}")
        if total == 0:
            return f"0 Blood (bedava) | Blood {after.blood}"
        return (
            f"{total} Blood ({', '.join(spends)}) | "
            f"Blood {before.blood} -> {after.blood}"
        )

    def _gains(
        self, before: _Snapshot, after: _Snapshot, events: list[Event]
    ) -> list[str]:
        lines: list[str] = []
        for event in events:
            kind = event.event_type
            payload = event.payload
            if kind == "blood_changed" and event.actor_id == self.player.id:
                delta = int(str(payload["delta"]))
                if delta > 0:
                    lines.append(f"+{delta} Blood ({payload['reason']})")
            elif kind == "harvest_created":
                lines.append(
                    f"Hasat alındı: {payload['limb']} — kalite {payload['quality']}"
                )
            elif kind == "limb_marked":
                lines.append(
                    f"Claim the Cut işareti: {payload['target']} (temiz hasat şansı)"
                )
            elif kind == "guard_flesh":
                lines.append(
                    f"Guard Flesh: gelen hasar %{int(float(str(payload['reduction'])) * 100)} azalır"
                )
            elif kind == "brace_activated":
                lines.append("Brace: bu tur devrilmeye karşı korunuyorsun")
            elif kind == "stand_performed":
                lines.append("Ayağa kalktın; eylemler yeniden açıldı")
            elif kind == "bleeding_removed":
                lines.append(f"Kanama durdu: {payload['slot']}")
            elif kind == "knockdown_prevented_by_brace":
                lines.append("Brace yükü devrilmeyi engelledi")
            elif kind == "knockdown_prevented_by_active_brace":
                lines.append("Aktif Brace devrilmeyi engelledi")
            elif kind == "guard_consumed":
                lines.append(
                    f"Guard Flesh hasarı {payload['before']} -> {payload['after']} indirdi"
                )
        if after.plead_pressure > before.plead_pressure:
            threshold = int(self.rules["plead"]["basic_threshold"])
            lines.append(
                f"{self.enemy.name} plead baskısı {after.plead_pressure}/{threshold}"
            )
        if any(event.event_type == "generic_plead_resolved" for event in events):
            lines.append(f"{self.enemy.name} pes etti")
        if any(event.event_type == "jeff_incapacity_surrender" for event in events):
            lines.append(f"{self.enemy.name} saldıramaz hale geldi ve teslim oldu")
        return lines

    def _risks(
        self, before: _Snapshot, after: _Snapshot, events: list[Event]
    ) -> list[str]:
        lines: list[str] = []
        for entry in after.limbs:
            old = before.limb(entry.owner, entry.slot)
            if old is None:
                continue
            for tag in sorted(entry.tags - old.tags, key=lambda value: value.value):
                lines.append(f"{entry.owner} / {entry.name}: {tag_label(tag)}")
            if old.state is not entry.state and entry.state is LimbState.RUINED:
                lines.append(
                    f"{entry.owner} / {entry.name} harap oldu — graft için hasat edilemez"
                )
        if _BAND_ORDER.index(after.band) < _BAND_ORDER.index(before.band):
            lines.append(f"Blood bandı {before.band} -> {after.band}")
        if after.downed and not before.downed:
            lines.append("Downed: ana eylemin Stand ile harcanacak")
        if after.enemy_rage and not before.enemy_rage:
            lines.append(f"{self.enemy.name} Rage kazandı — sonraki vuruş daha ağır")
        old_tools = dict(before.tools)
        for item_id, count in after.tools:
            if count < old_tools[item_id] and count == 0:
                lines.append(f"{self.config.items[item_id]['name']} tükendi")
        for event in events:
            kind = event.event_type
            payload = event.payload
            if kind == "panic_pulse":
                lines.append(
                    f"Panic Pulse harcandı (+{payload['gained']} Blood, bir daha yok)"
                )
            elif kind == "soft_collapse":
                lines.append(
                    f"Limb for Life: {payload['slot']} feda edildi, tek kullanım bitti"
                )
            elif kind == "collapse":
                lines.append("Çöktün — oturum kaybedildi")
            elif kind == "ache_stress_roll" and payload.get("disabled_next_round"):
                lines.append(f"{payload['slot']} önümüzdeki tur devre dışı")
            elif kind == "hell_saw_roll" and not payload.get("valid"):
                lines.append("Hell Saw geçersiz hedefe girdi — kesme şansı yok")
            elif kind == "stabilized_sever_roll" and not payload.get("success"):
                lines.append("Stabilized hedef kesilmeye direndi")
        return lines

    # -------------------------------------------------------------- summary

    def summary_lines(self) -> list[str]:
        graft = self.graftable_right_arm
        lines = [
            f"Sonuç: {self.outcome.value}",
            f"Tur sayısı: {self.log.round_number}",
            (
                f"Kalan Blood: {self.player.blood} "
                f"[{blood_band(self.player.blood, self.rules)}]"
            ),
            (
                f"Harcanan Blood: {self.metrics.blood_spent}; "
                f"kazanılan: {self.metrics.blood_gained}"
            ),
            "Hasat: "
            + (
                ", ".join(
                    f"{record.limb_name} ({record.quality.value})" for record in self.harvests
                )
                or "yok"
            ),
            "Graft edilebilir Sağ Kol: "
            + (f"{graft.limb_name} — {graft.quality.value}" if graft else "yok"),
        ]
        lines.append(
            "Faz 1 kilidi: graft, Anna ve Grafting Table bu arayüzün dışında."
        )
        return lines
