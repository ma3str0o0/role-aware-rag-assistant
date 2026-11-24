# Evaluation results (2026-11-24, mode=offline, corpus=real)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: real2 (45 questions)

| Metric | mistagged/A | mistagged/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|
| accuracy_% | 70.0 | 60.0 | 70.0 | 70.0 |
| accuracy_95ci | 70.0% [48.1, 85.5] | 60.0% [38.7, 78.1] | 70.0% [48.1, 85.5] | 70.0% [48.1, 85.5] |
| faithfulness_proxy_% | 80.2 | 93.6 | 82.1 | 92.9 |
| leak_rate_restricted_% | 20.0 | 0.0 | 20.0 | 0.0 |
| leak_rate_95ci | 20.0% [3.6, 62.4] | 0.0% [0.0, 43.4] | 20.0% [3.6, 62.4] | 0.0% [0.0, 43.4] |
| leaks_all_questions | 1 | 0 | 1 | 0 |
| over_refusal_% | 30.0 | 35.0 | 30.0 | 30.0 |
| unanswerable_refused_% | 95.0 | 100.0 | 95.0 | 100.0 |
| avg_latency_ms | 1687.6 | 2538.0 | 1903.0 | 2295.6 |
| p95_latency_ms | 2769.8 | 4482.3 | 3622.5 | 4272.6 |
| avg_cost_usd | 0.004254 | 0.005941 | 0.004397 | 0.005273 |
| verifier_blocks | 0 | 4 | 0 | 1 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| real2/mistagged | 5 | 1 | 0 | 1.0 |
| real2/mistagged_all_bad_register | 5 | 1 | 0 | 1.0 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
