# Evaluation results (2026-11-28, mode=offline, corpus=dubai)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: dubai (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 53.8 | 38.5 | 53.8 | 30.8 |
| accuracy_95ci | 53.8% [35.5, 71.2] | 38.5% [22.4, 57.5] | 53.8% [35.5, 71.2] | 30.8% [16.5, 50.0] |
| faithfulness_proxy_% | 80.4 | 87.2 | 74.4 | 90.1 |
| leak_rate_restricted_% | 0.0 | 0.0 | 16.7 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 39.0] | 0.0% [0.0, 39.0] | 16.7% [3.0, 56.4] | 0.0% [0.0, 39.0] |
| leaks_all_questions | 0 | 0 | 1 | 0 |
| over_refusal_% | 34.6 | 50.0 | 38.5 | 57.7 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 2162.6 | 3717.2 | 2468.9 | 4626.0 |
| p95_latency_ms | 3731.3 | 11160.0 | 4764.3 | 13434.8 |
| avg_cost_usd | 0.005987 | 0.009846 | 0.005918 | 0.010723 |
| verifier_blocks | 0 | 4 | 0 | 7 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| dubai/normal | 6 | 0 | 0 | 1.0 |
| dubai/mistagged_all | 6 | 1 | 0 | 1.0 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| dubai | 13 | 0 | 0 | 1.0 |
