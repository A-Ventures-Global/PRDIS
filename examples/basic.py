"""Minimal PRDIS example — the five-line version."""

from prdis import prdis, InferenceSpend, RoutedProfit

result = prdis(
    RoutedProfit(attributed_revenue=40_000, contribution_margin=0.30),
    InferenceSpend(token_compute_cost=1_000),
)

print(f"PRDIS = {result.prdis:.1f}  ({result.interpretation})")
