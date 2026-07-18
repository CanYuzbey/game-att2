# Game att2 Project Assimilation and Governance Audit v0.1

## Repository state

Audit date: 2026-07-18. Initial branch `research/minotaur-designer-selfplay-v01`; initial/current accepted HEAD `7caf5c6` (`docs: record interim Minotaur self-play closeout`). Commit `7caf5c6` is present. The simulator (`6fb2bf8`), post-table probe (`26ab586`), Knockdown/Brace validation (`7b783a5`), Minotaur paper packet (`e772b76`), human-test operations (`1c0b3cd`), self-play protocol (`f306dd6`), and interim closeout (`7caf5c6`) form a linear integrated history. Initial worktree was clean. No Git remote is configured. Documentation work moved to `skills/systemic-causal-design-v01`; no merge was performed.

## Current stage and gates

The accepted simulator and seven scenarios exist; the closeout reports 63 passing tests. The project is in narrow simulator/paper-test validation, not production. Designer self-play stopped after `SELF-S02`. `SELF-S01` and `SELF-S02` are **CONTAMINATED DESIGNER DIAGNOSTICS**, not successful playtests. `SELF-S03` and `SELF-S04` were not started. Encounter 3 has a paper/runtime gap and remains blocked. Unity remains blocked.

## Source-of-truth hierarchy

| Document | Current version | Authority | Governs | Status | Known contradiction | Required action |
|---|---:|---|---|---|---|---|
| `AGENTS.md` | handoff v0.6 | 1, binding | Codex implementation and scope | Current | Forbids new enemies while later Warden paper work exists | Preserve runtime block; owner must amend before implementation |
| Owner systemic-causality decision (2026-07-18) | approved decision | Owner, above repository artifacts | Design reasoning and skill governance | Current | Existing script-first language does not enforce capability recomputation | Encode in dedicated skill and production gates; no mechanics inferred |
| `docs/02_DEVELOPMENT_MASTER_v0_6.md` | 0.6 | 2, product source | Current simulator product/rules scope | Current | Predates later validation and systemic decision | Retain; use newer decision record/supporting artifacts for status only |
| `docs/03_COMBAT_RULES_v0_4.md` | 0.4 | 3, binding mechanics | Exact approved combat behavior | Current | No general consequence/behavior layer | Do not invent one; systemic skill wraps only represented rules |
| `docs/04_SIMULATOR_TECHNICAL_SPEC_v0_2.md` | 0.2 | 4, implementation spec | Architecture/contracts | Current | Narrow encounter scripting can bypass broader causal review | Add governance requirement, not runtime scope |
| `config/*.yaml` | 0.1/0.4 | 5, tunables | Numeric/data values | Current | Warden is absent by design | Preserve absence |
| `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md` | 0.2 | 6, acceptance | Simulator tests/gates | Current | Does not require full state-capability trace | Production skill now adds that criterion for future changes |
| `docs/08_DECISIONS_RISKS_OPEN_QUESTIONS.md` | rolling v0.6 | owner decisions/log | Locked, reversible, open decisions | Current supporting decision log | Later Warden paper approval is lower than `AGENTS.md` runtime prohibition | Paper only; runtime blocked |
| Minotaur paper packet and walkthrough | 0.1 | approved temporary/supporting | Paper diagnostic setup/evidence | Supporting | Calls Warden canonical for paper only; has no defeat/incapacity model | Preserve as non-runtime diagnostic evidence |
| Human-test operations/protocol | 0.1 | supporting operations | Test facilitation | Supporting | Planned four sessions but owner stopped after two | Do not resume |
| Interim closeout and raw `SELF-S01/02` | 0.1 | historical evidence | Contaminated diagnostic record | Historical/current blocker evidence | Sessions violate facilitation/action assumptions | Preserve verbatim and classify contaminated |
| Simulator/review/probe/validation reports | 0.1 | generated/supporting evidence | Observations and implementation verification | Supporting/historical | Original simulator report retains stale 32 while current result is 25 | Consolidate later; do not rewrite history |
| Older condensed handoff and skill artifacts | not present | none | Referenced historical predecessors | Superseded or absent | Manifest and Master say earlier condensed artifacts were superseded; exact files absent | Record absence; do not hallucinate content |

Numeric config can override duplicated tunables but not mechanic meaning. Generated reports never become binding design by confidence or recency alone.

## Authoritative mechanics and deferred systems

Approved simulator mechanics include six body slots; separate Blood and limb integrity; Blood collapse/Panic/one soft-collapse valve; limb thresholds and acting-source impairment; clean-sever and harvest-quality gating; Focus before the main action; one Fast item; Plead Pressure and Jeff incapacity surrender; emergency grafting/Unstable; Anna stabilization/trade; table options; Downed/mandatory Stand and one encounter Brace charge. Exact details remain in higher-precedence sources.

Deferred: Warden runtime definitions, offensive target/defeat logic for Encounter 3, anatomy/organ penetration, generalized surrender/escape psychology, new limb attacks, generalized AI/physics/biology, Unity, rewards, progression, full debt, save/load, and production content.

## Skill audit findings

| Finding | File/section | Severity | Conflict | Smallest correction |
|---|---|---:|---|---|
| Encounter work is framed as explicit scripts with no mandatory post-mutation capability pass | `CODEX_TASK.md` Phase 4; Production Skill §§10,25 | P0 | A script may continue after its source or resources become invalid | Require the systemic causal skill at design/review/acceptance gates |
| Encounter 3 has no offensive target, incapacity, or meaningful objective response | Minotaur paper packet, Warden sheet | P0 | Four rounds continue independently of player-caused state | Keep packet diagnostic and runtime blocked; require bounded action/target owner decision |
| Integration and Repair options were mechanically inert in supplied baseline | Interim closeout Blocking Findings | P0 | Labels implied consequences unsupported by runtime state | Require start-state and capability matrices before another test |
| Main-action consumption is incomplete | Interim closeout | P0 | Affordances remain available after economy is spent | Keep implementation fix blocked pending approval; add trace acceptance requirement |
| Guard can persist past intended round | Interim closeout | P1 | State mutation/expiry is not reevaluated consistently | Future approved fix plus round-end regression test |
| Runtime Warden authority conflicts with binding scope | `AGENTS.md`; decisions/paper packet | P1 | Lower-precedence paper authority cannot add runtime enemy | Preserve explicit block until owner reconciles sources |
| Enemy scripts are endorsed as small/explicit without a legality-yield clause | `CODEX_TASK.md` Phase 4; Master §19 | P1 | “Inspectable” is insufficient if state cannot invalidate actions | Add script-yields-to-capability rule in new/governing skills |
| Stale standalone 32-Blood report conflicts with current 25 result | Simulator report; closeout | P1 | Decision evidence can be read without later correction | Publish consolidated report in a later approved runtime task |
| Resources and limb state exist, but acceptance does not universally trace capability loss | Test Plan and Production Skill | P2 | Systemic terminology could remain decorative | Add state/capability traceability to future acceptance |
| Systemic expansion could invite invented anatomy or universal AI | New owner examples versus current approved rules | P2 | Plausible simulation would silently canonize mechanics | Add explicit deferred/owner-decision protocol |
| Self-play protocol evidence labels were initially sound but execution deviated | Protocol versus raw sessions/closeout | P2 | Results cannot validate intended Focus or agency | Preserve as contaminated diagnostics only |
| Static manifest hashes become stale whenever governance files change | `MANIFEST.md` | P3 | Reviewers could mistake outdated package metadata for current integrity evidence | Refresh and validate every changed/new entry in this commit |

No P0/P1 governance finding is left silently active: the dedicated skill and production amendments cover future work; runtime defects and authority conflicts remain explicitly blocked rather than “fixed” without approval.

## Documentation corrections and blockers

- Add the systemic skill to the README reading order and production gate.
- Preserve 37 as historical paper evidence, 32 as stale historical report output, and 25 as current deterministic seed-42 output; none is a balance target.
- Do not resume or repair the two self-play sessions.
- Owner decisions still required: intended pre-table baseline; whether Encounter 3 is explicitly an endurance probe or receives a bounded target/response model; authoritative anatomy/organ rules if ever needed; Warden intent, surrender, escape, and irrational-resistance behavior; reconciliation of `AGENTS.md` before runtime work.
