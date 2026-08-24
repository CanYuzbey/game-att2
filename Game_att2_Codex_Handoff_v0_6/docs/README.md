# Documentation Map

The repository separates the active playable-demo direction from the frozen legacy
simulator, protected engineering evidence, research, and history. A preserved file is
not automatically current product authority.

## Five living game-design documents

Read these for owner-led design work, in order:

| Document | Responsibility |
|---|---|
| `GAME_DIRECTOR_BRIEF.md` | Product intent, identity, experience hierarchy, pillars, and guardrails |
| `CORE_LOOP_ENCOUNTER_AND_RUN.md` | Active-play loop, encounter logic, same-day demo reset, and the explicitly open full-game run structure |
| `COMBAT_BODY_AND_BLOOD.md` | Consolidated body, Blood, wounds, defense, targeting, procedure, and survival paper rules |
| `DECK_BRAIN_AND_ACTIONS.md` | Anatomical deckbuilder ownership, action budget, inventory boundary, Brain doctrine, and open implementation details |
| `WORLD_PROGRESSION_AND_DECISIONS.md` | Narrative/progression direction, compact decision ledger, foundational open questions, scope locks, and current focus |

These five files are current paper game-design authority. They open D0 planning for a
bounded Underground City demo, but do not by themselves create an engine project or
change legacy runtime, configuration, tests, dependencies, or executable content.

## Active-demo AI operating contract

| Document | Role |
|---|---|
| `DEMO_MINIGAME_AI_WORKING_CONTRACT.md` | Operational truth/status rules, bounded mini-game target, work order, acceptance evidence, and anti-overclaiming return format for any AI-assisted contributor |

This is an operational contract, not a sixth living design authority. It summarizes
the living set for execution hygiene and cannot close an `OPEN` design choice.

## Concept-video communication plan

| Document | Role |
|---|---|
| `CONCEPT_VIDEO_PRODUCTION_PLAN.md` | Near-term concept/previsualization film purpose, truth boundary, beat sheet, production gates, program chain, file handoffs, review questions, and parallel playable-demo boundary |

This plan is a communication/production surface, not a sixth living design authority,
runtime approval, asset-existence claim, playable build, or investor-readiness proof.
Its scenes must inherit authority labels from the five living documents.

## Protected authority and engineering documents

| Document | Role |
|---|---|
| `02_DEVELOPMENT_MASTER_v0_6.md` | Product/simulator source of truth and dated governance amendments |
| `03_COMBAT_RULES_v0_5.md` | Current implemented simulator combat rules |
| `04_SIMULATOR_TECHNICAL_SPEC_v0_2.md` | Technical contracts |
| `05_CONTENT_CATALOG_v0_1.md` | Active simulator content summary |
| `06_TEST_PLAN_ACCEPTANCE_v0_2.md` | Acceptance and evidence gates |
| `07_PAPER_TEST_EVIDENCE_v0_1.md` | Paper evidence classification |
| `08_DECISIONS_RISKS_OPEN_QUESTIONS.md` | Protected runtime/project decision and risk history |
| `10_CODEX_RETURN_CONTRACT.md` | Completion-report contract |
| `11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md` | Causal design contract |

`AGENTS.md`, `.agents/skills/`, `config/`, `src/`, and `tests/` remain protected and
outside game-design consolidation.

## Preserved research and evidence

| Document/folder | Role |
|---|---|
| `../research/README.md` | Research navigation and active-versus-frozen classification |
| `20_H1_HYBRID_COMBAT_SPEC_v0_1.md` | Historical owner-approved H1 research contract |
| `21_H1_IMPLEMENTATION_RECORD_v0_1.md` | H1 implementation and evidence limits |
| `23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md` | Deferred reflex research direction |
| `25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md` | Visual-lab plan, fidelity result, and deferred gate |
| `encounter_3/` | Bounded paper-test packet; runtime remains blocked |
| `../research/defense_will_npc_balance_v0_1.md` | DWF-0.1 sourced Block/timing/Will/NPC comparison, exact paper calculator, and reject criteria; all values remain working hypotheses |

Research evidence cannot prove fun, accessibility, fairness, balance, or production
readiness and does not override the living design set.

## Historical design provenance

Former game-design documents 01, 17-19, 24, and 27-41 are preserved intact under
`archive/design_history_2026-08-21/`. Read them only for provenance, rejected
alternatives, exact provisional details, or earlier evidence. If they conflict with
the five living files, the living files win for paper design; documents 02-06 and
validated configuration still win for current simulator behavior.

Other archive categories remain evidence/history. See `archive/README.md`.

## Change rule

- Update a living design document instead of creating a new numbered design packet.
- Record a dated compact entry in `WORLD_PROGRESSION_AND_DECISIONS.md` when authority
  changes.
- Create a standalone research/evidence file only when it contains a real protocol,
  raw evidence, implementation record, or technical contract that does not belong in
  the living design surface.
- Never use documentation volume as a substitute for a player-facing decision or a
  bounded test.
