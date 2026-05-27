"""Data models for PRDIS calculation.

These dataclasses mirror the PRDIS v1.0 specification (see SPEC.md). They exist
to make the inputs and outputs of a PRDIS calculation explicit and
self-documenting rather than passing bare floats around.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class RoutedProfit:
    """The numerator of PRDIS — incremental, attributable contribution profit.

    Routed Profit = (attributed_revenue * contribution_margin) - decision_cost
    """

    attributed_revenue: float
    contribution_margin: float  # decimal, e.g. 0.30 for 30%
    decision_cost: float = 0.0

    def value(self) -> float:
        return (self.attributed_revenue * self.contribution_margin) - self.decision_cost


@dataclass(frozen=True)
class InferenceSpend:
    """The denominator of PRDIS — fully-loaded cost of inference.

    All components are in the same currency unit as RoutedProfit.
    """

    token_compute_cost: float
    retrieval_context_cost: float = 0.0
    orchestration_overhead: float = 0.0
    amortized_fixed_cost: float = 0.0

    def value(self) -> float:
        return (
            self.token_compute_cost
            + self.retrieval_context_cost
            + self.orchestration_overhead
            + self.amortized_fixed_cost
        )


@dataclass(frozen=True)
class Disclosure:
    """Conformance disclosure (SPEC.md section 6).

    A PRDIS value is only conformant when published with these fields.
    """

    scope: str
    window: str
    attribution_method: str
    contribution_margin_basis: str
    inference_components_included: str
    spec_version: str = "PRDIS v1.0"


@dataclass(frozen=True)
class PRDISResult:
    """The output of a PRDIS calculation."""

    prdis: float
    routed_profit: float
    inference_spend: float
    disclosure: Optional[Disclosure] = None

    @property
    def is_accretive(self) -> bool:
        return self.prdis > 1.0

    @property
    def interpretation(self) -> str:
        if self.prdis < 1.0:
            return "value-destroying (inference routes less profit than it costs)"
        if self.prdis == 1.0:
            return "break-even"
        return "accretive (inference routes more profit than it costs)"

    @property
    def is_conformant(self) -> bool:
        """Conformant per SPEC section 6 only if disclosure is attached."""
        return self.disclosure is not None
