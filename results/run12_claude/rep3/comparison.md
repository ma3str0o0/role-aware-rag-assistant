
### holdout2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 19/22 (86%) | 19/22 (86%) | 16/22 (73%) | 16/22 (73%) |
| confident wrong answers | 2 | 2 | 0 | 0 |
| over-refusal | 1/22 (5%) | 1/22 (5%) | 6/22 (27%) | 6/22 (27%) |
| unanswerable refused | 2/15 (13%) | 4/15 (27%) | 15/15 (100%) | 15/15 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 8/8 (100%) | 0/8 (0%) | 3/8 (38%) | 0/8 (0%) |
| mean latency ms | 1 | 1 | 1511 | 2471 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0027 | 0.0046 |
offline: accuracy A vs B paired p=1.000; leaks only-A 8 only-B 0 p=0.0078
claude: accuracy A vs B paired p=1.000; leaks only-A 3 only-B 0 p=0.2500

### real2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/20 (55%) | 10/20 (50%) | 14/20 (70%) | 14/20 (70%) |
| confident wrong answers | 9 | 6 | 0 | 0 |
| over-refusal | 0/20 (0%) | 4/20 (20%) | 6/20 (30%) | 6/20 (30%) |
| unanswerable refused | 2/20 (10%) | 18/20 (90%) | 19/20 (95%) | 20/20 (100%) |
| wrong-university traps refused | 1/15 (7%) | 14/15 (93%) | 14/15 (93%) | 15/15 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 4/5 (80%) | 0/5 (0%) | 1/5 (20%) | 0/5 (0%) |
| mean latency ms | 5 | 9 | 1593 | 2314 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0042 | 0.0055 |
offline: accuracy A vs B paired p=1.000; leaks only-A 4 only-B 0 p=0.1250
claude: accuracy A vs B paired p=1.000; leaks only-A 1 only-B 0 p=1.0000

### dubai
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/26 (42%) | 12/26 (46%) | 11/26 (42%) | 10/26 (38%) |
| confident wrong answers | 14 | 8 | 2 | 0 |
| over-refusal | 1/26 (4%) | 6/26 (23%) | 13/26 (50%) | 16/26 (62%) |
| unanswerable refused | 1/13 (8%) | 9/13 (69%) | 13/13 (100%) | 13/13 (100%) |
| wrong-university traps refused | 1/8 (12%) | 7/8 (88%) | 8/8 (100%) | 8/8 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 5/6 (83%) | 0/6 (0%) | 1/6 (17%) | 0/6 (0%) |
| mean latency ms | 17 | 59 | 1920 | 3248 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0052 | 0.0086 |
offline: accuracy A vs B paired p=1.000; leaks only-A 5 only-B 0 p=0.0625
claude: accuracy A vs B paired p=1.000; leaks only-A 1 only-B 0 p=1.0000
POOLED offline: only A leaked 17, only B 0, exact McNemar p=1.53e-05
POOLED claude: only A leaked 5, only B 0, exact McNemar p=6.25e-02
