"""Thin CLI boundary for deterministic and owner-diagnostic H1 runs."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections.abc import Sequence
from pathlib import Path
from typing import Any, cast

from .h1_research import (
    comparison_payload,
    comparison_requests,
    render_h1_markdown,
    run_comparisons,
)

COMPARISON_IDS = tuple(f"H1-C{index}" for index in range(1, 7))
VARIANT_IDS = {
    "H1-C1": ("H1-C1-unprepared", "H1-C1-prepared"),
    "H1-C2": ("H1-C2-usable", "H1-C2-unusable"),
    "H1-C3": ("H1-C3-ordinary", "H1-C3-high-risk"),
    "H1-C4": ("H1-C4-vague", "H1-C4-exact"),
    "H1-C5": ("H1-C5-precise", "H1-C5-assisted"),
    "H1-C6": ("H1-C6-normal", "H1-C6-threshold"),
}
ALL_VARIANT_IDS = {
    variant_id for comparison_variants in VARIANT_IDS.values() for variant_id in comparison_variants
}
VARIANT_PROMPTS = {
    "H1-C1-unprepared": (
        "TEST 1/6 — UNPREPARED BLOCK\n"
        "Anna's Surgical Jab is coming. You did not spend your Main action preparing "
        "Guard Flesh. This tests the weaker reaction available after another plan."
    ),
    "H1-C1-prepared": (
        "TEST 2/6 — PREPARED BLOCK\n"
        "Anna's same Surgical Jab is coming, but you deliberately prepared Guard Flesh "
        "with the grafted Right Arm. This tests whether strategy earns a better chance."
    ),
    "H1-C2-usable": (
        "BODY-SOURCE TEST — USABLE GRAFTED ARM\n"
        "Your grafted Right Arm is usable, so it can physically source the Block."
    ),
    "H1-C2-unusable": (
        "BODY-SOURCE TEST — UNUSABLE GRAFTED ARM\n"
        "Your grafted Right Arm is disabled. This tests that perfect timing cannot "
        "replace a missing physical capability."
    ),
    "H1-C3-ordinary": (
        "TEST 3/6 — ORDINARY BLOCK MISS\n"
        "This is the safe response. If your timing misses, only Anna's original attack "
        "applies; there is no extra punishment."
    ),
    "H1-C3-high-risk": (
        "TEST 4/6 — VOLUNTARY HIGH-RISK BLOCK\n"
        "You knowingly risk the grafted Right Arm for a rare stronger recovery chance. "
        "A miss may damage that arm in addition to Anna's original attack."
    ),
    "H1-C4-vague": (
        "INFORMATION TEST — VAGUE INTENT\n"
        "You know an attack is coming but not its exact source and target. This tests "
        "the cost of acting on incomplete information."
    ),
    "H1-C4-exact": (
        "INFORMATION TEST — EXACT INTENT\n"
        "You know Anna will use her Right Arm against your Torso. This tests whether "
        "better information improves execution without guaranteeing success."
    ),
    "H1-C5-precise": (
        "TEST 5/6 — PRECISE INPUT PROFILE\n"
        "The Block uses the narrower timing tolerance. This tests the default precision "
        "demand without changing the strategy or body rules."
    ),
    "H1-C5-assisted": (
        "TEST 6/6 — ASSISTED INPUT PROFILE\n"
        "The same Block uses a wider timing tolerance. This tests whether accommodation "
        "can preserve the same decision and consequence pipeline."
    ),
    "H1-C6-normal": (
        "PRESSURE TEST — NORMAL TORSO STATE\n"
        "The Block occurs under normal integrity pressure. This is the comparison "
        "baseline for a rare high-risk recovery attempt."
    ),
    "H1-C6-threshold": (
        "PRESSURE TEST — TORSO NEAR A KNOWN THRESHOLD\n"
        "Your Torso is close to zero integrity. This tests whether exceptional legal "
        "execution can preserve integrity without inventing a survival or wound rule."
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 H1 reflex research runner")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--comparison", choices=COMPARISON_IDS, action="append")
    selection.add_argument("--all-comparisons", action="store_true")
    parser.add_argument("--script", type=Path)
    parser.add_argument("--profile", choices=("precise", "assisted"))
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--session-id")
    parser.add_argument("--consent-confirmed", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--evidence-class",
        choices=("AUTOMATED_REGRESSION", "OWNER_DIAGNOSTIC"),
    )
    return parser


def _load_script(path: Path) -> tuple[str, dict[str, int]]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot load H1 script {path}: {error}") from error
    if not isinstance(raw, dict) or set(raw) != {
        "schema_version",
        "evidence_class",
        "inputs",
    }:
        raise ValueError("H1 script requires schema_version, evidence_class, and inputs")
    if raw["schema_version"] != "h1-script-0.1":
        raise ValueError("unsupported H1 script schema_version")
    if raw["evidence_class"] != "AUTOMATED_REGRESSION":
        raise ValueError("scripted H1 evidence must be AUTOMATED_REGRESSION")
    inputs_raw = raw["inputs"]
    if not isinstance(inputs_raw, dict):
        raise TypeError("H1 script inputs must be a mapping")
    inputs: dict[str, int] = {}
    for variant_id, value in cast(dict[str, Any], inputs_raw).items():
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError(f"H1 timing input for {variant_id} must be a non-negative integer")
        inputs[str(variant_id)] = value
    if set(inputs) != ALL_VARIANT_IDS:
        missing = sorted(ALL_VARIANT_IDS - set(inputs))
        extra = sorted(set(inputs) - ALL_VARIANT_IDS)
        raise ValueError(f"H1 script variant mismatch; missing={missing}, extra={extra}")
    return str(raw["evidence_class"]), inputs


def _capture_timing_error(variant_id: str) -> int:
    print("\n" + "=" * 72, file=sys.stderr)
    print(VARIANT_PROMPTS[variant_id], file=sys.stderr)
    print(
        "Your task is only to estimate one second; this is a diagnostic, not a score.",
        file=sys.stderr,
    )
    print(
        "Press Enter once to ARM the attempt.",
        file=sys.stderr,
    )
    input()
    started = time.perf_counter_ns()
    print("Now wait about ONE SECOND, then press Enter again.", file=sys.stderr)
    input()
    elapsed_ms = (time.perf_counter_ns() - started) // 1_000_000
    return abs(int(elapsed_ms) - 1000)


def _interactive_inputs(comparison_ids: tuple[str, ...]) -> dict[str, int]:
    inputs: dict[str, int] = {}
    for comparison_id in comparison_ids:
        for variant_id in VARIANT_IDS[comparison_id]:
            inputs[variant_id] = _capture_timing_error(variant_id)
    return inputs


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    comparison_ids = COMPARISON_IDS if args.all_comparisons else tuple(args.comparison or ())
    try:
        if len(set(comparison_ids)) != len(comparison_ids):
            raise ValueError("each H1 comparison may be selected only once")
        if args.script:
            script_evidence_class, inputs = _load_script(args.script)
            if args.evidence_class and args.evidence_class != script_evidence_class:
                raise ValueError("--evidence-class conflicts with the scripted evidence class")
            evidence_class = script_evidence_class
        else:
            if args.evidence_class == "AUTOMATED_REGRESSION":
                raise ValueError("AUTOMATED_REGRESSION requires --script")
            if not args.session_id:
                raise ValueError("OWNER_DIAGNOSTIC requires --session-id")
            if not args.consent_confirmed:
                raise ValueError("OWNER_DIAGNOSTIC requires --consent-confirmed")
            evidence_class = args.evidence_class or "OWNER_DIAGNOSTIC"
            inputs = _interactive_inputs(comparison_ids)
        for comparison_id in comparison_ids:
            comparison_requests(comparison_id, inputs, profile_override=args.profile)
        results = run_comparisons(
            comparison_ids,
            inputs,
            evidence_class=evidence_class,
            profile_override=args.profile,
        )
        if args.format == "json":
            payload = comparison_payload(results)
            payload["session_metadata"] = {
                "session_id": args.session_id or "AUTOMATED-H1-SCRIPT",
                "consent_confirmed": bool(args.consent_confirmed),
                "participant_identity_collected": False,
                "facilitator_deviations": [],
                "selected_comparisons": list(comparison_ids),
                "input_mode": "scripted" if args.script else "terminal_timing_capture",
            }
            rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
        else:
            rendered = render_h1_markdown(results)
        if args.output:
            if args.output.exists():
                raise ValueError(f"refusing to overwrite existing H1 evidence: {args.output}")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
            print(f"Saved H1 evidence to {args.output}", file=sys.stderr)
        else:
            print(rendered, end="")
    except (TypeError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
