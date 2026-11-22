#!/usr/bin/env python3
"""Cross-model scorer for the risk-informed prompt suite.

Reads one model's transcripts from tests/prompt-runs/transcripts/, sends each
sample's text (the rules scored in every case and the case's pass condition)
with the transcript to a scorer model and records a PASS or FAIL per sample. A
case with several samples passes only when every sample passes (ACCEPTANCE.md
(c)). The scorer must differ from the tested model; the script refuses
otherwise. It then reads the run against ACCEPTANCE.md (profile repository):
(a) every case exercised, (b) every critical case passes, (c) at least 80
percent of the other cases pass. Conditions (d), a disposition for every failed
case, and (e), the named reviewer's concurrence per case, are recorded by hand
in the score file this script writes; until they are, no status follows.

LABEL, carried on every artifact this script writes: LLM scoring. Developer
testing. Not independent assurance.

Usage (from the repository root):
    python3 tests/score_prompt_cases.py --stamp 20261126-R2 \\
        --tested-model claude-opus-5-5 --scorer-model claude-sonnet-5-5

Writes tests/prompt-runs/scores/<stamp>_<tested>_scored-by_<scorer>.json and .md.
The API key is read only from ANTHROPIC_API_KEY. Requires: pip install anthropic.
Ported on 23 November 2026 (KST) from origami-method/tests/score_prompt_cases.py:
the scorer's system text, samples, the scored turn and the facts computed by
code changed; the reading under ACCEPTANCE.md did not.
"""

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_prompt_cases import (REPO_ROOT, RUNS_DIR, TRANSCRIPTS_DIR, KST, call, load_cases,  # noqa: E402
                              load_system_prompt, safe, sha)

SCORES_DIR = RUNS_DIR / "scores"
LABEL = "LLM scoring. Developer testing. Not independent assurance."
CLOSING = "Final Liability rests with the Human."
SCORER_SYSTEM = (
    "You score one transcript from a test suite for a working prompt for risk-informed decision making and "
    "continuous risk management, which returns a Provenance block, a fixed-format risk register and a "
    "Required Close. You did not produce the response under test. Score the scored turn the case names: the "
    "assistant turn that delivers the analysis, Turn 1 unless Turn 1 asked a clarifying question and "
    "delivered no analysis, in which case Turn 2. When Turn 1 delivered the analysis, Turn 2 is not scored "
    "and its instructed reply is exempt from every element. Read the pass condition literally: the case "
    "passes only if every numbered element holds. Nothing else is a criterion. Use the facts computed by "
    "code rather than counting yourself. Where the case "
    "cannot be decided without judgment, decide it and record the call in judgment_calls. Quote the "
    "response briefly and verbatim as evidence. Reply with one JSON object and nothing else: "
    '{"expected_behavior_shown": bool, "fail_condition_met": bool, "verdict": "PASS" | "FAIL", '
    '"evidence": [str], "judgment_calls": [str], "reasoning": str}'
)


def parse_transcript(path: Path) -> dict:
    """One sample's transcript. The case id is read from the heading, the sample from the Sample field."""
    t = path.read_text(encoding="utf-8")

    def field(name):
        m = re.search(r"\*\*" + re.escape(name) + r":\*\*\s*([^*\n]+?)\s*(?:\*\*|$)", t, flags=re.MULTILINE)
        return m.group(1).strip() if m else ""
    head = re.match(r"# (RI-\d+) ", t)
    conv = t.split("## Conversation\n\n", 1)[-1].rsplit("\n<!-- end of transcript", 1)[0]
    hist = t.split("## History (constructed fixture, not model output)\n\n", 1)[1].split("\n\n## Conversation", 1)[0] if "## History (" in t else ""
    replies = re.findall(r"^### Turn (\d+), assistant \(stop_reason [^)]*\)\n\n(.*?)(?=^### Turn \d+, user|\Z)",
                         conv, flags=re.M | re.S)
    return {"case": head.group(1) if head else "", "sample": field("Sample") or "1 of 1", "file": path.name, "run": field("Run"),
            "model_requested": field("Model requested"), "model_returned": field("Model returned"),
            "prompt_sha256": field("Block SHA-256"), "input_sha256": field("Run input SHA-256"),
            "truncated": field("Truncated").upper().startswith("YES"), "stop_reason": field("Turns sent"),
            "user": "(the user turns are in the conversation below)", "response": conv, "history": hist,
            "replies": [(int(n), r.strip()) for n, r in replies]}


REGISTER = ["ID", "Risk statement", "Valid", "Likelihood", "Consequence", "Basis", "Uncertainty", "Timeframe",
            "Criticality", "Tolerance", "Driver", "Disposition", "Owner", "Track"]


def facts(tr: dict) -> dict:
    out = {"reply_words_by_turn": {n: len(r.split()) for n, r in tr["replies"]}}
    for n, r in tr["replies"]:
        lines = [ln for ln in r.splitlines() if ln.strip()]
        last = lines[-1] if lines else ""
        out[f"turn_{n}_last_line"] = last
        out[f"turn_{n}_last_line_is_outcome"] = bool(re.match(r"^[\s*\-]*OUTCOME\b", last))
        heads = [ln for ln in lines if re.match(r"^\|\s*ID\s*\|", ln)]
        if heads:
            cols = [c.strip() for c in heads[0].strip().strip("|").split("|")]
            out[f"turn_{n}_register_header"] = cols
            out[f"turn_{n}_register_header_matches_fourteen_columns"] = cols == REGISTER
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stamp", required=True)
    ap.add_argument("--tested-model", required=True)
    ap.add_argument("--scorer-model", required=True)
    ap.add_argument("--max-tokens", type=int, default=8000)
    args = ap.parse_args()
    if args.tested_model.strip() == args.scorer_model.strip():
        sys.exit("ERROR - Guardrail Violation: scorer model equals tested model; no model grades itself")
    cases, critical = load_cases()
    current = {sha(load_system_prompt())}
    files = sorted(TRANSCRIPTS_DIR.glob(f"{safe(args.stamp)}_{safe(args.tested_model)}_*.md"))
    trs = {}
    for f in files:
        tr = parse_transcript(f)
        if tr["case"]:
            if tr["model_requested"] != args.tested_model:
                sys.exit(f"ERROR - Guardrail Violation: {f.name} was run on {tr['model_requested']}")
            trs.setdefault(tr["case"], []).append(tr)
    if not trs:
        sys.exit("ERROR - Guardrail Violation: no transcripts matched")
    hashes = sorted({t["prompt_sha256"] for ts in trs.values() for t in ts})
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    import anthropic
    client = anthropic.Anthropic()
    print(LABEL)
    results = {}
    samples = {}
    for c in cases:
        cid, got = c["id"], sorted(trs.get(c["id"], []), key=lambda x: x["file"])
        res = []
        if len(got) < c["samples"]:
            results[cid] = {"result": "NOT EXERCISED", "why": f"{len(got)} of {c['samples']} sample(s) found"}
            print(f"  {cid}: {results[cid]['result']} ({results[cid]['why']})")
            continue
        for tr in got:
            if tr["truncated"]:
                res.append({"result": "NOT EXERCISED", "why": "truncated", "file": tr["file"]})
            elif tr["input_sha256"] != sha(c["message"]):
                res.append({"result": "NOT EXERCISED", "why": "run input differs from the case as now written",
                            "file": tr["file"]})
            else:
                fx = facts(tr)
                msg = (f"CASE {cid} ({'critical' if cid in critical else 'not critical'}), sample {tr['sample']}\n\n{c['spec']}\n\n"
                       f"FACTS COMPUTED BY CODE: {json.dumps(fx)}\n\n"
                       + (f"HISTORY (a constructed fixture sent before the conversation; setup, never scored):\n<<<\n{tr['history']}\n>>>\n\n" if tr.get("history") else "")
                       + f"CONVERSATION UNDER TEST (user turns as sent, assistant replies verbatim):\n<<<\n{tr['response']}\n>>>")
                msgs, v = [{"role": "user", "content": msg}], None
                for _ in range(2):
                    r = call(client, model=args.scorer_model, max_tokens=args.max_tokens, system=SCORER_SYSTEM, messages=msgs)
                    raw = "".join(b.text for b in r.content if b.type == "text")
                    try:
                        v = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
                        if v.get("verdict") in ("PASS", "FAIL"):
                            v["scorer_model_returned"] = r.model
                            break
                    except (json.JSONDecodeError, ValueError):
                        pass
                    v = None
                    msgs += [{"role": "assistant", "content": raw or "(empty)"},
                             {"role": "user", "content": "Reply again with only the JSON object."}]
                if v is None:
                    res.append({"result": "NOT EXERCISED", "why": "scorer reply unparseable", "file": tr["file"]})
                else:
                    ok = v["verdict"] == "PASS" and v.get("expected_behavior_shown") is True and v.get("fail_condition_met") is False
                    res.append({"result": "PASS" if ok else "FAIL", "file": tr["file"], "facts": fx,
                                "stop_reason": tr["stop_reason"], "model_returned": tr["model_returned"], "scorer": v})
            print(f"  {cid} sample {tr['sample']}: {res[-1]['result']}{'  (critical)' if cid in critical else ''}", flush=True)
        samples[cid] = res
        kinds = {x["result"] for x in res}
        result = "NOT EXERCISED" if "NOT EXERCISED" in kinds else ("FAIL" if "FAIL" in kinds else "PASS")
        results[cid] = {"result": result, "samples": res}
        if result == "NOT EXERCISED":
            results[cid]["why"] = "; ".join(x["why"] for x in res if x.get("why"))
        print(f"  {cid}: {result}{'  (critical)' if cid in critical else ''}", flush=True)

    ids = [c["id"] for c in cases]
    unexercised = [i for i in ids if results[i]["result"] == "NOT EXERCISED"]
    crit_fail = [i for i in ids if i in critical and results[i]["result"] == "FAIL"]
    other = [i for i in ids if i not in critical]
    other_pass = sum(1 for i in other if results[i]["result"] == "PASS")
    rate = other_pass / len(other)
    reasons = []
    if unexercised:
        reasons.append(f"(a) not exercised: {', '.join(unexercised)}")
    if crit_fail:
        reasons.append(f"(b) critical case failed: {', '.join(crit_fail)}")
    if rate < 0.8:
        reasons.append(f"(c) other cases passed {other_pass} of {len(other)}, below 80 percent")
    if len(hashes) != 1 or hashes[0] not in current:
        reasons.append("configuration: the transcripts' hash is not the loaded text's")
    fails = [i for i in ids if results[i]["result"] == "FAIL"]
    if reasons:
        reading = "NOT ACCEPTED as scored. " + "; ".join(reasons) + "."
    else:
        reading = ("MEETS (a) TO (c) AS SCORED. Status follows only when (d) a disposition is recorded for "
                   f"every failed case ({', '.join(fails) or 'none'}) and (e) the named reviewer concurs per case: "
                   + ("Accepted with residuals." if fails else "Accepted."))
    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    base = SCORES_DIR / f"{safe(args.stamp)}_{safe(args.tested_model)}_scored-by_{safe(args.scorer_model)}"
    rec = {"label": LABEL, "scored_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
           "stamp": args.stamp, "tested_model": args.tested_model, "scorer_model": args.scorer_model,
           "prompt_proper_sha256": hashes, "loaded_text_sha256": sorted(current),
           "critical": sorted(critical, key=ids.index), "other_passed": other_pass, "other_total": len(other),
           "reading": reading, "results": results}
    Path(f"{base}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = [f"# Scores: run {args.stamp}, {args.tested_model} scored by {args.scorer_model}", "",
          f"**{LABEL}** Read under ACCEPTANCE.md. Block SHA-256: {', '.join(hashes)}.", "",
          f"**Reading:** {reading}", "",
          "Reviewer columns are completed by hand: concurrence per case (ACCEPTANCE.md (e)) and, for each "
          "failed case, one disposition: fix in the next block, accepted model behavior or case defect (d).", "",
          "| Case | Critical | Scorer result | Reviewer concurs | Disposition |", "| --- | --- | --- | --- | --- |"]
    md += [f"| {i} | {'yes' if i in critical else 'no'} | {results[i]['result']} | | |" for i in ids]
    md += [""]
    for i in ids:
        if results[i].get("why"):
            md += [f"## {i}: {results[i]['result']}", f"- Not exercised: {results[i]['why']}", ""]
        for s in results[i].get("samples", []):
            v = s.get("scorer") or {}
            if s["result"] != "PASS" or v.get("judgment_calls"):
                md.append(f"## {i}, {s['file']}: {s['result']}")
                if v:
                    md.append(f"- Reasoning: {v.get('reasoning', '')}")
                    md += [f"- Evidence: {e}" for e in v.get("evidence", [])]
                    md += [f"- Judgment call: {j}" for j in v.get("judgment_calls", [])]
                md.append("")
    md += ["---", "", CLOSING]
    Path(f"{base}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\nOther cases {other_pass}/{len(other)}. {reading}\nWrote {base.relative_to(REPO_ROOT)}.json and .md")


if __name__ == "__main__":
    main()
