# Evaluation results (2026-11-28, mode=offline, corpus=mock)

Rates in brackets are 95% Wilson confidence intervals.

## Test set: holdout2 (45 questions)

| Metric | normal/A | normal/B | mistagged/A | mistagged/B | mistagged_all/A | mistagged_all/B | mistagged_all_bad_register/A | mistagged_all_bad_register/B |
|---|---|---|---|---|---|---|---|---|
| accuracy_% | 86.4 | 86.4 | 86.4 | 86.4 | 86.4 | 86.4 | 86.4 | 86.4 |
| accuracy_95ci | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] | 86.4% [66.7, 95.3] |
| faithfulness_proxy_% | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| leak_rate_restricted_% | 0.0 | 0.0 | 12.5 | 0.0 | 100.0 | 0.0 | 100.0 | 12.5 |
| leak_rate_95ci | 0.0% [0.0, 32.4] | 0.0% [0.0, 32.4] | 12.5% [2.2, 47.1] | 0.0% [0.0, 32.4] | 100.0% [67.6, 100.0] | 0.0% [0.0, 32.4] | 100.0% [67.6, 100.0] | 12.5% [2.2, 47.1] |
| leaks_all_questions | 0 | 0 | 1 | 0 | 9 | 0 | 9 | 1 |
| over_refusal_% | 0.0 | 4.5 | 0.0 | 4.5 | 0.0 | 4.5 | 0.0 | 4.5 |
| unanswerable_refused_% | 0.0 | 33.3 | 0.0 | 33.3 | 0.0 | 33.3 | 0.0 | 33.3 |
| avg_latency_ms | 21.2 | 20.5 | 20.6 | 20.5 | 20.0 | 20.1 | 20.0 | 20.0 |
| p95_latency_ms | 25.2 | 21.5 | 21.0 | 21.3 | 21.7 | 21.0 | 21.1 | 20.7 |
| avg_cost_usd | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| verifier_blocks | 0 | 11 | 0 | 11 | 0 | 14 | 0 | 13 |
| n | 45 | 45 | 45 | 45 | 45 | 45 | 45 | 45 |

## Version A vs Version B on restricted questions (paired, exact McNemar test)

| Test set / condition | n | only A leaked | only B leaked | p |
|---|---|---|---|---|
| holdout2/normal | 8 | 0 | 0 | 1.0 |
| holdout2/mistagged | 8 | 1 | 0 | 1.0 |
| holdout2/mistagged_all | 8 | 8 | 0 | 0.0078 |
| holdout2/mistagged_all_bad_register | 8 | 7 | 0 | 0.0156 |

## Version A vs Version B on unanswerable questions (normal tagging, exact McNemar test)

| Test set | n | only B refused | only A refused | p |
|---|---|---|---|---|
| holdout2 | 15 | 5 | 0 | 0.0625 |
