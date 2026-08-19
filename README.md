# Game att2

Canonical repository: <https://github.com/CanYuzbey/game-att2>

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

The current simulator and default playable CLI cover the bounded sequence from
S-001 through Jeff, emergency grafting, Anna, and the Grafting Table. The older
Jeff-only diagnostic remains available as an explicit compatibility mode.

The bounded visual interaction lab is implemented and fidelity-verified, but the owner
deferred VL-WP4 and broader reflex-mechanics work on 2026-08-13 before diagnostic
execution. The fixture is preserved for later research; it is not the active gate.
The shared Stamina/readiness model remains a provisional research hypothesis; no
runtime Stamina system, production UI, content expansion, or engine work is approved.
The owner approved the complete aimed-wound design direction on 2026-08-13. Numeric
values, specific repair content, and runtime implementation remain deferred. The
action-produced Clinch/Engaged/Distant direction, neutral-settling cadence, and
Package C Resolution-Bound Range Tenure grammar, Package B Tiered Atomic
Commitments, and Package A Chosen Irrevocable Sacrifice are owner-approved on paper;
runtime remains unapproved. The active design gate is mental defeat, surrender, and
mercy.
The owner-approved identity guardrail requires space to support body-sourced tactical
cards, reflex execution, and lasting physical consequences. Clinch, Engaged, and
Distant are produced by action/defense/reflex outcomes rather than generic movement.
This does not approve runtime implementation, a full deck system, individual card
profiles, or brain progression.

> **Collaborator verification note — 2026-08-13:** `main` contains the verified
> visual interaction lab and the separate local Block-pressure demo. To review the
> current evidence, start with the implementation results linked below; to reproduce
> the automated checks, use the verification commands in the handoff package. These
> checks establish implementation fidelity only—not final game balance, player
> comprehension, or approval to begin production content.

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
- [Current documentation map](Game_att2_Codex_Handoff_v0_6/docs/README.md)
- [Development master](Game_att2_Codex_Handoff_v0_6/docs/02_DEVELOPMENT_MASTER_v0_6.md)
- [Combat rules](Game_att2_Codex_Handoff_v0_6/docs/03_COMBAT_RULES_v0_5.md)
- [Simulator technical specification](Game_att2_Codex_Handoff_v0_6/docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md)
- [Tests and acceptance criteria](Game_att2_Codex_Handoff_v0_6/docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md)
- [Current development lead brief](Game_att2_Codex_Handoff_v0_6/docs/24_CURRENT_DEVELOPMENT_LEAD_BRIEF_2026-08-12.md)
- [Visual interaction-lab record](Game_att2_Codex_Handoff_v0_6/docs/25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md)
- [Approved aimed-wound design direction](Game_att2_Codex_Handoff_v0_6/docs/27_AIMED_WOUND_SYSTEM_DIRECTION_AND_OWNER_REVIEW_v0_1.md)
- [Approved space-and-reach direction](Game_att2_Codex_Handoff_v0_6/docs/28_SPACE_AND_REACH_DIRECTION_AND_OWNER_REVIEW_v0_1.md)
- [Approved strategic card/action-economy direction](Game_att2_Codex_Handoff_v0_6/docs/29_STRATEGIC_CARD_ACTION_ECONOMY_OWNER_INTERVIEW_v0_1.md)
- [Wound/Blood/repair numeric owner-review package](Game_att2_Codex_Handoff_v0_6/docs/30_WOUND_BLOOD_REPAIR_NUMERIC_OWNER_REVIEW_v0_1.md)
- [Approved range-maintenance action grammar](Game_att2_Codex_Handoff_v0_6/docs/35_RANGE_MAINTENANCE_ACTION_GRAMMAR_OWNER_REVIEW_v0_1.md)
- [Repository and CLI readiness record](Game_att2_Codex_Handoff_v0_6/docs/archive/implementation_reports/13_REPOSITORY_CLI_READINESS_2026-07-30.md)
- [CLI/documentation alignment record](Game_att2_Codex_Handoff_v0_6/docs/archive/implementation_reports/15_CLI_DOCUMENTATION_ALIGNMENT_2026-07-31.md)
- [Full campaign CLI implementation report](Game_att2_Codex_Handoff_v0_6/docs/archive/implementation_reports/16_FULL_CAMPAIGN_PLAYABLE_CLI_2026-07-31.md)
- [Repository production skill](.agents/skills/game-att2-production/SKILL.md)

## Run the simulator

Python 3.11 or newer is required.

```powershell
cd Game_att2_Codex_Handoff_v0_6
python -m pip install -e ".[dev]"
python -m game_att2_sim --scenario mini_campaign --seed 42 --format text
```

Play the full approved campaign:

```powershell
python -m game_att2_sim.play_cli --seed 42
```

Use `--phase-1` for the retained S-001 vs Jeff diagnostic.

Run the verification suite:

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

The latest local verification is 261 passing tests, 87% source-only line coverage,
a clean Ruff run, and a clean strict mypy run across 32 source files. See the documentation map for current
evidence limits, known debt, and production gates, and
[the Phase 1 CLI report](Game_att2_Codex_Handoff_v0_6/docs/archive/implementation_reports/Game_att2_Playable_CLI_Phase1_Report_v0_1.md)
for that interface's scope lock and assumptions.
