"""Core PRDIS calculation.

Profit Routed per Dollar of Inference Spend.

    PRDIS = Routed Profit / Inference Spend

See SPEC.md for the normative definition. This module is intentionally small —
PRDIS is a definition first and code second. The code exists to make the
definition runnable and unambiguous.
"""

from __future__ import annotations

from typing import Optional, Union

from .models import (
    Disclosure,
    InferenceSpend,
    PRDISResult,
    RoutedProfit,
)

Number = Union[int, float]


def prdis(
    routed_profit: Union[RoutedProfit, Number],
    inference_spend: Union[InferenceSpend, Number],
    disclosure: Optional[Disclosure] = None,
) -> PRDISResult:
    """Compute PRDIS.

    Accepts either structured inputs (RoutedProfit / InferenceSpend) or bare
    numbers for quick calculation.

    Args:
        routed_profit: A RoutedProfit object, or a precomputed profit number.
        inference_spend: An InferenceSpend object, or a precomputed spend number.
        disclosure: Optional conformance disclosure (SPEC section 6).

    Returns:
        A PRDISResult.

    Raises:
        ValueError: if inference spend is zero or negative.
    """
    profit_value = (
        routed_profit.value()
        if isinstance(routed_profit, RoutedProfit)
        else float(routed_profit)
    )
    spend_value = (
        inference_spend.value()
        if isinstance(inference_spend, InferenceSpend)
        else float(inference_spend)
    )

    if spend_value <= 0:
        raise ValueError(
            "Inference spend must be positive. PRDIS is undefined when no "
            "inference cost is incurred."
        )

    return PRDISResult(
        prdis=profit_value / spend_value,
        routed_profit=profit_value,
        inference_spend=spend_value,
        disclosure=disclosure,
    )


__all__ = [
    "prdis",
    "RoutedProfit",
    "InferenceSpend",
    "Disclosure",
    "PRDISResult",
]
