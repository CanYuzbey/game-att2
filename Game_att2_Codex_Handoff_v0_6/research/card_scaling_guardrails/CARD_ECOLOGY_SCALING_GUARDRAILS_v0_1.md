# Game att2 - Card Ecology Scaling Guardrails v0.1

Status date: 2026-08-25

Status: **OWNER-APPROVED DIAGNOSTIC RESEARCH BOUNDARY. NOT RUNTIME, CONFIGURATION,
CONTENT, FINAL BALANCE, UI, OR PRODUCTION APPROVAL.**

Current paper authority is `../../docs/DECK_BRAIN_AND_ACTIONS.md`. The companion
Embodied Technique Brain Synthesis v0.3 is retained as research provenance. This
document protects the Concept Deck direction from combinatorial growth; it changes no
runtime source, content, or final balance value.

## 1. Problem statement

The unsafe implementation is a Cartesian content model:

```text
individual limb x Concept Deck x card label x Brain Part x source state x reflex state
```

If every cell receives a handcrafted card or exception, content and test work grow
multiplicatively while supposedly individual cards converge on reskinned versions of
the same reliable effects.

The safe model factorizes authorship:

```text
limb expressions + Concept Deck exchanges + Brain access rules + shared execution grammar
```

- a limb expression is authored once;
- a Concept Deck atomically removes and adds compatible expressions;
- a Brain Part changes access or one declared slot behavior, never deck membership;
- the shared combat grammar resolves source, cost, target, reflex, wound, and Blood;
- the resulting runtime combinations are tested combinatorially rather than authored
  individually.

This preserves the product identity: the player rebuilds a body, and cards are
physical expressions of that body rather than detached class powers.

## 2. Evidence boundary

The framework uses four evidence classes:

1. **Static proof/check:** ownership, atomicity, size, duplicate and dominance checks.
2. **Finite combinatorial evidence:** exhaustive small spaces and t-way covering
   arrays for larger interaction spaces.
3. **Seeded synthetic evidence:** reproducible distributions across transparent
   procedural policies and adversarial source-state changes.
4. **Human evidence:** comprehension, perceived individuality, meaningful trade-offs,
   accessibility and replay desire.

Only the fourth class can support experience claims. Structural automation can reject
broken content; it cannot certify that content is creative or fun.

The test-selection method follows NIST's definition of t-way combinatorial coverage:
cover every value combination for every selected set of t factors without executing
the full Cartesian product. Coverage-guided property testing is retained for sparse
state preconditions, but explicit source-loss cases and finite enumeration remain
mandatory because unguided generators can miss meaningful rare states. Quality-
diversity ideas are used as an archive/audit lens, not as an automatic card designer:
the goal is several strong, behaviorally different builds rather than one maximized
solution.

Primary methods:

- [NIST Automated Combinatorial Testing](https://csrc.nist.gov/Projects/automated-combinatorial-testing-for-software/faqs)
- [Lampropoulos, Hicks, and Pierce - Coverage Guided, Property Based Testing](https://doi.org/10.1145/3360607)
- [Mouret and Clune - Illuminating Search Spaces by Mapping Elites](https://arxiv.org/abs/1504.04909)
- [Holmgard et al. - Persona Based Player Modeling](https://ojs.aaai.org/index.php/AIIDE/article/view/12849)

## 3. Scientific boundaries

### 3.1 Non-negotiable structural invariants

These are rejection rules, not tuning targets.

| ID | Boundary | Failure result |
|---|---|---|
| CSG-I01 | Every card declares one exact physical source or exact source set. | Block |
| CSG-I02 | Source legality is revalidated before commitment and execution. | Block |
| CSG-I03 | A disabled/missing source cannot execute or be silently substituted. | Block |
| CSG-I04 | Concept Deck sacrifices and gains resolve as one atomic transaction. | Block |
| CSG-I05 | An unavailable sacrifice can never produce a gain. | Block |
| CSG-I06 | Deck membership is owned by body compatibility plus Concept Deck; Brain owns access only. | Block |
| CSG-I07 | Brain cannot restore removed cards, invent capability or grant ordinary extra actions. | Block |
| CSG-I08 | Automatic reflexes and forced state reactions remain outside voluntary deck membership. | Block |
| CSG-I09 | A card's signature property must alter causal effect, cost, risk, target or execution; flavour-only text does not count. | Block |
| CSG-I10 | A Concept Deck exchange that changes total card count must declare that rule explicitly. | Block |

### 3.2 Provisional experimental content budgets

These are starting limits for a bounded diagnostic catalogue. They can change only
through an explicit versioned experiment; they are not production facts.

| Budget | v0.1 diagnostic limit | Reason |
|---|---:|---|
| Cards referencing one source | 5 | Forces selection and differentiation before breadth. |
| Functional labels per card | 3 | Prevents universal cards from matching every deck/Brain filter. |
| Mechanical atoms per card | 6 including timing, target and reflex grammar | Leaves room for effect, cost and risk without paragraph-cards. |
| Signature creativity atoms | Exactly 1 | Preserves an individual hook while keeping shared rules reusable. |
| Special cards added by one exchange | 2 | Stops one achievement from becoming a hidden second card set. |
| Novel engine primitives in one card | At most 1 and separately reviewed | Prevents every card from becoming a code feature. |
| Ordinary Concept Deck transformations | One primary exchange package before expansion | Makes the deck's promise and sacrifice explainable. |

The signature budget does **not** mean every card must be mechanically simple in
effect. It means complexity must be composed from common atoms around one memorable
exception. A proposed card needing two unrelated exceptions is two designs occupying
one card and must be split or promoted to a system-level proposal.

### 3.3 Individuality certificate

Every candidate card must answer all five questions:

1. **Source truth:** why does this exact body source perform the card?
2. **Decision truth:** what decision changes compared with the nearest existing card?
3. **Cost truth:** what capability, Blood, exposure, timing or future option is given
   up?
4. **Consequence truth:** which explicit state mutation can alter later affordances?
5. **Signature truth:** what single causal property should a player remember?

Failure on Source, Cost or Consequence is a blocker. Failure on Decision or Signature
is a near-duplicate/content-quality rejection.

The static detector builds a mechanical fingerprint from timing, target grammar,
reflex grammar, effects, costs and risks. It flags pairs at provisional Jaccard
similarity `>= 0.82`. This is a review trigger, not proof of sameness. Numerical name
changes do not create individuality.

### 3.4 Factorization boundary

No content author may implement a special rule named after a complete combination
such as `crab_arm_aggressive_brain_intercept`. The combination must resolve through:

```text
CardDefinition
  exact sources
  timing and labels
  shared effect atoms
  shared cost/risk atoms
  one signature atom

ConceptDeckDefinition
  removals/selectors
  additions
  atomic applicability rule

BrainPartDefinition
  one slot
  one primary lever
  visible buff and nerf

ExecutionState
  current sources, wounds, Blood, range, commitments and reflex conditions
```

If a desired card cannot be expressed through this factorization, it is classified as
a **new mechanic proposal**, not ordinary card content. That classification is the
main engineering firewall against uncontrolled scaling.

## 4. Risk classification

Severity and evidence are kept separate. A low-frequency identity violation still
blocks.

| Class | Meaning | Disposition |
|---|---|---|
| P0 | Breaks source truth, atomicity, action economy, determinism or authority boundary. | Reject immediately. |
| P1 | Creates multiplicative implementation, dominant strategy, routine dead hand, cosmetic anatomy or reflex erasure of strategy. | Revise before human test. |
| P2 | Tuning, frequency, readability or content-distribution risk with intact architecture. | Permit only in isolated diagnostic. |
| P3 | Presentation/naming issue with no causal effect. | Track; cannot be used to claim mechanical individuality. |

For prioritization, record Severity, Exposure and Detectability on a 1-5 ordinal
scale. Do not use their product to overrule a P0/P1 category. The scores order work
inside a class; they do not turn structural violations into acceptable averages.

## 5. Risk paths and algorithmic controls

| Risk path | Detection | Control | Kill/revise criterion |
|---|---|---|---|
| Limb x deck content explosion | Project authored cells and count new engine branches. | Factor card, exchange and Brain definitions; cap batch/content size. | Any ordinary card requires a full-combination branch. |
| Card homogenization | Nearest-neighbor fingerprint plus individuality certificate. | One causal signature; require source/cost/consequence truth. | Similarity trigger survives hostile review or only numbers/names differ. |
| Free aggressive conversion | Enumerate all missing-cost and missing-source states. | Atomic validate-then-commit exchange. | Any gain occurs when one sacrifice/source is invalid. |
| Achievement power ladder | Pareto compare benefits and unavoidable burdens across pressure regimes. | Decks are sidegrades with experienced losses. | One deck is no worse in every tested regime and better in at least one. |
| Double filtering frustration | Trace membership separately from Attention selection. | Deck decides membership; Brain weights only valid members. | Brain resurrects removed cards or deck promise is routinely absent without disclosed odds. |
| Dead/incoherent Attention | Paired seeded drought and source-loss distributions. | Revise exchange/card mix or visible redraw; never fabricate a guaranteed perfect hand silently. | Predeclared drought/choice bounds fail. |
| Reflex erases planning | Compare good/bad commitments under precise and assisted reflex profiles. | Execution modifies state result; it cannot directly select victory. | High reflex skill routinely neutralizes strategically bad commitments. |
| Unavoidable dominant card | Pareto test plus procedural-persona selection share. | Add meaningful burden, narrow state use, or remove card. | Same card dominates across personas, sources and pressure states. |
| Too many labels | Static label count and filter-match audit. | Maximum three functional labels; no flavour tags in mechanics. | Card matches most deck and Brain rules. |
| Rules become unreadable | Atom count plus human prediction/recall task. | Shared grammar around one signature atom. | Players cannot predict source, cost and consequence before commitment. |

## 6. Card Ecology Gate algorithm

```text
INPUT candidate batch, current catalogue, Concept Decks, Brain Parts, state factors

G0 AUTHORITY
  confirm proposal/runtime status and exact scope
  reject unauthorized engine/content expansion

G1 STATIC CAUSAL VALIDATION
  validate exact sources, timing, target, labels, effect, cost, risk, signature
  validate card/label/mechanic/source budgets
  reject decorative signatures and missing consequences

G2 ECOLOGY VALIDATION
  compare every candidate with nearest mechanical neighbors
  flag Jaccard similarity >= threshold
  compare benefits and burdens for Pareto dominance
  classify any new primitive as system work, not card work

G3 CONCEPT DECK TRANSACTION VALIDATION
  enumerate applicable and non-applicable body states
  validate every sacrifice and gain before mutation
  apply all removals/additions together or apply nothing
  revalidate every gained card's source

G4 INTERACTION TEST DESIGN
  exhaust all single cards, exchanges and source-loss cases
  use 2-way coverage for ordinary cross-system factors
  use 3-way coverage where deck x Brain x source-state or
    card x reflex x wound-state can alter legality or cost
  retain named adversarial cases for sparse catastrophic states

G5 SEEDED DYNAMIC AUDIT
  replay identical seeds across baseline and candidate
  run transparent aggressive, defensive, opportunistic and survival policies
  measure drought, legal choice count, source diversity, card concentration,
    exchange activation, downside exposure and invalid attempts
  reject structural dominance; do not claim human balance

G6 QUALITY-DIVERSITY AUDIT
  map surviving builds by behavior descriptors, for example:
    offence commitment x defence retention x source concentration
  retain several non-dominated, behaviorally distinct candidates
  reject an archive that collapses into one optimal niche

G7 HUMAN DIAGNOSTIC
  ask players to identify source, predict consequence, state the sacrifice,
    distinguish nearest cards and explain the deck/Brain contribution
  continue, revise or kill using predeclared criteria

OUTPUT accepted-for-next-evidence, revise, split-to-system-proposal, or kill
```

## 7. Combinatorial test strength

Full enumeration remains mandatory for:

- one exchange across every presence/absence combination of its sacrifices and gain
  sources;
- each card with every state that directly controls its legality;
- source invalidation before lock and before execution;
- shared-source Preparation/Main conflicts;
- Blood affordability boundaries and action-budget invariants.

Use pairwise coverage for ordinary combinations of:

- Concept Deck;
- Brain Part;
- Attention slot;
- source state;
- reflex mode;
- target state;
- encounter pressure profile.

Promote named high-risk interactions to three-way coverage, especially:

```text
Concept Deck x Brain Part x source state
Card x reflex mode x wound/source state
Preparation x Main x shared physical source
```

The research tool supplies a deterministic greedy covering-case generator. This is
not claimed to produce a mathematically minimal array; it produces reproducible full
t-way coverage for bounded fixture models.

## 8. Measurement contract

### Structural metrics

- invariant failures: required `0`;
- invalid action attempts after source loss: required `0`;
- partially applied Concept Deck exchanges: required `0`;
- undeclared new engine primitives: required `0`;
- pairwise coverage: required `100%` for the declared factor model;
- three-way coverage: required `100%` for named high-risk factor groups;
- near-duplicate and Pareto findings: require human hostile review, never silent pass.

### Distribution metrics

Record rather than prematurely fix universal production numbers:

- Main and Preparation drought;
- legal choice count and category/source diversity;
- card selection concentration and unused-card rate;
- how often every declared downside is actually experienced;
- Brain-induced shift relative to the same deck and seeds;
- deck-induced shift relative to the same body and Brain;
- results before and after each source-loss event;
- poor-strategy outcomes under high reflex performance.

Numeric continue/kill bands must be preregistered per fixture against its baseline.
Do not select thresholds after seeing which candidate wins.

### Human individuality metrics

For each tested card/deck, collect:

- source identification accuracy;
- predicted cost/consequence accuracy;
- remembered signature property;
- nearest-card distinction;
- stated deck sacrifice;
- stated Brain contribution;
- observed decision change rather than stated preference alone.

The first small owner diagnostic establishes task readability only. External
participants are needed before claiming comprehension or replay value.

## 9. Aggressive exchange example audit

Status: **EXAMPLE ONLY. NOT CARD CONTENT OR A BALANCE VALUE.**

```text
remove one defensive Leg expression
remove one defensive Left-Arm expression
add one brutal Left-Arm expression
add one brutal Right-Arm expression
```

Required causal handling:

1. All four card definitions and all exact sources exist.
2. Both sacrifices are currently members of the constructed deck and their exact
   sources are currently usable; a dormant card is not valid payment.
3. All sources required by the gained cards are compatible with the current body.
4. Validate the complete transaction without mutation.
5. If any check fails, leave the deck unchanged and report the blocking reason.
6. If all checks pass, remove and add in one mutation.
7. Brain weighting runs only after the new deck is complete.
8. Later source loss invalidates dependent cards; sacrificed defence does not return
   mid-encounter.

Count parity does not establish balance. The brutal gains still require Blood,
exposure, recovery, interception or lost future-option burdens that matter in the
states where their benefits matter.

## 10. Requirements

| ID | Requirement |
|---|---|
| CSG-001 | Content authorship is factorized across card, Concept Deck, Brain and shared execution definitions. |
| CSG-002 | Every card declares exact source ownership and one causal signature atom. |
| CSG-003 | Static budgets are configurable diagnostic gates rather than hidden production constants. |
| CSG-004 | Concept Deck exchanges validate and mutate atomically. |
| CSG-005 | Missing sacrifices or gained-card sources produce no partial gain. |
| CSG-006 | Near-duplicate fingerprints and Pareto dominance are reported deterministically. |
| CSG-007 | Ordinary interaction models receive complete pairwise coverage. |
| CSG-008 | Named legality/cost interactions receive exhaustive or three-way coverage. |
| CSG-009 | Seeded synthetic results remain structural evidence only. |
| CSG-010 | Human diagnostics test source, consequence, sacrifice and individuality comprehension. |
| CSG-011 | The framework adds no runtime content, dependency or current-authority change. |

## 11. Current risk disposition

| Risk | Severity | Current disposition |
|---|---|---|
| Cartesian implementation growth | P1 | Structurally controlled by factorization; requires enforcement in future schema/code review. |
| Loss of individual card identity | P1 | Controlled by individuality certificate and nearest-neighbor review; human evidence pending. |
| Free/partial Concept Deck gains | P0 | Deterministic atomic algorithm and adversarial fixture added. |
| Meta-progression power ladder | P1 | Pareto/quality-diversity method defined; representative mechanics and human evidence pending. |
| Brain/deck ownership collision | P0 | Deck membership and Brain access separated in proposal; authority update still pending. |
| Reflex dominance | P1 | Existing strategy-versus-execution evidence contract retained; new card content pending. |
| False scientific confidence | P1 | Evidence classes and claim limits explicit; fun/balance claims blocked. |

## 12. Verdict

The scalable solution is not to reduce cards to generic templates. It is to permit one
causal signature per card inside a strict shared grammar, while testing combinations
instead of hand-authoring them.

This protects creativity in three ways:

- every limb can express several roles without becoming mechanically identical;
- Concept Decks create real sacrifices and special moves through atomic exchanges;
- Brain Parts remain meaningful without duplicating deck construction.

The framework is ready for an isolated content-schema diagnostic. It is not approval
to implement the full card system, persistence, achievements or production content.
