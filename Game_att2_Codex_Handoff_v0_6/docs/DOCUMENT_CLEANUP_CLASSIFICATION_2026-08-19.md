# Game att2 — Document Cleanup Classification

Date: 2026-08-19

Purpose: keep the handoff small enough to navigate without deleting current authority,
runtime contracts, executable evidence, or irreplaceable research records.

## Classification rules

| Class | Treatment |
|---|---|
| `KEEP-ACTIVE` | Current authority, navigation, runtime/config contract, open decision, or active gate |
| `KEEP-EVIDENCE` | Raw/structured evidence needed to audit a claim or contamination status |
| `MERGED` | Completed continuation documents reduced to one current record; Git retains detailed history |
| `ARCHIVE` | Superseded or completed material with decision/evidence value; not current authority |
| `DELETE` | Generated cache/output, empty placeholder, exact duplicate, or compatibility copy with no unique authority/evidence |

## Applied in this cleanup

### DELETE

- `09_PRODUCTION_OPERATING_SKILL_v4_1_CODEX.md`: compatibility entry point only. The
  canonical repository skill is `.agents/skills/game-att2-production/SKILL.md`, and
  `AGENTS.md` plus this documentation index already establish its use.
- `research/minotaur_sessions_template.csv`, `minotaur_rounds_template.csv`, and
  `minotaur_debrief_template.csv`: unreferenced legacy fixed-column templates. The
  active P01-P08 free-choice schema, validity/contamination handling, and analysis
  categories are owned by `docs/encounter_3/SESSION_RECORD_PACK_v0_1.md` and
  `ANALYSIS_TEMPLATE_v0_1.md`.
- root `director.md`: unreferenced convenience handoff whose authority order and
  operating method duplicate `AGENTS.md`, the handoff README, the repository skill,
  and current status documents. Its recorded active gate is also superseded by later
  owner decisions. Git history retains the original continuity record.

### MERGED

- `21_H1_IMPLEMENTATION_PLAN_v0_1.md` +
  `22_H1_IMPLEMENTATION_RESULTS_v0_1.md` ->
  `21_H1_IMPLEMENTATION_RECORD_v0_1.md`.
- `25_BOUNDED_VISUAL_INTERACTION_LAB_PLAN_v0_1.md` +
  `26_VISUAL_INTERACTION_LAB_IMPLEMENTATION_RESULTS_v0_1.md` ->
  `25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md`.

The consolidated records preserve the binding boundary, implementation surface,
traceable result, evidence limits, historical verification, and current gate. Detailed
execution chronology remains recoverable from Git.

### ARCHIVE

- root `Game_att2_Oyun_Gelistirme_Belgesi.pdf` ->
  `docs/archive/legacy_design/Game_att2_Oyun_Gelistirme_Belgesi.pdf`: preserved as a
  pre-Rules-v0.5 historical design artifact, not current authority.

## KEEP-ACTIVE groups

- Root: `README.md`, `AGENTS.md`, `pyproject.toml`, `.gitignore`, launchers and demo
  tooling.
- `docs/01` through `08`, `10`, `11`, and `17` through `20`.
- Consolidated records `21` and `25`, direction/status documents `23` and `24`, and
  owner-review packages `27` through `37`.
- `docs/encounter_3/` while Encounter 3 remains an approved paper-test packet.
- All `config/*.yaml`, `src/game_att2_sim/*.py`, `tests/**/*.py`, and checked-in
  deterministic examples.

## KEEP-EVIDENCE groups

- `research/interactive_shell/`, `research/h1/`, and `research/designer_selfplay/`.
- Encounter-session templates and the WNR arithmetic record.
- Scripted comparison inputs under `examples/`.

## ARCHIVE groups

- Everything under `docs/archive/`: superseded rules, completed results,
  implementation reports, governance provenance, and legacy Encounter 3 packets.
- Archive files are not active authority. They are retained because no file in this
  audit was proven to have zero decision, evidence, or contamination value.

## Generated/local-only DELETE policy

The following may be deleted whenever present because they are reproducible and
already ignored: `.venv/`, `node_modules/`, `__pycache__/`, `.pytest_cache/`,
`.mypy_cache/`, `.ruff_cache/`, coverage output, build/dist artifacts,
`*.egg-info/`, `reports/play_feedback/`, and `tmp/`.

No such generated directory was committed in the reviewed package.

## Deferred consolidation candidates

Documents `27` through `37` form a sequential paper-design package, but each carries
distinct owner decisions, failure paths, and deferred-runtime boundaries. They are
similar in format, not redundant in meaning. Merge them only when a new Development
Master version promotes their decisions into one authoritative combat specification.

The active/open-decision ledgers (`08`, `18`, `24`) overlap in status language but
serve different scopes. They should be reconciled during the next Development Master
version rather than mechanically merged now.
