# PRDIS Specification — v1.0

**PRDIS** — *Profit Routed per Dollar of Inference Spend*

An open metric for measuring the economic efficiency of AI inference in
commerce systems. PRDIS answers one question: **for every dollar spent on
model inference, how much incremental profit did that inference route?**

This document is the normative definition. It is intentionally
implementation-agnostic — it defines *what* to measure and *how to normalize
it*, not how any particular system instruments it.

---

## 1. Motivation

As commerce systems delegate more decisions to AI agents — ranking, routing,
bidding, recommendation, fulfillment selection — inference becomes a real and
growing line item. Teams can measure inference *cost* easily (tokens, GPU
hours, API spend) and measure *outcomes* separately (revenue, conversion,
margin). What's missing is a single ratio that ties the two together and is
comparable across models, time windows, and use cases.

PRDIS is that ratio. It is deliberately a **profit** metric, not a revenue
metric, because inference that drives unprofitable revenue is not efficiency —
it is subsidized growth wearing efficiency's clothes.

---

## 2. Core definition

For a defined **scope** (a system, agent, or workflow) over a defined **window**
(a time period):
A PRDIS of `12.0` means each $1 of inference routes $12 of incremental profit.
Below `1.0`, your inference is destroying value. It's one dimensionless number,
comparable across models, agents, and time.

[**Read the spec →**](SPEC.md) · [**Try the calculator →**](https://a-ventures-global.github.io/prdis/)

---

## Why this exists

Commerce is handing decisions to AI agents — ranking, routing, bidding,
recommendation, fulfillment. Inference is now a line item that grows with every
decision you delegate.

Teams measure inference **cost** easily (tokens, GPU hours, API spend). They
measure **outcomes** separately (revenue, conversion). What's been missing is
the ratio that ties them together and survives a model swap, a pricing change,
or a quarter-over-quarter comparison.

PRDIS is that ratio. And it's deliberately a **profit** metric — inference that
drives unprofitable revenue isn't efficient, it's subsidized growth wearing
efficiency's clothes.

## Install

```bash
pip install prdis
```

## Use it

```python
from prdis import prdis, RoutedProfit, InferenceSpend

result = prdis(
    RoutedProfit(attributed_revenue=40_000, contribution_margin=0.30),
    InferenceSpend(token_compute_cost=1_000),
)

print(result.prdis)            # 12.0
print(result.interpretation)   # "accretive (inference routes more profit than it costs)"
```

Or pass numbers directly if you've already done the arithmetic:

```python
prdis(12_000, 1_000).prdis     # 12.0
```

## The two halves

**Routed Profit** (numerator) is *incremental, attributable* contribution profit
— not your total P&L:
**Inference Spend** (denominator) is *fully loaded* — not just the API bill:
The full normative definition, including attribution and disclosure rules, is
in [SPEC.md](SPEC.md).

## How to actually use the number

PRDIS earns its keep as a **comparison**, not a pass/fail line:

- **Same scope over time** — is your inference getting more or less efficient?
- **Model A vs Model B on the same scope** — does the premium model route enough
  extra profit to justify its higher cost? (Often the answer is surprising —
  see [`examples/scenarios.py`](examples/scenarios.py).)

Absolute thresholds are domain-specific. The trend and the comparison are where
the signal lives.

## Conformance

A PRDIS value is **conformant** only when published with its scope, window,
attribution method, margin basis, and which inference cost components are in the
denominator. Disclosure is the point — it makes two teams' different-but-
reasonable choices *legible and comparable* instead of buried in a dashboard.
See [SPEC §6](SPEC.md#6-disclosure-requirements).

## Adopt it

PRDIS is MIT-licensed and free to implement, extend, and build on. If you use it
in a dashboard, a vendor comparison, or a board deck, you're welcome to cite it
as `PRDIS v1.0`. The vocabulary is the contribution.

---

*PRDIS is published by [A-Ventures Global](https://a-ventures.global), a
commerce-AI application studio. We build the systems that score well on it; the
metric itself belongs to everyone.*
