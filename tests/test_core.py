"""Tests for the PRDIS core calculation."""

import pytest

from prdis import Disclosure, InferenceSpend, RoutedProfit, prdis


def test_basic_ratio_from_numbers():
    result = prdis(12000, 1000)
    assert result.prdis == 12.0
    assert result.is_accretive


def test_structured_inputs():
    result = prdis(
        RoutedProfit(attributed_revenue=40000, contribution_margin=0.30),
        InferenceSpend(token_compute_cost=1000),
    )
    # (40000 * 0.30) - 0 = 12000 ; 12000 / 1000 = 12.0
    assert result.prdis == 12.0


def test_routed_profit_subtracts_decision_cost():
    rp = RoutedProfit(
        attributed_revenue=40000, contribution_margin=0.30, decision_cost=2000
    )
    # 12000 - 2000 = 10000
    assert rp.value() == 10000


def test_inference_spend_sums_all_components():
    spend = InferenceSpend(
        token_compute_cost=1000,
        retrieval_context_cost=200,
        orchestration_overhead=300,
        amortized_fixed_cost=500,
    )
    assert spend.value() == 2000


def test_break_even():
    result = prdis(1000, 1000)
    assert result.prdis == 1.0
    assert not result.is_accretive
    assert result.interpretation == "break-even"


def test_value_destroying():
    result = prdis(500, 1000)
    assert result.prdis == 0.5
    assert "value-destroying" in result.interpretation


def test_zero_spend_raises():
    with pytest.raises(ValueError):
        prdis(1000, 0)


def test_negative_spend_raises():
    with pytest.raises(ValueError):
        prdis(1000, -50)


def test_conformance_requires_disclosure():
    bare = prdis(12000, 1000)
    assert not bare.is_conformant

    disclosed = prdis(
        12000,
        1000,
        disclosure=Disclosure(
            scope="ranking-agent",
            window="2026-Q1",
            attribution_method="counterfactual holdout",
            contribution_margin_basis="trailing 90-day blended",
            inference_components_included="token + retrieval + orchestration",
        ),
    )
    assert disclosed.is_conformant
    assert disclosed.disclosure.spec_version == "PRDIS v1.0"
