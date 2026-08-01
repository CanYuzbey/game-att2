"""Pure ASCII renderers for the Phase 1 playable CLI.

Rendering lives here so ``play_session`` stays print-free. Borders are plain
ASCII on purpose: only the text carries Turkish characters, so a console that
cannot draw box glyphs still lines the tables up.
"""

from __future__ import annotations

from .enums import LimbState, Slot
from .models import CombatantRuntime
from .play_session import (
    ATTACK_ACTIONS,
    ActionReport,
    MenuCategory,
    PlayOffer,
    PlaySession,
    blood_band,
    slot_label,
    state_label,
    tag_label,
)
from .rules import is_usable

WIDTH = 78
BAR_SEGMENTS = 10

#: Turkish surface text for the rules-owned blocking reasons this interface can
#: present. ``rules.py`` stays the single source of truth; anything not listed
#: here falls through in its original English rather than being guessed at.
_REASON_PREFIXES: tuple[tuple[str, str], ...] = (
    ("Main action already consumed this round", "Bu turun ana eylemi harcandı"),
    ("Downed requires Stand", "Yerdesin — önce Stand gerekiyor"),
    ("Stand requires Downed", "Stand yalnızca yerdeyken kullanılır"),
    ("Left Arm source is unavailable", "Sol Kol kaynağı kullanılamaz"),
    ("Right Arm source is unavailable", "Sağ Kol kaynağı kullanılamaz"),
    ("Legs source is unavailable", "Bacak kaynağı kullanılamaz"),
    ("Head source is unavailable", "Kafa kaynağı kullanılamaz"),
    ("Focus is unavailable while Downed", "Yerdeyken Focus kullanılamaz"),
    ("Focus must occur before the Main action", "Focus ana eylemden önce gelmeli"),
    ("Focus already used this round", "Bu tur Focus zaten kullanıldı"),
    ("Fast item must occur before the Main action", "Fast eşya ana eylemden önce gelmeli"),
    ("Fast item already used this round", "Bu tur bir Fast eşya zaten kullanıldı"),
    ("Requires a Bleeding target", "Kanayan bir hedef gerekiyor"),
    ("A target limb is required", "Bir hedef parça gerekiyor"),
    ("Target is too large for Bone Scissors", "Hedef Bone Scissors için fazla büyük"),
    ("Target must be Damaged or Critical", "Hedef hasarlı veya kritik olmalı"),
    ("Hell Saw requires a Large target", "Hell Saw büyük bir hedef ister"),
    ("Bone Scissors already used this fight", "Bone Scissors bu dövüşte tükendi"),
    ("Hell Saw already used this fight", "Hell Saw bu dövüşte tükendi"),
    ("Claim the Cut is unavailable", "Claim the Cut kalmadı"),
    ("Brace already used this encounter", "Brace bu karşılaşmada kullanıldı"),
    ("Action is not an approved Main action", "Bu onaylı bir ana eylem değil"),
)

_RISK_TEXT: tuple[tuple[str, str], ...] = (
    (
        "Critical Head may reveal incomplete information",
        "kritik Kafa eksik bilgi verebilir",
    ),
    ("Stabilized targets may resist severing", "Stabilized hedefler kesilmeye direnebilir"),
    (
        "Damaged/Critical Large targets use the configured sever roll",
        "hasarlı/kritik büyük hedeflerde kesme zarı atılır",
    ),
)


def localize(text: str, table_: tuple[tuple[str, str], ...]) -> str:
    for english, turkish in table_:
        if text == english:
            return turkish
        if text.startswith(english):
            return turkish + text[len(english) :]
    return text


def localize_reason(reason: str | None) -> str:
    if reason is None:
        return "sebep bildirilmedi"
    if reason.startswith("Requires ") and reason.endswith(" Blood"):
        return f"{reason[len('Requires '):-len(' Blood')]} Blood gerekiyor"
    if reason.endswith(" is unavailable"):
        return f"{reason[: -len(' is unavailable')]} kullanılabilir değil"
    return localize(reason, _REASON_PREFIXES)


def rule(char: str = "=") -> str:
    return char * WIDTH


def heading(text: str) -> str:
    return f"{rule()}\n  {text}\n{rule()}"


def integrity_bar(integrity: int, maximum: int) -> str:
    if maximum <= 0:  # pragma: no cover - config validation forbids this
        return "[" + " " * BAR_SEGMENTS + "]   0%"
    ratio = max(0.0, min(1.0, integrity / maximum))
    filled = round(ratio * BAR_SEGMENTS)
    percent = round(ratio * 100)
    return f"[{'#' * filled}{'.' * (BAR_SEGMENTS - filled)}] {percent:3d}%"


def table(headers: list[str], rows: list[list[str]], indent: str = "  ") -> str:
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))
    border = indent + "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    def line(cells: list[str]) -> str:
        padded = (f" {cell.ljust(widths[index])} " for index, cell in enumerate(cells))
        return indent + "|" + "|".join(padded) + "|"

    return "\n".join([border, line(headers), border, *(line(row) for row in rows), border])


def body_table(actor: CombatantRuntime, indent: str = "  ") -> str:
    rows: list[list[str]] = []
    for slot in Slot:
        limb = actor.body.slots[slot]
        tags = ", ".join(
            tag_label(tag) for tag in sorted(limb.tags, key=lambda value: value.value)
        )
        state = state_label(limb.state)
        if limb.state is not LimbState.MISSING and not is_usable(limb):
            state = f"{state} (kullanılamaz)"
        rows.append(
            [
                slot_label(slot),
                limb.name,
                f"{limb.integrity}/{limb.definition.max_integrity}",
                integrity_bar(limb.integrity, limb.definition.max_integrity),
                state,
                tags or "-",
            ]
        )
    return table(
        ["YUVA", "PARÇA", "BÜTÜNLÜK", "ORAN", "DURUM", "ETİKETLER"], rows, indent
    )


def render_state(session: PlaySession) -> str:
    player = session.player
    enemy = session.enemy
    band = blood_band(player.blood, session.rules)
    blocks = [
        heading(
            f"TUR {session.log.round_number}   |   {player.name} (S-001)  vs  {enemy.name}"
        ),
        f"  BLOOD: {player.blood}  [{band}]"
        + (
            "   ANA EYLEM: harcandı"
            if player.normal_action_consumed
            else "   ANA EYLEM: hazır"
        ),
        f"  DURUM: {', '.join(session.player_statuses()) or 'temiz'}",
        f"  ENVANTER: {' | '.join(session.inventory_lines())}",
        "",
        f"  SEN — {player.name}",
        body_table(player),
        "",
        f"  DÜŞMAN — {enemy.name}",
        body_table(enemy),
        f"  {enemy.name} durumu: {', '.join(session.enemy_statuses())}",
        "",
        f"  GÖRÜNEN NİYET: {session.intent_text()}"
        + ("" if session.intent_is_revealed() else "   (Focus ile netleştir)"),
    ]
    return "\n".join(blocks)


#: Widest question label in :meth:`ActionReport.as_pairs`, so answers line up.
QUESTION_WIDTH = 28


def render_report(report: ActionReport) -> str:
    title = (
        f"-- RİTÜEL KAYDI — Tur {report.round_number} — "
        f"{report.actor}: {report.action_label} "
    )
    inner = WIDTH - 4
    lines = ["  +" + title.ljust(inner, "-")[:inner] + "+"]
    for index, (question, answers) in enumerate(report.as_pairs(), start=1):
        head = f"{index}. {question}"
        lines.append(f"  | {head:<{QUESTION_WIDTH}}: {answers[0]}")
        for extra in answers[1:]:
            lines.append(f"  | {'':<{QUESTION_WIDTH}}  {extra}")
    lines.append("  +" + "-" * inner + "+")
    return "\n".join(lines)


def render_reports(reports: tuple[ActionReport, ...]) -> str:
    return "\n".join(render_report(report) for report in reports)


def _offer_detail(offer: PlayOffer) -> str:
    parts: list[str] = []
    if offer.cost:
        parts.append(f"{offer.cost} Blood")
    else:
        parts.append("bedava")
    if offer.availability.timing == "main":
        parts.append("ana eylem — turu bitirir")
    elif offer.availability.timing == "focus":
        parts.append("ana eylemden önce")
    elif offer.availability.timing == "fast":
        parts.append("fast — turda bir kez")
    if offer.risk:
        parts.append(f"risk: {localize(offer.risk, _RISK_TEXT)}")
    return "; ".join(parts)


def render_main_menu(session: PlaySession) -> str:
    attacks = session.attack_action_summaries()
    attack_open = any(enabled for _, enabled, _ in attacks)
    focus = session.find_offer("focus")
    items = [offer for offer in session.offers_in(MenuCategory.ITEM)]
    defends = session.offers_in(MenuCategory.DEFEND)
    forfeit = session.find_offer("forfeit_main")

    def mark(enabled: bool) -> str:
        return " " if enabled else "x"

    lines = [
        "  " + rule("-"),
        "  KARAR AŞAMASI — ne yapıyorsun?",
        (
            f"  [1]{mark(attack_open)} Saldır / Hedef Al   "
            f"({sum(1 for _, enabled, _ in attacks if enabled)} eylem açık)"
        ),
        f"  [2]{mark(bool(focus and focus.enabled))} Focus               "
        + (
            _offer_detail(focus)
            if focus and focus.enabled
            else f"KAPALI: {localize_reason(focus.reason) if focus else 'sunulmuyor'}"
        ),
        (
            f"  [3]{mark(any(offer.enabled for offer in items))} Eşya Kullan         "
            f"({sum(1 for offer in items if offer.enabled)} eşya açık)"
        ),
        (
            f"  [4]{mark(any(offer.enabled for offer in defends))} Defans / Duruş      "
            f"({sum(1 for offer in defends if offer.enabled)} eylem açık)"
        ),
        "  [5]  Durumu tekrar göster",
    ]
    if forfeit is not None:
        lines.append("  [6]  Ana eylemi geç (yasal ana eylem kalmadı)")
    lines.append("  [0]  Dövüşü bırak ve oturumu bitir")
    lines.append("  " + rule("-"))
    return "\n".join(lines)


def render_attack_menu(session: PlaySession) -> str:
    lines = ["  " + rule("-"), "  SALDIRI — hangi eylem?"]
    for index, (action_id, enabled, reason) in enumerate(
        session.attack_action_summaries(), start=1
    ):
        name = session.action_display_name(action_id)
        suffix = "" if enabled else f"   KAPALI: {localize_reason(reason)}"
        lines.append(f"  [{index}]{' ' if enabled else 'x'} {name}{suffix}")
    lines.append("  [0]  Geri")
    lines.append("  " + rule("-"))
    return "\n".join(lines)


def render_target_menu(session: PlaySession, action_id: str) -> str:
    name = session.action_display_name(action_id)
    lines = ["  " + rule("-"), f"  {name} — hangi yuvayı hedefliyorsun?"]
    rows: list[list[str]] = []
    for index, slot in enumerate(Slot, start=1):
        offer = session.find_offer(f"{action_id}:{slot.value}")
        limb = session.enemy.body.slots[slot]
        if offer is None:  # pragma: no cover - offers() covers every slot
            continue
        rows.append(
            [
                f"[{index}]{' ' if offer.enabled else 'x'}",
                slot_label(slot),
                limb.name,
                f"{limb.integrity}/{limb.definition.max_integrity}",
                state_label(limb.state),
                "AÇIK" if offer.enabled else f"KAPALI: {localize_reason(offer.reason)}",
            ]
        )
    lines.append(table(["#", "YUVA", "PARÇA", "BÜTÜNLÜK", "DURUM", "SEÇİLEBİLİR"], rows))
    lines.append(f"  Maliyet/risk: {_offer_detail_for_action(session, action_id)}")
    lines.append("  [0]  Geri")
    lines.append("  " + rule("-"))
    return "\n".join(lines)


def _offer_detail_for_action(session: PlaySession, action_id: str) -> str:
    for slot in Slot:
        offer = session.find_offer(f"{action_id}:{slot.value}")
        if offer is not None and offer.enabled:
            return _offer_detail(offer)
    return "bu eylem şu anda açık değil"


def render_choice_menu(title: str, offers: list[PlayOffer]) -> str:
    lines = ["  " + rule("-"), f"  {title}"]
    for index, offer in enumerate(offers, start=1):
        detail = (
            _offer_detail(offer)
            if offer.enabled
            else f"KAPALI: {localize_reason(offer.reason)}"
        )
        target = "" if offer.target_slot is None else f" -> {offer.target_text}"
        lines.append(
            f"  [{index}]{' ' if offer.enabled else 'x'} {offer.label}{target}   {detail}"
        )
    lines.append("  [0]  Geri")
    lines.append("  " + rule("-"))
    return "\n".join(lines)


def render_summary(session: PlaySession) -> str:
    lines = [heading("OTURUM ÖZETİ")]
    lines.extend(f"  {line}" for line in session.summary_lines())
    lines.extend(["", f"  SEN — {session.player.name}", body_table(session.player)])
    lines.extend(["", f"  DÜŞMAN — {session.enemy.name}", body_table(session.enemy)])
    return "\n".join(lines)


def render_intro(session: PlaySession) -> str:
    return "\n".join(
        [
            heading("GAME ATT2 — FAZ 1 OYNANABİLİR CLI (S-001 vs Jeff)"),
            "  Her tur: başlangıç etkileri -> niyet -> Focus -> Fast eşya -> ana eylem",
            "  -> düşman eylemi -> bitiş kontrolleri.",
            "  Focus ve Fast eşya ana eylemi harcamaz; ana eylem turu kapatır.",
            "  Blood 0 ölümdür; Limb for Life uygun bir uzvu feda ederek bunu bir kez önleyebilir.",
            "  Brace manuel bir tur duruşudur; Braced Legs otomatik yükü bundan ayrıdır.",
            f"  Kapsam kilidi: {', '.join(ATTACK_ACTIONS)} + Focus + eşya + defans.",
            "  Graft, Anna ve Grafting Table bu arayüzde YOK.",
            "",
        ]
    )
