# Evaluation results (2026-11-28, mode=offline, corpus=real)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: real2 (45 questions)

| Metric | normal/A | normal/B | mistagged/A | mistagged/B | mistagged_all/A | mistagged_all/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|---|---|---|---|
| accuracy_% | 55.0 | 50.0 | 55.0 | 50.0 | 55.0 | 50.0 | 55.0 | 50.0 |
| accuracy_95ci | 55.0% [34.2, 74.2] | 50.0% [29.9, 70.1] | 55.0% [34.2, 74.2] | 50.0% [29.9, 70.1] | 55.0% [34.2, 74.2] | 50.0% [29.9, 70.1] | 55.0% [34.2, 74.2] | 50.0% [29.9, 70.1] |
| faithfulness_proxy_% | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| leak_rate_restricted_% | 0.0 | 0.0 | 0.0 | 0.0 | 60.0 | 0.0 | 60.0 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 0.0% [0.0, 43.4] | 60.0% [23.1, 88.2] | 0.0% [0.0, 43.4] | 60.0% [23.1, 88.2] | 0.0% [0.0, 43.4] |
| leaks_all_questions | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 0 |
| over_refusal_% | 0.0 | 10.0 | 0.0 | 10.0 | 0.0 | 10.0 | 0.0 | 10.0 |
| unanswerable_refused_% | 0.0 | 70.0 | 0.0 | 70.0 | 0.0 | 70.0 | 0.0 | 70.0 |
| avg_latency_ms | 28.4 | 33.7 | 28.8 | 32.7 | 28.7 | 33.7 | 26.7 | 31.6 |
| p95_latency_ms | 31.1 | 40.5 | 31.3 | 38.2 | 31.7 | 40.3 | 30.5 | 38.0 |
| avg_cost_usd | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| verifier_blocks | 0 | 19 | 0 | 19 | 0 | 20 | 0 | 20 |
| n | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| real2/normal | 5 | 0 | 0 | 1.0 |
| real2/mistagged | 5 | 0 | 0 | 1.0 |
| real2/mistagged_all | 5 | 3 | 0 | 0.25 |
| real2/mistagged_all_bad_register | 5 | 3 | 0 | 0.25 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| real2 | 20 | 14 | 0 | 0.0001 |
