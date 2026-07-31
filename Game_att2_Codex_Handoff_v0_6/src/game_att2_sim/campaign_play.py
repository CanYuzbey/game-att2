"""Player-facing campaign console over the approved research-session state machine.

This module owns menu presentation only.  ``InteractiveResearchSession`` remains
the full-sequence orchestrator and ``RuleEngine`` remains the sole rule authority.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass, field

from .enums import Slot
from .factory import body_summary
from .models import ActionAvailability, Event
from .play_session import DEFAULT_ROUND_LIMIT
from .research_shell import (
    EvidenceClass,
    InteractiveResearchSession,
    SessionMetadata,
)

ATTACK_ACTIONS = ("grip_strike", "claim_the_cut", "bone_scissors", "hell_saw")
DEFENCE_ACTIONS = ("guard_flesh", "brace", "stand")
COMMITMENT_ACTIONS = {"emergency_graft", "accept_anna_trade", "end_session"}
CAMPAIGN_INTERFACE_VERSION = "0.1"
COMBAT_MENU = """  [1] Saldır / hedef al
  [2] Focus
  [3] Fast eşya
  [4] Defans / duruş
  [5] Karşılaşma çözümü
  [0] Oturumu bitir"""


def campaign_session(seed: int) -> InteractiveResearchSession:
    """Create an unexported play session without claiming external evidence."""
    metadata = SessionMetadata.create(
        f"PLAY-{seed}",
        EvidenceClass.UNCLASSIFIED_HUMAN_PLAY,
        seed,
        f"PLAY-{seed}",
        strategy_intention="free_choice_play",
    )
    return InteractiveResearchSession(metadata)


def _meaningfulness_note(
    session: InteractiveResearchSession, offer: ActionAvailability
) -> str | None:
    if offer.action_id == "brace" and session.encounter in {"Jeff", "Anna"}:
        return "anlamlılık uyarısı: mevcut düşman Knockdown kullanmıyor"
    if offer.target_slot is not None and session.enemy is not None:
        if session.encounter == "Jeff" and offer.target_slot in {
            Slot.LEFT_ARM,
            Slot.RIGHT_ARM,
        }:
            return "nedensel hedef: Desperate Swing kaynağı olabilir"
        if session.encounter == "Anna" and offer.target_slot is Slot.RIGHT_ARM:
            return "nedensel hedef: Surgical Jab kaynağı"
        if offer.action_id.startswith("hell_saw:"):
            target = session.enemy.body.slots[offer.target_slot]
            if target.state.value not in {"Damaged", "Critical"}:
                return "anlamlılık uyarısı: mevcut hedef temiz koparma eşiğinde değil"
    return None


def _offer_line(
    session: InteractiveResearchSession, index: int, offer: ActionAvailability
) -> str:
    state = "AÇIK" if offer.enabled else f"KAPALI: {offer.reason or 'sebep yok'}"
    details = [f"cost={offer.cost}", state]
    if offer.risk:
        details.append(f"risk={offer.risk}")
    note = _meaningfulness_note(session, offer)
    if note:
        details.append(note)
    return f"  [{index}] {offer.label} ({'; '.join(details)})"


def render_campaign_intro() -> str:
    return "\n".join(
        [
            "=" * 72,
            "GAME ATT2 — ONAYLI TAM CLI KAMPANYASI",
            "S-001 -> Jeff -> acil graft -> Anna -> Grafting Table",
            "Blood aynı anda hayatta kalma bütçesi, ödeme ve eylem yakıtıdır.",
            "Hasarlı eylem kaynakları zayıflar; kullanılamaz kaynakların niyeti iptal olur.",
            "Not: Jeff'in mevcut onaylı saldırısı gövde bütünlüğünü azaltır, Blood'ı değil.",
            "=" * 72,
        ]
    )


def _objective(encounter: str) -> str:
    return {
        "Jeff": "Jeff'i etkisiz bırak; mümkünse graft edilebilir Sağ Kol çıkar.",
        "Post-Jeff": "Kazandığın Sağ Kol için acil graft kararını ver.",
        "Anna": "Yeni beden riskini yönet; stabilizasyon veya greed yolunu seç.",
        "Grafting Table": "Bedenini entegre et, onar, güçlendir, borçlan veya koru.",
    }.get(encounter, "Mevcut durumdan yasal bir sonuç üret.")


def render_campaign_state(session: InteractiveResearchSession) -> str:
    lines = [
        "-" * 72,
        f"SAHNE: {session.encounter} | TUR: {session.log.round_number}",
        f"HEDEF: {_objective(session.encounter)}",
        f"BLOOD: {session.player.blood}",
        "SEN:",
        *(f"  {slot}: {description}" for slot, description in body_summary(session.player).items()),
    ]
    if session.enemy is not None:
        lines.extend(
            [
                f"DÜŞMAN — {session.enemy.name}:",
                *(
                    f"  {slot}: {description}"
                    for slot, description in body_summary(session.enemy).items()
                ),
                f"GÖRÜNEN NİYET: {session.current_intent}",
            ]
        )
        if session.encounter == "Jeff":
            lines.append(
                "NEDENSEL İPUCU: Desperate Swing kullanılabilir bir koldan gelir; "
                "o kaynak çözümden önce yok olursa saldırı iptal edilir."
            )
        elif session.encounter == "Anna":
            lines.append(
                "NEDENSEL İPUCU: Surgical Jab Sağ Kol kaynaklıdır; graft/kanama durumu "
                "Anna'nın takas seçeneğini değiştirebilir."
            )
    return "\n".join(lines)


@dataclass(frozen=True)
class CampaignViewSnapshot:
    blood: int
    encounter: str
    player_body: dict[str, str]
    enemy_body: dict[str, str]
    statuses: tuple[str, ...]
    visible_intent: str


def campaign_snapshot(session: InteractiveResearchSession) -> CampaignViewSnapshot:
    return CampaignViewSnapshot(
        blood=session.player.blood,
        encounter=session.encounter,
        player_body=body_summary(session.player),
        enemy_body=body_summary(session.enemy) if session.enemy is not None else {},
        statuses=tuple(session.statuses()),
        visible_intent=session.current_intent,
    )


def render_campaign_result(
    action_label: str,
    before: CampaignViewSnapshot,
    session: InteractiveResearchSession,
    events: Iterable[Event],
) -> str:
    after = campaign_snapshot(session)
    changes: list[str] = []
    for owner, old_body, new_body in (
        ("Sen", before.player_body, after.player_body),
        ("Düşman", before.enemy_body, after.enemy_body),
    ):
        for slot in sorted(set(old_body) | set(new_body)):
            if old_body.get(slot) != new_body.get(slot):
                changes.append(
                    f"{owner}/{slot}: {old_body.get(slot, 'yok')} -> {new_body.get(slot, 'yok')}"
                )
    if before.encounter != after.encounter:
        changes.append(f"Sahne: {before.encounter} -> {after.encounter}")
    if before.statuses != after.statuses:
        changes.append(
            f"Durumlar: {', '.join(before.statuses) or 'yok'} -> "
            f"{', '.join(after.statuses) or 'yok'}"
        )
    if before.visible_intent != after.visible_intent:
        changes.append(
            f"Görünen niyet: {before.visible_intent or 'yok'} -> "
            f"{after.visible_intent or 'yok'}"
        )
    event_list = list(events)
    kinds = list(dict.fromkeys(event.event_type for event in event_list))
    gains = [
        kind
        for kind in kinds
        if kind
        in {
            "harvest_created",
            "emergency_graft_completed",
            "anna_trade_accepted",
            "table_choice",
            "generic_plead_resolved",
            "jeff_incapacity_surrender",
            "emergency_graft",
            "enemy_action_cancelled",
            "focus_resolved",
        }
    ]
    if any(
        event.event_type == "blood_changed"
        and isinstance((delta := event.payload.get("delta")), int)
        and delta > 0
        for event in event_list
    ):
        gains.append("blood_gained")
    if any(
        event.event_type == "limb_state_changed"
        and event.actor_id != session.player.id
        for event in event_list
    ):
        gains.append("enemy_limb_state_changed")
    risks = [
        kind
        for kind in kinds
        if kind
        in {
            "bleeding_applied",
            "rage_gained",
            "unstable_result",
            "unstable_applied",
            "jeff_marked_source_selected",
            "panic_pulse",
            "soft_collapse",
        }
    ]
    if any(
        event.event_type == "limb_state_changed"
        and event.actor_id == session.player.id
        for event in event_list
    ):
        risks.append("player_limb_state_changed")
    return "\n".join(
        [
            "  + RİTÜEL SONUCU",
            f"  1. Ne hedeflendi? {action_label}",
            f"  2. Ne değişti? {' | '.join(changes) if changes else 'Açık durum değişikliği yok'}",
            f"  3. Blood maliyeti? {before.blood} -> {after.blood}",
            f"  4. Ne kazanıldı? {', '.join(gains) if gains else 'Yeni kazanım yok'}",
            f"  5. Hangi yeni risk doğdu? {', '.join(risks) if risks else 'Yeni risk yok'}",
        ]
    )


def render_campaign_summary(session: InteractiveResearchSession) -> str:
    """Render an honest play summary without claiming an owner diagnostic."""
    return "\n".join(
        [
            f"Playable session PLAY-{session.metadata.seed} ({session.metadata.evidence_class.value})",
            f"Seed: {session.metadata.seed}; campaign interface: {CAMPAIGN_INTERFACE_VERSION}",
            f"Outcome: {session.outcome}; Anna path: {session.anna_path or 'not reached'}",
            f"Table choice: {session.metrics.table_choice or 'none'}",
            f"Final Blood: {session.player.blood}",
            f"Decisions: {len(session.decisions)}; events: {len(session.log.events)}",
            "Final body:",
            *(
                f"- {slot}: {description}"
                for slot, description in body_summary(session.player).items()
            ),
        ]
    )


def _enforce_round_limit(
    session: InteractiveResearchSession,
    *,
    limit: int,
    action_timing: str,
    encounter_before: str,
    round_before: int,
) -> None:
    """Apply the CLI safety guard after a combat Main action, never as a game rule."""
    if (
        not session.complete
        and action_timing == "main"
        and encounter_before in {"Jeff", "Anna"}
        and session.encounter == encounter_before
        and round_before >= limit
    ):
        session.outcome = "ROUND_LIMIT_REACHED"
        session.log.emit(
            "campaign_round_limit_reached",
            session.player.id,
            round_limit=limit,
        )


@dataclass
class CampaignConsole:
    session: InteractiveResearchSession
    round_limit: int = DEFAULT_ROUND_LIMIT
    input_fn: Callable[[str], str] = input
    output_fn: Callable[[str], None] = print
    transcript: list[str] = field(default_factory=list)
    stopped: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        if self.round_limit < 1:
            raise ValueError("round_limit must be positive")

    def emit(self, value: str) -> None:
        self.transcript.append(value)
        self.output_fn(value)

    def ask(self, prompt: str) -> str:
        try:
            answer = self.input_fn(prompt).strip()
        except EOFError:
            self.stopped = True
            self.transcript.append(f"{prompt}<girdi bitti>")
            return "0"
        self.transcript.append(f"{prompt}{answer}")
        self.output_fn("")
        return answer

    def run(self) -> None:
        self.emit(render_campaign_intro())
        while not self.session.complete and not self.stopped:
            self.emit(render_campaign_state(self.session))
            self._decision()
        if self.stopped and not self.session.complete:
            self.session.perform("end_session", confirmed=True)
        self.emit(render_campaign_summary(self.session))

    def _decision(self) -> None:
        if self.session.encounter not in {"Jeff", "Anna"}:
            self._offer_menu(self.session.offers(), "KARAR")
            return
        self.emit(COMBAT_MENU)
        choice = self.ask("  Seçim: ")
        if choice == "1":
            self._attack_menu()
        elif choice == "2":
            self._execute("focus")
        elif choice == "3":
            self._offer_menu(
                [offer for offer in self.session.offers() if offer.timing == "fast"],
                "FAST EŞYA",
            )
        elif choice == "4":
            self._offer_menu(
                [offer for offer in self.session.offers() if offer.action_id in DEFENCE_ACTIONS],
                "DEFANS / DURUŞ",
            )
        elif choice == "5":
            self._offer_menu(
                [
                    offer
                    for offer in self.session.offers()
                    if offer.action_id in {"accept_anna_trade", "end_session"}
                ],
                "KARŞILAŞMA ÇÖZÜMÜ",
            )
        elif choice == "0":
            self._execute("end_session")
        else:
            self.emit("  ! Geçersiz seçim.")

    def _attack_menu(self) -> None:
        offers = self.session.offers()
        groups: list[tuple[str, list[ActionAvailability]]] = []
        for action_id in ATTACK_ACTIONS:
            targeted = [
                offer for offer in offers if offer.action_id.startswith(f"{action_id}:")
            ]
            if targeted:
                groups.append((action_id, targeted))
        for display_index, (action_id, targeted) in enumerate(groups, start=1):
            enabled = sum(offer.enabled for offer in targeted)
            label = targeted[0].label.split(" -> ", 1)[0]
            self.emit(f"  [{display_index}] {label} ({enabled} hedef açık)")
        choice = self.ask("  Saldırı: ")
        selected_index = self._index(choice, len(groups))
        if selected_index is None:
            return
        _action_id, targeted = groups[selected_index]
        self._offer_menu(targeted, "HEDEF")

    def _offer_menu(self, offers: list[ActionAvailability], title: str) -> None:
        if not offers:
            self.emit("  ! Bu durumda seçenek yok.")
            return
        self.emit(f"  {title}")
        for display_index, offer in enumerate(offers, start=1):
            self.emit(_offer_line(self.session, display_index, offer))
        choice = self.ask("  Seçim: ")
        selected_index = self._index(choice, len(offers))
        if selected_index is None:
            return
        self._execute(offers[selected_index].action_id)

    @staticmethod
    def _index(choice: str, count: int) -> int | None:
        if not choice.isdigit():
            return None
        index = int(choice) - 1
        return index if 0 <= index < count else None

    def _execute(self, action_id: str) -> None:
        offer = next(
            (offer for offer in self.session.offers() if offer.action_id == action_id),
            None,
        )
        if offer is None:
            self.emit("  ! Bu eylem mevcut durumda sunulmuyor.")
            return
        if not offer.enabled:
            self.emit(f"  ! Eylem kapalı: {offer.reason or 'sebep yok'}")
            return
        if (
            action_id in COMMITMENT_ACTIONS or action_id.startswith("table:")
        ) and self.ask("  Bu geri alınamaz kararı onayla? [e/H]: ").lower() != "e":
            self.emit("  Karar iptal edildi.")
            return
        before = campaign_snapshot(self.session)
        round_before = self.session.log.round_number
        event_start = len(self.session.log.events)
        result = self.session.perform(action_id, confirmed=True)
        if result != "executed":
            self.emit(f"  ! {result}")
            return
        _enforce_round_limit(
            self.session,
            limit=self.round_limit,
            action_timing=offer.timing,
            encounter_before=before.encounter,
            round_before=round_before,
        )
        events = self.session.log.events[event_start:]
        self.emit(
            render_campaign_result(
                offer.label,
                before,
                self.session,
                events,
            )
        )


def run_campaign_actions(
    session: InteractiveResearchSession,
    actions: Iterable[str],
    emit: Callable[[str], None],
    round_limit: int = DEFAULT_ROUND_LIMIT,
) -> None:
    if round_limit < 1:
        raise ValueError("round_limit must be positive")
    emit(render_campaign_intro())
    emit(render_campaign_state(session))
    for action_id in actions:
        if session.complete:
            break
        offer = next(
            (offer for offer in session.offers() if offer.action_id == action_id),
            None,
        )
        if offer is None or not offer.enabled:
            emit(f"  ! {action_id} uygulanmadı: {offer.reason if offer else 'sunulmuyor'}")
            continue
        before = campaign_snapshot(session)
        round_before = session.log.round_number
        event_start = len(session.log.events)
        result = session.perform(action_id, confirmed=True)
        if result == "executed":
            _enforce_round_limit(
                session,
                limit=round_limit,
                action_timing=offer.timing,
                encounter_before=before.encounter,
                round_before=round_before,
            )
            emit(
                render_campaign_result(
                    offer.label,
                    before,
                    session,
                    session.log.events[event_start:],
                )
            )
            if not session.complete:
                emit(render_campaign_state(session))
    emit(render_campaign_summary(session))
