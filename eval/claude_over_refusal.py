"""Run 12 follow-up. Why does Claude refuse answerable questions? For each refused answerable question (run 12, normal
tagging) check whether the expected document was among the chunks the answerer was given."""
import csv, json, os, sys
from pathlib import Path
os.environ["RAG_MODE"] = "offline"
REPO = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(REPO))
from src import config
from src.ingest import ingest
from src.agents.retriever import Retriever
OUT = REPO / "results" / "run12_claude"
PLAN = [("holdout2", "mock", "run5"), ("real2", "real", "run9"), ("dubai", "dubai", "run11")]
out = {}
for s, corpus, run in PLAN:
    config.CORPUS = corpus
    col, _ = ingest(mistag=False, path=REPO / ".chroma_eval" / "overref" / corpus)
    ret = Retriever(col)
    qs = {r["id"]: r for r in csv.DictReader(open(REPO / "eval" / f"test_set_{s}.csv", encoding="utf-8"))}
    cl = [r for r in csv.DictReader(open(REPO / "results/run12_claude" / s / "eval_results.csv")) if r["condition"] == "normal"]
    off = {(r["version"], r["id"]): r for r in csv.DictReader(open(REPO / "results" / run / "eval_results.csv"))
           if r["condition"] == "normal" and r["set"] == s}
    rows = []
    for r in cl:
        if r["type"] != "answerable" or r["refused"] != "True":
            continue
        q = qs[r["id"]]
        chunks = [c for c in ret.run(q["question"], q["role"]) if c["score"] >= config.MIN_SCORE]
        exp = q["expected_doc"].split("|")
        docs = [c["doc_id"] for c in chunks]
        hit = [c for c in chunks if c["doc_id"] in exp]
        kw = q["expected_keyword"].split("|")
        kw_in = any(k.lower() in c["text"].lower() for c in hit for k in kw)
        o = off[(r["version"], r["id"])]
        rows.append({"version": r["version"], "id": r["id"], "question": q["question"],
                     "expected_doc_retrieved": bool(hit), "keyword_in_retrieved": kw_in,
                     "offline_correct": o["correct"] == "True", "offline_refused": o["refused"] == "True",
                     "verifier": r["verifier_decision"], "reasons": r["verifier_reasons"][:160], "docs": docs})
    out[s] = rows
json.dump(out, open(OUT / "over_refusal.json", "w"), indent=1)
for s, rows in out.items():
    for v in "AB":
        R = [x for x in rows if x["version"] == v]
        if not R: continue
        miss = sum(not x["expected_doc_retrieved"] for x in R)
        nokw = sum(x["expected_doc_retrieved"] and not x["keyword_in_retrieved"] for x in R)
        model = sum(x["keyword_in_retrieved"] and x["verifier"] in ("none", "pass") for x in R)
        ver = sum(x["keyword_in_retrieved"] and x["verifier"] in ("block",) for x in R)
        offok = sum(x["offline_correct"] for x in R)
        print(f"{s} {v}: refused {len(R)} | expected doc not retrieved {miss} | doc retrieved but answer passage not {nokw} | "
              f"answer in context, answerer refused {model} | blocked by verifier {ver} | offline got it right {offok}")
