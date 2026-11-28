"""Run 13: the three fair-test sets with neural retrieval from a local open model (bge-small).

Only the search changes; documents, register, questions, scoring and the offline answerer and
verifier are the same as in runs 5, 9 and 11. Needs `pip install sentence-transformers`.

    python -m eval.run_local_embed --out results/run13_local/offline
    RAG_EMBED=local python -m eval.run_claude --no-smoke --out results/run13_local/claude   # with Claude
"""
import argparse
import os
import sys
from pathlib import Path

os.environ["RAG_EMBED"] = "local"
os.environ.setdefault("RAG_MODE", "offline")
REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from src import config  # noqa: E402
import eval.run_eval as run_eval  # noqa: E402

PLAN = [("holdout2", "mock"), ("real2", "real"), ("dubai", "dubai")]
_build = run_eval.build_index


def build_index(condition, workdir):
    # Separate folder, so the hashing-embedding indexes of the other runs are not touched.
    return _build(condition, workdir.parent.parent / ".chroma_eval_local" / workdir.name)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=REPO / "results" / "run13_local" / "offline")
    ap.add_argument("--sets", nargs="+", default=[s for s, _ in PLAN])
    args = ap.parse_args()
    run_eval.build_index = build_index
    for set_name, corpus in PLAN:
        if set_name not in args.sets:
            continue
        config.CORPUS = corpus
        print(f"=== {set_name} on {corpus}", flush=True)
        run_eval.run([set_name], args.out / set_name)


if __name__ == "__main__":
    main()
