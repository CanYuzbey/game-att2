"""Pure renderers for structured simulator events and metrics."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any, cast

from .models import ScenarioResult


def result_payload(result: ScenarioResult, include_events: bool = True) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "metrics": asdict(result.metrics),
        "body_summary": result.body_summary,
        "notes": result.notes,
    }
    if include_events:
        payload["events"] = [asdict(event) for event in result.events]
    return payload


def render_json(value: object) -> str:
    if isinstance(value, ScenarioResult):
        value = result_payload(value)
    return json.dumps(value, indent=2, sort_keys=True, default=str)


def render_text(result: ScenarioResult, verbose: bool = False) -> str:
    metrics = result.metrics
    lines = [
        f"Scenario: {metrics.scenario} | seed={metrics.seed} | strategy={metrics.strategy}",
        f"Result: {metrics.result}; final blood: {metrics.final_blood}; rounds: {metrics.rounds}",
        f"Harvests: clean={metrics.clean_harvests}, stressed={metrics.stressed_harvests}, ruined={metrics.ruined_harvests}",
        f"Panic Pulse={metrics.panic_pulse_used}; soft collapse={metrics.soft_collapse_used}; table={metrics.table_choice or 'n/a'}",
        "Body: " + metrics.final_body_summary,
    ]
    if result.notes:
        lines.append("Notes: " + " | ".join(result.notes))
    if verbose:
        lines.append("Events:")
        for event in result.events:
            lines.append(
                f"  #{event.sequence} r{event.round_number} {event.phase} {event.event_type}: {event.payload}"
            )
    return "\n".join(lines)


def render_markdown(results: list[ScenarioResult], batches: list[dict[str, object]] | None = None) -> str:
    lines = [
        "# Game att2 Combat Simulator Results v0.1",
        "",
        "Generated from deterministic simulator runs. These results validate implementation behavior; they do not prove player fun or market demand.",
        "",
        "## Required Scenarios",
        "",
        "| Scenario | Seed | Result | Final Blood | Clean/Stressed/Ruined | Key Outcome |",
        "|---|---:|---|---:|---|---|",
    ]
    for result in results:
        metrics = result.metrics
        key = ", ".join(result.notes) if result.notes else (metrics.table_choice or "scenario completed")
        lines.append(
            f"| {metrics.scenario} | {metrics.seed} | {metrics.result} | {metrics.final_blood} | "
            f"{metrics.clean_harvests}/{metrics.stressed_harvests}/{metrics.ruined_harvests} | {key} |"
        )
    lines.extend(["", "## Batch Metrics", ""])
    if batches:
        lines.extend([
            "| Strategy | Completion | Collapse | Avg Blood | Median Blood | Table Paths | Identical Body Rate |",
            "|---|---:|---:|---:|---:|---|---:|",
        ])
        for batch in batches:
            lines.append(
                f"| {batch['strategy']} | {float(cast(float, batch['completion_rate'])):.0%} | {float(cast(float, batch['collapse_rate'])):.0%} | "
                f"{float(cast(float, batch['average_final_blood'])):.1f} | {float(cast(float, batch['median_final_blood'])):.1f} | "
                f"{batch['table_choices']} | {float(cast(float, batch['identical_final_body_rate'])):.0%} |"
            )
        lines.extend(["", "### Strategy Detail", ""])
        for batch in batches:
            lines.append(
                f"- **{batch['strategy']}**: actions={batch['action_frequency']}; "
                f"Clean/Stressed/Ruined={batch['clean_harvests']}/{batch['stressed_harvests']}/{batch['ruined_harvests']}; "
                f"trade acceptance={float(cast(float, batch['trade_acceptance_rate'])):.0%}."
            )
    else:
        lines.append("No batch supplied.")
    lines.extend([
        "",
        "## Observations",
        "",
        "- Free Grip Strike paths produce ruined arms and surrender pressure, not premium clean grafts.",
        "- The reported batch is a deterministic strategy probe, not player behavior evidence.",
        "- Unity remains blocked pending owner review of this simulator evidence and any needed rule revisions.",
    ])
    return "\n".join(lines) + "\n"
