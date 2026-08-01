# Game att2 — Systemic Causal Design Skill v0.1 (Codex Edition)

## 0. Status and authority

This skill implements the owner-approved design principle that outcomes derive from state. It governs future design, audits, prototypes, and acceptance work, but does not itself approve new mechanics. `AGENTS.md` and the repository precedence chain still govern implementation. Existing approved rules, evidence controls, AI quarantine, scope limits, and stage gates remain unchanged.

Changed: future work must trace action → state mutation → capability change → affordances → forced or chosen response → resulting state. Why: the owner rejected individually authored consequence branches as the primary design model. Unchanged: current numeric rules, anatomy, Warden behavior, Encounter 3 implementation block, and Unity block.

## 1. Operating boundaries

- Use a small set of explicit, reusable, testable rules. Systemic does not mean a universal physics, anatomy, psychology, or behavior simulation.
- Definitions describe stable entities; runtime state records only mutable facts supported by sources or clearly labeled proposals.
- Capabilities are derived from definitions and current state. Affordances are the legal, reachable actions in the present situation.
- Actions mutate state; they do not teleport to endings. Consequence resolution evaluates the resulting state.
- Examples are diagnostics, not canonical values or mechanics. Unsupported categories are `DEFERRED`, not filled by plausible invention.
- Encounter scripts may select among legal actions and express authored pacing. They may never restore destroyed sources, waive costs, or override forced consequences.

## 2. Systemic Causal Resolution Loop

Run this loop for every meaningful action.

### Step 1 — Validate declared action

Check that the actor and target exist; required life/consciousness conditions hold; the action definition and source exist; the source is functional; required tools and items exist; costs are affordable; status and action economy permit the action; the target is reachable; and the action is physically and mechanically legal. Reject with a traceable reason when any check fails.

### Step 2 — Resolve action

Use only approved deterministic rules, injected randomness, attack and damage rules, targeting, tools, medicine, and resource transactions. Never invent a rule to preserve a desired scene.

### Step 3 — Apply state mutation

Record every supported change explicitly: resources, integrity, wounds/tags, severance, exposure, item quantities, debt, Downed, action consumption, or other approved runtime state.

### Step 4 — Recompute capabilities

Derive which actions or objective paths were lost, gained, weakened, exposed, or made irrational. Definition existence alone does not imply current availability.

### Step 5 — Evaluate forced consequences

Check approved rules for death, collapse, unconsciousness, catastrophic Bleeding, unaffordable actions, total offensive incapacity, inability to defend, debt triggers, mandatory Stand, item depletion, and organ failure. An unsupported check is `DEFERRED`, not a result.

### Step 6 — Evaluate actor response

If no result is forced, choose among legal responses using documented personality, survival drive, goals, pain, fear, hostility, contracts, escape options, ability to affect the opponent, and expected continuation cost. Personality may select a poor legal action; it cannot restore an impossible one.

### Step 7 — Determine whether the encounter continues

Continue only if at least one side can act, can meaningfully pursue an objective, and has a rational or forced reason to continue. Otherwise resolve through an approved state-derived conclusion such as surrender, escape, incapacity, negotiation, capture, mutual inability to continue, or death. If the necessary rule or behavior is undefined and identity-defining, stop for one owner decision.

### Step 8 — Log evidence

Every material result must expose: prior state; declared action; legality checks; rules and authority used; injected random results; state mutations; capability changes; consequence checks; actor-response basis; and final resolution or unresolved question.

## 3. Controlled consequence taxonomy

| Category | Minimum question | Current handling |
|---|---|---|
| Physical viability | Alive, conscious, structurally capable, and represented vital systems functioning? | Apply only approved Blood, limb, Downed, and other explicit rules; anatomy otherwise deferred. |
| Action viability | Source/tool/resource/action economy/status requirements satisfied? | Required for every action. |
| Threat viability | Can at least one legal action meaningfully affect the opponent or objective? | Required as an encounter audit; “meaningfully” must reference an approved effect. |
| Objective viability | Can the actor still pursue its documented goal? | Required when goals are documented; otherwise open. |
| Behavioral viability | Is continuation consistent with documented intent, fear, pain, loyalty, desperation, or irrationality? | Evaluate only from approved character definitions; otherwise owner decision. |
| Encounter viability | Can further turns still produce meaningful change? | Required before continuing a loop. |

Not every prototype must simulate every category. Mark unsupported categories `DEFERRED` and design the test around the categories it actually represents.

## 4. Forced, chosen, and exceptional outcomes

- **Forced systemic:** an established rule compels the result—for example Blood-0
  death after explicit prevention checks, unusable required source, mandatory Stand,
  or no legal action.
- **Rational actor:** multiple legal outcomes remain; documented goals and behavior select surrender, retreat, bargain, or continued fighting.
- **Owner-authored exception:** a documented supernatural, berserk, contractual, or special-source rule changes ordinary behavior. Record its source. Never invent an exception during resolution.

## 5. State-derived encounter design

Begin with these questions, not a victory branch:

```text
What state does each actor start in?
What capabilities follow from that state?
What resources constrain them?
Which body part or tool sources each action?
Which mutations remove or alter those actions?
What goals support continuation, surrender, retreat, or bargaining?
Which conclusions emerge without dedicated ending branches?
```

Define actor objectives, starting state, action sources, capability requirements, resource costs, vulnerabilities, response tendencies, surrender/escape logic, consequence checks, and approved rewards/post-combat states. A scripted sequence is acceptable only as a test driver or authored preference among legal choices; it must yield when state invalidates an action.

## 6. Reusable templates

### Runtime state record

| Entity | Field/tag | Prior value | Current value | Mutation source | Authority | Supported / proposed / deferred |
|---|---|---|---|---|---|---|

Do not create a universal schema. Add only fields required by approved rules or a clearly isolated proposal.

### Causal action requirement matrix

| Action | Actor | Required source | Required tool | Resource cost | Required state | Illegal states | Target requirements | State effects | Capabilities affected | Possible downstream resolutions | Authority/source |
|---|---|---|---|---:|---|---|---|---|---|---|---|

### Combatant capability matrix

| Capability | Current availability | Reason | Required source | Resource requirement | Blocking states | What would restore it | Authority/source |
|---|---|---|---|---|---|---|---|

### Affordance record

| Situation | Candidate action | Legal? | Reachable? | Affordable? | Intent-supported? | Exclusion reason | Evidence |
|---|---|---|---|---|---|---|---|

### Consequence-resolution record

| Check category | Result: pass/fail/deferred | Rule/source | Forced effect | Behavioral choice still open | Next state/check |
|---|---|---|---|---|---|

### Encounter audit

| Actor/state | Remaining objectives | Remaining threats | Lost capabilities | Forced results | Legal chosen responses | Undefined owner decisions | Can further turns matter? |
|---|---|---|---|---|---|---|---|

## 7. Prohibited anti-patterns

- **Hard-coded answer design:** `two arms lost → player wins` without general capability and consequence proof.
- **Script immortality:** using an attack after its required body part or tool is unusable.
- **Resource theatre:** displaying Blood or another cost without allowing it to constrain actions.
- **Decorative limb damage:** changing integrity while leaving sourced actions unaffected.
- **Outcome teleportation:** direct death or surrender without intervening state and rule explanation.
- **Fake emergence:** many encounter/action special cases disguised as a system.
- **Narrative override:** continuing conventional combat with no legal threat unless a documented irrational action remains possible.
- **Unapproved biological invention:** assumed penetration, organ, Blood-loss, or death behavior.
- **Universal rationality:** treating every opponent as optimal; poor choices must still be legal.
- **Single-answer encounter design:** selecting one intended solution and invalidating alternatives.
- **Infinite-possibility excuse:** refusing finite rules because “anything can happen.”

## 8. Undefined-rule protocol

1. Name the missing rule and affected causal link.
2. Classify it as technical/reversible or identity-defining.
3. Use the smallest reversible technical interpretation only when product experience is unchanged; isolate and label it.
4. For anatomy, personality, surrender, escape, or scope that changes experience, stop and ask one focused owner question.
5. Never hide the choice in config, implementation defaults, test fixtures, or narrative prose.

## 9. Acceptance and hostile review

Acceptance requires a trace from definition and prior state through legality, mutation, recomputed capability, consequence category, and result. Tests must include loss of action source, unaffordable costs, status/action-economy blocks, and encounter termination or `DEFERRED` handling where in scope.

Before approval ask: Is this branching renamed as state? Is the model speculative or unbounded? Were anatomy, intent, or rationality invented? Can every rule be tested? Did an example become canon? Can a script override destroyed capability? Do contaminated tests support an overstated claim? Does any change silently unblock Encounter 3 or Unity? Resolve P0/P1 findings before acceptance.
