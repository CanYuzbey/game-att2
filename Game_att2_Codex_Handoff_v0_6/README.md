# Game att2 — Codex handoff

This package defines the selected two-NPC/Boneatour sample on paper and preserves
the deterministic Python simulator and isolated research fixtures as legacy evidence.

**2026-09-15: the selected open-bone-landscape demo is documented, not implemented.**
The owner Z01–Z55 answers supersede the earlier Underground City/Guard/escape
comparison for this demo. Z48/A exact tables and isolated route/termination arithmetic
exist; no new engine project, runtime, production assets or playable build does.

## Read in this order

1. AGENTS.md — binding scope and evidence rules.
2. [AI working contract](docs/DEMO_MINIGAME_AI_WORKING_CONTRACT.md).
3. [Documentation map](docs/README.md) and the five living documents in its order.
4. [Research map](research/README.md) — paper arithmetic versus frozen fixtures.

Start with current living design, not numbered simulator docs or archived packets.

## Current selected paper chain

Injured freely controllable person -> asymmetric NPC Rusk ->
kill for bowl Blood OR living clamp bargain -> table/Grip study ->
human Mara tests body change -> Boneatour/real horn change ->
finite-resource bodily death -> retry with another authored person.

Four main areas and one optional non-combat story pocket. Two NPC fights,
Preparation/Main and Attention8/4, D2 preselected timed defense, body-source and
target legality, bilateral90Will, one counteroffer/Defy, finite item/activation costs,
kill30Blood vs living limb/zeroBlood, and session Concept/fixed Brain are declared
in the five living files. No growing Mana, captive Guard or Memory-death print is
in this fixture.

The graft/no-kill favorable budget witness reaches the boss at48Blood/empty bowl;
two kills reach80Blood plus32bowl. All player structural damage is bounded by
560 even with140total initial+eligible Blood; each lethal boss vital starts600.
These numbers are paper arithmetic, not fun/fairness/real-input evidence.
Approx30minutes is a soft reference; real durations must be observed.

The engine choice is Godot4/Compatibility; the exact paper vehicle pin and checked
official source are in [World P12](docs/WORLD_PROGRESSION_AND_DECISIONS.md).
No download/install/export occurred. M01–M03 device/capacity/asset/voice facts and
all engine/build/input/human acceptance remain open. AGENTS requires a separate
explicit implementation gate.

## Verify only the paper arithmetic

~~~powershell
python research/z_fixture_2026_09_15_arithmetic.py --report research/z_fixture_2026_09_15_evidence.md
~~~

[Evidence report](research/z_fixture_2026_09_15_evidence.md) states its fixed witness
assumptions, conserved budgets, limits and unsafe counterexamples. It is not a
runnable game, complete event model or playable combat claim.

## Repository map

| Path | Role |
|---|---|
| docs/ | Five living paper authorities, operating/video contracts, protected legacy rules and archives |
| docs/v3/ | Preserved 2026-09-04 V3 specification mirror, questionnaire and isolated V3-1 sandbox contracts (not current Z01–Z55 demo authority) |
| research/ | Z paper arithmetic, Brain/card diagnostics and superseded comparisons; frozen H1/visual fixtures |
| src/game_att2_sim/ | Frozen deterministic legacy simulator/research CLIs |
| src/game_att2_v3/, tests/v3/ | Preserved deterministic V3-1 isolated combat/Attention sandbox and unit tests |
| config/, tests/, examples/ | Protected legacy definitions, verification and replay inputs |
| docs/archive/ | Historical evidence including pre-Z living snapshots and original questionnaire |
| docs/encounter_3/ | Paper-only packet; no runtime gate |

Old Guard/Avcı/grafted-Legs/Mana YAML and paper runner are superseded research, not
this sample's content or engine foundation. No legacy executable tree is deleted.

## Verify frozen legacy evidence only when requested

Install development tools from this directory:

~~~powershell
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
python -m game_att2_sim.h1_cli --all-comparisons --script examples/h1_scripted_comparisons.json --format json
python -m game_att2_sim.visual_lab_cli --script examples/visual_lab_scripted_comparisons.json --all-comparisons --format json
~~~

These commands were not run for this paper task and cannot verify the new demo.
