"""Console driver and entry point for the Phase 1 playable CLI.

This module owns all input/output. It stops the automation at the decision
phase of every round, presents numbered prompts, and prints the Pillar 5
readability record for each resolved action.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from .enums import Slot
from .play_render import (
    localize_reason,
    render_attack_menu,
    render_choice_menu,
    render_intro,
    render_main_menu,
    render_reports,
    render_state,
    render_summary,
    render_target_menu,
)
from .play_session import (
    ATTACK_ACTIONS,
    DEFAULT_ROUND_LIMIT,
    MenuCategory,
    PlayOffer,
    PlaySession,
)

BACK = "0"


@dataclass
class PlayConsole:
    """Menu state machine over one :class:`PlaySession`."""

    session: PlaySession
    input_fn: Callable[[str], str] = input
    output_fn: Callable[[str], None] = print
    transcript: list[str] = field(default_factory=list)
    _stopped: bool = field(default=False, init=False)

    def emit(self, text: str) -> None:
        self.transcript.append(text)
        self.output_fn(text)

    def ask(self, prompt: str) -> str:
        """Read one selection.

        ``input`` already echoes the prompt to the console, so the prompt and
        the answer are recorded in the transcript only -- emitting them again
        would double every line on screen.
        """
        try:
            answer = self.input_fn(prompt)
        except EOFError:
            self._stopped = True
            self.transcript.append(f"{prompt}<girdi bitti>")
            return BACK
        answer = answer.strip()
        self.transcript.append(f"{prompt}{answer}")
        # Piped input echoes nothing, so close the prompt line ourselves.
        self.output_fn("")
        return answer

    def run(self) -> None:
        self.emit(render_intro(self.session))
        self.emit(render_state(self.session))
        while not self.session.complete and not self._stopped:
            self._main_menu()
        if self._stopped and not self.session.complete:
            self.session.perform("end_session")
        self.emit(render_summary(self.session))

    # ----------------------------------------------------------------- menus

    def _main_menu(self) -> None:
        self.emit(render_main_menu(self.session))
        choice = self.ask("  Seçim: ")
        if self._stopped:
            return
        if choice == "1":
            self._attack_menu()
        elif choice == "2":
            self._resolve("focus")
        elif choice == "3":
            self._choice_menu(
                "EŞYA KULLAN — hangi eşya?", self.session.offers_in(MenuCategory.ITEM)
            )
        elif choice == "4":
            self._choice_menu(
                "DEFANS / DURUŞ — hangi eylem?",
                self.session.offers_in(MenuCategory.DEFEND),
            )
        elif choice == "5":
            self.emit(render_state(self.session))
        elif choice == "6" and self.session.find_offer("forfeit_main") is not None:
            self._resolve("forfeit_main")
        elif choice == BACK:
            self._resolve("end_session")
        else:
            self.emit("  ! Geçersiz seçim. Listedeki numaralardan birini gir.")

    def _attack_menu(self) -> None:
        summaries = self.session.attack_action_summaries()
        self.emit(render_attack_menu(self.session))
        choice = self.ask("  Saldırı seçimi: ")
        if self._stopped or choice == BACK:
            return
        index = self._index(choice, len(summaries))
        if index is None:
            self.emit("  ! Geçersiz saldırı numarası.")
            return
        action_id, enabled, reason = summaries[index]
        if not enabled:
            self.emit(
                f"  ! {self.session.action_display_name(action_id)} kapalı: "
                f"{localize_reason(reason)}"
            )
            return
        self._target_menu(action_id)

    def _target_menu(self, action_id: str) -> None:
        slots = list(Slot)
        self.emit(render_target_menu(self.session, action_id))
        choice = self.ask("  Hedef seçimi: ")
        if self._stopped or choice == BACK:
            return
        index = self._index(choice, len(slots))
        if index is None:
            self.emit("  ! Geçersiz hedef numarası.")
            return
        self._resolve(f"{action_id}:{slots[index].value}")

    def _choice_menu(self, title: str, offers: list[PlayOffer]) -> None:
        if not offers:
            self.emit("  ! Bu kategoride sunulacak bir şey yok.")
            return
        self.emit(render_choice_menu(title, offers))
        choice = self.ask("  Seçim: ")
        if self._stopped or choice == BACK:
            return
        index = self._index(choice, len(offers))
        if index is None:
            self.emit("  ! Geçersiz numara.")
            return
        self._resolve(offers[index].action_id)

    @staticmethod
    def _index(choice: str, count: int) -> int | None:
        if not choice.isdigit():
            return None
        value = int(choice)
        if not 1 <= value <= count:
            return None
        return value - 1

    def _resolve(self, action_id: str) -> None:
        result = self.session.perform(action_id)
        if not result.accepted:
            self.emit(f"  ! Eylem uygulanmadı: {localize_reason(result.message)}")
            return
        if result.reports:
            self.emit(render_reports(result.reports))
        if not self.session.complete:
            self.emit(render_state(self.session))


def _script_run(session: PlaySession, actions: Sequence[str], emit: Callable[[str], None]) -> None:
    emit(render_intro(session))
    emit(render_state(session))
    for action_id in actions:
        if session.complete:
            break
        result = session.perform(action_id)
        if not result.accepted:
            emit(f"  ! {action_id} uygulanmadı: {result.message}")
            continue
        if result.reports:
            emit(render_reports(result.reports))
        if not session.complete:
            emit(render_state(session))
    emit(render_summary(session))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Game att2 Phase 1 playable CLI — S-001 vs Jeff only"
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--round-limit",
        type=int,
        default=DEFAULT_ROUND_LIMIT,
        help="harness guard against an endless session; not a game rule",
    )
    parser.add_argument(
        "--script",
        type=Path,
        help=f"JSON list of action ids for a non-interactive replay, e.g. "
        f'["{ATTACK_ACTIONS[0]}:right_arm"]',
    )
    parser.add_argument("--transcript-output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:  # pragma: no cover - depends on the console
            reconfigure(encoding="utf-8", errors="replace")
    session = PlaySession(seed=args.seed, round_limit=args.round_limit)
    if args.script:
        # utf-8-sig: PowerShell's redirection writes a BOM this parser must tolerate.
        actions = json.loads(args.script.read_text(encoding="utf-8-sig"))
        if not isinstance(actions, list):
            raise ValueError("script must contain a JSON list of action ids")
        transcript: list[str] = []

        def emit(text: str) -> None:
            transcript.append(text)
            print(text)

        _script_run(session, [str(action) for action in actions], emit)
        lines = transcript
    else:
        console = PlayConsole(session)
        console.run()
        lines = console.transcript
    if args.transcript_output:
        args.transcript_output.parent.mkdir(parents=True, exist_ok=True)
        args.transcript_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
