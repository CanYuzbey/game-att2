"""Run deterministic structural comparisons for the Brain synthesis proposal."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass
from typing import Any

from fixture import (
    ACCESS_BRAIN,
    EXECUTION_BRAIN,
    NO_BRAIN,
    FixtureConfig,
    Variant,
    run_session,
)


@dataclass(frozen=True)
class BatchMetrics:
    variant: str
    attention_slots: int
    profile: str
    commitment_guarantee: bool
    brain: str
    rounds_observed: int
    main_drought_pct: float
    post_loss_main_drought_pct: float
    dead_hand_pct: float
    meaningful_choice_pct: float
    prep_main_coverage_pct: float
    item_visibility_pct: float
    avg_visible_options: float
    avg_unique_sources: float
    attack_share_pct: float
    body_share_pct: float
    technique_share_pct: float
    action_budget_violations: int
    invalid_action_attempts: int
    source_commitment_violations: int
    avg_source_loss_removals: float
    execution_delta_risk_ignored: float
    execution_delta_risk_half_valued: float
    execution_delta_risk_fully_valued: float


def _pct(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return round(100.0 * numerator / denominator, 3)


def run_batch(config: FixtureConfig, runs: int) -> BatchMetrics:
    total_rounds = 0
    main_droughts = 0
    post_loss_rounds = 0
    post_loss_main_droughts = 0
    dead_hands = 0
    meaningful_choices = 0
    prep_main_coverage = 0
    item_visible = 0
    visible_options = 0
    unique_sources = 0
    attack_cards = 0
    body_cards = 0
    technique_cards = 0
    legal_action_cards = 0
    action_budget_violations = 0
    invalid_action_attempts = 0
    source_commitment_violations = 0
    source_loss_removals = 0
    execution_deltas: Counter[str] = Counter()

    for seed in range(runs):
        result = run_session(config, seed)
        source_loss_removals += result.source_loss_removed
        execution_deltas["ignored"] += result.execution_delta_if_risk_ignored
        execution_deltas["half"] += result.execution_delta_if_risk_half_valued
        execution_deltas["full"] += result.execution_delta_if_risk_fully_valued
        for observation in result.observations:
            total_rounds += 1
            main_droughts += observation.legal_main_cards == 0
            dead_hands += observation.legal_action_cards == 0
            meaningful_choices += observation.visible_options >= 2
            prep_main_coverage += observation.compatible_prep_main_pairs > 0
            item_visible += observation.item_card_visible
            visible_options += observation.visible_options
            unique_sources += observation.unique_sources
            attack_cards += observation.attack_cards
            body_cards += observation.body_cards
            technique_cards += observation.technique_cards
            legal_action_cards += observation.legal_action_cards
            action_budget_violations += observation.preparations_used > 1
            action_budget_violations += observation.mains_used > 1
            action_budget_violations += observation.item_actions > 1
            invalid_action_attempts += observation.invalid_action_attempts
            source_commitment_violations += observation.source_commitment_violations
            if observation.round_number > config.source_loss_round:
                post_loss_rounds += 1
                post_loss_main_droughts += observation.legal_main_cards == 0

    return BatchMetrics(
        variant=config.variant.value,
        attention_slots=config.attention_slots,
        profile=config.technique_profile,
        commitment_guarantee=config.commitment_guarantee,
        brain=config.brain.part_id,
        rounds_observed=total_rounds,
        main_drought_pct=_pct(main_droughts, total_rounds),
        post_loss_main_drought_pct=_pct(post_loss_main_droughts, post_loss_rounds),
        dead_hand_pct=_pct(dead_hands, total_rounds),
        meaningful_choice_pct=_pct(meaningful_choices, total_rounds),
        prep_main_coverage_pct=_pct(prep_main_coverage, total_rounds),
        item_visibility_pct=_pct(item_visible, total_rounds),
        avg_visible_options=round(visible_options / total_rounds, 3),
        avg_unique_sources=round(unique_sources / total_rounds, 3),
        attack_share_pct=_pct(attack_cards, legal_action_cards),
        body_share_pct=_pct(body_cards, legal_action_cards),
        technique_share_pct=_pct(technique_cards, legal_action_cards),
        action_budget_violations=action_budget_violations,
        invalid_action_attempts=invalid_action_attempts,
        source_commitment_violations=source_commitment_violations,
        avg_source_loss_removals=round(source_loss_removals / runs, 3),
        execution_delta_risk_ignored=round(execution_deltas["ignored"] / runs, 3),
        execution_delta_risk_half_valued=round(execution_deltas["half"] / runs, 3),
        execution_delta_risk_fully_valued=round(execution_deltas["full"] / runs, 3),
    )


def build_matrix(runs: int) -> list[BatchMetrics]:
    rows: list[BatchMetrics] = []
    for slots in (3, 4, 5):
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.OWNER_ORIGINAL,
                    attention_slots=slots,
                    commitment_guarantee=True,
                    brain=ACCESS_BRAIN,
                ),
                runs,
            )
        )
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.ACTIVE_DECK,
                    attention_slots=slots,
                    commitment_guarantee=False,
                    brain=EXECUTION_BRAIN,
                ),
                runs,
            )
        )
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=slots,
                    commitment_guarantee=False,
                    brain=EXECUTION_BRAIN,
                ),
                runs,
            )
        )
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=slots,
                    commitment_guarantee=True,
                    brain=EXECUTION_BRAIN,
                ),
                runs,
            )
        )

    for profile in ("aggressive", "defensive"):
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.ACTIVE_DECK,
                    attention_slots=4,
                    technique_profile=profile,
                    brain=EXECUTION_BRAIN,
                ),
                runs,
            )
        )
        rows.append(
            run_batch(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=4,
                    technique_profile=profile,
                    commitment_guarantee=True,
                    brain=EXECUTION_BRAIN,
                ),
                runs,
            )
        )

    rows.append(
        run_batch(
            FixtureConfig(
                Variant.SYNTHESIS,
                attention_slots=4,
                commitment_guarantee=True,
                brain=NO_BRAIN,
            ),
            runs,
        )
    )
    rows.append(
        run_batch(
            FixtureConfig(
                Variant.SYNTHESIS,
                attention_slots=4,
                commitment_guarantee=True,
                brain=ACCESS_BRAIN,
            ),
            runs,
        )
    )
    return rows


def structural_verdict(row: BatchMetrics) -> str:
    if (
        row.action_budget_violations
        or row.invalid_action_attempts
        or row.source_commitment_violations
        or row.dead_hand_pct > 1.0
    ):
        return "FAIL"
    if row.main_drought_pct > 8.0 or row.post_loss_main_drought_pct > 12.0:
        return "REVISE"
    if row.meaningful_choice_pct < 90.0:
        return "REVISE"
    return "PASS"


def render_markdown(rows: list[BatchMetrics], runs: int) -> str:
    lines = [
        "# Brain Synthesis Structural Diagnostic",
        "",
        f"Deterministic sessions per configuration: **{runs}**",
        "",
        "These are neutral structural fixtures, not production balance values or human-play evidence.",
        "",
        "| Variant | Slots | Profile | Main drought | Post-loss drought | Dead hand | Meaningful choices | Item visible | Avg options | Brain | Guarantee | Verdict |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                (
                    row.variant,
                    str(row.attention_slots),
                    row.profile,
                    f"{row.main_drought_pct:.2f}%",
                    f"{row.post_loss_main_drought_pct:.2f}%",
                    f"{row.dead_hand_pct:.2f}%",
                    f"{row.meaningful_choice_pct:.2f}%",
                    f"{row.item_visibility_pct:.2f}%",
                    f"{row.avg_visible_options:.2f}",
                    row.brain,
                    "yes" if row.commitment_guarantee else "no",
                    structural_verdict(row),
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=5000)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.runs < 1:
        raise SystemExit("--runs must be positive")
    rows = build_matrix(args.runs)
    if args.format == "json":
        payload: dict[str, Any] = {
            "runs_per_configuration": args.runs,
            "rows": [asdict(row) | {"verdict": structural_verdict(row)} for row in rows],
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_markdown(rows, args.runs), end="")


if __name__ == "__main__":
    main()
