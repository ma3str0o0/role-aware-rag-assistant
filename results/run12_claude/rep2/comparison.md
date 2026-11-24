
### holdout2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 19/22 (86%) | 19/22 (86%) | 16/22 (73%) | 18/22 (82%) |
| confident wrong answers | 2 | 2 | 2 | 0 |
| over-refusal | 1/22 (5%) | 1/22 (5%) | 4/22 (18%) | 4/22 (18%) |
| unanswerable refused | 2/15 (13%) | 4/15 (27%) | 15/15 (100%) | 15/15 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 8/8 (100%) | 0/8 (0%) | 4/8 (50%) | 0/8 (0%) |
| mean latency ms | 1 | 1 | 1612 | 2489 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0028 | 0.0043 |
offline: accuracy A vs B paired p=1.000; leaks only-A 8 only-B 0 p=0.0078
claude: accuracy A vs B paired p=0.625; leaks only-A 4 only-B 0 p=0.1250

### real2
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/20 (55%) | 10/20 (50%) | 14/20 (70%) | 13/20 (65%) |
| confident wrong answers | 9 | 6 | 0 | 0 |
| over-refusal | 0/20 (0%) | 4/20 (20%) | 6/20 (30%) | 7/20 (35%) |
| unanswerable refused | 2/20 (10%) | 18/20 (90%) | 20/20 (100%) | 20/20 (100%) |
| wrong-university traps refused | 1/15 (7%) | 14/15 (93%) | 15/15 (100%) | 15/15 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 4/5 (80%) | 0/5 (0%) | 1/5 (20%) | 0/5 (0%) |
| mean latency ms | 5 | 9 | 1915 | 2381 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0042 | 0.0057 |
offline: accuracy A vs B paired p=1.000; leaks only-A 4 only-B 0 p=0.1250
claude: accuracy A vs B paired p=1.000; leaks only-A 1 only-B 0 p=1.0000

### dubai
| metric | offline A | offline B | Claude A | Claude B |
|---|---|---|---|---|
| accuracy | 11/26 (42%) | 12/26 (46%) | 12/26 (46%) | 9/26 (35%) |
| confident wrong answers | 14 | 8 | 1 | 1 |
| over-refusal | 1/26 (4%) | 6/26 (23%) | 13/26 (50%) | 16/26 (62%) |
| unanswerable refused | 1/13 (8%) | 9/13 (69%) | 13/13 (100%) | 13/13 (100%) |
| wrong-university traps refused | 1/8 (12%) | 7/8 (88%) | 8/8 (100%) | 8/8 (100%) |
| leaks, normal tagging | 0 | 0 | 0 | 0 |
| leaks, all restricted mis-tagged | 5/6 (83%) | 0/6 (0%) | 1/6 (17%) | 0/6 (0%) |
| mean latency ms | 17 | 59 | 1899 | 3105 |
| mean cost per question $ | 0.0000 | 0.0000 | 0.0051 | 0.0080 |
offline: accuracy A vs B paired p=1.000; leaks only-A 5 only-B 0 p=0.0625
claude: accuracy A vs B paired p=0.250; leaks only-A 1 only-B 0 p=1.0000
POOLED offline: only A leaked 17, only B 0, exact McNemar p=1.53e-05
POOLED claude: only A leaked 6, only B 0, exact McNemar p=3.12e-02
