# Game att2 — CLI / Documentation Alignment Work Record

> **ARCHIVED IMPLEMENTATION REPORT.** Preserved as delivery evidence; it is not
> a current rule or operating instruction.

Status date: 2026-07-31

Branch: `codex/cli-documentation-alignment`

## Goal and scope

Bring the human-playable CLI into conformance with the currently approved digital
prototype scope:

```text
S-001 -> Jeff -> harvest -> emergency graft -> Anna -> Grafting Table
```

This work does not authorize Encounter 3 runtime content, Unity, production UI,
additional enemies, final balance, or an invented anatomy/death model.

## Source precedence

Implementation uses the repository precedence without silently resolving product
contradictions:

```text
AGENTS.md
-> Development Master v0.6
-> Combat Rules v0.4
-> Simulator Technical Spec v0.2
-> config/*.yaml for tunable values
-> Test Plan / Acceptance
-> supporting evidence and historical documents
```

## Chain of proof

| Work item | Requirement / decision | Implementation boundary | Acceptance test | Status |
|---|---|---|---|---|
| Exact enemy-intent revalidation | Systemic Causal Skill steps 4–7; RQ-004 | Encounter drivers retain and revalidate the declared source | Destroyed declared source cancels; no same-phase replacement | Ready |
| Marked Jeff-arm response | Combat Rules §8 and §14; Development Master Jeff v0.4 | Jeff may aggressively use a usable Marked arm; no invented protection value | Next intent uses the usable Marked arm | Ready |
| Full playable campaign | RQ-007–013; S6 | Player-facing orchestration over existing RuleEngine rules | Jeff -> graft -> Anna -> table completes by free choice | Ready by owner directive |
| Player-facing causal affordances | Pillar 5; Production Skill §17 | Renderer only; no rule mutation | Source, cost, target, consequence and disabled reason visible | Ready |
| Playtest evidence capture | RQ-014–015 | Versioned local evidence; no gameplay authority | Consent and version fields preserved | Ready |
| General motivation model | 2026-07-31 owner decision | Data-defined actor motivations guide legal response scoring | Jeff intent records motivation and responds to assets/body state | Ready as survey prototype |
| Multiple state-derived victory routes | 2026-07-31 owner decision; systemic causal rule | Predicates evaluate mutated state separately for each actor | Bargain permits mutual success; incapacity/surrender remain distinct routes | Ready as survey prototype |
| Jeff behavior variety | Survey-test need | Legal intent candidates use configured scores and exact-repeat penalty | Target changes when repetition penalty changes ranking | Ready as survey prototype |
| Natural Jeff bargain | 2026-07-31 owner decision | Existing marked limb and inventory asset enable or disable exchange | Accept transfers assets; hostile action rejects and escalates | Ready as survey prototype |
| Jeff Blood threat | D-011 and active Blood-economy risk | Requires a new approved damage/Bleeding/torso consequence rule | Collapse route is state-derived and deterministic | BLOCKED — owner decision |
| Ruined player torso consequence | Undefined physical-viability rule | Cannot be inferred from generic limb state | Explicit consequence and recovery path tested | BLOCKED — owner decision |
| `Cover It` protection effect | Jeff content lists the action but no effect magnitude/duration | Cannot invent reduction, redirection, or charge | Configured effect is visible and testable | BLOCKED — owner decision |
| Brace authority reconciliation | Development Master/config permit manual Weak-Legs Brace; Combat Rules and 2026-07-18 decision specify automatic Braced-Legs Brace | Product meaning differs | One model remains in docs/config/code/tests | BLOCKED — owner decision |

## Scrum execution order

1. Correct declared-intent source revalidation and Marked-arm use response.
2. Reuse the existing full-sequence research state machine for the player-facing
   campaign instead of creating a second rule engine.
3. Add contextual, causal presentation and versioned feedback evidence.
4. Add contract, integration, deterministic replay, and CLI subprocess tests.
5. Update current documentation and regenerate verification evidence.
6. Hold the Blood lethality, torso viability, `Cover It`, and Brace changes behind
   explicit owner decisions.

## Definition of done

- Every implemented behavior maps to an approved source and an automated test.
- The declared enemy intent cannot migrate to a different source after player
  mutation.
- The player-facing path reaches every approved campaign phase without duplicating
  RuleEngine rules.
- Costs, targets, state changes, new capabilities, disabled reasons, and endings are
  inspectable.
- Same seed and action sequence reproduce the same gameplay events.
- All existing scenarios and evidence labels remain valid.
- P0/P1 hostile-review findings are resolved or explicitly blocked by an owner
  decision.

## Implemented result

- Default `game_att2_sim.play_cli` now traverses the full approved sequence.
- `--phase-1` retains the former Jeff-only interface without making it the default.
- Declared enemy action sources are retained and revalidated at resolution; a
  destroyed source cancels instead of migrating to another limb.
- A usable Marked Jeff arm is selected for aggressive use on the next declared
  action, which is one of the two responses already allowed by Combat Rules v0.4.
- Target lists identify causal enemy-action sources and warn when Brace or Hell Saw
  has no meaningful current payoff.
- Optional feedback is local, versioned, opt-in, non-overwriting, transcript-free,
  and labeled `UNCLASSIFIED_HUMAN_PLAY` with independence unverified.
- The campaign questionnaire measures inferred enemy motivation, perceived victory
  routes, and whether resolution felt natural. The retained Phase 1 questionnaire is
  unchanged so the two evidence sets are not mixed.
- Verification: 181 tests passed; total line coverage 87%; Ruff and strict mypy pass.

The four blocked items in the table remain intentionally unchanged.
