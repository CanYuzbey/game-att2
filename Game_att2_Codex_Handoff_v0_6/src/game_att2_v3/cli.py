from __future__ import annotations

import argparse
import json

from .attention import AttentionPolicy, AttentionResolver, coverage_report
from .fixtures import aggressive_brain, balanced_brain, prototype_expressions, prototype_sources
from .model import AttentionHistory
from .rng import SeededRNG


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 V3 isolated Attention sandbox")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--brain", choices=("balanced", "aggressive"), default="balanced")
    parser.add_argument("--focus-source")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    brain = balanced_brain() if args.brain == "balanced" else aggressive_brain()
    sources = prototype_sources()
    expressions = prototype_expressions()
    history = AttentionHistory()
    resolver = AttentionResolver(AttentionPolicy())
    results = resolver.resolve(
        brain,
        expressions,
        sources,
        history,
        SeededRNG(args.seed),
        args.focus_source,
    )
    payload = {
        "seed": args.seed,
        "brain": brain.id,
        "coverage": {
            duty.value: {"available": available, "required": required}
            for duty, (available, required) in coverage_report(brain, expressions, sources).items()
        },
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
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
