# Run R2 evidence: risk-informed suite for prompt v1.9.0, 25 November 2026 (KST)

Run record for [tests.md](../../tests.md). The working prompt [risk-informed-prompt.md](../../risk-informed-prompt.md) v1.9.0 was loaded as the text between its first and its last horizontal rule (24,274 bytes, SHA-256 `2355229a4330d0b3b5fcebe316ebc2dfa88b14058b57935202a1f42829065e5a`) and run on the three cases of [tests/prompt-cases.md](../../tests/prompt-cases.md), RI-01 in two samples. Repository HEAD `bdd1e86` (v1.9.0).

**When.** 25 November 2026 (KST), at the first Test Thursday session, held a day early on Michael Paik's instruction; started 19:36 KST, finished 19:56 KST, max_tokens 64,000 per reply, streamed; no turn truncated. Output tokens of the scored turns: 40,313 and 36,508 (RI-01), 29,967 (RI-02), 22,392 (RI-03).

**Models.** Tested: `claude-opus-5-5`. Scorer: `claude-sonnet-5-5`, a different model, so no model graded itself. LLM scoring is developer testing, not independent assurance. The named reviewer, Michael Paik, concurs per case with the session review in [tests.md](../../tests.md), which dissents to FAIL on RI-01 sample 2.

**How produced.** [tests/run_prompt_cases.py](../../tests/run_prompt_cases.py) and [tests/score_prompt_cases.py](../../tests/score_prompt_cases.py) at v1.9.0, run from a copy of the tagged tree in Michael Paik's own Terminal; the API key never entered the session.

**Integrity.** Each transcript is copied byte for byte from the harness output; the only change is the closing line appended at the end. The run manifest and the scores are copied byte for byte under shorter names, with nothing appended. SHA-256 of each file as the harness wrote it:

| File | Case | Scorer verdict | After review | SHA-256 of the harness output |
| --- | --- | --- | --- | --- |
| [RI-01-s1.md](RI-01-s1.md) | RI-01, sample 1 | FAIL | FAIL | `5812714961be94e1dbc9f39c290359d2182e9a8e1356745d01c4adc20eb10cbf` |
| [RI-01-s2.md](RI-01-s2.md) | RI-01, sample 2 | PASS | FAIL | `8394ae9562951d388ed22f90dd3891c6f40a832452817742914861f63801e57c` |
| [RI-02.md](RI-02.md) | RI-02 | FAIL | FAIL | `c58dbb142005edf93218acce2aeefae7b2038529766b30ad34e046993a055371` |
| [RI-03.md](RI-03.md) | RI-03 | FAIL | FAIL | `83f9addc42367c6e0d836d69affc0bf78a6be76bcceb0e369f1075871b09b4d2` |
| [run.json](run.json) | run manifest | n/a | n/a | `8db57ffbd06e66f6ed882f98f09a913e543fc8557ca9a341062b873aaa4f681d` |
| [scores.json](scores.json) | scores, JSON | n/a | n/a | `f65cd59300f6d10d37a0f6baa6fd3fbbcf3a4ae56cb14c78119e2b9646dd98f1` |
| [scores.md](scores.md) | scores, readable | n/a | n/a | `1b29375593b9ce6a015287381e963145030dfa3695de02f3331cbf197c270526` |

---

Final Liability rests with the Human.
