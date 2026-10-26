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

## Current sample-demo contract — 2026-09-08 second revision

**2026-10-26 paper update:** The owner answered Z01-Z10=A and delegated the
remaining option optimization. [The consolidated D0 plan](docs/planning/DEMO_D0_CONSOLIDATED_PLAN_2026-10-26.md)
records all 55 selections, four deliberate B exceptions, and the exact fixture,
device/resource, and terminal-proof work still to do. Earlier OPEN statements below
are historical where that plan and the living ledger explicitly supersede them.
The new-demo runtime is still absent and D0 is not closed.

```text
O1: wounded new person in Hell, immediate bodily need
-> S1: asymmetric NPC -> living/graft or kill/Blood maintenance route
-> human NPC, post-graft capability proof on graft route
-> Boneatour: skeletal minotaur, horn Charge stopped only by reflexive Parry
-> unstopped Charge: next Preparation/Main lost, defense retained
-> intended bodily death and demo ending (exact terminal rule OPEN)
```

This replaces the former gate-boss victory/escape objective. Exact loss mechanism,
Charge source/avoidance/status ordering, location, soul/body explanation and
retry/progression boundaries are OPEN. O1/S1 are selected; Guard is excluded from
the first demo. See the living decision ledger and
[execution plan](docs/planning/D0_EXECUTION_PLAN_2026-09-06.md).

The sample must teach bodily combat and create grounded anticipation for the full
game. Human interest and perceived fairness must be observed; documentation cannot
prove them. Approximately 30 minutes remains a soft reference. Runtime is not
implemented or authorized by this paper revision.

Core ownership remains body -> compatible Concept Deck -> Anatomical Deck ->
Brain/Attention. Ordinary play remains at most one Preparation and one Main.
Blood/limb reward exclusivity, source-based legality, and ordinary Yellow/Red defense
remain current. An exact novel boss exception needs its own reviewed causal contract.

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

The demo fight order, opening direction, camera, retry scope, and Concept/Brain
demo boundary now have selected paper directions. Continue with exact P01-P12
fixtures, two-route legality and the Q25 terminal counterexample proof in the
consolidated plan before treating D0 as closed or creating an engine runtime.

Owner response surface: [complete demo/general-layout questionnaire and technical filing](docs/planning/DEMO_FINALIZATION_QUESTIONNAIRE_2026-09-07.md).

Latest owner answers: [2026-09-08 response review and calibrated options](docs/planning/DEMO_ANSWER_REVIEW_2026-09-08.md).
Different person per attempt; pixel art family; inevitable boss bodily-death ending;
Panic Pulse/Limb for Life excluded; settings-only storage. The 2026-10-26 plan
selects first-demo camera, sequence, Concept/Brain and retry boundaries. Exact
mechanics, two-route/boss proof and production facts remain unfinished. No new-demo
runtime exists.
