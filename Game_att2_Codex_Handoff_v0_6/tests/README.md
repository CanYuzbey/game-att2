# Tests

Canonical repository: <https://github.com/CanYuzbey/game-att2>

The acceptance source is `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`.

## Test layers

- `unit/` checks rule branches, action economy, RNG injection, and causal integrity.
- `integration/test_scenarios.py` checks the seven approved deterministic scenarios and batches.
- `integration/test_cli_reporting.py` checks simulator CLI selection, formats, and file output.
- `integration/test_play_cli.py` checks the Phase 1 play session, renderer, menus, and script mode.
- `integration/test_research_cli.py` checks research CLI exports and input contracts.
- `integration/test_console_entrypoints.py` launches all three documented `python -m` commands as subprocesses.
- `integration/test_research_shell.py` and `integration/test_post_table_probe.py` check the evidence shell and non-canonical probes.

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
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_win_sequence.json
python -m game_att2_sim.research_cli `
  --session-id AUTO-SMOKE-001 `
  --evidence-class AUTOMATED_REGRESSION `
  --participant-code AUTO-SMOKE `
  --seed 42 `
  --script research/interactive_shell/example_action_sequence.json
```

Use scripted/fake RNG for branch-level unit tests and seeded RNG for reproducibility
integration tests. These commands validate deterministic implementation behavior; they
do not replace moderated human playtests or prove fun, readability, or balance.
