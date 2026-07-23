"""Command line entry point for Interactive Research Shell v0.1."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .research_shell import (
    EvidenceClass,
    InteractiveResearchSession,
    SessionMetadata,
    replay_session,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 Interactive Research Shell v0.1")
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--evidence-class", choices=[value.value for value in EvidenceClass], required=True)
    parser.add_argument("--participant-code", required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--information-condition",
        choices=("KNOWN", "UNKNOWN", "NOT_APPLICABLE"),
        default="NOT_APPLICABLE",
    )
    parser.add_argument("--strategy-intention")
    parser.add_argument("--script", type=Path, help="JSON action sequence for deterministic replay")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--summary-output", type=Path)
    parser.add_argument("--transcript-output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    metadata = SessionMetadata.create(
        args.session_id,
        EvidenceClass(args.evidence_class),
        args.seed,
        args.participant_code,
        information_condition=args.information_condition,
        strategy_intention=args.strategy_intention,
    )
    if args.script:
        actions = json.loads(args.script.read_text(encoding="utf-8"))
        if not isinstance(actions, list):
            raise ValueError("script must contain a JSON list")
        session = replay_session(metadata, actions)
    else:
        session = InteractiveResearchSession(metadata)
        session.run_console()
    if args.json_output and args.summary_output:
        session.write_exports(args.json_output, args.summary_output)
    elif args.json_output or args.summary_output:
        raise ValueError("both --json-output and --summary-output are required together")
    if args.transcript_output:
        if args.script:
            raise ValueError("--transcript-output is available only for interactive sessions")
        session.write_transcript(args.transcript_output)
    if args.script:
        print(session.human_summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
