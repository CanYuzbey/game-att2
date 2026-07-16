"""Argparse command line entry point for scenarios and strategy batches."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .errors import SimulatorError
from .reporting import render_json, render_markdown, render_text
from .scenarios import STRATEGIES, run_all, run_batch, run_scenario


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 deterministic combat-loop simulator")
    selected = parser.add_mutually_exclusive_group()
    selected.add_argument("--scenario", help="named scenario")
    selected.add_argument("--all-scenarios", action="store_true", help="run all required scenarios")
    parser.add_argument("--seed", type=int, default=42, help="seed for deterministic runs")
    parser.add_argument("--strategy", choices=sorted(STRATEGIES), help="strategy for a scenario or batch")
    parser.add_argument("--batch", type=int, help="run this many mini-campaign seeds")
    parser.add_argument("--table-choice", choices=("integrate_arm", "repair_torso", "strengthen_legs", "table_loan", "leave"))
    parser.add_argument("--threat-profile", choices=("graft_pressure", "torso_pressure", "knockdown_pressure", "mixed_unknown_pressure"))
    parser.add_argument("--fixture", help="controlled post-table probe fixture")
    parser.add_argument("--format", choices=("text", "json", "markdown"), default="text")
    parser.add_argument("--output", type=Path, help="write report to this path")
    parser.add_argument("--verbose", action="store_true", help="include detailed structured events in text output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.batch is not None:
            payload = run_batch(args.strategy or "balanced", args.batch, args.seed)
            output = render_json(payload) if args.format == "json" else str(payload)
        elif args.all_scenarios:
            results = run_all(args.seed)
            if args.format == "json":
                output = render_json([{"metrics": result.metrics.__dict__, "body_summary": result.body_summary} for result in results])
            elif args.format == "markdown":
                output = render_markdown(results)
            else:
                output = "\n\n".join(render_text(result, args.verbose) for result in results)
        else:
            result = run_scenario(
                args.scenario or "mini_campaign",
                args.seed,
                args.strategy,
                table_choice=args.table_choice or "integrate_arm",
                threat_profile=args.threat_profile or "graft_pressure",
                fixture=args.fixture or "campaign_pretable",
            )
            if args.format == "json":
                output = render_json(result)
            elif args.format == "markdown":
                output = render_markdown([result])
            else:
                output = render_text(result, args.verbose)
    except SimulatorError as error:
        parser.error(str(error))
        return 2
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output + ("" if output.endswith("\n") else "\n"), encoding="utf-8")
    else:
        print(output)
    return 0
