# Evaluation results (2026-11-24, mode=offline, corpus=mock)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: holdout2 (45 questions)

| Metric | mistagged/A | mistagged/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|
| accuracy_% | 72.7 | 72.7 | 72.7 | 68.2 |
| accuracy_95ci | 72.7% [51.8, 86.8] | 72.7% [51.8, 86.8] | 72.7% [51.8, 86.8] | 68.2% [47.3, 83.6] |
| faithfulness_proxy_% | 91.5 | 100.0 | 97.5 | 100.0 |
| leak_rate_restricted_% | 12.5 | 0.0 | 50.0 | 12.5 |
| leak_rate_95ci | 12.5% [2.2, 47.1] | 0.0% [0.0, 32.4] | 50.0% [21.5, 78.5] | 12.5% [2.2, 47.1] |
| leaks_all_questions | 1 | 0 | 4 | 1 |
| over_refusal_% | 22.7 | 22.7 | 27.3 | 31.8 |
| unanswerable_refused_% | 100.0 | 100.0 | 100.0 | 100.0 |
| avg_latency_ms | 1634.2 | 2700.4 | 1905.6 | 3358.6 |
| p95_latency_ms | 3092.6 | 4502.6 | 3937.3 | 6547.8 |
| avg_cost_usd | 0.002876 | 0.004786 | 0.003506 | 0.006405 |
| verifier_blocks | 0 | 2 | 0 | 4 |
| n | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| holdout2/mistagged | 8 | 1 | 0 | 1.0 |
| holdout2/mistagged_all_bad_register | 8 | 3 | 0 | 0.25 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
