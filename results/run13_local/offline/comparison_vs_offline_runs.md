
### holdout2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 19/22 (86%) | 19/22 (86%) | 19/22 (86%) | 19/22 (86%) |
| confident wrong answers | 2 | 2 | 3 | 2 |
| over-refusal | 1/22 (5%) | 1/22 (5%) | 0/22 (0%) | 1/22 (5%) |
| unanswerable refused | 2/15 (13%) | 4/15 (27%) | 0/15 (0%) | 5/15 (33%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 8/8 (100%) | 0/8 (0%) | 8/8 (100%) | 0/8 (0%) |
| mean latency ms | 1 | 1 | 21 | 21 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
offline: accuracy A vs B paired p=1.000; leaks only-A 8 only-B 0 p=0.0078
claude: accuracy A vs B paired p=1.000; leaks only-A 8 only-B 0 p=0.0078

### real2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/20 (55%) | 10/20 (50%) | 11/20 (55%) | 10/20 (50%) |
| confident wrong answers | 9 | 6 | 9 | 8 |
| over-refusal | 0/20 (0%) | 4/20 (20%) | 0/20 (0%) | 2/20 (10%) |
| unanswerable refused | 2/20 (10%) | 18/20 (90%) | 0/20 (0%) | 14/20 (70%) |
| wrong-university traps refused | 1/15 (7%) | 14/15 (93%) | 0/15 (0%) | 12/15 (80%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 4/5 (80%) | 0/5 (0%) | 3/5 (60%) | 0/5 (0%) |
| mean latency ms | 5 | 9 | 28 | 34 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
offline: accuracy A vs B paired p=1.000; leaks only-A 4 only-B 0 p=0.1250
claude: accuracy A vs B paired p=1.000; leaks only-A 3 only-B 0 p=0.2500

### dubai
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/26 (42%) | 12/26 (46%) | 15/26 (58%) | 15/26 (58%) |
| confident wrong answers | 14 | 8 | 10 | 5 |
| over-refusal | 1/26 (4%) | 6/26 (23%) | 1/26 (4%) | 6/26 (23%) |
| unanswerable refused | 1/13 (8%) | 9/13 (69%) | 0/13 (0%) | 8/13 (62%) |
| wrong-university traps refused | 1/8 (12%) | 7/8 (88%) | 0/8 (0%) | 6/8 (75%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 5/6 (83%) | 0/6 (0%) | 5/6 (83%) | 0/6 (0%) |
| mean latency ms | 17 | 59 | 44 | 85 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
offline: accuracy A vs B paired p=1.000; leaks only-A 5 only-B 0 p=0.0625
claude: accuracy A vs B paired p=1.000; leaks only-A 5 only-B 0 p=0.0625
POOLED offline: only A leaked 17, only B 0, exact McNemar p=1.53e-05
POOLED claude: only A leaked 16, only B 0, exact McNemar p=3.05e-05
