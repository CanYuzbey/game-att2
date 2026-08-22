"""Deterministic paper-model checks for DWF-0.1.

This is a research calculator, not Game att2 runtime or balance evidence. It computes
the documented Block matrix, an exact independent-round Will pacing distribution, and
the two G1 release invariants without random sampling or third-party dependencies.
"""

from collections import defaultdict
from fractions import Fraction


def ceil_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def block_loss(impact: int, guard_factor: Fraction) -> int:
    return ceil_fraction(Fraction(impact) * Fraction(3, 4) * guard_factor)


def will_distribution(parry_success: Fraction, max_rounds: int = 200) -> dict[str, float | int]:
    """Return exact quantiles for the bounded toy assumptions in the research note."""

    yellow = Fraction(3, 4)
    success = yellow * parry_success
    outcomes = {
        0: 1 - success,
        24: success * Fraction(1, 2),
        30: success * Fraction(7, 20),
        36: success * Fraction(3, 20),
    }

    alive = {90: Fraction(1)}
    broken = Fraction(0)
    cdf: dict[int, Fraction] = {}

    for round_number in range(1, max_rounds + 1):
        next_alive: defaultdict[int, Fraction] = defaultdict(Fraction)
        for will, state_probability in alive.items():
            for loss, outcome_probability in outcomes.items():
                probability = state_probability * outcome_probability
                remaining = will - loss
                if remaining <= 0:
                    broken += probability
                else:
                    next_alive[remaining] += probability
        alive = dict(next_alive)
        cdf[round_number] = broken

    def quantile(threshold: Fraction) -> int:
        return next(round_number for round_number, value in cdf.items() if value >= threshold)

    return {
        "median": quantile(Fraction(1, 2)),
        "p90": quantile(Fraction(9, 10)),
        "p95": quantile(Fraction(19, 20)),
        "over_12": float(1 - cdf[12]),
    }


def release_is_playable(blood: int, attack_families: int, block: int, parry: int, evade: int) -> bool:
    return blood >= 35 and attack_families >= 2 and block >= 1 and parry >= 1 and evade >= 1


def main() -> None:
    impacts = (5, 8, 12)
    guards = {
        "reinforced": Fraction(4, 5),
        "ordinary": Fraction(1),
        "fragile": Fraction(6, 5),
    }
    matrix = {name: [block_loss(impact, factor) for impact in impacts] for name, factor in guards.items()}
    assert matrix == {
        "reinforced": [3, 5, 8],
        "ordinary": [4, 6, 9],
        "fragile": [5, 8, 11],
    }

    profiles = {
        "35%": Fraction(35, 100),
        "55%": Fraction(55, 100),
        "70%": Fraction(70, 100),
        "85%": Fraction(85, 100),
    }
    pacing = {name: will_distribution(probability) for name, probability in profiles.items()}
    assert [(value["median"], value["p90"], value["p95"]) for value in pacing.values()] == [
        (13, 23, 26),
        (8, 14, 16),
        (7, 11, 12),
        (5, 8, 9),
    ]

    releases = {
        "blood_payment": release_is_playable(50, 3, 2, 2, 1),
        "right_arm_payment": release_is_playable(60, 3, 1, 1, 1),
    }
    assert all(releases.values())

    print("DWF-0.1 BLOCK MATRIX")
    print("profile,D5,D8,D12")
    for name, values in matrix.items():
        print(f"{name},{values[0]},{values[1]},{values[2]}")

    print("\nDWF-0.1 EXACT WILL MODEL")
    print("parry_success,median,p90,p95,probability_over_12")
    for name, values in pacing.items():
        print(
            f"{name},{values['median']},{values['p90']},{values['p95']},"
            f"{values['over_12']:.4f}"
        )

    print("\nG1 RELEASE INVARIANT")
    for name, passes in releases.items():
        print(f"{name},{'PASS' if passes else 'FAIL'}")

    print("\nPAPER MODEL ONLY: no runtime, fun, balance, or accessibility claim")


if __name__ == "__main__":
    main()
