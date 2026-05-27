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
