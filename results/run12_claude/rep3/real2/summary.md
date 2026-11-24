# Evaluation results (2026-11-24, mode=offline, corpus=real)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: real2 (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 70.0 | 70.0 | 65.0 | 70.0 |
| accuracy_95ci | 70.0% [48.1, 85.5] | 70.0% [48.1, 85.5] | 65.0% [43.3, 81.9] | 70.0% [48.1, 85.5] |
| faithfulness_proxy_% | 90.0 | 89.3 | 87.5 | 95.0 |
| leak_rate_restricted_% | 0.0 | 0.0 | 20.0 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 20.0% [3.6, 62.4] | 0.0% [0.0, 43.4] |
| leaks_all_questions | 0 | 0 | 1 | 0 |
| over_refusal_% | 30.0 | 30.0 | 30.0 | 30.0 |
| unanswerable_refused_% | 95.0 | 100.0 | 95.0 | 100.0 |
| avg_latency_ms | 1593.0 | 2314.1 | 2193.9 | 2859.1 |
| p95_latency_ms | 2512.3 | 4060.4 | 5611.5 | 5801.2 |
| avg_cost_usd | 0.004172 | 0.005537 | 0.004337 | 0.005593 |
| verifier_blocks | 0 | 1 | 0 | 2 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| real2/normal | 5 | 0 | 0 | 1.0 |
| real2/mistagged_all | 5 | 1 | 0 | 1.0 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| real2 | 20 | 1 | 0 | 1.0 |
