"""
Combat Demo Paper Sim v0.1
==========================
Deterministic 8-round paper simulation using owner-decided values (2026-08-26).

STATUS: Research artifact. Does NOT modify legacy simulator code or config.
PURPOSE: Verify that the chosen Mana / card / integrity / defense numbers produce
         a playable combat arc across both G1 release branches.

Run:
    python research/combat_demo_paper_sim_v0_1.py
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional


# ─── Configuration (from combat_demo_core_v0_1.yaml) ─────────────────────────

MANA_START = 1
MANA_INCREMENT = 1
MANA_CAP = 6

BLOCK_T = 0.75
GUARD_FACTORS = {"reinforced": 0.80, "ordinary": 1.00, "fragile": 1.20}

WILL_START = 90
PARRY_WILL_LOSS = {1: 24, 2: 30, 3: 36}  # tier -> loss

KILL_BLOOD_YIELD = 15

PANIC_PULSE_TRIGGER = 25
PANIC_PULSE_RESTORE = 10
PANIC_PULSE_CAP = 35


# ─── Cards ────────────────────────────────────────────────────────────────────

@dataclass
class Card:
    name: str
    mana_cost: int
    base_impact: int
    source: str
    category: str = "attack"


PUNCH = Card("Punch", 1, 8, "arm")
KICK = Card("Kick", 2, 12, "legs")
HEADBUTT = Card("Headbutt", 2, 10, "head")
BRACE = Card("Brace", 1, 0, "arm", "preparation")
FEINT = Card("Feint", 1, 0, "any", "preparation")

STARTER_DECK = [PUNCH, PUNCH, KICK, KICK, HEADBUTT, HEADBUTT, BRACE, FEINT]


# ─── Body ─────────────────────────────────────────────────────────────────────

@dataclass
class BodySlot:
    name: str
    max_integrity: int
    current: int = -1

    def __post_init__(self):
        if self.current < 0:
            self.current = self.max_integrity

    @property
    def ratio(self) -> float:
        return self.current / self.max_integrity if self.max_integrity > 0 else 0.0

    @property
    def state(self) -> str:
        r = self.ratio
        if r > 0.70:
            return "Full"
        if r > 0.35:
            return "Strained"
        if r > 0.00:
            return "Desperate"
        return "Offline"

    def take_damage(self, impact: int) -> int:
        actual = min(impact, self.current)
        self.current = max(0, self.current - impact)
        return actual


@dataclass
class Body:
    slots: dict[str, BodySlot] = field(default_factory=dict)

    @classmethod
    def g1_full(cls) -> Body:
        return cls(slots={
            "head": BodySlot("Head", 25),
            "torso": BodySlot("Torso", 45),
            "left_arm": BodySlot("Left Arm", 30),
            "right_arm": BodySlot("Right Arm", 30),
            "legs": BodySlot("Legs", 35),
            "core": BodySlot("Core", 35),
        })

    @classmethod
    def g1_blood_payment(cls) -> Body:
        """After paying 20 Blood to Guard. Body intact, 50 Blood."""
        return cls.g1_full()

    @classmethod
    def g1_arm_payment(cls) -> Body:
        """After surrendering Right Arm. Missing R.Arm, 60 Blood."""
        body = cls.g1_full()
        body.slots["right_arm"].current = 0  # Missing
        return body

    def status_line(self) -> str:
        parts = []
        for key, slot in self.slots.items():
            parts.append(f"{slot.name}: {slot.current}/{slot.max_integrity} ({slot.state})")
        return " | ".join(parts)

    def compact_status(self) -> str:
        parts = []
        for slot in self.slots.values():
            state_char = {"Full": "F", "Strained": "S", "Desperate": "D", "Offline": "X"}
            parts.append(f"{slot.name[:2]}:{slot.current}/{slot.max_integrity}({state_char[slot.state]})")
        return "  ".join(parts)


# ─── Combat Actor ─────────────────────────────────────────────────────────────

@dataclass
class Actor:
    name: str
    body: Body
    blood: int
    will: int = WILL_START
    panic_pulse_used: bool = False

    def is_alive(self) -> bool:
        return self.blood > 0

    def status_line(self) -> str:
        return f"{self.name}: Blood={self.blood} Will={self.will} | {self.body.compact_status()}"


# ─── Block Calculation ────────────────────────────────────────────────────────

def calc_block_loss(impact: int, guard_profile: str = "ordinary") -> int:
    gf = GUARD_FACTORS[guard_profile]
    return math.ceil(impact * BLOCK_T * gf)


# ─── Simulation ───────────────────────────────────────────────────────────────

def mana_for_round(rnd: int) -> int:
    return min(MANA_START + (rnd - 1) * MANA_INCREMENT, MANA_CAP)


def simulate_attack_on_slot(
    attacker_card: Card,
    target_slot: BodySlot,
    feint_bonus: int = 0,
) -> dict:
    total_impact = attacker_card.base_impact + feint_bonus
    old = target_slot.current
    actual = target_slot.take_damage(total_impact)
    return {
        "card": attacker_card.name,
        "impact": total_impact,
        "target": target_slot.name,
        "integrity_before": old,
        "integrity_after": target_slot.current,
        "state_after": target_slot.state,
    }


def simulate_block(
    impact: int,
    guard_slot: BodySlot,
    guard_profile: str = "ordinary",
) -> dict:
    loss = calc_block_loss(impact, guard_profile)
    old = guard_slot.current
    actual = guard_slot.take_damage(loss)
    return {
        "impact": impact,
        "guard_profile": guard_profile,
        "guard_loss": loss,
        "guard_slot": guard_slot.name,
        "guard_before": old,
        "guard_after": guard_slot.current,
        "guard_state": guard_slot.state,
        "target_damage": 0,
    }


def run_mana_progression_table():
    """Show what card combinations are possible each round."""
    print("=" * 80)
    print("MANA PROGRESSION & LEGAL PLAYS")
    print("=" * 80)
    print(f"{'Round':>5} | {'Mana':>4} | Example Legal Plays")
    print("-" * 80)

    examples = {
        1: ["Punch(1)"],
        2: ["Kick(2)", "Punch(1)+Brace(1)", "Punch(1)+Feint(1)"],
        3: ["Kick(2)+Punch(1)", "Headbutt(2)+Brace(1)", "Punch(1)+Brace(1)+Feint(1)"],
        4: ["Kick(2)+Headbutt(2)", "Kick(2)+Punch(1)+Brace(1)", "Punch(1)×2+Kick(2)"],
        5: ["Kick(2)+Headbutt(2)+Punch(1)", "Kick(2)+Punch(1)+Brace(1)+Feint(1)"],
        6: ["Kick(2)+Headbutt(2)+Punch(1)+Brace(1)", "Kick(2)×2+Punch(1)+Feint(1)"],
    }

    for rnd in range(1, 9):
        m = mana_for_round(rnd)
        ex = examples.get(rnd, examples[6])
        print(f"{rnd:>5} | {m:>4} | {' / '.join(ex)}")
    print()


def run_damage_arithmetic():
    """Show how many hits to reach each integrity state for each slot."""
    print("=" * 80)
    print("DAMAGE ARITHMETIC — Hits to State Transition")
    print("=" * 80)

    targets = [
        ("Left Arm (30)", 30),
        ("Legs (35)", 35),
        ("Head (25)", 25),
        ("Torso (45)", 45),
    ]

    attacks = [
        ("Punch (8I)", 8),
        ("Kick (12I)", 12),
        ("Headbutt (10I)", 10),
        ("Feint+Punch (11I)", 11),
        ("Feint+Kick (15I)", 15),
    ]

    for target_name, max_int in targets:
        print(f"\n  Target: {target_name}")
        strained_threshold = math.ceil(max_int * 0.70)  # Above this = Full
        desperate_threshold = math.ceil(max_int * 0.35)  # Above this = Strained
        print(f"  Thresholds: Full>{strained_threshold}  Strained>{desperate_threshold}  Desperate>0  Offline=0")

        for atk_name, impact in attacks:
            hits_to_strained = 0
            hits_to_desperate = 0
            hits_to_offline = 0
            hp = max_int
            while hp > 0:
                hp = max(0, hp - impact)
                ratio = hp / max_int
                if ratio <= 0.70 and hits_to_strained == 0:
                    hits_to_strained = hits_to_offline + 1
                if ratio <= 0.35 and hits_to_desperate == 0:
                    hits_to_desperate = hits_to_offline + 1
                if hp == 0 and hits_to_offline == 0:
                    hits_to_offline = hits_to_offline + 1
                    break
                hits_to_offline += 1
            # Recalculate correctly
            hp = max_int
            h_s = h_d = h_o = 0
            for i in range(1, 100):
                hp = max(0, hp - impact)
                ratio = hp / max_int
                if ratio <= 0.70 and h_s == 0:
                    h_s = i
                if ratio <= 0.35 and h_d == 0:
                    h_d = i
                if hp == 0:
                    h_o = i
                    break

            print(f"    {atk_name:>20}: →Strained={h_s} hits  →Desperate={h_d} hits  →Offline={h_o} hits")
    print()


def run_block_matrix():
    """Show Block guard loss for all impact/profile combos."""
    print("=" * 80)
    print("BLOCK GUARD LOSS MATRIX (T=0.75)")
    print("=" * 80)
    impacts = [6, 8, 10, 11, 12, 15]
    print(f"{'Impact':>8} | {'Reinforced(0.80)':>16} | {'Ordinary(1.00)':>16} | {'Fragile(1.20)':>16}")
    print("-" * 70)
    for imp in impacts:
        r = calc_block_loss(imp, "reinforced")
        o = calc_block_loss(imp, "ordinary")
        f = calc_block_loss(imp, "fragile")
        print(f"{imp:>8} | {r:>16} | {o:>16} | {f:>16}")
    print()

    # Brace effect
    print("  With Brace: Ordinary(1.00) → Reinforced(0.80)")
    print("  Example: Impact 12 Block loss: Ordinary=9 → Braced=8 (saves 1 integrity)")
    print("  Example: Impact 8 Block loss:  Ordinary=6 → Braced=5 (saves 1 integrity)")
    print()


def run_will_pacing():
    """Show Will pacing for different Parry success rates."""
    print("=" * 80)
    print("WILL PACING (90 Start, 0 Recovery)")
    print("=" * 80)
    print("Assumes 75% Yellow attacks, distribution: 50% Routine / 35% Committed / 15% Critical")
    print(f"Weighted average Parry Will loss per success: "
          f"{0.50 * 24 + 0.35 * 30 + 0.15 * 36:.1f}")

    avg_loss = 0.50 * 24 + 0.35 * 30 + 0.15 * 36  # = 27.9

    print(f"\n{'Parry Rate':>12} | {'Avg Loss/Round':>14} | {'Rounds to Break':>16} | {'Within 5-7?':>12}")
    print("-" * 62)
    for rate in [0.35, 0.45, 0.55, 0.65, 0.70, 0.85]:
        effective_per_round = rate * 0.75 * avg_loss  # 75% Yellow
        if effective_per_round > 0:
            rounds = math.ceil(WILL_START / effective_per_round)
        else:
            rounds = 999
        in_band = "✓" if 5 <= rounds <= 7 else "△" if 4 <= rounds <= 9 else "✗"
        print(f"{rate:>11.0%} | {effective_per_round:>14.1f} | {rounds:>16} | {in_band:>12}")
    print()


def run_blood_economy():
    """Show Blood economy for both G1 branches across a fight."""
    print("=" * 80)
    print("BLOOD ECONOMY — G1 Branches")
    print("=" * 80)

    branches = [
        ("Blood Payment (50 Blood, full body)", 50, True),
        ("Arm Payment (60 Blood, missing R.Arm)", 60, False),
    ]

    for name, blood, has_right_arm in branches:
        print(f"\n  Branch: {name}")
        print(f"  Starting Blood: {blood}")

        # Scenario: take some hits, get wounds
        scenarios = [
            "Take 1 Open Wound (arm hit through Block)",
            "Take 1 Major Wound (arm Ruined)",
            "Fight ends, kill opponent",
        ]
        events = [
            ("Open Wound immediate", -3, "periodic: -5/tick"),
            ("Major Wound immediate", -8, "periodic: -8/tick"),
            ("Kill reward", +KILL_BLOOD_YIELD, ""),
        ]

        running = blood
        print(f"  {'Event':<45} {'Δ Blood':>8} {'Running':>8} {'Note'}")
        print(f"  {'-'*80}")
        for (event, delta, note) in events:
            running += delta
            status = ""
            if running < PANIC_PULSE_TRIGGER:
                status = " ← PANIC PULSE zone"
            print(f"  {event:<45} {delta:>+8} {running:>8} {note} {status}")

        print(f"\n  Final Blood after kill: {running}")
        if not has_right_arm:
            print(f"  Note: Missing R.Arm → only 1 Punch source, 1 Block/Parry source")
        print(f"  If SURRENDER instead: Blood stays at {blood - 3 - 8} (no kill yield), gain limb")
    print()


def run_round_by_round_scenario():
    """Simulate a 7-round combat scenario step by step."""
    print("=" * 80)
    print("ROUND-BY-ROUND SCENARIO — Player (Blood branch, 50 Blood) vs Enemy")
    print("=" * 80)
    print("Assumptions: Player attacks optimally. Enemy has similar body (200 total).")
    print("             Enemy attacks once per round with ~10 Impact on varied targets.")
    print("             Player Blocks all Yellow, no Parry attempts (conservative).\n")

    player = Actor("Player", Body.g1_blood_payment(), blood=50)
    enemy = Actor("Enemy", Body.g1_full(), blood=70, will=90)

    # Scripted scenario: player attacks, enemy attacks back
    # Player strategy: focus enemy left arm first, then legs
    player_script = [
        # (round, cards_played, target_slot, feint_bonus)
        (1, [("Punch", 8)], "left_arm"),
        (2, [("Kick", 12)], "left_arm"),
        (3, [("Punch", 8), ("Headbutt", 10)], "left_arm"),  # 3 Mana
        (4, [("Kick", 12), ("Punch", 8)], "legs"),           # 4 Mana, switch to legs
        (5, [("Kick", 12), ("Headbutt", 10), ("Punch", 8)], "legs"),  # 5 Mana
        (6, [("Kick", 12), ("Headbutt", 10), ("Punch", 8), ("Brace", 0)], "legs"),  # 6 Mana
        (7, [("Kick", 12), ("Punch", 8), ("Punch", 8)], "torso"),  # 6 Mana, finish
    ]

    # Enemy script: attacks player with ~10 impact on rotating targets
    enemy_attacks = [
        ("left_arm", 10), ("legs", 10), ("torso", 10),
        ("left_arm", 10), ("head", 10), ("torso", 10), ("legs", 10),
    ]

    for rnd in range(1, 8):
        mana = mana_for_round(rnd)
        print(f"─── Round {rnd} (Mana: {mana}) ───")

        # Player attacks
        if rnd <= len(player_script):
            _, cards, primary_target = player_script[rnd - 1]
            total_damage = 0
            card_names = []
            for card_name, impact in cards:
                if card_name == "Brace":
                    card_names.append("Brace")
                    continue
                target = enemy.body.slots[primary_target]
                old = target.current
                target.take_damage(impact)
                total_damage += impact
                card_names.append(f"{card_name}({impact})")

            print(f"  Player plays: {' + '.join(card_names)} → {primary_target}")
            t = enemy.body.slots[primary_target]
            print(f"  Enemy {primary_target}: {t.current}/{t.max_integrity} ({t.state})")

        # Enemy attacks player
        if rnd <= len(enemy_attacks):
            target_key, e_impact = enemy_attacks[rnd - 1]
            target_slot = player.body.slots[target_key]

            # Player Blocks with left arm (if available and legal)
            guard_slot = player.body.slots["left_arm"]
            if guard_slot.current > 0 and guard_slot.name != target_slot.name:
                guard_loss = calc_block_loss(e_impact, "ordinary")
                if guard_slot.current >= guard_loss:
                    guard_slot.take_damage(guard_loss)
                    print(f"  Enemy attacks {target_slot.name} ({e_impact}I) → Player BLOCKS with L.Arm "
                          f"(guard loss: {guard_loss}, L.Arm: {guard_slot.current}/{guard_slot.max_integrity} "
                          f"{guard_slot.state})")
                else:
                    # Block illegal, take direct hit
                    target_slot.take_damage(e_impact)
                    print(f"  Enemy attacks {target_slot.name} ({e_impact}I) → Block ILLEGAL, direct hit "
                          f"({target_slot.current}/{target_slot.max_integrity} {target_slot.state})")
            else:
                target_slot.take_damage(e_impact)
                print(f"  Enemy attacks {target_slot.name} ({e_impact}I) → direct hit "
                      f"({target_slot.current}/{target_slot.max_integrity} {target_slot.state})")

        print(f"  >> Player: Blood={player.blood} | {player.body.compact_status()}")
        print(f"  >> Enemy:  Blood={enemy.blood} | {enemy.body.compact_status()}")
        print()

    print("─── Post-Combat ───")
    print(f"  Kill enemy → Player gains {KILL_BLOOD_YIELD} Blood → {player.blood + KILL_BLOOD_YIELD} Blood")
    print(f"  Surrender  → Player gains limb, stays at {player.blood} Blood")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  COMBAT DEMO PAPER SIM v0.1 — Owner Values (2026-08-26)    ║")
    print("║  STATUS: Research artifact, not legacy simulator            ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    run_mana_progression_table()
    run_damage_arithmetic()
    run_block_matrix()
    run_will_pacing()
    run_blood_economy()
    run_round_by_round_scenario()

    print()
    print("=" * 80)
    print("OPEN QUESTIONS FOR NEXT ITERATION")
    print("=" * 80)
    print("  1. Headbutt Will pressure: should Headbutt add +3/+6 Will loss?")
    print("  2. Card source conditions for Strained/Desperate (current: all need Full/Strained)")
    print("  3. Enemy attack patterns, commitment tiers, and Yellow/Red distribution")
    print("  4. Wound generation thresholds (how much damage triggers Open vs Major)")
    print("  5. Anti-stall: exact rule at Mana cap (round 6+)")
    print()


if __name__ == "__main__":
    main()
