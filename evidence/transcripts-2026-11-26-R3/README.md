# Run R3 evidence: risk-informed suite for prompt v1.10.0, 26 November 2026 (KST)

Run record for [tests.md](../../tests.md). The working prompt [risk-informed-prompt.md](../../risk-informed-prompt.md) v1.10.0 was loaded as the text between its first and its last horizontal rule (24,658 bytes, SHA-256 `535aaf3dc0fac48b78d88e1a99775e1fd28805b187440fe707cc96f9341ef65a`) and run on the four cases of [tests/prompt-cases.md](../../tests/prompt-cases.md), RI-01 in two samples and the critical case RI-04 in three. Repository HEAD `95454a0` (v1.10.0).

**When.** 26 November 2026 (KST), at Test Thursday; started 00:30 KST, finished 01:06 KST, scored 01:09 KST, max_tokens 64,000 per reply, streamed; no turn truncated. Output tokens, both turns: 60,427 and 46,175 (RI-01), 28,485 (RI-02), 24,828 (RI-03), 23,841, 29,001 and 28,528 (RI-04).

**Models.** Tested: `claude-opus-5-5`. Scorer: `claude-sonnet-5-5`, a different model, so no model graded itself. LLM scoring is developer testing, not independent assurance. The named reviewer, Michael Paik, concurs per case with the session review in [tests.md](../../tests.md), which dissents to FAIL on RI-01 sample 2.

**How produced.** [tests/run_prompt_cases.py](../../tests/run_prompt_cases.py) and [tests/score_prompt_cases.py](../../tests/score_prompt_cases.py) at v1.10.0, run from a copy of the tagged tree in Michael Paik's own Terminal; the API key never entered the session.

**Integrity.** Each transcript is copied byte for byte from the harness output; the only change is the closing line appended at the end. The run manifest and the scores are copied byte for byte under shorter names, with nothing appended. SHA-256 of each file as the harness wrote it:

| File | Case | Scorer verdict | After review | SHA-256 of the harness output |
| --- | --- | --- | --- | --- |
| [RI-01-s1.md](RI-01-s1.md) | RI-01, sample 1 | FAIL | FAIL | `fb738a0670853f08d28629f62b9ceea015579f06544fe43825f9f6af7b7e47d3` |
| [RI-01-s2.md](RI-01-s2.md) | RI-01, sample 2 | PASS | FAIL | `1e1b7bcb5d872fab2fc3c9c5b8172d4d7e53cb697d2951c1043c822449dd0150` |
| [RI-02.md](RI-02.md) | RI-02 | PASS | PASS | `57b938299f0ed1fe89b04328bed09a643615b4781714b4f486c8da9967ec0534` |
| [RI-03.md](RI-03.md) | RI-03 | PASS | PASS | `0bbb0576269d534c26bb337749a4904325ef6b138edee7305a916e6518e008b5` |
| [RI-04-s1.md](RI-04-s1.md) | RI-04, sample 1 | PASS | PASS | `cb4ed2081a8dbbe3d7bc2994d7be5bb2e191ea71b7706da4c0bbf15b1c055042` |
| [RI-04-s2.md](RI-04-s2.md) | RI-04, sample 2 | PASS | PASS | `480dc741c2f56ab06a0572ff67b7921d7e594adf066d308fdb102a27c63fd085` |
| [RI-04-s3.md](RI-04-s3.md) | RI-04, sample 3 | PASS | PASS | `8a1268b3dee643157e0619a01de3dca57e23f87328bf15d6465ca60b88bfe63d` |
| [run.json](run.json) | run manifest | n/a | n/a | `68cbaa20408ee1bf52c2c905f28e7f9399b5e13370777dfc70b6f6242237af03` |
| [scores.json](scores.json) | scores, JSON | n/a | n/a | `854c4c5cb94688eecc38b1a2b4e1c30fd10bcdb93aade3eaf909f0d29f5e4424` |
| [scores.md](scores.md) | scores, readable | n/a | n/a | `208ec23e8bc600cd3ea95f8c266428a5b24627103b96908492ad0096b53afb50` |

---

Final Liability rests with the Human.
