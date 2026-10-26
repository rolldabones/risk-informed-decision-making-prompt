# Run R1 evidence: risk-informed sample cases, 26 October 2026 (KST)

Run record for [tests.md](../../tests.md). The working prompt [risk-informed-prompt.md](../../risk-informed-prompt.md) v1.7.0 was loaded as everything below its horizontal rule (23,073 bytes, SHA-256 `4263af696112a4bd01a22ec540838e317c9e9c8f759892f1c31bd6d317864645`) and run on the two fictional cases of run T5, RI-01 and RI-02, unchanged. Repository HEAD `a2a459f` (v1.7.1).

**When.** 26 October 2026 (KST), finished 10:13 KST, max_tokens 64,000, streamed.

**Models.** Tested: `claude-opus-5-5`. Scorer: `claude-sonnet-5-5`, a different model, so no model graded itself. LLM scoring is developer testing, not independent assurance. The named reviewer, Michael Paik, concurs per case with the session review in [tests.md](../../tests.md), which dissents to FAIL on RI-02 (K3).

**How produced.** The session harness `t5_run.py` (not shipped in this repository; SHA-256 `2c0648ecf36761a3010ab5e41c629cbbc53b6ebbfb00d6e89f4665635ce43461`) sent each case to the Anthropic API with the prompt as the system prompt and no tools, then sent the transcript, the case's pass condition and the acceptance rule to the scorer. Michael Paik ran it in his own Terminal; the API key never entered the session. The `../Claude outputs/...` path in `summary.json` is the maintainer's local path at run time, not a path in this repository.

**Integrity.** Each transcript is copied byte for byte from the harness output; the only change is the closing line appended at the end. The JSON summary is copied byte for byte with nothing appended. SHA-256 of each file as the harness wrote it:

| File | Case | Scorer verdict | After review | SHA-256 of the harness output |
| --- | --- | --- | --- | --- |
| [RI-01.md](RI-01.md) | RI-01 | FAIL | FAIL | `02444db61f032cd5e5e50e038b92352faba7241d09ed0664a1c5b29832f71b89` |
| [RI-02.md](RI-02.md) | RI-02 | PASS | FAIL | `46d836a47d932b2549678c12dc1e7ce350b5f845f8f3877d4efc8361c9ab97ba` |
| [summary.json](summary.json) | run summary | n/a | n/a | `1f949f151731d791d492e834716cb36a23d3d2f81d8365b8f8d2ed61fa40b98e` |

---

Final Liability rests with the Human.
