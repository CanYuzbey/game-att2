---
name: game-att2-production
description: Analyze and develop Game att2 through its paper-design and demo gates; audit causal rules, decisions, tickets, research, and evidence. Separately maintain the frozen Python simulator when requested. Use for Game att2 project work, never as runtime authorization.
---

# Game att2 Production

Protect the identity: the player rebuilds their body while Blood is life, currency,
and selected ability fuel. Turn uncertainty into a reviewable decision or bounded
test, not more purportedly authoritative prose.

## Establish the correct authority lane

1. Locate the Git root and active `Game_att2_Codex_Handoff_v0_6/` package.
2. Read applicable `AGENTS.md`; inspect worktree and preserve unrelated changes.
3. For active-demo work, read package `README.md`, the mini-game AI working contract,
   `docs/README.md`, its five living documents in order, and `research/README.md`.
4. Select the lane below before resolving conflicts. Current user instructions and
   explicit owner decisions apply within system/developer constraints. Skill guidance
   is neither product authority nor a new approval requirement.

| Lane | Rule authority | Operational / evidence sources |
|---|---|---|
| Active-demo paper design, planning, status | Five living documents and explicit owner amendments | AGENTS, mini-game working contract, research map |
| Frozen simulator maintenance | Development Master v0.6 -> Combat Rules v0.5 -> Technical Spec v0.2 -> validated config for tunables -> acceptance plan | Fresh scoped Python evidence |
| H1 / visual lab / Encounter 3 | Their explicitly bounded approved research contracts | Research records; never product evidence |

Do not put the legacy chain above the living set for active-demo decisions.
The operating contract governs work and claims; it cannot close an OPEN design choice.
Archives and the old PDF provide provenance only. Follow explicit supersession;
otherwise identify conflicting passages and keep the affected product choice open.

## Choose the work mode

- Audit/explanation: read and report; edit only within the requested scope.
- D0 design/planning: read [decision-to-delivery](references/decision-to-delivery.md).
  Use the local `grill-me`, `to-spec`, and `to-tickets` adaptations when relevant.
- Research/comparables: read [research method](references/research-method.md).
- Authorized implementation: name the exact capability, authority, gate, affected
  artifact, negative cases, and evidence before changing the smallest coherent slice.
- Legacy maintenance: use the simulator procedure below; do not port the campaign.
- H1/lab research: read docs 20, 21, 23, 25 only when this is the actual task.
  Verify current status; historical fidelity reports are not fresh verification.
- Encounter 3: read its README and ordered packet; remain paper-only unless the owner
  explicitly opens a separate runtime gate.

Assign role outputs, not ceremonial titles: designer -> alternatives and tradeoffs;
systems analyst -> causal counterexamples; researcher -> sources and limits;
UX/accessibility reviewer -> inspectable choices and input barriers;
QA -> failure oracles; producer -> dependency frontier and scope.
A single agent using these lenses is not an independent multi-person review.

## Active-demo invariants

Read current scope and D0-D5 status from `WORLD_PROGRESSION_AND_DECISIONS.md` and the
working contract; do not maintain a second authoritative gate roster here.

- D0 covers the currently selected opening, ordinary fights, graft evidence, boss
  signature and exact ending/retry boundaries. Read their current owner revision;
  do not freeze a former Guard, escape, donor order or reward path into this skill.
- Planning does not open an engine/runtime gate. Use explicit owner authorization;
  preserve authorization already given rather than asking again.
- Legacy S-001/Jeff/Anna, H1, visual lab, and Encounter 3 are separate artifacts.
  Deferred research does not reopen because active-demo planning is requested.
- Body -> compatible Concept Deck exchange -> Anatomical Deck -> Brain/Attention
  access. A Brain cannot invent a source, restore a removed card, or add ordinary plays.
- Zero/one Preparation and zero/one Main; Readied Item uses its authored budget.
  No growing Mana, attack QTE, corpse-limb reward, or combat range/reposition.
- Yellow -> Block/Parry; Red -> Evade. Require redundant non-color information.
  Assistance and exact numeric hypotheses are not silently promoted.
- Kill -> Blood and no same-day limb access; accepted living surrender -> agreed
  limb and no kill-Blood. Validate life, leverage, and transferable source first.
- Reconcile final demo ending with early-death/retry and progression before applying
  the retained same-day model. When that model applies, flesh/world/temporary
  instability reset and earned abstract layers persist. Do not invent a death reward.
- Do not silently decide identity, actor motives, losses, rewards, probabilities,
  thresholds, content count, or player-facing behavior. Reversible technical choices
  that do not alter experience can be made and recorded.
- Runtime dependencies need explicit justification and approval. Final presentation,
  broad content, and full-game systems are not implied by a bounded demo gate.

## Apply the causal contract

For each meaningful transition:

```text
prior state -> exact source/target/cost legality -> revalidation
-> pay when execution starts -> complete started atomic action
-> explicit mutation -> recomputed capability and remaining legality
-> forced consequences -> goal-supported legal response -> continuation/resolution
-> structured evidence
```

Read `docs/11_SYSTEMIC_CAUSAL_DESIGN_SKILL_v0_1_CODEX.md` for taxonomy/templates,
interpreted inside the selected lane: its historical reach/Downed examples do not
reintroduce removed demo systems. Reject script immortality, resource theatre,
decorative limb damage, invented anatomy/psychology, and outcome teleportation.

Cancellation before execution must not create partial mutation. A lost source cancels
a later unstarted commitment, never a completed atomic action; do not invent replacement
sources or an OPEN refund rule. NPC goals choose legal actions, not exceptions to costs.

Distinguish safety (nothing illegal happens), reachability (a legal route exists),
and liveness (play cannot cycle forever). A changed round is not proof of termination:
check free cycles, replenishment, optimal defense, and card refresh against a named
finite irreversible fact. A round limit in a diagnostic is not an approved gameplay rule.

## Research and creative work

For each material proposal record: question; source/current status; alternatives;
predicted state dynamic; desired player experience; counterexample; test and observable
revise/stop criterion; evidence limit; decision owner. Separate preference, fact, and
testable hypothesis. D0 can choose provisional fixture values for a named test without
claiming final balance. An unresolved required rule blocks its dependent ticket.

Human comprehension and combat appeal need actual human observations. Simulator,
synthetic personas, LLM critique, and designer self-play cannot prove general fun,
fairness, accessibility, retention, market demand, or investor readiness. Preserve
version, consent, prior exposure, facilitator deviations, raw observations, and bias.

## Implement and verify simulator work only when requested

Use immutable definitions, explicit typed state, narrow modules and domain errors.
Inject RNGService; centralize validated tunables; keep domain systems silent and emit
events. Invalid action rejection is atomic. Include source-loss, failure, survival,
and reward-exclusivity tests appropriate to the changed behavior.

From the package directory, discover the available interpreter and dependencies:

```powershell
python -m pytest -q
python -m ruff check src tests
python -m mypy src
python -m game_att2_sim --all-scenarios --seed 42 --format markdown
python -m game_att2_sim.play_cli --seed 42 --script examples/play_cli_full_campaign_sequence.json
```

Repeat seeds when determinism is material. Use property/state-machine tests for real
combinatorial gaps; preserve failing seeds. Never claim unrelated tests verify the demo.

For documentation/skill work, verify frontmatter, local links, authority, current
tool prerequisites, status labels, decision-to-ticket coverage, and acyclic blockers.
Run changed helpers. Do not run the entire legacy suite merely to decorate a docs report.

## External skills and tools

Read [plugin routing](references/plugin-routing.md) when discovering skills/connectors,
using external data or trackers, or considering dependencies. Prefer locally available
capabilities; audit actual instructions and licenses before adopting a third-party skill.
A plugin install count is not evidence of compatibility or correctness.
Do not weaken sandbox settings, edit global configuration, scaffold a web project, or
publish to a tracker just because a helper skill suggests it.

## Hostile review and return

Check authority drift, hidden defaults, cyclic blockers, unowned OPEN decisions,
unreachable reward/persistence demonstrations, free combat loops, scope creep,
unverified tooling, and claims stronger than evidence. P0/P1 fidelity findings block
acceptance of the affected artifact/gate, not unrelated documentation progress.

Start every report with what exists. Use PAPER ONLY, OPEN, WORKING HYPOTHESIS,
IMPLEMENTED — NOT VERIFIED, or VERIFIED IN <artifact> precisely. No completion
percentage. Runtime claims require exact artifact, fresh build/command, exit status,
and player-visible evidence. Never promote historical status from a skill's wording.

For active-demo work use the working contract's return format; for simulator
implementation use `docs/10_CODEX_RETURN_CONTRACT.md`. Scale documentation reports:
changed files, checks/exit statuses, open decisions, scope audit, hostile findings,
limitations, merge recommendation. End with one bounded next step.
