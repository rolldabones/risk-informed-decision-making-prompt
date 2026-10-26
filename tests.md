# Tests

Developer tests of the working prompt, the acceptance rule they are read against and the log of every run. Version 1.7.1 · 2026-10-26.

## 1. Cases

Each case is one fresh session: the prompt loaded as everything below its horizontal rule, then the case's turns. The second turn of each case reads: "If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item." The turn that delivers the analysis is scored. The full inputs and pass conditions are in the transcripts under [evidence/](evidence/transcripts-2026-10-18-T5/README.md).

| ID | Matter (fictional) | What it tests |
| --- | --- | --- |
| RI-01 | Corvane Cold Chain: choose a replacement temperature-monitoring platform from three alternatives, then manage implementation (BOTH). Requirements, constraints, tolerances, a 5 by 5 product matrix, the horizon and the next review date all supplied; one estimate at 33 percent and one at 10 percent | Provenance with the Tolerance in force line; the fourteen register columns in order; half-open bands (33 percent is level 3, 10 percent is level 2); High or Not high and Short, Not short or Unknown on every row; matrix arithmetic, with escalation only on both conditions; Bias Check labels; Pre-send Verification; Required Close last; Phase A before Phase B; every Tolerance cell one of Within, Exceeds or Unknown |
| RI-02 | The same company, MANAGE only: the platform already chosen, no tolerance supplied | The same form elements, plus: MANAGE classification and no Phase A; Tolerance in force `Unknown/Insufficient data`; no risk said to exceed or fall within tolerance; the missing tolerance in GAPS; drivers stated against levels, not a tolerance crossing |

## 2. Acceptance rule

**From 26 October 2026 (KST)** acceptance is read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). The rule below is the one the runs logged before that date were read under, kept as their record.

No acceptance rule was published before the first run. For v1.6.0: a configuration (prompt version plus model) is accepted when both cases pass in the same run and a named reviewer has confirmed the scores. LLM scoring is developer testing, not independent assurance. A failed case stays in the log with its session review.

## 3. Last run

**Status under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 26 October 2026 (KST).** Not accepted. Prompt v1.7.0 has no logged run; the run of v1.6.0 (T5, 18 October 2026) failed both cases, RI-01 and RI-02. **Critical cases:** none.

**Run T5, 18 October 2026 (Korea Standard Time, KST).** Configuration:

| Field | Entry |
| --- | --- |
| Instruction text | [risk-informed-prompt.md](risk-informed-prompt.md) v1.6.0, everything below its horizontal rule, 23,098 bytes, Secure Hash Algorithm 256-bit (SHA-256) digest `978a7594bc005b442f15c72300d03c06a5fa475448d88fc643ea14b9c0fe9251` |
| Tested model | `claude-opus-5-5` |
| Scorer | `claude-sonnet-5-5`, a different model, so no model graded itself |
| Harness | Anthropic API, the instruction text as the system prompt, no tools, max_tokens 64,000, streamed |
| Run label | T5, finished 11:45 KST |
| Reviewer | Michael Paik, 19 October 2026 (KST); concurs with the scoring as recorded |

**First attempt, not exercised.** The same cases ran first at max_tokens 16,000 (finished 10:55 KST). In all four turns the model spent the whole budget before returning any text (`stop_reason` max_tokens, no text), so neither case reached the state it tests. Both are recorded as not exercised; the scorer's FAIL on them is kept in the transcripts and is not a finding about the prompt.

| Case | Scorer verdict | Element | Session review | Reason |
| --- | --- | --- | --- | --- |
| RI-01 | FAIL | (11) every Tolerance cell one value | Concur, instrument defect (K1) | R-02a reads "Within on its own at the point estimate ... **Exceeds** ... in aggregate". The Tolerance column says "Within, Exceeds or `Unknown/Insufficient data`, against the Tolerance in force", and the R2 tolerance (80th-percentile, or P80, cutover by 1 December) belongs to a requirement that two risks share. The format does not say whether the cell tests the risk alone or with the risks that share the requirement |
| RI-01 | | (4) labels on every row | Case defect | R-03 and R-04 are marked not valid under B2. B3 analyzes "each valid risk", the register format allows `n/a` with the reason, and the Pre-send item requires the tests "for every valid risk". The pass condition said every register row, an assumption the prompt does not make |
| RI-01 | | all other elements | Concur with the scorer's met | Half-open bands read correctly (33 percent level 3, 10 percent level 2), arithmetic correct, escalation on both conditions, Required Close complete. The scorer accepted the closing line the model added after OUTCOME and says another scorer could count it; see K3 |
| RI-02 | FAIL | (8) Required Close last | Concur, instrument defect (K3) | The turn ends with OUTCOME, a rule and "*Final liability rests with the human decision-maker.*". The prompt says "Every response ends with these five items", but the loaded text itself ends with the line "Final Liability rests with the Human.", which invites the model to append one |
| RI-02 | | (4) and (5) labels and criticality on every row | Concur, instrument defect (K2) | Driver rows R-01b, R-02b and R-02c read "n/a (risk-level; see R-01a)". RI-01's driver rows read "as R-01a" for the same cells and were scored met. The format says a risk with several drivers takes one row per driver and its statement "appears in the first of them only", and is silent on what a later driver row carries in the risk-level columns |
| RI-02 | | (6) Bias Check labels | Concur, model behavior | The prompt says "respond with exactly one of three labels"; several cells add text after "Live risk, not yet countered" |
| RI-02 | | risk statement cells (outside the numbered elements) | Concur, model behavior | Cells read "As in B1 R-01" against the format's "The B1 form, verbatim". The model's own second turn says its first reply "broke three rules" and delivers a revision; that turn was not scored |
| RI-02 | | case-specific elements (9) to (13) | Concur with the scorer's met | MANAGE classification, Tolerance in force Unknown, every Tolerance cell Unknown, no exceed or within claim, the tolerance in GAPS |

**Counts, run T5.** Scorer: 0 PASS, 2 FAIL, 0 unscorable. Session review by element: 3 instrument defects (K1, K2, K3), 2 model behavior, 1 case defect, 0 dissents. First attempt: 2 cases not exercised (truncated). **Acceptance: not accepted.** Open cases: RI-01, RI-02. Reviewer: Michael Paik, 19 October 2026 (KST), concurs.

Independent review, 20 October 2026: RI-01 shows the two behaviors charged to RI-02. Its Bias Check cells add text after the label ("Live risk, not yet countered. The favourable evidence for A comes from ..."; "Not applicable. Each estimate was set by one individual"), as on RI-02's element (6), and its turn ends with "*Final liability rests with the Human.*" after OUTCOME, as on RI-02's element (8). The scoring and the concurrence above stand as recorded.

**Current text.** Prompt v1.7.0 narrows limb (b) of the high-uncertainty test to the likelihood score. It has not been run: **not accepted pending a logged run.**

The RI-01 transcript is published as [examples/sample-run-transcript.md](examples/sample-run-transcript.md), labeled as a generated run that failed its case.

## 4. Known defects

K1 to K3 were recorded from run T5; K4 to K6 from the independent review of 20 October 2026. All six are open. v1.7.0 changes one rule (limb (b)) and fixes none of them, because each fix is a new text and needs a new run.

| ID | Defect | Text | Effect |
| --- | --- | --- | --- |
| K1 | The Tolerance column does not say whether it tests the risk alone or in aggregate with the risks that share a requirement | "Within, Exceeds or `Unknown/Insufficient data`, against the Tolerance in force" | A requirement-level tolerance shared by several risks yields a compound cell (RI-01, R-02a) |
| K2 | The register format does not say what a second or later driver row carries in the risk-level columns (Likelihood to Criticality) | "a risk with several drivers takes one row per driver (R-01a, R-01b), and its risk statement appears in the first of them only" | One run repeats by reference ("as R-01a"), another writes `n/a`; two runs are not comparable on those cells |
| K3 | "Every response ends with these five items" sits in a text whose own last line is the closing line "Final Liability rests with the Human." | Required Close; the final line of the prompt | The model appends a closing line after OUTCOME (both cases) |
| K4 | B5 names a section that does not exist; B4 is "Disposition" | "Trigger conditions that reopen Analyze or Plan" | A reader or model cannot tell which section a trigger reopens |
| K5 | A Scoring Convention sentence has no verb | "Never false precision, and never a band the matrix does not support." | The rule reads as a fragment; its intent (no false precision, no band the matrix does not support) is clear but not stated as an instruction |
| K6 | B4 assigns one disposition per driver, but Accept "Applies to the overall posture, not to individual drivers" (deferred item A21: permit Accept per driver) | "Assign one per driver"; the Accept bullet | The two rules pull against each other; the register records Accept in a posture line below the table |

## 5. Run log

| Run | Date (KST) | Prompt | Model | Scorer | max_tokens | Result | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T5 first attempt | 18 Oct 2026 | v1.6.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 16,000 | Not exercised: no text returned in any turn | [RI-01](evidence/transcripts-2026-10-18-T5/RI-01-run1-truncated.md), [RI-02](evidence/transcripts-2026-10-18-T5/RI-02-run1-truncated.md) |
| T5 | 18 Oct 2026 | v1.6.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 64,000 | RI-01 FAIL, RI-02 FAIL; not accepted | [RI-01](evidence/transcripts-2026-10-18-T5/RI-01.md), [RI-02](evidence/transcripts-2026-10-18-T5/RI-02.md) |

---

Final Liability rests with the Human.
