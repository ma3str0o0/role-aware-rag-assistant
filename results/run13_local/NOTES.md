# Run 13 notes (28 Nov 2026): the fair-test sets with neural retrieval

**What changed:** only the search. Instead of hashing embeddings (bag of words), chunks are embedded with a
small open neural model, `BAAI/bge-small-en-v1.5`, that runs on the laptop (`RAG_EMBED=local`,
`src/embeddings.py` `LocalEmbedding`; needs `pip install sentence-transformers`). Documents, register,
questions, scoring, the answerer and the verifier are unchanged, and no threshold was re-tuned for the new
search (fair test). Two parts:

- `offline/`: the offline answerer and rule-based verifier, `python -m eval.run_local_embed`
  (four tagging conditions). Compare with runs 5, 9 and 11.
- `claude/`: Claude as answerer and judge, `RAG_EMBED=local python -m eval.run_claude --no-smoke`
  (normal and all-mis-tagged). Compare with run 12. 681 API calls, $3.29, no model refusals.

`*/comparison_vs_offline_runs.md` puts each part next to runs 5/9/11 (the script's column titles say
"Claude" for the new run in both files; for `offline/` read them as "neural search").

## Leaks, every restricted document mis-tagged (three sets pooled)

| | Version A | Version B |
|---|---|---|
| Offline, hashing search (runs 5, 9, 11) | 17 / 19 | 0 / 19 |
| Offline, neural search | 16 / 19 | **0 / 19** (McNemar 16 vs 0, p = 3e-5) |
| Claude, hashing search (run 12) | 6 / 19 | 0 / 19 |
| Claude, neural search | 4 / 19 | **0 / 19** (4 vs 0, p = 0.125) |

The leak result holds with better retrieval. With Claude, A leaked too rarely for this run alone to be
significant, but it points the same way as every other run.

## Answer quality, normal tagging (A / B)

| | Held-out 2 | Real 2 | Dubai |
|---|---|---|---|
| Accuracy, offline hashing | 86 / 86% | 55 / 50% | 42 / 46% |
| Accuracy, offline neural | 86 / 86% | 55 / 50% | **58 / 58%** |
| Accuracy, Claude hashing (run 12) | 77 / 68% | 70 / 70% | 38 / 42% |
| Accuracy, Claude neural | 77 / 73% | 65 / 65% | 54 / 38% |
| Over-refusal, offline hashing → neural | 5 / 5% → 0 / 5% | 0 / 20% → 0 / 10% | 4 / 23% → 4 / 23% |
| Over-refusal, Claude hashing → neural | 23 / 27% → 23 / 27% | 30 / 30% → 30 / 30% | 50 / 58% → 35 / 50% |
| Wrong-university traps refused by B, offline hashing → neural | – | 14 → 12 of 15 | 7 → 6 of 8 |
| Mean latency, offline neural (A / B) | 21 / 21 ms | 28 / 34 ms | 44 / 85 ms |
| Mean latency, Claude neural (A / B) | 1.8 / 2.4 s | 1.9 / 2.5 s | 2.2 / 3.7 s |

## What this shows

1. **The verifier's leak protection does not depend on the search.** B leaked nothing in either mode.
2. **Weak retrieval was the main cause of low accuracy on the large corpus.** On the Dubai corpus (4,217
   chunks) accuracy rose from 42–46% to 58% offline, and Claude A from 38% to 54% with fewer refusals
   (50% → 35%). This confirms the run 12 follow-up: most of Claude's refusals there happened because the
   answer was not in the retrieved chunks.
3. **New trade-offs.** Neural search always finds something semantically close, so Version A never says
   "I don't know" on unanswerable questions (0 of 48), and B caught slightly fewer wrong-university traps
   (18 of 23 instead of 21 of 23). With Claude, B on the Dubai set still refuses half of the answerable
   questions (accuracy 38% vs 54% for A): the checker remains too strict there.
4. **Cost.** Local embeddings are free; offline latency rose to 21–85 ms (index build takes about a minute
   on a laptop CPU for the Dubai corpus).

Not changed: the main results in the paper and README stay runs 5, 9, 11 and 12; run 13 is a robustness check.
