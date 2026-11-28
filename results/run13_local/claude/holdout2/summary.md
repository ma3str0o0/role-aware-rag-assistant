# Evaluation results (2026-11-28, mode=offline, corpus=mock)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: holdout2 (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 77.3 | 72.7 | 72.7 | 77.3 |
| accuracy_95ci | 77.3% [56.6, 89.9] | 72.7% [51.8, 86.8] | 72.7% [51.8, 86.8] | 77.3% [56.6, 89.9] |
| faithfulness_proxy_% | 93.1 | 100.0 | 95.2 | 93.1 |
| leak_rate_restricted_% | 0.0 | 0.0 | 37.5 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 32.4] | 0.0% [0.0, 32.4] | 37.5% [13.7, 69.4] | 0.0% [0.0, 32.4] |
| leaks_all_questions | 0 | 0 | 3 | 0 |
| over_refusal_% | 22.7 | 27.3 | 27.3 | 22.7 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1791.1 | 2411.6 | 2024.2 | 3620.1 |
| p95_latency_ms | 2778.4 | 4502.4 | 3792.6 | 7396.9 |
| avg_cost_usd | 0.003435 | 0.00449 | 0.00379 | 0.006826 |
| verifier_blocks | 0 | 0 | 0 | 5 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| holdout2/normal | 8 | 0 | 0 | 1.0 |
| holdout2/mistagged_all | 8 | 3 | 0 | 0.25 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| holdout2 | 15 | 0 | 0 | 1.0 |
