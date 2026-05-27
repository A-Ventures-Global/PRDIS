"""Worked PRDIS scenarios — using the metric for comparison, which is its
primary intended use (SPEC section 7).

This compares two candidate models on the *same scope* — the canonical
"should we switch models?" question PRDIS is designed to answer.
"""

from prdis import prdis, InferenceSpend, RoutedProfit, Disclosure

SCOPE = "product-recommendation-agent"
WINDOW = "2026-Q1"

disclosure = Disclosure(
    scope=SCOPE,
    window=WINDOW,
    attribution_method="counterfactual holdout (5% control)",
    contribution_margin_basis="trailing 90-day blended contribution margin",
    inference_components_included="token + retrieval + orchestration",
)

# --- Model A: cheaper per call, but lower-quality decisions ---
model_a = prdis(
    RoutedProfit(attributed_revenue=120_000, contribution_margin=0.28),
    InferenceSpend(
        token_compute_cost=2_000,
        retrieval_context_cost=400,
        orchestration_overhead=600,
    ),
    disclosure=disclosure,
)

# --- Model B: 2.5x the inference cost, but routes materially more profit ---
model_b = prdis(
    RoutedProfit(attributed_revenue=190_000, contribution_margin=0.28),
    InferenceSpend(
        token_compute_cost=5_500,
        retrieval_context_cost=900,
        orchestration_overhead=1_100,
    ),
    disclosure=disclosure,
)

print(f"Scope: {SCOPE}  |  Window: {WINDOW}\n")
for name, r in [("Model A (cheap)", model_a), ("Model B (premium)", model_b)]:
    print(
        f"{name:<18}  PRDIS {r.prdis:5.2f}  "
        f"| routed profit ${r.routed_profit:>8,.0f}  "
        f"| inference ${r.inference_spend:>6,.0f}"
    )

winner = "B" if model_b.prdis > model_a.prdis else "A"
print(
    f"\nModel {winner} is more inference-efficient. Note that the more "
    f"expensive model can win on PRDIS\nif the profit it routes outpaces its "
    f"higher cost — which is exactly the tradeoff\nPRDIS is built to surface."
)
