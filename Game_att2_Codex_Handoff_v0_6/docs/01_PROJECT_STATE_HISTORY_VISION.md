# Game att2 — Project State, History, Objective, and Future Vision

Version: 0.6  
Owner: Can Yüzbey  
Current development stage: pre-digital prototype / simulator handoff

## 1. Original creative direction

Game att2 began as an exploration of a tense, contained, replayable horror game with a **Buckshot Roulette-dominant atmosphere** and a **hell-loop-defining structure**. The influence was never intended as a mechanical copy. The project takes from that reference the ritual tension, oppressive intimacy, contained encounters, minimalist brutality, and high-stakes readability. Its own identity is based on body reconstruction.

The initial fantasy became:

```text
I wake up broken.
I fight other broken things.
I cut away what I need.
I graft it onto myself.
I become something that can survive the loop.
```

The player is a mostly silent self-insert. They wake with missing, damaged, or poorly repaired body parts in a fantasy hell-loop. Opponents may eventually include humans, monsters, animals, celestial beings, cyborgs, and abnormal flesh entities. Their limbs are not cosmetic loot. A limb can define actions, passives, economy behavior, risk, graft stability, and tactical identity.

Blood was chosen as the unifying resource: health, currency, ability fuel, trade value, debt material, and wager. This is one of the project's strongest hooks and one of its highest risks.

## 2. Early concept decisions

The concept was narrowed to a single-player PC roguelike/roguelite. The central loop was defined as:

```text
wake damaged → duel → spend/lose/gain blood → damage or sever limbs
→ harvest/graft/sell/preserve → carry a changed body forward → eventually fail and wake again
```

A six-slot body model was selected for the first demo:

- Head
- Torso
- Left Arm
- Right Arm
- Legs
- Core

This is deliberately abstract enough to remain manageable while making body change visible. Missing-limb builds are reserved for rare or special strategies; normal play should not routinely remove most of the player's agency.

Grafting was split into two modes:

- **Emergency grafting:** immediate after a fight, useful but risky and potentially Unstable.
- **Grafting table:** safer, more expensive, and capable of integration/repair decisions.

The presentation direction was locked for prototype planning:

- decision time at a ritual table;
- action time in a side/body-duel cut-in optimized for showing which limb acted, what was targeted, what changed, what it cost, and what risk appeared.

## 3. Scope discipline

The project explicitly rejected premature work on final art, maps, large lore, base building, multiplayer, advanced RPG leveling, large enemy rosters, full procedural generation, and store systems. The immediate question was not “Can this become a large game?” It was:

```text
Can repeated turn-based fights about losing, acquiring, grafting, and exploiting limbs—while blood is both life and money—create meaningful, repeatable decisions?
```

The first prototype was named **The Grafting Table Prototype**.

## 4. First paper encounter: Jeff

Jeff was designed as a tortured human tutorial opponent. The player began as `S-001 Torn but Stable`: 85 blood, damaged torso, missing right arm, one basic attacking arm, weak legs, and a Human Heart.

The key test chain became:

```text
Claim Jeff's Right Arm → damage it → spend heavily on Hell Saw
→ sever it cleanly → disable the remaining arm → force a plea
→ choose body progression over immediate blood → emergency graft the arm
```

The manually played Jeff test produced the first strong project-specific moment. The player cared about the right arm because their own right arm was missing. They spent blood to secure it, chose both arms instead of Jeff's offered blood, grafted the desired arm, and sold the spare. The body changed and gained `Guard Flesh`.

However, the test also revealed structural problems:

- limb-state thresholds were awkward;
- enemy blood appeared disconnected from losing limbs;
- action timing needed rules when the acting limb was damaged first;
- harvest quality was undefined;
- tool charges were ambiguous.

## 5. Adversarial paper-test batch

The next tests were intentionally hostile rather than celebratory.

### No-spend Jeff exploit

Repeated free `Grip Strike` attacks could remove both arms while spending no blood. If those attacks produced good grafts, blood hoarding would be optimal and the central economy would fail.

Resolution:

- free/basic attacks may damage, disable, mangle, or ruin limbs;
- they cannot create premium Clean Harvest on their own;
- clean extraction requires a tool, contract, special ability, bargain, or table procedure.

### Failed Hell Saw / death spiral

Bleeding plus an expensive failed saw, enemy Rage, medical costs, and a follow-up attack created rapid collapse.

Resolution:

- blood danger must be projected clearly;
- emergency medical items can be `Fast`;
- one tutorial soft-collapse/low-blood escape valve is allowed;
- danger is retained, but failure should be readable rather than surprising.

### Focus versus heavy threat

When Focus consumed the only main action, information could not be acted upon and became a trap.

Resolution:

- Focus became a pre-action information purchase;
- it costs blood, uses the Head, and does not consume the main action.

### Anna medical test

Anna was introduced as a calm medical survivor with a Crude Graft Arm, Stitched Torso, Leaking Heart, Surgical Jab, Black Stitch, and a trade offer.

Anna successfully differentiated the second encounter from Jeff:

- Jeff asks whether the player wants a limb enough to pay for it.
- Anna asks whether the player wants another limb more than they want to stabilize the body they already have.

Fast Blood Bag and Fast Clotting Cream allowed recovery without surrendering all offensive tempo. Anna's `Stabilized` state and trade logic needed explicit visibility, but the medical/non-butchering path was promising.

### Forced Unstable graft

The first emergency graft had rolled Stable, so a forced bad outcome was tested. A purely automatic “disabled this round” result was judged too punitive. The v0.4 model changed instability into a more choice-oriented state:

- Twitch: pay extra blood or lose access for the round;
- Works: normal;
- Ache: works but may create next-round stress;
- Surge: discount the limb action or gain a small fallback benefit.

A key production rule emerged: the tutorial arc must provide a stabilization route after the player's first Unstable graft.

## 6. Mini-campaign paper validation

The smallest complete loop was tested:

```text
S-001 start → Jeff → emergency graft → Anna → stabilization trade → grafting table
```

The run began at 85 blood with a missing right arm. The player took Jeff's right arm, emergency-grafted it, rolled Unstable, sold the spare arm, and entered Anna's encounter with the new `Guard Flesh` action and graft risk. Against Anna, the player used Focus, defended the graft, managed blood, and ultimately accepted medical stabilization instead of taking another arm. At the table, the arm was integrated. The run ended at 37 blood with an Integrated Grafted Human Right Arm and the torso vulnerability still unresolved.

The historical paper record was 37 Blood. It remains evidence, not an automated expected value. The current source-compliant seed-42 simulator result is 25 Blood under Combat Rules v0.4 and configuration. The difference is an unreconciled arithmetic/source-history contradiction, including an unconfigured spare-arm sale; neither isolated number is the intended balance target. Future balance decisions require distributions and playtests.

The important result was not the exact number 37. It was the coherent body arc:

```text
I wanted a limb → I paid to take it → the graft caused a problem
→ the next encounter tested that problem → I sacrificed greed to stabilize it
→ the table let me lock the change into my body
```

This was judged sufficient for a narrow Python simulator, but not sufficient for Unity.

## 7. Current condition

### Confirmed

- The conceptual hook is promising.
- Jeff → graft → Anna → table is the current first-prototype sequence.
- Six body slots, blood economy, clean-sever gating, harvest quality, emergency grafting, Unstable v0.4, Focus, Fast medical timing, Plead Pressure, and table integration are approved for simulator testing.
- The paper evidence is designer-run internal evidence, not blind-player proof.
- The project is ready to automate rules and collect numerical evidence.

### Not yet confirmed

- that the game is fun for external players;
- that repeated runs remain varied;
- that blood costs are balanced;
- that Blood Bag is not dominant;
- that Anna's greed and stabilization routes are equally viable;
- that table choices remain competitive;
- that the game is ready for Unity;
- the final engine, art style, title, run map, meta progression, or release plan.

## 8. Current objective

Build a deterministic Python console simulator that can reproduce the approved encounters and stress the mechanics across seeds and simple strategy profiles. The simulator must expose blood curves, limb transitions, action-source impairment, extraction quality, graft results, plea/trade states, and table decisions.

The simulator is not expected to prove fun. It is expected to find contradictions, exploits, dominant choices, dead-end states, and implementation ambiguities faster than manual paper play.

## 9. Future vision

### Current paper-test status

Encounter 3 paper structure and moderated human-test operations are prepared. Human testing has not yet run. Encounter implementation and Unity remain blocked pending real session evidence and owner approval.

### Near term

1. Implement simulator v0.1.
2. Run required deterministic scenarios.
3. Run small strategy batches.
4. Produce Simulator Results v0.1.
5. Revise rules/config without expanding content.
6. Decide whether a tiny interactive text prototype is useful.

### Next gate

A Unity graybox becomes reasonable only if:

- body changes reliably affect later fights;
- blood spending remains rational but tense;
- no-spend premium extraction remains blocked;
- Unstable grafts are risky but not automatic failure;
- Anna's offers are not automatic;
- table choices vary;
- event logs are clear enough to translate into future UI feedback.

### Long term

After a validated graybox and vertical slice, the game may expand into:

- additional body archetypes and starting bodies;
- enemies such as Bone-Minotaur and simplified Many-Eyed Flesh;
- carefully bounded contracts/tools;
- curses, rot, celestial judgment, and mechanical organs;
- a full run structure and hell-loop meta progression;
- stylized art, animation, audio, narrative bureaucracy, and dark satire;
- production, accessibility, licensing, release, and platform preparation.

These are future possibilities, not commitments for the simulator.

## 10. Product identity to preserve

The project should remain recognizable by this statement:

> You are not collecting weapons. You are becoming the weapon, piece by piece, using your own blood as money.

Any implementation or future feature that weakens body-as-build, turns blood into ordinary mana/HP, makes severing free, or reduces grafting to passive stat equipment should be challenged.
