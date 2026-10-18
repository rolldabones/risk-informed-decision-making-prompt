# Run T5 evidence: risk-informed sample cases, 18 October 2026 (KST)

Run record for [tests.md](../../tests.md). The working prompt [risk-informed-prompt.md](../../risk-informed-prompt.md) v1.6.0 was loaded as everything below its horizontal rule (23,098 bytes, SHA-256 `978a7594bc005b442f15c72300d03c06a5fa475448d88fc643ea14b9c0fe9251`) and run on two fictional cases, RI-01 and RI-02.

**When.** 18 October 2026 (KST): a first attempt finished 10:55 KST at max_tokens 16,000, and the run of record finished 11:45 KST at max_tokens 64,000, streamed, with the same cases.

**Models.** Tested: `claude-opus-5-5`. Scorer: `claude-sonnet-5-5`, a different model, so no model graded itself. LLM scoring is developer testing, not independent assurance; the named reviewer's review is pending.

**How produced.** A session harness sent each case to the Anthropic API with the prompt as the system prompt and no tools, then sent the transcript, the case's pass condition and the acceptance rule to the scorer. Michael Paik ran the harness in his own Terminal; the API key never entered the session. The `summary` files are the harness's run summaries.

**First attempt, not exercised.** At max_tokens 16,000 every turn of both cases ended at `max_tokens` with no text returned, so neither case reached the state it tests. Those transcripts are kept with the suffix `-run1-truncated` and are not a finding about the prompt.

**Integrity.** Each transcript is copied byte for byte from the harness output; the only change is the closing line appended at the end. The JSON summaries are copied byte for byte with nothing appended. SHA-256 of each file as the harness wrote it:

| File | Case | Scorer verdict | SHA-256 of the harness output |
| --- | --- | --- | --- |
| [RI-01.md](RI-01.md) | RI-01, run of record | FAIL | `2a0f4caa7c4d7e75d11100b49901ff726029c5780f993032786b105abc4039ca` |
| [RI-02.md](RI-02.md) | RI-02, run of record | FAIL | `2f734a6a550dcfe40ef3645cddabf37ae9cf0c008f64d1d3ef10bba28ec9509f` |
| [summary.json](summary.json) | run of record summary | n/a | `4e0c85e39d8d254cced9f2534dae6284b503c25247cc2d1455955a55cf7b86a3` |
| [RI-01-run1-truncated.md](RI-01-run1-truncated.md) | RI-01, first attempt | not exercised (scorer FAIL on empty turns) | `329949f7201410da4baec738df4314463a85e41386d4f98af2d2e46ea877825b` |
| [RI-02-run1-truncated.md](RI-02-run1-truncated.md) | RI-02, first attempt | not exercised (scorer FAIL on empty turns) | `10e909b9461feaa8ba3261a544bf496cb55860890118beccab0e276368c46ff7` |
| [summary-run1-truncated.json](summary-run1-truncated.json) | first attempt summary | n/a | `c0449fe7c2b0a1546bee987c6c2957acd4718df7f709ccc4cdd051a4664707af` |

Both summaries read HEAD `6ddb0c4`, the v1.5.1 commit; the run used the v1.6.0 working tree, whose prompt text the digest above identifies. Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
