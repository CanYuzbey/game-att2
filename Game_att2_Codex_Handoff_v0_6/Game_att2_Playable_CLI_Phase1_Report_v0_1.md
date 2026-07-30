# Game att2 Playable CLI — Faz 1 Report v0.1

Status date: 2026-07-30

Parent baseline: `b4b48553eb559976f099369ad432c9439bea91c4`

Evidence status: implementation complete and regression-tested; no human play evidence

## 1. Scope and purpose

Faz 1 delivers an interactive, playable terminal loop over the accepted deterministic
simulator. Its only encounter is:

```text
S-001 (Torn but Stable) -> Jeff
```

The interface exists to answer one question: is the round-by-round decision readable
and playable by a human at a keyboard, before any GUI or Unity work. It is not a
balance claim, not production UI, and not evidence that the loop is fun.

**Scope lock.** Emergency grafting, Anna, and the Grafting Table are deliberately
absent. They are not offered, not reachable, and regression-tested as unreachable
(`test_phase_two_content_is_not_reachable_from_this_interface`). The full approved
sequence remains owned by `research_shell.py`, whose evidence contract, exports, and
byte-identical replay tests are untouched by this work.

## 2. Architecture and authority

Three new modules, matching the repository's separation rules:

| Module | Owns | Does not own |
|---|---|---|
| `play_session.py` | Encounter progression, offer categories, event-derived readability records | Any rule, cost, threshold, or probability. Never prints |
| `play_render.py` | ASCII tables, menus, readability blocks, Turkish surface text | Any state mutation |
| `play_cli.py` | Input loop, two-level menu state machine, argparse, transcript | Any rule or rendering decision |

`RuleEngine` remains the sole authority for legality, cost, Main/Focus/Fast timing,
source usability, damage, harvest quality, plead pressure, and all state mutation.
The session asks `main_action_availability`, `focus_availability`, and
`fast_item_availability` for both legal and disabled offers, then calls the existing
rule method. No rule is reimplemented, waived, or duplicated.

Nothing in `config/` was changed. No cost, threshold, probability, encounter order, or
reward was altered.

## 3. Round sequence and the decision stop

The loop follows `docs/03_COMBAT_RULES_v0_4.md` §1. Automation stops at steps 4-6:

| Step | Rule | Interface behavior |
|---|---|---|
| 1-2 | Start effects, Unstable checks | `RuleEngine.start_round`, then collapse check |
| 3 | Expose enemy visible intent | Public telegraph printed; exact source/target withheld |
| 4 | Focus once | Menu `[2]`; does not consume Main |
| 5 | At most one Fast item | Menu `[3]`; does not consume Main |
| 6 | One Main action | Menu `[1]` attack, `[4]` defence; closes the round |
| 7 | Enemy action if valid | Resolved automatically, with its own readability record |
| 8 | End checks | Plead, incapacity surrender, collapse, round boundary |

Menu structure is two-level so no prompt lists 24 lines:

```text
[1] Saldır  ->  Grip Strike / Claim the Cut / Bone Scissors / Hell Saw  ->  six slots
[2] Focus
[3] Eşya Kullan  ->  Blood Bag / Clotting Cream
[4] Defans       ->  Guard Flesh / Brace / Stand
[5] Durumu tekrar göster        [0] Bitir
```

Disabled options stay visible, marked `x` with the rules-owned reason, so the player
learns why a choice is closed rather than seeing it disappear.

## 4. Ritual readability (Pillar 5)

Every resolved action — the player's and Jeff's — prints one record answering the five
Pillar 5 questions. Answers are derived from the structured event stream plus a
before/after state snapshot, never from a second calculation:

| Question | Source |
|---|---|
| Ne hedeflendi? | Selected action plus the chosen target slot and limb |
| Ne değişti? | Integrity deltas, limb state transitions, cleared tags, Downed/Guard changes |
| Kan maliyeti? | Negative `blood_changed` deltas with their rule-supplied reasons, plus net Blood |
| Ne kazanıldı? | Blood gains, harvest quality, Marked, Guard/Brace effect, plead pressure, surrender |
| Hangi yeni risk doğdu? | Newly added tags (Bleeding, Unstable, Marked, Hanging), worsened Blood band, Downed, enemy Rage, Ruined limbs, depleted one-use tools, spent Panic Pulse / Limb for Life |

Worked example, seed 42:

```text
+-- RİTÜEL KAYDI — Tur 5 — Sen: Grip Strike -------------------------------+
| 1. Ne hedeflendi?           : Grip Strike -> Jeff: Jeff Left Arm (Sol Kol)
| 2. Ne değişti?              : Jeff / Jeff Left Arm: bütünlük 10 -> 0 (-10)
|                               Jeff / Jeff Left Arm: hasarlı -> harap
| 3. Kan maliyeti?            : 0 Blood (bedava) | Blood 54
| 4. Ne kazanıldı?            : Jeff plead baskısı 2/2
|                               Jeff pes etti
| 5. Hangi yeni risk doğdu?   : Jeff / Jeff Left Arm harap oldu — graft için hasat edilemez
+--------------------------------------------------------------------------+
```

The encounter is resolved before the report window closes, so the action that ends the
fight is the action whose record says the fight ended.

## 5. State screen

At the start of every round both bodies print as ASCII tables covering all six slots
with limb name, integrity, integrity ratio bar, state, and orthogonal tags. Alongside
them: Blood with its configured band, Main-action availability, player statuses,
inventory counts, Jeff's plead pressure and Rage, and the visible intent.

Borders are plain ASCII; only the text carries Turkish characters, and `play_cli`
reconfigures stdout to UTF-8 with replacement so a legacy console degrades instead of
crashing.

## 6. Language

Interface chrome (menus, the five questions, states, tags, slot names) is Turkish.
Rule-owned content names — limbs, actions, items, tags such as `Unstable` and
`Bleeding` — keep their canonical English identifiers from `config/`, so nothing in the
approved content was renamed. Blocking reasons produced by `rules.py` are mapped to
Turkish in `play_render.localize_reason`, which falls through to the original English
wording for any reason it does not recognize; `rules.py` stays the single source of
truth.

## 7. Verification

Run from `Game_att2_Codex_Handoff_v0_6`:

```powershell
python -m game_att2_sim.play_cli --seed 42
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

Local results for this branch:

- `python -m pytest -q` — **131 passed** (91 pre-existing plus 40 new).
- `ruff check` on the three new modules and the new test file — clean.
- `mypy src` under the project's strict settings — clean for the new modules.

Verification notes, recorded rather than hidden:

- The primary local interpreter is an MSYS2 CPython 3.12 with no usable `pip`. Tests
  were run in a venv from that interpreter; `ruff` and `mypy` have no mingw wheels, so
  they were run from a separate venv on the Store CPython 3.12.10.
- Those linters resolve to newer versions than the project pins (`ruff` 0.16,
  `mypy` 2.3). They report 12 findings in files this work did not touch
  (`cli.py`, `rules.py`, `scenarios.py`, `probe.py`, two existing test modules) and one
  now-unnecessary `type: ignore` in `config_loader.py` that is still required when
  `types-PyYAML` is absent. These are pre-existing under newer tool versions and were
  deliberately left alone as out of scope.
- `MANIFEST.md` was not regenerated; the repository contains no manifest generator, and
  its hashes were already stale for several tracked files.

## 8. Ambiguities and assumptions

Per `AGENTS.md`, each is the simplest reversible choice and is listed rather than
silently taken:

1. **Visible intent granularity.** Rule §1.3 requires exposing enemy visible intent but
   does not fix its precision, and Focus must remain worth its cost. Assumption: the
   public telegraph names the action and withholds source and target slots; Focus
   reveals both through the existing `RuleEngine.focus` path, including its Critical
   Head incomplete-information roll.
2. **No legal Main action.** The paper rules assume a Main action is always available
   and define no pass. A player whose Left Arm is gone, with no Blood and no tools, has
   no legal Main action and would deadlock. Assumption: a `forfeit_main` option appears
   **only** when no Main action is legal, and emits
   `play_main_action_forfeited`. Owner review should confirm or replace this.
3. **Round limit.** `--round-limit` (default 50) terminates an endless session with
   `ROUND_LIMIT_REACHED`. This is a harness guard, not a game rule, and is documented as
   such in code.
4. **Jeff's swing stays non-bleeding.** `enemy_attack` is called with the same
   parameters the research shell uses for Jeff (10 base damage, torso, `can_bleed`
   false), so this interface cannot drift from existing Jeff evidence.
5. **Harvest on sever.** As in the research shell, a Clean or Stressed sever harvests
   immediately. Faz 1 records the harvest and reports whether a graftable Right Arm was
   secured, but performs no graft.

## 9. What this does and does not prove

Proven: the round sequence is playable from a terminal; every action's target, change,
cost, gain, and new risk is inspectable; illegal and disabled choices are refused
without mutating state or advancing the RNG; identical seed and inputs reproduce an
identical event stream; Faz 2 content is unreachable.

Not proven: that the fight is fun, fair, readable to anyone but its author, or
correctly tuned. No human other than the implementer has played it. Unity remains
blocked, and Anna, grafting, and the Grafting Table remain outside this interface
until the owner opens Faz 2.
