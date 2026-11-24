# Evaluation results (2026-11-24, mode=offline, corpus=mock)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: holdout2 (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 72.7 | 81.8 | 72.7 | 77.3 |
| accuracy_95ci | 72.7% [51.8, 86.8] | 81.8% [61.5, 92.7] | 72.7% [51.8, 86.8] | 77.3% [56.6, 89.9] |
| faithfulness_proxy_% | 94.4 | 98.6 | 87.3 | 98.8 |
| leak_rate_restricted_% | 0.0 | 0.0 | 50.0 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 32.4] | 0.0% [0.0, 32.4] | 50.0% [21.5, 78.5] | 0.0% [0.0, 32.4] |
| leaks_all_questions | 0 | 0 | 4 | 0 |
| over_refusal_% | 18.2 | 18.2 | 22.7 | 22.7 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1612.3 | 2489.3 | 1921.8 | 3208.2 |
| p95_latency_ms | 2492.9 | 4656.8 | 3873.9 | 5332.3 |
| avg_cost_usd | 0.002813 | 0.004255 | 0.0037 | 0.005856 |
| verifier_blocks | 0 | 0 | 0 | 2 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| holdout2/normal | 8 | 0 | 0 | 1.0 |
| holdout2/mistagged_all | 8 | 4 | 0 | 0.125 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| holdout2 | 15 | 0 | 0 | 1.0 |
