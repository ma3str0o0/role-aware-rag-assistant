# Evaluation results (2026-11-28, mode=offline, corpus=real)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: real2 (45 questions)

| Metric | normal/A | normal/B | mistagged_all/A | mistagged_all/B |
|---|---|---|---|---|
| accuracy_% | 65.0 | 65.0 | 65.0 | 65.0 |
| accuracy_95ci | 65.0% [43.3, 81.9] | 65.0% [43.3, 81.9] | 65.0% [43.3, 81.9] | 65.0% [43.3, 81.9] |
| faithfulness_proxy_% | 90.3 | 92.4 | 92.9 | 96.8 |
| leak_rate_restricted_% | 0.0 | 0.0 | 0.0 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] |
| leaks_all_questions | 0 | 0 | 0 | 0 |
| over_refusal_% | 30.0 | 30.0 | 30.0 | 30.0 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1932.2 | 2507.6 | 2390.7 | 3160.5 |
| p95_latency_ms | 3600.4 | 4967.0 | 5214.4 | 7353.3 |
| avg_cost_usd | 0.004802 | 0.006227 | 0.004789 | 0.006323 |
| verifier_blocks | 0 | 1 | 0 | 2 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| real2/normal | 5 | 0 | 0 | 1.0 |
| real2/mistagged_all | 5 | 0 | 0 | 1.0 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| real2 | 20 | 0 | 0 | 1.0 |
