# Evaluation results (2026-11-28, mode=offline, corpus=dubai)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: dubai (45 questions)

| Metric | normal/A | normal/B | mistagged/A | mistagged/B | mistagged_all/A | mistagged_all/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|---|---|---|---|
| accuracy_% | 57.7 | 57.7 | 57.7 | 57.7 | 57.7 | 57.7 | 57.7 | 57.7 |
| accuracy_95ci | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] | 57.7% [38.9, 74.5] |
| faithfulness_proxy_% | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| leak_rate_restricted_% | 0.0 | 0.0 | 16.7 | 0.0 | 83.3 | 0.0 | 83.3 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 39.0] | 0.0% [0.0, 39.0] | 16.7% [3.0, 56.4] | 0.0% [0.0, 39.0] | 83.3% [43.6, 97.0] | 0.0% [0.0, 39.0] | 83.3% [43.6, 97.0] | 0.0% [0.0, 39.0] |
| leaks_all_questions | 0 | 0 | 1 | 0 | 6 | 0 | 6 | 0 |
| over_refusal_% | 3.8 | 23.1 | 3.8 | 23.1 | 3.8 | 23.1 | 3.8 | 23.1 |
| unanswerable_refused_% | 0.0 | 61.5 | 0.0 | 61.5 | 0.0 | 61.5 | 0.0 | 61.5 |
| avg_latency_ms | 43.9 | 84.8 | 40.6 | 87.9 | 39.2 | 84.5 | 38.0 | 83.9 |
| p95_latency_ms | 45.7 | 151.2 | 43.2 | 155.2 | 40.4 | 152.2 | 39.7 | 150.9 |
| avg_cost_usd | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| verifier_blocks | 0 | 15 | 0 | 15 | 0 | 15 | 0 | 15 |
| n | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| dubai/normal | 6 | 0 | 0 | 1.0 |
| dubai/mistagged | 6 | 1 | 0 | 1.0 |
| dubai/mistagged_all | 6 | 5 | 0 | 0.0625 |
| dubai/mistagged_all_bad_register | 6 | 5 | 0 | 0.0625 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| dubai | 13 | 8 | 0 | 0.0078 |
