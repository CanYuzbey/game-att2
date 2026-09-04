from __future__ import annotations

import argparse
import json

from .attention import AttentionPolicy, AttentionResolver, coverage_report, coverage_warnings
from .fixtures import aggressive_brain, balanced_brain, prototype_expressions, prototype_sources
from .model import AttentionHistory
from .rng import SeededRNG


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 V3 isolated Attention sandbox")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--brain", choices=("balanced", "aggressive"), default="balanced")
    parser.add_argument("--focus-source")
    parser.add_argument("--debug-trace", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    brain = balanced_brain() if args.brain == "balanced" else aggressive_brain()
    sources = prototype_sources()
    expressions = prototype_expressions()
    history = AttentionHistory()
    resolver = AttentionResolver(AttentionPolicy())
    results, traces = resolver.resolve_with_trace(
        brain,
        expressions,
        sources,
        history,
        SeededRNG(args.seed),
        args.focus_source,
    )
    payload: dict[str, object] = {
        "seed": args.seed,
        "brain": brain.id,
        "coverage": {
            duty.value: {"available": available, "required": required}
            for duty, (available, required) in coverage_report(brain, expressions, sources).items()
        },
        "coverage_warnings": [
            {
                "duty": warning.duty.value,
                "available": warning.available,
                "required": warning.required,
                "shortfall": warning.shortfall,
            }
            for warning in coverage_warnings(brain, expressions, sources)
        ],
        "attention": [
            {
                "slot": result.slot_id,
                "duty": result.duty.value if result.duty else None,
                "expression": result.expression_id,
                "shaded": result.shaded,
                "reason": result.reason,
                "weights": dict(result.normalized_weights),
            }
            for result in results
        ],
    }
    if args.debug_trace:
        payload["trace"] = [
            {
                "slot": trace.slot_id,
                "duty": trace.duty.value if trace.duty else None,
                "rejected": [list(item) for item in trace.rejected],
                "weights": [
                    {
                        "expression": weight.expression_id,
                        "base": weight.base,
                        "brain": weight.brain,
                        "recency": weight.recency,
                        "state": weight.state,
                        "focus": weight.focus,
                        "final": weight.final,
                    }
                    for weight in trace.weights
                ],
                "roll": trace.roll,
                "total_weight": trace.total_weight,
                "selected": trace.selected_expression_id,
            }
            for trace in traces
        ]
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
