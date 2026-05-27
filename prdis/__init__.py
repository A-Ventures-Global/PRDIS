"""PRDIS — Profit Routed per Dollar of Inference Spend.

An open metric for measuring the economic efficiency of AI inference in
commerce systems, published by A-Ventures Global.

    >>> from prdis import prdis, RoutedProfit, InferenceSpend
    >>> result = prdis(
    ...     RoutedProfit(attributed_revenue=40000, contribution_margin=0.30),
    ...     InferenceSpend(token_compute_cost=1000),
    ... )
    >>> round(result.prdis, 1)
    12.0
"""

from .core import prdis
from .models import Disclosure, InferenceSpend, PRDISResult, RoutedProfit

__version__ = "1.0.0"

__all__ = [
    "prdis",
    "RoutedProfit",
    "InferenceSpend",
    "Disclosure",
    "PRDISResult",
    "__version__",
]
