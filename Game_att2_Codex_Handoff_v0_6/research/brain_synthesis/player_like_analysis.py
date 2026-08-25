"""Player-like and adversarial diagnostics for the Brain synthesis proposal.

This is an isolated research model. Procedural personas are transparent utility
policies, not claims about real players. The fixture measures structural agency,
policy differentiation, hostile build cases, and causal invariants; it cannot measure
fun, comprehension, fairness, or production balance.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from itertools import combinations
from statistics import mean

from fixture import (
    ACCESS_BRAIN,
    ALL_BY_ID,
    EXECUTION_BRAIN,
    NO_BRAIN,
    SOURCES,
    TECHNIQUE_CARDS,
    BrainPart,
    Card,
    Category,
    DiagnosticSession,
    FixtureConfig,
    Origin,
    RoundObservation,
    Timing,
    Variant,
    deck_for,
    run_session,
)
from run_analysis import BatchMetrics, run_batch


@dataclass(frozen=True)
class Persona:
    persona_id: str
    attack_weight: float
    defence_weight: float
    utility_weight: float
    preparation_weight: float
    item_weight: float
    retention_weight: float
    future_loss_awareness: float = 0.0
    policy: str = "utility"

    def category_weight(self, category: Category) -> float:
        return {
            Category.ATTACK: self.attack_weight,
            Category.DEFENCE: self.defence_weight,
            Category.UTILITY: self.utility_weight,
        }[category]


PERSONAS: tuple[Persona, ...] = (
    Persona("bruiser", 3.0, 0.7, 0.9, 0.35, -2.50, 0.10),
    Persona("survivor", 0.7, 3.0, 1.2, 1.10, 1.60, 0.35),
    Persona("schemer", 1.0, 1.2, 3.0, 1.25, 0.80, 0.60),
    Persona("adapter", 1.4, 1.4, 1.4, 0.80, 0.70, 0.35, 1.50),
    Persona("satisficer", 1.0, 1.0, 1.0, 0.50, 0.50, 0.0, policy="first_legal"),
    Persona("wanderer", 1.0, 1.0, 1.0, 0.50, 0.50, 0.0, policy="random"),
)


@dataclass(frozen=True)
class Plan:
    preparation_index: int | None
    main_index: int | None
    use_item: bool = False


@dataclass(frozen=True)
class DecisionRecord:
    round_number: int
    legal_plan_count: int
    meaningful_plan_count: int
    legal_main_option_count: int
    legal_main_category_count: int
    technique_option_present: bool
    preparation_card_id: str | None
    main_card_id: str | None
    used_item: bool
    selected_categories: tuple[str, ...]
    selected_origins: tuple[str, ...]
    selected_sources: tuple[str, ...]


def _plan_cards(hand: list[Card | None], plan: Plan, item_card: Card | None) -> tuple[Card, ...]:
    cards: list[Card] = []
    if plan.preparation_index is not None:
        card = hand[plan.preparation_index]
        if card is not None:
            cards.append(card)
    if plan.use_item and item_card is not None:
        cards.append(item_card)
    if plan.main_index is not None:
        card = hand[plan.main_index]
        if card is not None:
            cards.append(card)
    return tuple(cards)


def _plan_signature(hand: list[Card | None], plan: Plan, item_card: Card | None) -> tuple[str, ...]:
    cards = _plan_cards(hand, plan, item_card)
    return tuple(
        sorted(
            f"{card.timing.value}:{card.category.value}:{card.origin.value}"
            for card in cards
        )
    )


class PersonaSession(DiagnosticSession):
    def __init__(self, config: FixtureConfig, seed: int, persona: Persona) -> None:
        self.persona = persona
        self.decisions: list[DecisionRecord] = []
        super().__init__(config, seed)

    def legal_plans(self) -> list[Plan]:
        legal = [
            (index, card)
            for index, card in enumerate(self.hand)
            if card is not None and card.is_legal(self.active_sources)
        ]
        preparations: list[tuple[int | None, Card | None, bool]] = [(None, None, False)]
        preparations.extend(
            (index, card, False)
            for index, card in legal
            if card.timing is Timing.PREPARATION
        )
        if self.item_card is not None and self.item_card.is_legal(self.active_sources):
            preparations.append((None, self.item_card, True))

        mains: list[tuple[int | None, Card | None]] = [(None, None)]
        mains.extend((index, card) for index, card in legal if card.timing is Timing.MAIN)

        plans: list[Plan] = []
        for preparation_index, preparation_card, use_item in preparations:
            for main_index, main_card in mains:
                if preparation_card is None and main_card is None:
                    continue
                preparation_sources = set(preparation_card.sources) if preparation_card else set()
                main_sources = set(main_card.sources) if main_card else set()
                if preparation_sources & main_sources:
                    continue
                plans.append(Plan(preparation_index, main_index, use_item))
        return plans

    def _score_plan(self, plan: Plan, round_number: int) -> float:
        cards = _plan_cards(self.hand, plan, self.item_card)
        score = 0.0
        if plan.main_index is not None:
            score += 5.0
        if plan.preparation_index is not None or plan.use_item:
            score += self.persona.preparation_weight
        if plan.use_item:
            score += self.persona.item_weight
        for card in cards:
            score += self.persona.category_weight(card.category)
            if (
                round_number == self.config.source_loss_round
                and self.config.lost_source in card.sources
            ):
                score += self.persona.future_loss_awareness

        selected_ids = {card.card_id for card in cards}
        held_values = [
            self.persona.category_weight(card.category)
            for card in self.hand
            if card is not None and card.card_id not in selected_ids
        ]
        if held_values:
            score += self.persona.retention_weight * max(held_values)
        return score

    def _select_plan(self, plans: list[Plan], round_number: int) -> Plan:
        main_plans = [plan for plan in plans if plan.main_index is not None]
        candidates = main_plans or plans
        if self.persona.policy == "random":
            return self.rng.choice(candidates)
        if self.persona.policy == "first_legal":
            return min(
                candidates,
                key=lambda plan: (
                    plan.main_index is None,
                    plan.preparation_index is None and not plan.use_item,
                    _plan_signature(self.hand, plan, self.item_card),
                ),
            )
        return max(
            candidates,
            key=lambda plan: (
                self._score_plan(plan, round_number),
                _plan_signature(self.hand, plan, self.item_card),
            ),
        )

    def _play_round(self, observation: RoundObservation) -> None:
        plans = self.legal_plans()
        if not plans:
            self.decisions.append(
                DecisionRecord(
                    observation.round_number,
                    0,
                    0,
                    0,
                    0,
                    False,
                    None,
                    None,
                    False,
                    (),
                    (),
                    (),
                )
            )
            return

        meaningful = {
            _plan_signature(self.hand, plan, self.item_card) for plan in plans
        }
        legal_main_cards = [
            card
            for card in self.hand
            if card is not None
            and card.is_legal(self.active_sources)
            and card.timing is Timing.MAIN
        ]
        legal_action_cards = [
            card
            for card in self.hand
            if card is not None and card.is_legal(self.active_sources)
        ]
        plan = self._select_plan(plans, observation.round_number)
        selected_cards = _plan_cards(self.hand, plan, self.item_card)
        preparation_id = None
        main_id = None
        if plan.preparation_index is not None:
            preparation = self.hand[plan.preparation_index]
            preparation_id = preparation.card_id if preparation is not None else None
            self.hand[plan.preparation_index] = None
            observation.preparations_used = 1
        elif plan.use_item and self.item_card is not None:
            preparation_id = self.item_card.card_id
            self.item_uses[self.item_card.card_id] -= 1
            self.item_card = None
            observation.preparations_used = 1
            observation.item_actions = 1

        if plan.main_index is not None:
            main = self.hand[plan.main_index]
            main_id = main.card_id if main is not None else None
            self.hand[plan.main_index] = None
            observation.mains_used = 1

        self.decisions.append(
            DecisionRecord(
                observation.round_number,
                len(plans),
                len(meaningful),
                len(legal_main_cards),
                len({card.category for card in legal_main_cards}),
                any(card.origin is Origin.TECHNIQUE for card in legal_action_cards),
                preparation_id,
                main_id,
                plan.use_item,
                tuple(card.category.value for card in selected_cards),
                tuple(card.origin.value for card in selected_cards),
                tuple(sorted({source for card in selected_cards for source in card.sources})),
            )
        )


@dataclass(frozen=True)
class PersonaMetrics:
    persona: str
    rounds: int
    main_play_pct: float
    preparation_play_pct: float
    item_use_pct: float
    meaningful_choice_pct: float
    forced_signature_pct: float
    multiple_main_options_pct: float
    cross_category_main_choice_pct: float
    technique_option_visible_pct: float
    avg_legal_plans: float
    main_attack_pct: float
    main_defence_pct: float
    main_utility_pct: float
    technique_selection_pct: float
    max_card_selection_pct: float


def _pct(numerator: float, denominator: float) -> float:
    return round(100.0 * numerator / denominator, 3) if denominator else 0.0


def run_persona_batch(
    persona: Persona,
    configs: Iterable[FixtureConfig],
    seeds_per_config: int,
) -> PersonaMetrics:
    configs = tuple(configs)
    if not configs:
        raise ValueError("at least one fixture configuration is required")
    decisions: list[DecisionRecord] = []
    card_selections: Counter[str] = Counter()
    for config_index, config in enumerate(configs):
        for seed in range(seeds_per_config):
            session = PersonaSession(config, seed + config_index * 100_003, persona)
            session.run()
            decisions.extend(session.decisions)
            for decision in session.decisions:
                if decision.preparation_card_id:
                    card_selections[decision.preparation_card_id] += 1
                if decision.main_card_id:
                    card_selections[decision.main_card_id] += 1

    rounds = len(decisions)
    categories = Counter(
        category for decision in decisions for category in decision.selected_categories
    )
    origins = Counter(origin for decision in decisions for origin in decision.selected_origins)
    selected_total = sum(categories.values())
    main_categories = Counter()
    for decision in decisions:
        if decision.main_card_id is not None:
            main_categories[ALL_BY_ID[decision.main_card_id].category.value] += 1
    main_total = sum(main_categories.values())
    card_total = sum(card_selections.values())
    return PersonaMetrics(
        persona=persona.persona_id,
        rounds=rounds,
        main_play_pct=_pct(sum(d.main_card_id is not None for d in decisions), rounds),
        preparation_play_pct=_pct(
            sum(d.preparation_card_id is not None for d in decisions), rounds
        ),
        item_use_pct=_pct(sum(d.used_item for d in decisions), rounds),
        meaningful_choice_pct=_pct(
            sum(d.meaningful_plan_count >= 2 for d in decisions), rounds
        ),
        forced_signature_pct=_pct(
            sum(d.meaningful_plan_count <= 1 for d in decisions), rounds
        ),
        multiple_main_options_pct=_pct(
            sum(d.legal_main_option_count >= 2 for d in decisions), rounds
        ),
        cross_category_main_choice_pct=_pct(
            sum(d.legal_main_category_count >= 2 for d in decisions), rounds
        ),
        technique_option_visible_pct=_pct(
            sum(d.technique_option_present for d in decisions), rounds
        ),
        avg_legal_plans=round(mean(d.legal_plan_count for d in decisions), 3),
        main_attack_pct=_pct(main_categories[Category.ATTACK.value], main_total),
        main_defence_pct=_pct(main_categories[Category.DEFENCE.value], main_total),
        main_utility_pct=_pct(main_categories[Category.UTILITY.value], main_total),
        technique_selection_pct=_pct(origins[Origin.TECHNIQUE.value], selected_total),
        max_card_selection_pct=_pct(max(card_selections.values(), default=0), card_total),
    )


@dataclass(frozen=True)
class PackageSearchRow:
    technique_count: int
    package_count: int
    constrained_package_count: int
    worst_main_drought_pct: float
    average_main_drought_pct: float
    best_main_drought_pct: float
    worst_post_loss_drought_pct: float
    worst_prep_main_coverage_pct: float
    average_prep_main_coverage_pct: float
    best_prep_main_coverage_pct: float
    worst_technique_share_pct: float
    average_technique_share_pct: float
    best_technique_share_pct: float
    worst_source_diversity: float
    average_source_diversity: float
    best_source_diversity: float


def package_is_well_formed(cards: tuple[Card, ...]) -> bool:
    timings = {card.timing for card in cards}
    sources = {source for card in cards for source in card.sources}
    return Timing.MAIN in timings and Timing.PREPARATION in timings and len(sources) >= 2


def search_technique_packages(runs: int) -> tuple[list[PackageSearchRow], list[tuple[str, ...]]]:
    rows: list[PackageSearchRow] = []
    constrained_three_card_packages: list[tuple[str, ...]] = []
    for count in (2, 3, 4):
        all_packages = list(combinations(TECHNIQUE_CARDS, count))
        constrained = [package for package in all_packages if package_is_well_formed(package)]
        if count == 3:
            constrained_three_card_packages = [
                tuple(card.card_id for card in package)
                for package in constrained
                if sum(card.timing is Timing.MAIN for card in package) == 2
            ]
        metrics: list[BatchMetrics] = []
        for package in constrained:
            metrics.append(
                run_batch(
                    FixtureConfig(
                        Variant.SYNTHESIS,
                        attention_slots=4,
                        commitment_guarantee=False,
                        item_uses_attention_slot=False,
                        technique_ids=tuple(card.card_id for card in package),
                        brain=NO_BRAIN,
                    ),
                    runs,
                )
            )
        coverage = [metric.prep_main_coverage_pct for metric in metrics]
        drought = [metric.main_drought_pct for metric in metrics]
        post_loss_drought = [metric.post_loss_main_drought_pct for metric in metrics]
        technique_share = [metric.technique_share_pct for metric in metrics]
        diversity = [metric.avg_unique_sources for metric in metrics]
        rows.append(
            PackageSearchRow(
                technique_count=count,
                package_count=len(all_packages),
                constrained_package_count=len(constrained),
                worst_main_drought_pct=max(drought),
                average_main_drought_pct=round(mean(drought), 3),
                best_main_drought_pct=min(drought),
                worst_post_loss_drought_pct=max(post_loss_drought),
                worst_prep_main_coverage_pct=min(coverage),
                average_prep_main_coverage_pct=round(mean(coverage), 3),
                best_prep_main_coverage_pct=max(coverage),
                worst_technique_share_pct=min(technique_share),
                average_technique_share_pct=round(mean(technique_share), 3),
                best_technique_share_pct=max(technique_share),
                worst_source_diversity=min(diversity),
                average_source_diversity=round(mean(diversity), 3),
                best_source_diversity=max(diversity),
            )
        )
    return rows, constrained_three_card_packages


@dataclass(frozen=True)
class FuzzResult:
    cases: int
    observed_rounds: int
    invariant_failures: int


@dataclass(frozen=True)
class CandidateBrainMetrics:
    brain: str
    average_main_drought_pct: float
    worst_main_drought_pct: float
    average_post_loss_drought_pct: float
    worst_post_loss_drought_pct: float
    average_prep_main_coverage_pct: float
    average_technique_share_pct: float
    average_attack_share_pct: float


def analyze_candidate_brains(
    package_ids: list[tuple[str, ...]], runs: int
) -> list[CandidateBrainMetrics]:
    rows: list[CandidateBrainMetrics] = []
    for brain in (NO_BRAIN, ACCESS_BRAIN):
        metrics = [
            run_batch(
                FixtureConfig(
                    Variant.SYNTHESIS,
                    attention_slots=4,
                    item_uses_attention_slot=False,
                    commitment_guarantee=False,
                    technique_ids=ids,
                    brain=brain,
                ),
                runs,
            )
            for ids in package_ids
        ]
        rows.append(
            CandidateBrainMetrics(
                brain=brain.part_id,
                average_main_drought_pct=round(mean(m.main_drought_pct for m in metrics), 3),
                worst_main_drought_pct=max(m.main_drought_pct for m in metrics),
                average_post_loss_drought_pct=round(
                    mean(m.post_loss_main_drought_pct for m in metrics), 3
                ),
                worst_post_loss_drought_pct=max(
                    m.post_loss_main_drought_pct for m in metrics
                ),
                average_prep_main_coverage_pct=round(
                    mean(m.prep_main_coverage_pct for m in metrics), 3
                ),
                average_technique_share_pct=round(
                    mean(m.technique_share_pct for m in metrics), 3
                ),
                average_attack_share_pct=round(
                    mean(m.attack_share_pct for m in metrics), 3
                ),
            )
        )
    return rows


def fuzz_state_invariants(cases: int, seed: int = 91_771) -> FuzzResult:
    rng = random.Random(seed)
    observed_rounds = 0
    failures = 0
    technique_ids = [card.card_id for card in TECHNIQUE_CARDS]
    brains: tuple[BrainPart, ...] = (NO_BRAIN, ACCESS_BRAIN, EXECUTION_BRAIN)
    for case in range(cases):
        rounds = rng.randint(1, 9)
        loss_round = rng.randint(1, rounds)
        package_size = rng.randint(1, len(technique_ids))
        config = FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=rng.randint(3, 6),
            rounds=rounds,
            source_loss_round=loss_round,
            lost_source=rng.choice(SOURCES),
            technique_ids=tuple(rng.sample(technique_ids, package_size)),
            commitment_guarantee=rng.choice((False, True)),
            item_uses_attention_slot=rng.choice((False, True)),
            brain=rng.choice(brains),
        )
        result = run_session(config, case + seed)
        observed_rounds += len(result.observations)
        for observation in result.observations:
            invalid = (
                observation.preparations_used > 1
                or observation.mains_used > 1
                or observation.item_actions > observation.preparations_used
                or observation.invalid_action_attempts > 0
                or observation.source_commitment_violations > 0
            )
            if invalid:
                failures += 1
            if config.commitment_guarantee:
                active_sources = set(SOURCES)
                if observation.round_number > config.source_loss_round:
                    active_sources.discard(config.lost_source)
                legal_main_exists = any(
                    card.timing is Timing.MAIN and card.is_legal(active_sources)
                    for card in deck_for(config)
                )
                if legal_main_exists and observation.legal_main_cards == 0:
                    failures += 1
    return FuzzResult(cases, observed_rounds, failures)


def category_distance(left: PersonaMetrics, right: PersonaMetrics) -> float:
    left_values = (
        left.main_attack_pct,
        left.main_defence_pct,
        left.main_utility_pct,
    )
    right_values = (
        right.main_attack_pct,
        right.main_defence_pct,
        right.main_utility_pct,
    )
    return round(sum(abs(a - b) for a, b in zip(left_values, right_values)) / 2.0, 3)


def render_report(
    package_rows: list[PackageSearchRow],
    candidate_rows: list[CandidateBrainMetrics],
    persona_rows: list[PersonaMetrics],
    fuzz: FuzzResult,
    package_runs: int,
    persona_runs: int,
    package_count: int,
) -> str:
    lines = [
        "# Player-like Brain Synthesis Diagnostic",
        "",
        "Status: isolated synthetic evidence; procedural personas are not humans.",
        "",
        "## Adversarial Technique-package search",
        "",
        f"Seeded sessions per package: **{package_runs}**",
        "",
        "| Technique cards | All packages | Well-formed packages | Main drought best / avg / worst | Worst post-loss | Prep+Main worst / avg / best | Technique share worst / avg / best | Source diversity worst / avg / best |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in package_rows:
        lines.append(
            f"| {row.technique_count} | {row.package_count} | {row.constrained_package_count} "
            f"| {row.best_main_drought_pct:.2f}% / {row.average_main_drought_pct:.2f}% / {row.worst_main_drought_pct:.2f}% "
            f"| {row.worst_post_loss_drought_pct:.2f}% "
            f"| {row.worst_prep_main_coverage_pct:.2f}% / {row.average_prep_main_coverage_pct:.2f}% / {row.best_prep_main_coverage_pct:.2f}% "
            f"| {row.worst_technique_share_pct:.2f}% / {row.average_technique_share_pct:.2f}% / {row.best_technique_share_pct:.2f}% "
            f"| {row.worst_source_diversity:.2f} / {row.average_source_diversity:.2f} / {row.best_source_diversity:.2f} |"
        )

    lines.extend(
        [
            "",
            "## Optimized candidate: three Techniques, two Main plus one Preparation",
            "",
            "| Brain | Main drought avg / worst | Post-loss avg / worst | Prep+Main coverage | Technique share | Attack share |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in candidate_rows:
        lines.append(
            f"| {row.brain} | {row.average_main_drought_pct:.2f}% / {row.worst_main_drought_pct:.2f}% "
            f"| {row.average_post_loss_drought_pct:.2f}% / {row.worst_post_loss_drought_pct:.2f}% "
            f"| {row.average_prep_main_coverage_pct:.2f}% | {row.average_technique_share_pct:.2f}% "
            f"| {row.average_attack_share_pct:.2f}% |"
        )
    lines.extend(
        [
            "",
            "## Procedural-persona results",
            "",
            f"Personas used every well-formed three-Technique package ({package_count}) across **{persona_runs}** seeds each.",
            "",
            "| Persona | Main | Preparation | Item use | 2+ Main options | 2+ Main categories | Technique visible | Avg legal plans | Main Attack | Main Defence | Main Utility | Technique use | Max-card share |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in persona_rows:
        lines.append(
            f"| {row.persona} | {row.main_play_pct:.2f}% | {row.preparation_play_pct:.2f}% "
            f"| {row.item_use_pct:.2f}% | {row.multiple_main_options_pct:.2f}% "
            f"| {row.cross_category_main_choice_pct:.2f}% | {row.technique_option_visible_pct:.2f}% "
            f"| {row.avg_legal_plans:.2f} | {row.main_attack_pct:.2f}% "
            f"| {row.main_defence_pct:.2f}% | {row.main_utility_pct:.2f}% "
            f"| {row.technique_selection_pct:.2f}% | {row.max_card_selection_pct:.2f}% |"
        )

    utility_personas = [row for row in persona_rows if row.persona in {"bruiser", "survivor", "schemer"}]
    distances = [
        category_distance(left, right)
        for left, right in combinations(utility_personas, 2)
    ]
    lines.extend(
        [
            "",
            "## State-machine fuzzing",
            "",
            f"- Generated configurations: **{fuzz.cases}**",
            f"- Observed rounds: **{fuzz.observed_rounds}**",
            f"- Causal/action-budget invariant failures: **{fuzz.invariant_failures}**",
            f"- Minimum category-style distance among Bruiser/Survivor/Schemer: **{min(distances):.2f} percentage points**",
            "",
            "These metrics establish structural reachability, policy differentiation, and invariant resistance only.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_report(package_runs: int, persona_runs: int, fuzz_cases: int) -> str:
    package_rows, package_ids = search_technique_packages(package_runs)
    candidate_rows = analyze_candidate_brains(package_ids, package_runs)
    configs = [
        FixtureConfig(
            Variant.SYNTHESIS,
            attention_slots=4,
            commitment_guarantee=False,
            item_uses_attention_slot=False,
            technique_ids=ids,
            brain=ACCESS_BRAIN,
        )
        for ids in package_ids
    ]
    persona_rows = [
        run_persona_batch(persona, configs, persona_runs) for persona in PERSONAS
    ]
    fuzz = fuzz_state_invariants(fuzz_cases)
    return render_report(
        package_rows,
        candidate_rows,
        persona_rows,
        fuzz,
        package_runs,
        persona_runs,
        len(package_ids),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-runs", type=int, default=500)
    parser.add_argument("--persona-runs", type=int, default=250)
    parser.add_argument("--fuzz-cases", type=int, default=10_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if min(args.package_runs, args.persona_runs, args.fuzz_cases) < 1:
        raise SystemExit("all run counts must be positive")
    print(build_report(args.package_runs, args.persona_runs, args.fuzz_cases), end="")


if __name__ == "__main__":
    main()
