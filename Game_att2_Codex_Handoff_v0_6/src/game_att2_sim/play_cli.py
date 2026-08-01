"""Console driver and entry point for the approved playable campaign CLI.

This module owns all input/output. It stops the automation at the decision
phase of every round, presents numbered prompts, and prints the Pillar 5
readability record for each resolved action.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from .campaign_play import CampaignConsole, campaign_session, run_campaign_actions
from .cli_support import CLIInputError, load_json_list, positive_int
from .enums import Slot
from .play_feedback import (
    DEFAULT_FEEDBACK_DIRECTORY,
    PlayableSession,
    build_feedback_record,
    write_feedback_record,
)
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

SCALE_QUESTIONS: tuple[tuple[str, str], ...] = (
    ("goal_clarity", "Amacı ne kadar net anladın?"),
    ("blood_importance", "Blood kararlarında ne kadar önemli hissettirdi?"),
    ("danger_pressure", "Yenilme / ölme baskısını ne kadar hissettin?"),
    ("consequence_clarity", "Eylemlerin sonuçları ne kadar anlaşılırdı?"),
    ("choice_meaningfulness", "Seçimler ne kadar anlamlı hissettirdi?"),
    ("replay_intent", "Bir kez daha oynama isteğin ne kadar yüksek?"),
)

MOTIVATION_SCALE_QUESTIONS: tuple[tuple[str, str], ...] = (
    ("enemy_motivation_clarity", "Rakibin ne istediğini ne kadar anlayabildin?"),
    ("victory_route_breadth", "Karşılaşmayı farklı yollarla çözebilme alanı ne kadar genişti?"),
    ("resolution_naturalness", "Karşılaşma sonuçları durumun doğal devamı gibi hissettirdi mi?"),
)

TEXT_QUESTIONS: tuple[tuple[str, str], ...] = (
    ("ending_cause", "Sence bu oyun deneyimi neden bu sonuçla bitti?"),
    ("blood_strategy", "Blood harcarken veya saklarken ne düşündün?"),
    ("threat_model", "Seni güvende ya da ölüm tehlikesinde hissettiren neydi?"),
    ("desired_change", "Tek bir şeyi değiştirebilseydin neyi değiştirirdin?"),
)

MOTIVATION_TEXT_QUESTIONS: tuple[tuple[str, str], ...] = (
    ("enemy_motivation_inference", "Sence Jeff ne istiyordu ve bunu sana ne düşündürdü?"),
    (
        "perceived_victory_routes",
        "Jeff karşılaşmasını hangi farklı yollarla sonuçlandırabileceğini düşündün?",
    ),
)


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


@dataclass
class FeedbackConsole:
    """Optional post-play questionnaire; answers stay out of the transcript."""

    session: PlayableSession
    input_fn: Callable[[str], str] = input
    output_fn: Callable[[str], None] = print
    _stopped: bool = field(default=False, init=False)

    def collect(self) -> dict[str, object] | None:
        self.output_fn("")
        self.output_fn("=== İSTEĞE BAĞLI OYUN TESTİ GERİ BİLDİRİMİ ===")
        self.output_fn(
            "Kayıt yalnızca bu bilgisayarda saklanır; otomatik yükleme yapılmaz."
        )
        self.output_fn("Lütfen kişisel veya hassas bilgi yazma.")
        consent = self._ask_yes_no(
            "Anonim oyun özeti ve cevapların yerel tasarım araştırması için "
            "kaydedilsin mi? [e/H]: "
        )
        if consent is not True:
            self.output_fn("Geri bildirim kaydedilmedi.")
            return None

        training = self._ask_yes_no(
            "Bu kayıt, insan incelemesi ve anonimleştirme sonrası gelecekte "
            "model eğitimi için kullanılabilir mi? [e/H]: "
        )
        self.output_fn("1 = hiç / çok kötü, 5 = çok / çok iyi; Enter = atla.")
        ratings: dict[str, int | None] = {}
        scale_questions = SCALE_QUESTIONS
        text_questions = TEXT_QUESTIONS
        if not isinstance(self.session, PlaySession):
            scale_questions = (
                *SCALE_QUESTIONS[:-1],
                *MOTIVATION_SCALE_QUESTIONS,
                SCALE_QUESTIONS[-1],
            )
            text_questions = (
                *TEXT_QUESTIONS[:-1],
                *MOTIVATION_TEXT_QUESTIONS,
                TEXT_QUESTIONS[-1],
            )
        for key, prompt in scale_questions:
            if self._stopped:
                break
            rating = self._ask_scale(f"{prompt} [1-5]: ")
            if self._stopped:
                break
            ratings[key] = rating

        reflections: dict[str, str] = {}
        if not self._stopped:
            self.output_fn("Kısa cevaplar isteğe bağlıdır; Enter ile atlayabilirsin.")
        for key, prompt in text_questions:
            if self._stopped:
                break
            reflections[key] = self._ask_text(f"{prompt}\n> ")

        return build_feedback_record(
            self.session,
            ratings=ratings,
            reflections=reflections,
            model_training_consent=training is True,
            collection_status="partial" if self._stopped else "complete",
        )

    def _read(self, prompt: str) -> str | None:
        try:
            return self.input_fn(prompt).strip()
        except EOFError:
            self._stopped = True
            return None

    def _ask_yes_no(self, prompt: str) -> bool | None:
        while not self._stopped:
            answer = self._read(prompt)
            if answer is None:
                return None
            normalized = answer.casefold()
            if normalized in {"e", "evet", "y", "yes"}:
                return True
            if normalized in {"", "h", "hayır", "hayir", "n", "no"}:
                return False
            self.output_fn("  Lütfen 'e' veya 'h' gir.")
        return None

    def _ask_scale(self, prompt: str) -> int | None:
        while not self._stopped:
            answer = self._read(prompt)
            if answer is None or answer == "":
                return None
            if answer in {"1", "2", "3", "4", "5"}:
                return int(answer)
            self.output_fn("  1 ile 5 arasında bir sayı gir veya Enter ile atla.")
        return None

    def _ask_text(self, prompt: str) -> str:
        answer = self._read(prompt)
        return "" if answer is None else answer


def _collect_feedback(session: PlayableSession, directory: Path) -> None:
    feedback = FeedbackConsole(session).collect()
    if feedback is not None:
        feedback_path = write_feedback_record(feedback, directory)
        print(f"Geri bildirim yerel olarak kaydedildi: {feedback_path}")


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
        description="Game att2 playable CLI — full approved campaign by default"
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--phase-1",
        action="store_true",
        help="run the retained S-001 vs Jeff-only diagnostic interface",
    )
    parser.add_argument(
        "--round-limit",
        type=positive_int,
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
    parser.add_argument(
        "--feedback-dir",
        type=Path,
        default=DEFAULT_FEEDBACK_DIRECTORY,
        help="directory for consented local playtest JSON records",
    )
    parser.add_argument(
        "--no-feedback",
        action="store_true",
        help="skip the optional post-play questionnaire",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:  # pragma: no cover - depends on the console
            reconfigure(encoding="utf-8", errors="replace")
    try:
        actions = load_json_list(args.script, label="play script") if args.script else None
        if actions is not None and not all(isinstance(action, str) for action in actions):
            raise CLIInputError("play script entries must be action-id strings")
        if args.phase_1:
            session = PlaySession(seed=args.seed, round_limit=args.round_limit)
            if actions is not None:
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
                if not args.no_feedback:
                    _collect_feedback(session, args.feedback_dir)
        else:
            full_session = campaign_session(args.seed)
            if actions is not None:
                transcript = []

                def emit_campaign(text: str) -> None:
                    transcript.append(text)
                    print(text)

                run_campaign_actions(
                    full_session,
                    [str(action) for action in actions],
                    emit_campaign,
                    args.round_limit,
                )
                lines = transcript
            else:
                campaign_console = CampaignConsole(
                    full_session,
                    round_limit=args.round_limit,
                )
                campaign_console.run()
                lines = campaign_console.transcript
                if not args.no_feedback:
                    _collect_feedback(full_session, args.feedback_dir)
        if args.transcript_output:
            args.transcript_output.parent.mkdir(parents=True, exist_ok=True)
            args.transcript_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except (CLIInputError, OSError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
