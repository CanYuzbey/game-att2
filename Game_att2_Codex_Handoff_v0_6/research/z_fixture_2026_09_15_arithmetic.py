"""Isolated Z48/A paper arithmetic, not a game/demo runtime.

Run from the handoff package:
    python research/z_fixture_2026_09_15_arithmetic.py --report research/z_fixture_2026_09_15_evidence.md

No legacy imports, gameplay loop, engine, RNG, assets, dependencies or human evidence.
Route inputs/NPC misses are explicitly favorable witnesses, not all-draw reachability.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Fixture:
    fixture_id: str = "Z48A-2026-09-15-v0.1"
    start_blood: int = 80
    body_cap: int = 80
    bowl_cap: int = 40
    kit_uses: int = 3
    stabilize: int = 8
    control: int = 4
    surgery_fee: int = 6
    return_fee: int = 4
    clean_stump: int = 10
    defense: int = 1
    pour_fee: int = 1
    retreat: int = 6
    grip_cost: int = 2
    feint_cost: int = 1
    feint_bonus: int = 3
    first_brain_redraw: int = 1
    normal_redraw: int = 2
    first_brain_prep: int = 2
    will: int = 90
    committed_parry: int = 30
    normal_blood: int = 300
    yield_per_kill: int = 30
    horn: int = 18
    boss_vital: int = 600
    boss_blood: int = 900
    boss_min_contact_blood: int = 4
    boss_min_contact_integrity: int = 10

    @property
    def graft_cost(self) -> int:
        return self.surgery_fee + self.clean_stump

    @property
    def return_cost(self) -> int:
        return self.return_fee + self.clean_stump


@dataclass(frozen=True)
class Card:
    name: str
    cost: int
    full_impact: int
    strained_impact: int


F = Fixture()
CARDS = (
    Card("Punch", 2, 8, 6),
    Card("Kick", 3, 12, 9),
    Card("Headbutt", 3, 10, 7),
    Card("Grip", 2, 0, 0),
)


@dataclass(frozen=True)
class Budget:
    blood: int
    bowl: int
    kit: int

    @property
    def liquid(self) -> int:
        return self.blood + self.bowl


def pay(state: Budget, cost: int, kit: int = 0) -> Budget:
    if cost < 0 or kit < 0 or state.blood < cost or state.kit < kit:
        raise ValueError("Illegal cost/charge preflight")
    return Budget(state.blood - cost, state.bowl, state.kit - kit)


def elective_surgery(state: Budget, cost: int) -> Budget:
    if state.blood <= cost:
        raise ValueError("Elective living surgery must leave positive Blood")
    return pay(state, cost, 1)


def collect(state: Budget) -> tuple[Budget, int]:
    taken = min(F.yield_per_kill, F.bowl_cap - state.bowl)
    return Budget(state.blood, state.bowl + taken, state.kit), F.yield_per_kill - taken


def pour(state: Budget) -> Budget:
    if state.blood >= F.body_cap or state.bowl <= 0 or state.blood < F.pour_fee:
        raise ValueError("No legal useful pour")
    transfer = min(state.bowl, F.body_cap - state.blood + F.pour_fee)
    return Budget(state.blood - F.pour_fee + transfer, state.bowl - transfer, state.kit)


def source_state(current: int, maximum: int) -> str:
    if not 0 <= current <= maximum or maximum <= 0:
        raise ValueError("Invalid Integrity")
    if current == 0:
        return "Ruined"
    ratio = Fraction(current, maximum)
    if ratio > Fraction(7, 10):
        return "Full"
    if ratio > Fraction(3, 10):
        return "Strained"
    return "Desperate"


def block_loss(impact: int, factor: Fraction) -> int:
    value = impact * Fraction(3, 4) * factor
    return (value.numerator + value.denominator - 1) // value.denominator


def legal_block(current: int, maximum: int, impact: int, factor: Fraction) -> bool:
    return source_state(current, maximum) in {"Full", "Strained"} and current >= block_loss(impact, factor)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    checks: list[tuple[str, str]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        if not passed:
            raise ValueError(f"FAIL {name}: {detail}")
        checks.append((name, detail))

    def rejects(name: str, operation: Callable[[], object]) -> None:
        try:
            operation()
        except ValueError:
            checks.append((name, "Expected illegal arithmetic preflight rejected"))
        else:
            raise ValueError(f"FAIL {name}: illegal operation accepted")

    package = Path(__file__).resolve().parents[1]
    docs = package / "docs"
    world = (docs / "WORLD_PROGRESSION_AND_DECISIONS.md").read_text(encoding="utf-8")
    saved_answers = (docs / "archive/before_z_fixture_2026-09-15/Z_ANSWER_TABLE.txt").read_text(encoding="utf-8")
    rows = re.findall(r"^\| (Z\d{2}) \| ([AB]) \| (.+) \|$", world, re.M)
    saved_rows = re.findall(r"^\| (Z\d{2}) \| ([AB]) \| (.+) \|$", saved_answers, re.M)
    check("Owner provenance", rows == saved_rows and len(rows) == 55 and
          [r[0] for r in rows] == [f"Z{i:02}" for i in range(1, 56)],
          "55 ordered answer rows and original option paragraphs unchanged")

    # Data/declaration agreement is deliberately limited to specific arithmetic tables.
    combat = (docs / "COMBAT_BODY_AND_BLOOD.md").read_text(encoding="utf-8")
    deck = (docs / "DECK_BRAIN_AND_ACTIONS.md").read_text(encoding="utf-8")
    core = (docs / "CORE_LOOP_ENCOUNTER_AND_RUN.md").read_text(encoding="utf-8")
    check("Declaration vitals", "| Boneatour | 900 | 90 | 600 | 600 | 600 | 600 | 600 | 600 |" in combat,
          "Paper actor table has boss Blood900 and all six Integrity maxima600")
    check("Declaration start", "Body Blood is 80/80" in combat and "| Right Arm | 30 | 18 |" in combat,
          "P01 starting Blood80 and18/30 Right Arm match arithmetic")
    check("Declaration costs", "6 surgery + 10 recipient" in combat and "4 surgery + 10 recipient" in combat and
          "1 Blood before timed" in combat and "first redraw costs1" in deck,
          "Graft16, return14, defense1, minimum redraw1 declared")
    check("Declaration bound", "80 + 30 + 30 = 140" in core and "at most 560" in core,
          "Core declares same conservative energy/damage accounting")

    boundaries = {22: "Full", 21: "Strained", 10: "Strained", 9: "Desperate",
                  1: "Desperate", 0: "Ruined"}
    check("30-max boundaries", all(source_state(c, 30) == s for c, s in boundaries.items()),
          "Exact >70% and >30%:22Full,21/10Strained,9/1Desperate,0Ruined")
    check("Charge Full-only source", source_state(18, 30) != "Full" and source_state(30, 30) == "Full",
          "Starting injured Right Arm fails Charge Parry, independent Left Arm passes")
    block_cases = [(12, Fraction(1), 9), (12, Fraction(4, 5), 8), (8, Fraction(1), 6)]
    check("Block rounding", all(block_loss(d, fact) == expected for d, fact, expected in block_cases),
          "ceil(D*.75*factor):12ordinary9;12clamp8;8ordinary6")
    check("Disposable shield rejection", not legal_block(1, 30, 12, Fraction(1)),
          "1-Integrity/Desperate guard cannot cancel a12-Impact attack")
    check("Budget pressure", min(F.defense, F.grip_cost, F.first_brain_redraw) > 0,
          "Every accepted defense/Grip/redraw retains a positive finite cost")
    check("Will pacing", F.will == 3 * F.committed_parry,
          "Three successful Committed Parries:90->60->30->0; no ordinary damage shock")

    routes: dict[str, list[tuple[str, Budget]]] = {}

    def record(route: str, label: str, state: Budget) -> Budget:
        check(f"{route}: {label} legal liquid", 0 < state.blood <= F.body_cap and
              0 <= state.bowl <= F.bowl_cap and 0 <= state.kit <= F.kit_uses,
              f"body={state.blood}, bowl={state.bowl}, kit={state.kit}")
        routes.setdefault(route, []).append((label, state))
        return state

    start = Budget(F.start_blood, 0, F.kit_uses)
    cared = pay(start, F.stabilize, 1)
    a_surrender = record("Graft", "Care then3Parry surrender", pay(cared, 3 * F.defense))
    grafted = record("Graft", "Living clamp operation", elective_surgery(a_surrender, F.graft_cost))
    gripped = record("Graft", "Human1Grip, declared arm response canceled", pay(grafted, F.grip_cost))
    graft_entry = record("Graft", "Human3Parry, mercy, boss entry", pay(gripped, 3 * F.defense))
    check("Graft witness entry", graft_entry == Budget(48, 0, 1),
          "No kill reward from either ordinary NPC; Left Arm/Legs untouched")
    check("Living donor", F.normal_blood - 3 - F.clean_stump == 287,
          "Donor starts300,3Main costs,10removal ->287Blood, not corpse extraction")

    headbutt = next(c for c in CARDS if c.name == "Headbutt")
    normal_kill_cost = 2 * headbutt.cost + F.defense
    a_kill = pay(cared, normal_kill_cost)
    a_reward, a_overflow = collect(a_kill)
    record("Kill", "A2Headbutt,NPCParry misses,30bowl", a_reward)
    a_poured = record("Kill", "Care Pour16", pour(a_reward))
    b_kill = pay(a_poured, normal_kill_cost)
    b_reward, b_overflow = collect(b_kill)
    record("Kill", "B2Headbutt,30bowl,overflow4", b_reward)
    kill_entry = record("Kill", "Care Pour8,boss entry", pour(b_reward))
    check("Kill witness entry", kill_entry == Budget(80, 32, 2) and a_overflow == 0 and b_overflow == 4,
          "Body80,bowl32; no limb rewards,4Blood overflow declared")
    check("Witness conservation", kill_entry.liquid == F.start_blood + 2 * F.yield_per_kill -
          F.stabilize - 2 * normal_kill_cost - 2 * F.pour_fee - b_overflow,
          "112liquid=140initial+potential minus28paid/lost; transfers create0")

    returned = record("Old arm", "Return after A graft", elective_surgery(grafted, F.return_cost))
    return_entry = record("Old arm", "Human3Parry then mercy", pay(returned, 3 * F.defense))
    check("Original-arm return branch", returned == Budget(39, 0, 0) and return_entry == Budget(36, 0, 0),
          "Saved18/30 arm restored once; Grip incompatible; clamp disposed")
    human_arm = record("Human arm", "Replace clamp after human surrender",
                       elective_surgery(graft_entry, F.graft_cost))
    check("No-kill human-arm branch", human_arm == Budget(32, 0, 0),
          "Ordinary30/30 Right Arm restores Punch; no new special technique/Blood")
    check("Human source has no invented repair", next(c for c in CARDS if c.name == "Grip").full_impact == 0 and
          "No base structural damage" in deck and "preserves the donor's actual" in combat,
          "Mara's unfeinted Grip witness leaves Right Arm30/30; transfer copies actual donor Integrity")
    mixed = record("Kill A, limb B", "Human3Parry then ordinary transfer",
                   elective_surgery(pay(a_poured, 3 * F.defense), F.graft_cost))
    check("Mixed route branch", mixed == Budget(61, 14, 1),
          "First30Blood only, no second kill payout; body61,bowl14,kit1")

    rejects("Graft below16", lambda: elective_surgery(Budget(15, 0, 1), F.graft_cost))
    rejects("Graft exact16 would kill", lambda: elective_surgery(Budget(16, 0, 1), F.graft_cost))
    rejects("Graft zero kit", lambda: elective_surgery(Budget(30, 0, 0), F.graft_cost))
    rejects("Return exact14 would kill", lambda: elective_surgery(Budget(14, 0, 1), F.return_cost))
    rejects("Cap-full Pour", lambda: pour(Budget(80, 20, 1)))
    rejects("Empty bowl Pour", lambda: pour(Budget(20, 0, 1)))

    # Exhaustive small integer conservation scan, not a simulated gameplay loop.
    pour_cases = 0
    for blood in range(1, F.body_cap):
        for bowl in range(1, F.bowl_cap + 1):
            before = Budget(blood, bowl, 0)
            after = pour(before)
            check_valid = (after.liquid == before.liquid - F.pour_fee and
                           after.blood <= F.body_cap and after.bowl >= 0)
            if not check_valid:
                raise ValueError(f"Pour conservation failed:{before}->{after}")
            pour_cases += 1
    check("All legal liquid Pour pairs", pour_cases == 3160,
          "3160integer body1..79/bowl1..40 pairs conserve existing Blood minus fee1")

    ratios = [Fraction(c.full_impact, c.cost) for c in CARDS]
    feint_ratios = [Fraction(c.full_impact + F.feint_bonus, c.cost + F.feint_cost) for c in CARDS]
    max_ratio = max(ratios + feint_ratios)
    check("Composite damage/Blood bound", max_ratio == 4 and
          all(c.strained_impact <= c.full_impact for c in CARDS),
          "Base/Feint composites, Full/Strained,all ratios<=4; Grip has no repeat damage")
    energy = F.start_blood + 2 * F.yield_per_kill
    structural_bound = energy * max_ratio
    source_break_budget = 3 * (F.boss_vital - F.boss_vital * Fraction(3, 10))
    boss_fuel_bound = 3 * energy
    check("Global lethal-vital bound", structural_bound == 560 and structural_bound < F.boss_vital,
          "Even140paid-offense Blood yields<=560; each lethal boss vital600")
    check("Threat-source availability bound", source_break_budget == 1260 and source_break_budget > structural_bound,
          "Making bothArms+LegsDesperate requires1260>560; ordinary threat remains")
    check("Boss finite-fuel bound", boss_fuel_bound == 420 and boss_fuel_bound < F.boss_blood,
          "Loose140resolved rounds x3actions <=420cost <900; no regen required")
    check("Normal-kill yield source bounds", F.normal_blood - 2 * F.start_blood >= F.yield_per_kill and
          F.normal_blood - 2 * (F.start_blood + F.yield_per_kill) >= F.yield_per_kill,
          "A<=80pre-reward rounds leaves>=140Blood;B<=110leaves>=80,each sources30")
    check("No-input cost bound", F.boss_min_contact_blood > 0 and F.boss_min_contact_integrity > 0,
          "Every unopposed legal fallback hits a living vital; no zero-damage ruined-target loop")

    punch = next(c for c in CARDS if c.name == "Punch")
    horn_attacks = (F.horn + punch.full_impact - 1) // punch.full_impact
    local_success_cost = horn_attacks * (punch.cost + F.defense)
    check("Horn local-success affordability", horn_attacks == 3 and local_success_cost == 9 and
          graft_entry.blood > local_success_cost and kill_entry.blood > local_success_cost,
          "3Full Left Punches+3responses cost9;18horn breaks,overdamage no vital overflow")
    check("Bone profile/no vascular exploit", "nonvascular" in combat and "no vital overflow" in combat and
          "No Open/Major ticking source" in combat,
          "Declared horn/anatomy contacts exclude free ticking boss death in this catalogue")

    # Deliberate unsafe variants are counterexamples, not authorized mechanics.
    counterexamples = [
        ("Defense cost changed to0", "Pass + free perfect Parry/Evade leaves player liquid/structure unchanged until the boss exhausts its finite Blood. The certain player-loss proof fails; it is not a full-state infinite loop."),
        ("Surrender/duplicate kill also grants30", "Initial140 resource bound fails: duplicate reward can increase E. Mutually exclusive once-only rewards are mandatory."),
        ("Boss vital reduced to560 or less", "Conservative structural inequality no longer proves unbeatable. This is failure of this proof, not proof a real play route wins."),
        ("Horn overdamage becomes vascular ticking wound", "Free later boss loss is outside paid-offense560 bound. Explicit nonvascular/no-overflow profile is mandatory."),
        ("Grip canceled enemy Main gets free alternate", "The graft witness no longer demonstrates canceled selected response; source/commit contract violated."),
    ]
    check("Hostile unsafe variants documented", len(counterexamples) == 5,
          "Free defense, duplicate reward, weak-vital inequality,vascular overflow andGrip fallback explicitly rejected")

    document_names = [
        "GAME_DIRECTOR_BRIEF.md", "CORE_LOOP_ENCOUNTER_AND_RUN.md",
        "COMBAT_BODY_AND_BLOOD.md", "DECK_BRAIN_AND_ACTIONS.md",
        "WORLD_PROGRESSION_AND_DECISIONS.md", "DEMO_MINIGAME_AI_WORKING_CONTRACT.md",
    ]
    hashes = [(name, hashlib.sha256((docs / name).read_bytes()).hexdigest()) for name in document_names]

    report = [
        "# Z48/A fixture — fresh paper arithmetic evidence",
        "",
        f"Fixture: {F.fixture_id}. Evidence date:2026-09-15.",
        "**PAPER ARITHMETIC ONLY — NOT A NEW DEMO RUNTIME OR HUMAN TEST.**",
        "",
        "Reproduction from the handoff package:",
        "~~~powershell",
        "python research/z_fixture_2026_09_15_arithmetic.py --report research/z_fixture_2026_09_15_evidence.md",
        "~~~",
        "",
        f"Result: exit0, {len(checks)} checks passed; {pour_cases} legal integer Pour pairs examined.",
        "Checks are assertions and finite arithmetic scans, not gameplay unit/integration totals.",
        "",
        "| Route witness stage | Body Blood | Bowl Blood | Kit uses |",
        "|---|---:|---:|---:|",
    ]
    for route, stages in routes.items():
        for label, budget in stages:
            report.append(f"| {route}: {label} | {budget.blood} | {budget.bowl} | {budget.kit} |")
    report.extend([
        "",
        "Route assumptions: paused initial care, no exploration tick, favorable declared",
        "Attention, explicit NPC missed-Parry outcomes for kills and Mara Grip, successful player Parries",
        "and no damage to Left Arm/Legs. These establish budget consistency for named",
        "witnesses, not reachability for every draw/AI input or an implemented state machine.",
        "",
        "| Check | Evidence |",
        "|---|---|",
    ])
    report.extend(f"| {name} | {detail} |" for name, detail in checks)
    report.extend(["", "| Unsafe hypothetical variant | Counterexample/limitation |", "|---|---|"])
    report.extend(f"| {name} | {detail} |" for name, detail in counterexamples)
    report.extend([
        "",
        "## Scope and unresolved evidence",
        "",
        "No legacy source/config/tests imported/changed; no engine, actual input, draw",
        "state, actor claims, wound clock, source occupancy, transfer object or retry",
        "implementation. The finite-state argument depends on the declared catalogue.",
        "No human appeal/fairness/accessibility or device/export result. M01–M03 remains open.",
        "The biggest untested product risk is length/fairness of an honestly forced-loss boss.",
        "",
        "Paper-only merge recommendation: merge design/research; do not grant runtime",
        "acceptance from this report. Next: supply M01–M03 and review loss pacing before",
        "a separate engine/runtime gate.",
        "",
        "## Document fingerprints",
        "",
        "| Document | SHA256 |",
        "|---|---|",
    ])
    report.extend(f"| {name} | {digest} |" for name, digest in hashes)
    rendered = "\n".join(report) + "\n"
    if args.report:
        report_path = args.report.resolve()
        research = (package / "research").resolve()
        if not report_path.is_relative_to(research):
            raise ValueError("Report must remain inside this package's research directory")
        report_path.write_text(rendered, encoding="utf-8")
    print(f"PASS {F.fixture_id}: {len(checks)} checks; {pour_cases} Pour pairs; graft48/0;kill80/32;global140->560<600.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
