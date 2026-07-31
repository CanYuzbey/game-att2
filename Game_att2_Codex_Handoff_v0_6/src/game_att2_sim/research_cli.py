"""Command line entry point for Interactive Research Shell v0.1."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from .cli_support import CLIInputError, load_json_list
from .research_shell import (
    EvidenceClass,
    InteractiveResearchSession,
    SessionMetadata,
    replay_session,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Game att2 Interactive Research Shell v0.1")
    parser.add_argument("--session-id", required=True)
    parser.add_argument(
        "--evidence-class",
        choices=[
            EvidenceClass.OWNER_DIAGNOSTIC.value,
            EvidenceClass.EXTERNAL_PILOT.value,
            EvidenceClass.AUTOMATED_REGRESSION.value,
        ],
        required=True,
    )
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
    parser = build_parser()
    args = parser.parse_args(argv)
    if bool(args.json_output) != bool(args.summary_output):
        parser.error("both --json-output and --summary-output are required together")
    if args.script and args.transcript_output:
        parser.error("--transcript-output is available only for interactive sessions")
    try:
        metadata = SessionMetadata.create(
            args.session_id,
            EvidenceClass(args.evidence_class),
            args.seed,
            args.participant_code,
            information_condition=args.information_condition,
            strategy_intention=args.strategy_intention,
        )
        if args.script:
            session = replay_session(
                metadata,
                load_json_list(args.script, label="research script"),
            )
        else:
            session = InteractiveResearchSession(metadata)
            session.run_console()
        if args.json_output and args.summary_output:
            session.write_exports(args.json_output, args.summary_output)
        if args.transcript_output:
            session.write_transcript(args.transcript_output)
        if args.script:
            print(session.human_summary())
    except (CLIInputError, OSError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
