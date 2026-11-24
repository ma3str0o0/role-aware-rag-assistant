# Evaluation results (2026-11-24, mode=offline, corpus=dubai)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: dubai (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 42.3 | 38.5 | 50.0 | 34.6 |
| accuracy_95ci | 42.3% [25.5, 61.1] | 38.5% [22.4, 57.5] | 50.0% [32.1, 67.9] | 34.6% [19.4, 53.8] |
| faithfulness_proxy_% | 74.9 | 89.2 | 81.0 | 93.3 |
| leak_rate_restricted_% | 0.0 | 0.0 | 16.7 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 39.0] | 0.0% [0.0, 39.0] | 16.7% [3.0, 56.4] | 0.0% [0.0, 39.0] |
| leaks_all_questions | 0 | 0 | 1 | 0 |
| over_refusal_% | 50.0 | 61.5 | 50.0 | 61.5 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1919.8 | 3248.2 | 2295.9 | 3293.2 |
| p95_latency_ms | 3833.1 | 11486.6 | 5083.0 | 7527.6 |
| avg_cost_usd | 0.005188 | 0.0086 | 0.005207 | 0.008353 |
| verifier_blocks | 0 | 4 | 0 | 4 |
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
