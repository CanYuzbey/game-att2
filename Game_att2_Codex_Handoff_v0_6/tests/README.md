# Tests

Canonical repository: <https://github.com/CanYuzbey/game-att2>

The acceptance source is `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`.

## Test layers

- `unit/` checks rule branches, action economy, RNG injection, and causal integrity.
- `integration/test_scenarios.py` checks the seven approved deterministic scenarios and batches.
- `integration/test_cli_reporting.py` checks simulator CLI selection, formats, and file output.
- `integration/test_play_cli.py` checks the Phase 1 play session, renderer, menus, and script mode.
- `integration/test_campaign_play.py` checks the default Jeff → graft → Anna → table
  player path, causal hints, and Pillar 5 output.
- `unit/test_play_feedback.py` checks consented, versioned, non-overwriting local
  feedback records for both playable modes and keeps campaign-only motivation
  questions out of the retained Phase 1 instrument.
- `unit/test_encounter_design.py` checks motivation/route configuration, mutual actor
  outcomes, capability-break outcomes, deterministic repeat-aware intent scoring,
  and the deferred one-round Cover It contract.
- `unit/test_rules.py` includes the atomic item-for-limb exchange contract used by the
  Jeff survey bargain, Blood-0 death, and Limb for Life death prevention.
- `integration/test_research_cli.py` checks research CLI exports and input contracts.
- `integration/test_console_entrypoints.py` launches the documented simulator,
  playable, research-shell, and visual-lab `python -m` commands as subprocesses.
- `integration/test_research_shell.py` and `integration/test_post_table_probe.py` check the evidence shell and non-canonical probes.
- `unit/test_h1_config.py` and `unit/test_reflex.py` validate the isolated H1 schema,
  pure legality, grades, risk commitment, assisted input, and prohibited scope.
- `integration/test_h1_research.py` and `integration/test_h1_cli.py` cover H1-C1 through
  H1-C6, deterministic exports, capability recomputation, and CLI boundaries without
  adding H1 to the approved scenario runner.
- `unit/test_visual_lab_config.py` and `unit/test_visual_lab.py` check the isolated
  readiness, recovery, signed timing, body-source, and failure contracts.
- `integration/test_visual_lab_research.py` and `integration/test_visual_lab_cli.py`
  check VL-C1 through VL-C10, deterministic evidence, local page generation, claims
  boundaries, and campaign isolation.

## Complete automated gate

```powershell
python -m pytest -q
python -m pytest --cov=game_att2_sim --cov-report=term-missing -q
python -m ruff check src tests
python -m mypy src
```

## Operator smoke runs

```powershell
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim --batch 100 --strategy balanced --seed 42 --format json
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
python -m game_att2_sim.play_cli --phase-1 --seed 42 --script examples/play_cli_win_sequence.json
python -m game_att2_sim.research_cli `
  --session-id AUTO-SMOKE-001 `
  --evidence-class AUTOMATED_REGRESSION `
  --participant-code AUTO-SMOKE `
  --seed 42 `
  --script research/interactive_shell/example_action_sequence.json
python -m game_att2_sim.h1_cli `
  --all-comparisons `
  --script examples/h1_scripted_comparisons.json `
  --format json
python -m game_att2_sim.visual_lab_cli `
  --script examples/visual_lab_scripted_comparisons.json `
  --all-comparisons `
  --format json
```

Use scripted/fake RNG for branch-level unit tests and seeded RNG for reproducibility
integration tests. These commands validate deterministic implementation behavior; they
do not replace moderated human playtests or prove fun, readability, or balance.
