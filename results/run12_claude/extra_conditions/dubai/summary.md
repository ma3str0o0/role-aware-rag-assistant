# Evaluation results (2026-11-25, mode=offline, corpus=dubai)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: dubai (45 questions)

| Metric | mistagged/A | mistagged/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|
| accuracy_% | 46.2 | 38.5 | 50.0 | 38.5 |
| accuracy_95ci | 46.2% [28.8, 64.5] | 38.5% [22.4, 57.5] | 50.0% [32.1, 67.9] | 38.5% [22.4, 57.5] |
| faithfulness_proxy_% | 76.4 | 89.2 | 81.0 | 89.4 |
| leak_rate_restricted_% | 0.0 | 0.0 | 16.7 | 0.0 |
| leak_rate_95ci | 0.0% [0.0, 39.0] | 0.0% [0.0, 39.0] | 16.7% [3.0, 56.4] | 0.0% [0.0, 39.0] |
| leaks_all_questions | 0 | 0 | 1 | 0 |
| over_refusal_% | 50.0 | 61.5 | 50.0 | 57.7 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1846.7 | 16479.4 | 4986.5 | 8025.8 |
| p95_latency_ms | 3394.9 | 15093.7 | 4092.4 | 16139.4 |
| avg_cost_usd | 0.005187 | 0.00828 | 0.005216 | 0.007975 |
| verifier_blocks | 0 | 3 | 0 | 3 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| dubai/mistagged | 6 | 0 | 0 | 1.0 |
| dubai/mistagged_all_bad_register | 6 | 1 | 0 | 1.0 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
