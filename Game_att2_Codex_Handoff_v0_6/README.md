# Game att2 — Codex handoff

This package has two deliberately separate responsibilities:

1. define the paper contract for a bounded Underground City sample demo; and
2. preserve the deterministic Python simulator and isolated research fixtures as
   legacy evidence.

The Underground City mini-game is **documented, not implemented**. No engine project,
runtime content, production UI, or playable new-demo build exists in this package.

## Read in this order

1. `AGENTS.md` — binding repository and evidence rules.
2. `docs/DEMO_MINIGAME_AI_WORKING_CONTRACT.md` — active demo scope and claim contract.
3. `docs/README.md` — the five living design documents and authority map.
4. `research/README.md` — current paper research versus frozen research evidence.

Do not start with the numbered legacy simulator documents or `docs/archive/` for new
game-design work.

## Current sample-demo contract

The current paper direction is:

```text
captive Guard offer
-> accept one disclosed, unfavorable concession to buy freedom
-> weaker but playable release
-> one small Underground City section
-> pre-boss limb fight A
-> kill for Blood OR living surrender for an agreed limb
-> Grafting Table consequence
-> optional pre-boss fight B carries that consequence into ordinary combat
-> gate boss integrates the already-taught combat rules
-> defeat opens escape, or death causes same-day reset
```

This is a proof floor, not a fixed encounter count, content ceiling, or duration
requirement. Approximately 30 minutes is only a soft planning reference until real
sample sessions produce observed durations. The intended artifact is for owner
self-play and informal friend play, helping decide whether the combat merits further
full-time development or investor pursuit. Such a convenience sample cannot establish
general fun, retention, market demand, or investor readiness.

Combat currently separates these resources and outcomes:

- `Mana`: renewable card/turn effort whose capacity grows by round;
- `Blood`: life, economy, and selected ability fuel; active-demo encounter Blood is
  earned by killing;
- `Will`: bilateral surrender pressure, reduced by successful Parry and explicit
  goal-critical shocks in the current comparison model;
- Yellow defense: Block or precise Parry;
- Red defense: Evade;
- kill: Blood, no limb opportunity from that opponent for the day;
- living surrender: agreed limb, no kill-Blood.

NPC purpose is authored as:

```text
Faction doctrine -> current role/duty -> individual Goal/Need/RedLine/Claim
```

Capability and risk tolerance are separate from purpose. An actor may seek Blood, a
specific function, custody/compliance, a bounty, trade, escape, or `NoClaim`.

These are paper rules or working hypotheses as labeled in the living documents; they
are not runtime claims.

## Repository map

| Path | Purpose | Status |
|---|---|---|
| `docs/` | Living design, active operating contract, protected simulator authority, and bounded paper packets | Start at `docs/README.md` |
| `research/` | DWF/WNR paper models plus isolated H1 and visual-lab evidence | Start at `research/README.md` |
| `src/game_att2_sim/` | Deterministic Python simulator and research CLIs | Frozen legacy evidence |
| `config/` | Simulator and research-fixture configuration | Frozen legacy evidence |
| `tests/` | Unit/integration evidence for the Python artifacts | Protected verification surface |
| `examples/` | Deterministic replay fixtures | Protected verification inputs |
| `docs/archive/` | Superseded design, reports, and provenance | Historical evidence; not active authority |
| `docs/encounter_3/` | Approved bounded paper-research packet | Paper-only; no runtime gate |

Why is the Python code still here? Its modules, configuration discovery, tests, H1,
visual lab, and replay fixtures are coupled deterministic evidence. Moving or deleting
individual pieces would make old claims harder to verify. It remains frozen and
isolated by status rather than presented as the new game.

## Current paper research

Run the deterministic defense/Will comparison with Python 3.11+:

```powershell
python research/defense_will_npc_balance_v0_1_model.py
```

The model checks the provisional Block matrix, exact Will pacing distribution, and
both weaker-but-playable Guard release branches. It cannot prove fun, fairness,
comprehension, accessibility, or final balance.

## Verify the frozen Python evidence

Install development tools from this directory:

```powershell
python -m pip install -e ".[dev]"
```

Run the complete automated gate:

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

Run deterministic smoke paths:

```powershell
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
python -m game_att2_sim.h1_cli --all-comparisons --script examples/h1_scripted_comparisons.json --format json
python -m game_att2_sim.visual_lab_cli --script examples/visual_lab_scripted_comparisons.json --all-comparisons --format json
```

Passing these commands verifies only the named legacy/research artifacts. It does not
prove that the Underground City mini-game exists or is playable.

## Current owner decisions still open

- promote, revise, or reject the exact `G1` Guard payment/released-state package;
- choose enforced disclosed claim versus one lethal `Defy` at player Will zero;
- set Mana cadence, card costs, defense inputs/windows, Block loss, and Will values;
- choose one versus two pre-boss limb fights and assign each a unique proof question;
- define their actors, one exact graft consequence, Memory/Brain persistence details,
  and the gate boss's integrated-combat test;
- explicitly open an implementation gate before creating any engine/runtime project.
