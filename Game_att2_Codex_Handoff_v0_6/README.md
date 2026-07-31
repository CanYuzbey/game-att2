# Game att2

Canonical repository: <https://github.com/CanYuzbey/game-att2>

Game att2 is a single-player PC hell-loop limb-grafting roguelike/roguelite concept. The player survives ritualized turn-based duels by damaging, extracting, grafting, stabilizing, and integrating body parts while spending Blood as health, currency, and ability fuel.

> You are not collecting weapons. You are becoming the weapon, piece by piece, using your own blood as money.

This repository is currently a **design-research and deterministic Python simulator project**. It is not a production game, Unity project, playable vertical slice, or proof that the design is fun.

## Current status

Evidence baseline: **2026-07-23**. CLI/documentation alignment rechecked: **2026-07-31**.

- Current maturity: pre-production rules validation / simulator stage.
- Approved digital scope: the narrow Python simulator for S-001 → Jeff → emergency graft → Anna → Grafting Table.
- Simulator implementation gate: **passes with known technical and diagnostic debt**.
- Product evidence: **insufficient for a continue-to-production decision**.
- Encounter 3: approved only for bounded, moderated paper testing.
- Human Encounter 3 evidence: P01–P08 are still pending.
- Unity graybox: **blocked**.
- Latest local verification: **163 tests passed**, **87% line coverage**, Ruff passed, and strict mypy passed.
- Deterministic regression: `mini_campaign`, seed `42`, ends at **25 Blood** with an Integrated Grafted Human Right Arm.
- Interactive Research Shell v0.1: implemented and owner-diagnostic verified on the
  same narrow sequence; no external-pilot evidence exists yet.
- Playable CLI: the default interface now covers **S-001 → Jeff → emergency graft
  → Anna → Grafting Table**. The Jeff-only Phase 1 diagnostic remains behind
  `--phase-1`. No valid external human-play evidence exists yet.

The historical paper result of 37 Blood is preserved as evidence but is not an automated target. Its arithmetic includes an unconfigured spare-arm sale. The current 25-Blood result follows the configured costs and seeded events. Neither number is an approved balance target.

For the full evidence-backed assessment, known defects, risks, timeline, and questions, read [docs/12_CURRENT_PROJECT_REPORT_2026-07-23.md](docs/12_CURRENT_PROJECT_REPORT_2026-07-23.md).

## Vision and player fantasy

The project is built around a contained horror loop:

```text
I wake up broken.
I fight other broken things.
I cut away what I need.
I graft it onto myself.
I become something that can survive the loop.
```

The atmosphere takes inspiration from the ritual tension, oppressive intimacy, minimalist brutality, and high-stakes readability associated with *Buckshot Roulette*. It is not intended as a mechanical copy. Game att2’s identity is **body reconstruction as buildcraft**.

The intended high-level loop is:

```text
wake damaged
→ duel
→ spend, lose, or gain Blood
→ damage, disable, or sever limbs
→ harvest, graft, sell, preserve, or refuse parts
→ carry a changed body into the next pressure
→ stabilize or specialize at the table
→ eventually fail and wake again
```

## Design pillars

1. **Body as Build** — important limbs create actions, passives, tradeoffs, economy interactions, or tactical identity.
2. **Blood as Volatile Bankroll** — Blood is survival, purchasing power, and action fuel; spending should feel rational but dangerous.
3. **Combat as Extraction** — success is not only reducing health; it is deciding what to take, how cleanly, and at what cost.
4. **Desperate Maintenance** — acquired body parts create new stabilization, repair, integration, preservation, or debt decisions.
5. **Ritualized Readability** — every major action should make its target, cost, result, reward, and new risk inspectable.

## What the simulator covers

The simulator validates rules, timing, reproducibility, and numerical behavior for:

- six body slots: Head, Torso, Left Arm, Right Arm, Legs, and Core;
- Blood spending, gaining, Panic Pulse, collapse, and one tutorial soft-collapse valve;
- limb integrity, state transitions, tags, and acting-limb impairment;
- basic attacks that can disable or ruin but cannot independently create premium Clean Harvest;
- Clean, Stressed, and Ruined harvest quality;
- Focus before the main action and at most one Fast item per round;
- Jeff’s Plead Pressure and special combat-incapacity surrender;
- emergency grafting, stability rolls, and Unstable v0.4;
- Anna’s stabilization/trade path and greed path;
- Grafting Table v0.2;
- structured event logs, seeded runs, scenario metrics, and batch diagnostics;
- a non-canonical post-table consequence probe;
- owner-approved Downed, Stand, and automatic Brace behavior.

The simulator is a validation tool. Its strategies are test drivers, not models of real player behavior.

## What is explicitly out of scope

The current repository does not approve:

- Unity or another final engine;
- graphics, animation, final UI, audio, or final art;
- save/load, meta progression, a run map, or procedural generation;
- multiplayer, platform/store work, or release planning;
- a large inventory, full card/deck system, full debt economy, or dialogue framework;
- additional runtime enemies, including the Encounter 3 Warden;
- Warden rewards, harvest, anatomy, organs, death, surrender, bargaining, escape, or personality;
- claims of fun, accessibility, market demand, or balance from simulator output.

Paper-test approval is not runtime implementation approval.

## Repository map

```text
AGENTS.md                         Binding project rules
CODEX_TASK.md                     Original simulator implementation brief
config/                           Authoritative tunable simulator data
docs/                             Product, rules, technical, test, and status documents
src/game_att2_sim/                Python simulator package
tests/                            Unit and integration tests
research/                         Paper/self-play records and blank test templates
Game_att2_*Results*.md            Generated or reviewed evidence artifacts
Game_att2_Encounter_3_*.md        Paper-only Encounter 3 materials
pyproject.toml                    Package and development-tool configuration
```

Important code boundaries:

- `models.py` separates mutable runtime state from definitions.
- `config_loader.py` loads and validates YAML.
- `rng.py` centralizes seeded and scripted randomness.
- `rules.py` owns Blood, limbs, actions, harvesting, grafting, conditions, and table rules.
- `scenarios.py` owns the approved scenario drivers and strategy batches.
- `events.py` and `reporting.py` keep domain logic separate from output rendering.
- `probe.py` contains explicitly non-canonical validation probes.
- `research_shell.py` presents state-derived choices and records research evidence
  while leaving rule authority in `rules.py`.
- `research_cli.py` runs interactive sessions and deterministic scripted replays.
- `play_session.py` drives the Faz 1 playable Jeff encounter and turns the event
  stream into the five-question readability record; it never prints.
- `campaign_play.py` presents the full approved sequence over the existing research
  state machine and rule engine; it does not create a parallel rules layer.
- `play_render.py` renders the ASCII state tables, menus, and readability blocks.
- `play_cli.py` selects full-campaign or retained Phase 1 presentation and owns
  optional, consented local feedback collection.
- `play_feedback.py` writes versioned anonymous gameplay/answer records without raw
  terminal transcripts or automatic upload.

## Required reading order

Anyone changing rules, simulator behavior, tests, or project status must read these files in order:

1. `AGENTS.md`
2. `CODEX_TASK.md`
3. `docs/01_PROJECT_STATE_HISTORY_VISION.md`
4. `docs/02_DEVELOPMENT_MASTER_v0_6.md`
5. `docs/03_COMBAT_RULES_v0_4.md`
6. `docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md`
7. `docs/05_CONTENT_CATALOG_v0_1.md` and `config/*.yaml`
8. `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`
9. `docs/07_PAPER_TEST_EVIDENCE_v0_1.md`
10. `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md`
11. `docs/09_PRODUCTION_OPERATING_SKILL_v4_1_CODEX.md`
12. `docs/10_CODEX_RETURN_CONTRACT.md`
13. `docs/11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md`
14. `Game_att2_Encounter_3_Owner_Decision_Reconciliation_v0_1.md`
15. `Game_att2_Encounter_3_Bounded_Causal_Paper_Spec_v0_2.md`
16. `Game_att2_Encounter_3_Participant_Cards_v0_2.md`
17. `Game_att2_Encounter_3_Facilitator_Policy_Cards_v0_1.md`
18. `Game_att2_Encounter_3_Session_Record_Pack_v0_1.md`
19. `docs/12_CURRENT_PROJECT_REPORT_2026-07-23.md`

When sources conflict, use this precedence:

```text
AGENTS.md
→ Development Master v0.6
→ Combat Rules v0.4
→ Simulator Technical Spec v0.2
→ config/*.yaml for tunable values
→ Test Plan / Acceptance
→ supporting evidence and historical documents
```

Do not silently resolve a product contradiction. Use the smallest reversible technical interpretation only when it does not change the product experience; otherwise record an owner question.

## Systemic causal rule

Meaningful actions must follow this trace:

```text
validate action and source
→ resolve approved rule and injected randomness
→ mutate explicit state
→ recompute capabilities and legal affordances
→ evaluate forced consequences
→ choose among remaining legal responses
→ determine whether the encounter can meaningfully continue
→ log the evidence
```

Scripts may express preferences among legal actions. They may not restore destroyed sources, waive costs, preserve a planned scene, or directly teleport to an ending.

## Setup

Requirements:

- Python 3.11 or newer;
- PyYAML 6 or newer;
- optional development tools: pytest, pytest-cov, Ruff, and mypy.

From the repository directory:

```powershell
python -m pip install -e ".[dev]"
```

No runtime UI or engine dependency is required.

## Run the simulator

```powershell
python -m game_att2_sim --scenario jeff_baseline --seed 42
python -m game_att2_sim --scenario mini_campaign --seed 42 --format text
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim --batch 100 --strategy balanced --seed 42 --format json
```

Installed console-script equivalent:

```powershell
game-att2-sim --scenario mini_campaign --seed 42 --format text
```

## Run the playable CLI

The default human-playable loop covers **S-001 → Jeff → emergency graft → Anna →
Grafting Table**. It exposes costs, disabled reasons, body state, visible intent,
causal source hints, and the five Pillar 5 readability questions after each action.

```powershell
python -m game_att2_sim.play_cli --seed 42
python -m game_att2_sim.play_cli --seed 42 --transcript-output reports/play-001.txt
```

The post-play questionnaire is opt-in, stays local, separates research and model
training consent, and can be disabled with `--no-feedback`. Its default output is
ignored under `reports/play_feedback/`.

For a deterministic non-interactive replay, pass a JSON list of action ids:

```powershell
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
```

The retained Jeff-only diagnostic is explicit:

```powershell
python -m game_att2_sim.play_cli --phase-1 --seed 42
python -m game_att2_sim.play_cli --phase-1 --seed 42 --script examples/play_cli_win_sequence.json
```

Current scope and blocked identity decisions are recorded in
`docs/15_CLI_DOCUMENTATION_ALIGNMENT_2026-07-31.md` and
`docs/16_FULL_CAMPAIGN_PLAYABLE_CLI_2026-07-31.md`. The older Phase 1 report remains
a historical record of that compatibility interface.

## Run Interactive Research Shell v0.1

The shell is limited to S-001 -> Jeff -> emergency graft -> Anna -> Grafting Table.
It shows legal and disabled actions with reasons, asks before irreversible commitment,
and writes a machine-readable trace plus a human summary.

```powershell
python -m game_att2_sim.research_cli `
  --session-id OWNER-DIAG-002 `
  --evidence-class OWNER_DIAGNOSTIC `
  --participant-code OWNER-002 `
  --seed 42 `
  --json-output research/interactive_shell/OWNER-DIAG-002.json `
  --summary-output research/interactive_shell/OWNER-DIAG-002-summary.md `
  --transcript-output research/interactive_shell/OWNER-DIAG-002-transcript.txt
```

Use `EXTERNAL_PILOT` only for a genuinely external participant and
`AUTOMATED_REGRESSION` only for scripted automation. The retained implementation
report and owner-diagnostic evidence are in
`Game_att2_Interactive_Research_Shell_Report_v0_1.md` and
`research/interactive_shell/`.

Supported formats are text, JSON, and Markdown. Use `--verbose` for detailed events and `--output PATH` to save output.

The seven approved scenario names are:

- `jeff_baseline`
- `jeff_no_spend`
- `failed_hell_saw`
- `anna_stabilization`
- `anna_greed`
- `mini_campaign`
- `blood_bag_balance`

`post_table_probe` is a separate `NON_CANONICAL_VALIDATION_ONLY` diagnostic and must not be presented as a new encounter or production content.

## Verify the project

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
```

Current verification on 2026-07-31:

```text
pytest: 163 passed
coverage: 87%
ruff: all checks passed
mypy: success, no issues in 22 source files
mini_campaign seed 42: completed, 25 Blood
```

The repository identity, CLI roles, current smoke commands, and readiness limits are
recorded in [docs/13_REPOSITORY_CLI_READINESS_2026-07-30.md](docs/13_REPOSITORY_CLI_READINESS_2026-07-30.md).

## Evidence status

Confirmed:

- the simulator package runs deterministically;
- the seven approved scenarios execute;
- no-spend Grip Strike paths do not create premium Clean Harvest;
- body acquisition changes later legal actions;
- seeded event logs expose Blood and limb-state changes;
- conditional post-table effects are observable in non-canonical probes;
- Downed, Stand, and Brace are implemented and tested.

Not confirmed:

- that the game is fun or understandable to outside players;
- that repeated runs remain varied;
- that Blood values are balanced;
- that Blood Bag timing is healthy in representative play;
- that Anna’s trade and greed paths are equally attractive;
- that all table choices are competitive in a real encounter;
- that Encounter 3 is ready for runtime implementation;
- that Unity is the correct engine or the next development step.

## Known issues and blockers

The automated suite passes, but passing tests do not erase known gaps:

- **P1 — Encounter 3 evidence:** P01–P08 human sessions have not run; the completed designer sessions are contaminated diagnostics.
- **P1 — product gate:** simulator evidence does not establish fun, balance, or readiness for Unity.
- **P2 — player evidence:** the interactive shell has owner-diagnostic and automated
  coverage, but no valid external-pilot session.
- **P1 — unresolved identity rules:** Jeff's direct Blood threat, the consequence of
  a Ruined player torso, `Cover It` protection, and the conflicting Brace definitions
  require owner decisions and are not invented by the CLI.
- **Documentation age:** several historical files describe “simulator pending” or superseded outputs. Use the current report and review-gate documents to interpret them.

The 2026-07-23 causal-integrity correction resolved centralized Main-action consumption and round-end Guard expiry. The current authoritative implementation evidence is `Game_att2_Combat_Simulator_Results_v0_2.md`.

## Project timeline

Known Git history:

| Date | Milestone |
|---|---|
| 2026-07-16 19:07 +03:00 | Combat-loop simulator review gate added |
| 2026-07-16 19:41 +03:00 | Non-canonical post-table consequence probe added |
| 2026-07-17 12:17 +03:00 | Knockdown and Brace validated |
| 2026-07-17 12:28 +03:00 | Minotaur Warden paper encounter materials added |
| 2026-07-17 12:35 +03:00 | Human-test operations added |
| 2026-07-18 14:59 +03:00 | Designer self-play protocol added |
| 2026-07-18 16:24 +03:00 | Interim self-play closeout recorded |
| 2026-07-18 19:37 +03:00 | Systemic causal design skill added |
| 2026-07-18 20:11 +03:00 | Encounter 3 paper requirements reconciled |
| 2026-07-23 | Repository re-audited; current project report and README consolidated |

These timestamps are repository events, not complete labor-hour records. No authoritative person-hour log exists in the files.

## Recommended next step

The evidence-backed recommendation is:

1. review the new authoritative simulator results artifact;
2. obtain owner answers to the remaining consolidated questions in the current project report;
3. conduct eight valid P01–P08 moderated human paper sessions;
4. review evidence before approving any Encounter 3 runtime work or Unity proposal.

Do not begin Unity, add the Warden to runtime configuration, or expand production content from the current evidence.

## Ownership

Can Yüzbey owns identity-level, creative, product, and major technical decisions. Reversible implementation details may be resolved within the binding repository rules. Identity-defining ambiguity must be raised rather than hidden in code, configuration, tests, or narrative.
