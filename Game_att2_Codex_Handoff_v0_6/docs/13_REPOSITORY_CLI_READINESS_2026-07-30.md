# Game att2 — Repository and CLI Readiness Record

Date: 2026-07-30

Canonical repository: <https://github.com/CanYuzbey/game-att2>

Reviewed upstream commit: `ce2b836` (`origin/main`)

Working branch: `chore/cli-test-readiness`

## Purpose

This record makes the repository identity and the command-line test boundary durable.
It supplements the 2026-07-23 evidence report; it does not rewrite historical evidence
or authorize production, Unity, Encounter 3 runtime, new enemies, or new game content.

## Repository layout

The active Python handoff package is `Game_att2_Codex_Handoff_v0_6/`. The top-level
repository README is the navigation entry point. `docs/02_DEVELOPMENT_MASTER_v0_6.md`
through `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md` remain the binding design, technical, and
acceptance sources. `docs/12_CURRENT_PROJECT_REPORT_2026-07-23.md` remains the evidence
baseline and must be read with its original date.

## CLI roles

| Interface | Purpose | Appropriate evidence |
|---|---|---|
| `python -m game_att2_sim` | Seven approved scenarios, strategy batches, text/JSON/Markdown reports | Deterministic implementation and regression evidence |
| `python -m game_att2_sim.play_cli` | Human-playable Phase 1 encounter, S-001 vs Jeff only | Interaction smoke tests and future human play evidence |
| `python -m game_att2_sim.research_cli` | Full approved S-001 → Jeff → graft → Anna → table research sequence | Labeled owner, automated, or external-pilot evidence |

## Readiness result

The CLI system is sufficient for deterministic automated test runs and repeatable
operator smoke runs. It is not sufficient by itself for product validation.

The 2026-07-30 pass added or verified:

- shared file/JSON/positive-integer validation at the CLI boundary;
- clean nonzero usage errors without Python tracebacks;
- mutually exclusive simulator run selectors;
- actual human-readable text and Markdown batch reports;
- paired research export validation;
- subprocess coverage of all three documented module entry points;
- a reusable Phase 1 scripted-win example;
- 145 passing tests, 88% line coverage, clean Ruff, and clean strict mypy.

## Remaining limits

- Phase 1 play remains intentionally locked to S-001 vs Jeff.
- The research shell, not the play CLI, owns graft, Anna, and Grafting Table evidence.
- Automated strategies are diagnostic test drivers, not models of player behavior.
- No P01–P08 external human evidence exists; fun, comprehension, pacing, and balance
  remain unproven.
- Unity and Encounter 3 runtime implementation remain blocked by the existing gates.

## Recommended operator commands

```powershell
python -m pytest -q
python -m pytest --cov=game_att2_sim --cov-report=term-missing -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_win_sequence.json
python -m game_att2_sim.research_cli `
  --session-id AUTO-SMOKE-001 `
  --evidence-class AUTOMATED_REGRESSION `
  --participant-code AUTO-SMOKE `
  --seed 42 `
  --script research/interactive_shell/example_action_sequence.json
```
