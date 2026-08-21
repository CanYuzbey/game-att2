# Game att2 - Current System Comparison and Collision Audit

Status date: 2026-08-21

Status: **OWNER-DELEGATED REPOSITORY AND PAPER-DESIGN RECONCILIATION; NO RUNTIME,
CONFIGURATION, CONTENT, VALUE, ENGINE, OR EXPERIENCE APPROVAL**

> **Later owner amendment (2026-08-21):** Document 41 supersedes INT-002 and every
> conclusion that makes Brain configuration the author of weighted card access or
> excludes a player-authored active deck. This audit remains the history of the
> earlier reconciliation; document 41 is the current Brain doctrine.

## 1. Purpose and authority

This document compares the current simulator, owner-approved paper packages, the
Director's Choice working record, and the Brain Module as one project. It records
where they agree, where they operate at different maturity levels, and how collisions
are resolved.

It is a navigation and reconciliation authority, not a replacement for detailed
contracts. Source precedence remains:

```text
AGENTS.md
-> Development Master plus dated owner amendments
-> Combat Rules v0.5 for current runtime
-> Simulator Technical Spec
-> validated YAML for current tunables
-> test and evidence records
-> working hypotheses and history
```

When this audit says `DEFERRED`, that is the answer: logic or simulator output cannot
safely decide the item without content, human evidence, or another owner gate.

## 2. Whole-project comparison

| Aspect | Current simulator | Approved paper direction | Working or deferred layer | Reconciled result |
|---|---|---|---|---|
| Product identity | Narrow deterministic combat/graft simulator | Body as Build; Blood as life/currency/fuel; hybrid strategic/reflex combat | Bounded weekend product and anatomical-deckbuilder language remain working positioning | Paper systems must strengthen body reconstruction; simulator fidelity is not product proof. |
| Body and capability | Six body slots with explicit limb states and acting-source impairment | Source-First profiles, exact source commitments, wounds, repair, extraction, grafting | Final body roster and Head/Brain fiction deferred | Body state exclusively decides which physical capabilities exist. |
| Blood | Runtime health/currency/fuel with Panic Pulse and Blood-0 consequences | WNR-0.1 values, procedure payment, sacrifice, and Brain redraw cost families | Final balance and Brain redraw cost deferred | Every Blood use follows one shared transaction and consequence chain; no parallel Brain currency. |
| Wounds and structural loss | Current integrity/state model; full wound package not implemented | Four wound families, treatment states, Ruined-Torso deadline, atomic procedures | Final values and content deferred | Brain selection cannot conceal, restore, or bypass source loss. |
| Voluntary action budget | Focus, optional Fast item, Main in the existing runtime | Future staged turn: zero/one Preparation, zero/one Main | Migration from runtime Fast timing is unapproved | Paper Brain/cards use the staged budget; current runtime remains unchanged until a bounded migration gate. |
| Card opportunity source | No runtime card hand | Usable body sources generate exact card instances | Conventional learned-technique deck remains unapproved | Body configuration is the approved card-pool author; no separate active deck is required. |
| Attention access | Not implemented | Weighted selection without replacement, persistent cards, Decision Refresh, one Blood-paid redraw | Counts, weights, cost, repetition rules, and UI deferred | Brain shapes imperfect access but never creates physical capability or extra ordinary plays. |
| Brain progression | Not implemented | Rare permanent Brain Parts, one non-stacking part per slot, configured before and locked during a run | Acquisition content, save format, Head/Stun interaction deferred | Brain Parts are the only currently approved permanent Brain progression owner. |
| Inventory | Runtime permits at most one Fast item before Main | Direct owned inventory access under Preparation/Main timing and one voluntary inventory-origin action per round | Production capacity, content, and runtime migration deferred | Inventory never occupies or competes for Attention Slots and cannot chain through redraw. |
| Defence and reflex | Manual Brace and limited current rules; isolated research fixtures | Chosen preparation -> one automatic build-derived reflex route -> compatible passive -> consequence | Exact input families, success model, values, accessibility, and reopening deferred | Reflex remains cardless and cannot grant a second voluntary play. |
| Initiative/conflict | Existing scenario order | Public Lead, two locks, Lead-first sequential resolution, Reply revalidation | Runtime implementation and special windows deferred | Cards, inventory, range, and Brain modifiers all submit to the same lock/revalidation contract. |
| Range | No general runtime range layer | Clinch/Engaged/Distant from meaningful outcomes; execution-bound non-stacking maintenance | Production action profiles and pursuit/escape content deferred | Brain may select only currently source-valid cards; it does not move or maintain range itself. |
| Procedures | Current bounded graft/harvest actions | Separate treatment, Blood restoration, repair, extraction, and graft effects with tiered atomic commitments | Production profiles and interruption content deferred | Direct inventory access does not waive timing, exact reservations, payment, or atomicity. |
| Catastrophic survival | Seeded tutorial Limb for Life runtime behavior | Exact chosen eligible limb or death; untreated stump; provisional net result; Torso failure remains separate | Final value, fiction, availability, and runtime migration deferred | Brain Parts survive death and are not valid sacrifice targets or harvested anatomy. |
| Enemy behavior | Deterministic legal intent ranking | Same future hidden hand/source-legality engine with fixed hidden profiles | Enemy Brain content and AI ranking values deferred | Player sees intent and results, not enemy hand or Brain Parts. Ordinary enemies do not yield Brain Parts. |
| Outcome and negotiation | Jeff survey behavior and state-derived result framework | Causal outcomes must follow state, capability, objective, and behavior | Mental defeat, surrender, mercy, negotiation, and persistence are the next product gates | Brain approval does not define victory, surrender, or run structure. |
| Evidence and production | Automated deterministic fidelity only | Paper authorities define future fixtures and negative cases | Fun, balance, comprehension, accessibility, market, Unity, and final UI lack evidence | No paper approval silently changes runtime or opens production. |

## 3. Collision resolutions

| ID | Collision | Resolution | Authority effect |
|---|---|---|---|
| INT-001 | Both remote cleanup and Brain approval independently used document number 38. | Keep the earlier Director's Choice record as document 38 and renumber the later Brain authority to document 39. | All active links and supersession notes use the unique numbers. |
| INT-002 | Director exploration expected a separate active-deck construction layer; Brain discussion said body parts add their own cards. | The approved baseline has no conventional active deck. Body construction authors the pool and Brain configuration authors access. | Director deck construction remains a future hypothesis only. |
| INT-003 | Document 29 guaranteed hand roles and treated three/five slots as approved capacity. | Document 39 uses weighted no-guarantee selection; three/five remain test fixtures. | Historical guarantees cannot be used as runtime acceptance criteria. |
| INT-004 | Document 29 offered free delayed Reconsider. | Document 39 permits one validated immediate Blood-paid redraw per round before lock. | The rejected card is excluded only for that redraw and may return at a later refresh. |
| INT-005 | Document 34 required inventory to occupy an Attention Slot. | Inventory is directly accessed outside the hand while preserving timing, ownership, exact source, use, one-action, and no-substitution rules. | Readied-slot requirements are historical; inventory cannot be refreshed by Brain redraw. |
| INT-006 | Multiple cards may come from one source, risking impossible simultaneous use. | Each is a distinct instance, but exact source compatibility is revalidated before lock and execution. | One commitment may Dormant/Invalid the source's other instances. |
| INT-007 | Multi-tag cards could be counted twice or bypass filters. | One instance may satisfy any matching filter but is selected once and receives no duplicate weighting merely from tag count. | Tags never waive source, timing, cost, range, or target legality. |
| INT-008 | Permanent Brain progression could be confused with Head anatomy or ordinary enemy extraction. | Brain Part ownership is meta progression separate from body anatomy and inventory. | Ordinary damage/death cannot destroy it; ordinary enemies cannot supply it. |
| INT-009 | Shared player/enemy legality might expose hidden enemy state. | Share the internal engine, not the UI. | Enemy hand and Brain rules remain hidden behind visible intent and results. |
| INT-010 | Paper Preparation/Main timing conflicts with the current runtime Focus/Fast/Main sequence. | Treat them as different maturity layers. | No runtime change occurs until a separate migration plan updates rules, config, code, and tests together. |
| INT-011 | Brain modifiers could become a second effect system or overpower body state. | Slot-local modifiers pass through the existing source, effect-package, commitment, and consequence contracts. | A modifier cannot fabricate capability, add a generic play, or remain attached to a card outside its slot. |
| INT-012 | `Run` terminology could silently define world structure and death rules. | For document 39, a run is only the interval in which Brain configuration is locked. | Map, checkpoint, body retention, restart, and narrative structure remain deferred. |

No unresolved P0 contradiction remains among the approved paper packages. The largest
remaining integration risk is maturity drift: prose now describes systems that the
current simulator intentionally does not implement.

## 4. Unanswered-question disposition

### Answered now through reversible logic

- Card-pool authorship: the usable body, not a separate technique inventory.
- Access authorship: run-configured Brain Parts and later-tested baseline weights.
- Multi-tag matching: eligible once, never duplicated by matching multiple tags.
- Redraw rejection: temporary for one redraw, not permanent card destruction.
- Empty pool: shade slots; do not invent cards or silently convert inventory/reflexes.
- Slot execution modifiers: owned by the slot, not permanently by the card.
- Enemy implementation: shared hidden engine; no enemy-hand interface.
- Brain/Head boundary: permanent Brain Parts are progression records, not destructible
  ordinary anatomy.
- Run terminology: a Brain lock boundary only.

### Answered by deliberate deferral

- Slot counts, weights, redraw Blood cost, and Brain Part strength require comparative
  deterministic distributions followed by human comprehension/choice evidence.
- Technique discovery, mastery, card rarity, draw/discard piles, and active-deck editing
  are unnecessary in the approved baseline and stay closed unless tests reveal a
  specific authorship problem.
- Head-linked Stun, rare extra-card plays, reflex/inventory exceptions, and production
  Brain content remain content/mechanic gates, not safe defaults.
- Complete run structure, body retention, world topology, narrative truth, final UI,
  engine, price, and release strategy remain identity or production decisions.
- Mental defeat, surrender, mercy, negotiation, victory persistence, and outcome
  presentation remain the next dependency-ordered design work. They are not implied
  by the Brain Module.
- Fun, fairness, balance, comprehension, accessibility, and market claims remain
  unanswered until valid evidence exists.

This is not avoidance: selecting a number, world structure, or psychological rule
without its required evidence would create a stronger collision than the one being
removed.

## 5. Documentation organization result

The 2026-08-19 cleanup from `origin/main` is retained:

- the H1 plan/results pair is consolidated as document 21;
- the visual-lab plan/results pair is consolidated as document 25;
- the compatibility operating-skill copy is removed in favor of the canonical skill;
- unused fixed-column Minotaur templates are removed;
- the legacy Turkish PDF is archived under `docs/archive/legacy_design/`;
- the Director's Choice working record remains document 38;
- the Brain Module becomes document 39;
- this audit becomes document 40 and the current cross-system navigation layer.

Documents 29 and 34 remain active historical bridges because they retain unique
staged-turn, physical-compatibility, inventory-ownership, timing, and evidence
contracts. Their superseded sections are explicitly labelled and must not be treated
as current Brain behavior. No further tracked file was proven unrelated, empty,
duplicated, or evidence-free; deleting more would remove useful provenance.

## 6. Requirements

| ID | Reconciliation requirement |
|---|---|
| INT-RQ-001 | Every active document number and local link is unique and resolvable. |
| INT-RQ-002 | Current runtime rules and future paper rules are labelled as separate maturity layers. |
| INT-RQ-003 | The body remains the sole owner of physical card capability. |
| INT-RQ-004 | Brain progression changes access without becoming a second body or ordinary action budget. |
| INT-RQ-005 | Inventory remains outside Attention while preserving its existing causal safeguards. |
| INT-RQ-006 | Historical/superseded rules cannot be used as current acceptance criteria. |
| INT-RQ-007 | Evidence-bound and identity-defining questions remain explicitly deferred. |
| INT-RQ-008 | No cleanup deletes unique authority, evidence, or contamination history. |
| INT-RQ-009 | Git integration accepts current `origin/main` cleanup/director work before updating `main`. |
| INT-RQ-010 | Runtime verification must pass before merge even though the authored changes are documentation-only. |

## 7. Hostile review

| Risk | Severity | Disposition |
|---|---|---|
| Conventional deck construction quietly returns and duplicates Brain progression | High | Closed in the approved baseline; requires a separate evidence-backed proposal. |
| Document 29/34 historical prose is mistaken for current Brain behavior | High | Top-level status, reconciliation sections, index descriptions, and this matrix identify the supersession. |
| Paper rules are mistaken for implemented behavior | Critical | Combat Rules and README preserve the runtime boundary; full regression remains required before merge. |
| Logic-filled answers become unsupported values or content | Critical | Only reversible ownership/instance semantics are resolved; values/content stay deferred. |
| Cleanup erases provenance | High | Unique historical contracts stay active or archived; only documented duplicates/generated material are removed. |
| Branch merging reintroduces obsolete content | High | Compare ancestry and patch equivalence; merge only non-duplicated reviewed changes. |
| Brain becomes perfect-hand or extra-action progression | Critical | No guarantees, no invented capability, and no ordinary extra play remain binding. |

No P0/P1 issue remains in this documentation reconciliation. This audit makes no
claim that the paper model is balanced, fun, understandable, or ready for runtime.

## 8. Current gate

This section records the gate at the time of this earlier audit. Document 41 later
superseded the weighted Brain-access architecture and opened its paper implementation
model as the current owner-design gate. The simulator, configuration, seven scenarios,
H1 fixture, and visual lab remain unchanged. Mental defeat, surrender, and mercy now
follows that Brain doctrine gate.
