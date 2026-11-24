# Evaluation results (2026-11-24, mode=offline, corpus=mock)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: holdout2 (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 72.7 | 72.7 | 72.7 | 68.2 |
| accuracy_95ci | 72.7% [51.8, 86.8] | 72.7% [51.8, 86.8] | 72.7% [51.8, 86.8] | 68.2% [47.3, 83.6] |
| faithfulness_proxy_% | 95.6 | 100.0 | 86.9 | 98.3 |
| leak_rate_restricted_% | 0.0 | 0.0 | 37.5 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 32.4] | 0.0% [0.0, 32.4] | 37.5% [13.7, 69.4] | 0.0% [0.0, 32.4] |
| leaks_all_questions | 0 | 0 | 3 | 0 |
| over_refusal_% | 27.3 | 27.3 | 18.2 | 31.8 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1510.8 | 2471.2 | 1946.1 | 3166.3 |
| p95_latency_ms | 2480.8 | 4004.4 | 4286.0 | 6531.6 |
| avg_cost_usd | 0.002716 | 0.004584 | 0.003638 | 0.006091 |
| verifier_blocks | 0 | 1 | 0 | 7 |
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
