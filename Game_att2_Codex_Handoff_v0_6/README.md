# Game att2 — Codex Development Handoff v0.6

Prepared for: Can Yüzbey  
Current stage: **Sprint 0.5 — Python Combat Loop Simulator**  
Gate status: **Paper mini-campaign passed for a narrow simulator; Unity remains blocked.**

## Start here

Codex must read these files in this order:

1. `AGENTS.md` — binding operating constraints.
2. `CODEX_TASK.md` — the implementation task to execute now.
3. `docs/01_PROJECT_STATE_HISTORY_VISION.md` — why the game exists and how the design evolved.
4. `docs/02_DEVELOPMENT_MASTER_v0_6.md` — current product source of truth.
5. `docs/03_COMBAT_RULES_v0_4.md` — exact mechanics to implement.
6. `docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md` — architecture and public contracts.
7. `docs/05_CONTENT_CATALOG_v0_1.md` and `config/*.yaml` — initial content and tunable values.
8. `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md` — required tests and gate criteria.
9. `docs/07_PAPER_TEST_EVIDENCE_v0_1.md` — evidence and limitations behind the rules.
10. `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md` — what is locked, provisional, or unresolved.
11. `docs/09_PRODUCTION_OPERATING_SKILL_v4_1_CODEX.md` — broader production workflow.
12. `docs/10_CODEX_RETURN_CONTRACT.md` — required completion report.

## Source precedence

When two files appear inconsistent, use this order:

1. `AGENTS.md`
2. `docs/02_DEVELOPMENT_MASTER_v0_6.md`
3. `docs/03_COMBAT_RULES_v0_4.md`
4. `docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md`
5. `config/*.yaml` for numeric/tunable data
6. `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`
7. remaining supporting documents

Do not silently resolve a product contradiction. Implement the least irreversible interpretation, document it in the completion report, and keep the value configurable.

## Immediate deliverable

A deterministic, typed, tested Python console simulator for:

`S-001 start → Jeff → bargain/harvest → emergency graft → Anna → stabilization/trade → grafting table → summary`

This is a **validation tool**, not the final game.

## Explicitly excluded

Unity, graphics, animation, map generation, save/load, meta progression, full dialogue, additional enemies, curses, rot, celestial systems, full debt economy, full deck/card systems, multiplayer, and store integration.
