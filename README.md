# Game att2

Game att2 is a single-player hell-loop limb-grafting roguelike concept built
around a simple fantasy: survive ritualized duels by turning damaged bodies
into the next version of your own.

> You are not collecting weapons. You are becoming the weapon, piece by piece,
> using your own blood as money.

## Project status

This repository is currently a **design-research project and deterministic
Python simulator**. It validates combat rules, timing, reproducibility, and the
body-as-build economy. It is not yet a production game, Unity project, playable
vertical slice, or proof that the design is fun.

The current simulator covers the bounded sequence from S-001 through Jeff,
emergency grafting, Anna, and the Grafting Table. An interactive research shell
records deterministic diagnostic sessions for the same sequence.

## Design pillars

- **Body as Build** - limbs create actions, passives, tradeoffs, and tactical
  identity.
- **Blood as Volatile Bankroll** - Blood is health, currency, and ability fuel.
- **Combat as Extraction** - winning includes deciding what to damage, preserve,
  harvest, graft, or sell.
- **Desperate Maintenance** - every acquired part creates stabilization,
  integration, preservation, or debt decisions.
- **Ritualized Readability** - costs, targets, outcomes, rewards, and new risks
  must remain inspectable.

## Repository guide

The active handoff package lives in
[`Game_att2_Codex_Handoff_v0_6`](Game_att2_Codex_Handoff_v0_6/).

- [Full project overview](Game_att2_Codex_Handoff_v0_6/README.md)
- [Current evidence-backed report](Game_att2_Codex_Handoff_v0_6/docs/12_CURRENT_PROJECT_REPORT_2026-07-23.md)
- [Development master](Game_att2_Codex_Handoff_v0_6/docs/02_DEVELOPMENT_MASTER_v0_6.md)
- [Combat rules](Game_att2_Codex_Handoff_v0_6/docs/03_COMBAT_RULES_v0_4.md)
- [Simulator technical specification](Game_att2_Codex_Handoff_v0_6/docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md)
- [Tests and acceptance criteria](Game_att2_Codex_Handoff_v0_6/docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md)

## Run the simulator

Python 3.11 or newer is required.

```powershell
cd Game_att2_Codex_Handoff_v0_6
python -m pip install -e ".[dev]"
python -m game_att2_sim --scenario mini_campaign --seed 42 --format text
```

Run the verification suite:

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

The latest recorded local verification is 91 passing tests, a clean Ruff run,
and a clean strict mypy run. See the linked project report for the current
evidence limits, known debt, and production gates.
