"""CLI for the approved local visual-lab page and deterministic evidence replay."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any, cast

from .visual_lab import (
    comparison_payload,
    run_visual_lab_comparisons,
    visual_lab_variant_ids,
)
from .visual_lab_page import render_visual_lab_fragment

COMPARISON_IDS = tuple(f"VL-C{index}" for index in range(1, 11))
ALL_VARIANT_IDS = {
    variant
    for variants in visual_lab_variant_ids().values()
    for variant in variants
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 bounded visual interaction lab")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--page", action="store_true", help="render the local HTML fragment")
    mode.add_argument("--script", type=Path, help="replay signed deterministic inputs")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--comparison", action="append", choices=COMPARISON_IDS)
    selection.add_argument("--all-comparisons", action="store_true")
    parser.add_argument("--format", choices=("json",), default="json")
    parser.add_argument("--output", type=Path)
    return parser


def load_visual_lab_script(path: Path) -> tuple[str, dict[str, int]]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot load visual-lab script {path}: {error}") from error
    if not isinstance(raw, dict) or set(raw) != {
        "schema_version",
        "evidence_class",
        "signed_offsets_ms",
    }:
        raise ValueError(
            "visual-lab script requires schema_version, evidence_class, and signed_offsets_ms"
        )
    if raw["schema_version"] != "visual-lab-script-0.1":
        raise ValueError("unsupported visual-lab script schema_version")
    if raw["evidence_class"] != "AUTOMATED_REGRESSION":
        raise ValueError("scripted visual-lab evidence must be AUTOMATED_REGRESSION")
    offsets_raw = raw["signed_offsets_ms"]
    if not isinstance(offsets_raw, dict):
        raise TypeError("visual-lab signed_offsets_ms must be a mapping")
    offsets: dict[str, int] = {}
    for variant_id, value in cast(dict[str, Any], offsets_raw).items():
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"visual-lab offset for {variant_id} must be an integer")
        offsets[str(variant_id)] = value
    if set(offsets) != ALL_VARIANT_IDS:
        raise ValueError(
            "visual-lab script variant mismatch; "
            f"missing={sorted(ALL_VARIANT_IDS - set(offsets))}, "
            f"extra={sorted(set(offsets) - ALL_VARIANT_IDS)}"
        )
    return str(raw["evidence_class"]), offsets


def _write_new(path: Path, content: str) -> None:
    if path.exists():
        raise ValueError(f"refusing to overwrite existing visual-lab output: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.page:
            if args.comparison or args.all_comparisons:
                raise ValueError("comparison selection is valid only with --script")
            if not args.output:
                raise ValueError("--page requires --output")
            _write_new(args.output, render_visual_lab_fragment())
            return 0

        if not args.comparison and not args.all_comparisons:
            raise ValueError("--script requires --comparison or --all-comparisons")
        comparison_ids = COMPARISON_IDS if args.all_comparisons else tuple(args.comparison)
        if len(set(comparison_ids)) != len(comparison_ids):
            raise ValueError("each visual-lab comparison may be selected only once")
        evidence_class, offsets = load_visual_lab_script(args.script)
        results = run_visual_lab_comparisons(comparison_ids, offsets, evidence_class)
        rendered = json.dumps(comparison_payload(results), indent=2, sort_keys=True) + "\n"
        if args.output:
            _write_new(args.output, rendered)
        else:
            print(rendered, end="")
    except (TypeError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
