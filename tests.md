# Tests

Developer tests of the working prompt, the acceptance rule they are read against and the log of every run. Version 1.9.1 · 2026-11-25.

## 1. Cases

**The suite for prompt v1.9.0** is [tests/prompt-cases.md](tests/prompt-cases.md): three cases, RI-01 to RI-03, each with its literal run inputs, its pass condition and the Critical cases line, run by [tests/run_prompt_cases.py](tests/run_prompt_cases.py) and scored by [tests/score_prompt_cases.py](tests/score_prompt_cases.py) (`claude-opus-5-5` scored by `claude-sonnet-5-5`, max_tokens 64,000, output tokens logged per turn). RI-01 and RI-02 carry the inputs of runs T5 and R1 byte for byte, with their pass conditions repaired (elements (4) and (5): a row whose risk fails B2 reads n/a, and later driver rows repeat by reference; element (8): nothing follows OUTCOME); RI-01 runs two samples, so that a run shows whether its scores repeat; RI-03 is new and tests the no-matrix path; RI-01 element (12), added with v1.9.0, tests that the product rule is stated as a banding convention over ordinal levels. Turn 2 is not scored when Turn 1 delivered the analysis.

**Cases as run in T5 and R1 (record).** Each case was one fresh session: the prompt loaded as everything below its first horizontal rule, then the case's turns. The second turn of each case read: "If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item." The turn that delivered the analysis was scored. Those inputs and pass conditions are in the transcripts under evidence/ ([T5](evidence/transcripts-2026-10-18-T5/README.md), [R1](evidence/transcripts-2026-10-26-R1/README.md)).

| ID | Matter (fictional) | What it tests |
| --- | --- | --- |
| RI-01 | Corvane Cold Chain: choose a replacement temperature-monitoring platform from three alternatives, then manage implementation (BOTH). Requirements, constraints, tolerances, a 5 by 5 product matrix, the horizon and the next review date all supplied; one estimate at 33 percent and one at 10 percent | Provenance with the Tolerance in force line; the fourteen register columns in order; half-open bands (33 percent is level 3, 10 percent is level 2); High or Not high and Short, Not short or Unknown on every row; matrix arithmetic, with escalation only on both conditions; Bias Check labels; Pre-send Verification; Required Close last; Phase A before Phase B; every Tolerance cell one of Within, Exceeds or Unknown |
| RI-02 | The same company, MANAGE only: the platform already chosen, no tolerance supplied | The same form elements, plus: MANAGE classification and no Phase A; Tolerance in force `Unknown/Insufficient data`; no risk said to exceed or fall within tolerance; the missing tolerance in GAPS; drivers stated against levels, not a tolerance crossing |

## 2. Acceptance rule

**From 26 October 2026 (KST)** acceptance is read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). The rule below is the one the runs logged before that date were read under, kept as their record.

No acceptance rule was published before the first run. For v1.6.0: a configuration (prompt version plus model) is accepted when both cases pass in the same run and a named reviewer has confirmed the scores. LLM scoring is developer testing, not independent assurance. A failed case stays in the log with its session review.

## 3. Last run

**Status under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 25 November 2026 (Korea Standard Time, KST).** Not accepted. Run R2 (25 November 2026) of prompt v1.9.0 passed 0 of 3 cases after review: the critical cases RI-02 and RI-03 and the case RI-01 failed on the register's form (K7, K8), while the no-invention rule the critical cases name held in both. No version of the prompt has an accepted run.

**Critical cases:** RI-02 and RI-03 (no-invention: a risk tolerance or risk matrix not supplied reads `Unknown/Insufficient data` and is never supplied by the model), on Michael Paik's ruling of 23 November 2026 (KST).

Runs T5 and R1 were read with no critical case named; their record below is unchanged.

**Run R2, 25 November 2026 (KST).** The logged run of prompt v1.9.0 that the account requires when a rule changes, the suite [tests/prompt-cases.md](tests/prompt-cases.md), at the first Test Thursday session, read under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). Evidence: [evidence/transcripts-2026-11-25-R2/](evidence/transcripts-2026-11-25-R2/README.md). Configuration:

| Field | Entry |
| --- | --- |
| Instruction text | [risk-informed-prompt.md](risk-informed-prompt.md) v1.9.0, the loaded text, 24,274 bytes, SHA-256 `2355229a4330d0b3b5fcebe316ebc2dfa88b14058b57935202a1f42829065e5a`; repository HEAD `bdd1e86` (v1.9.0) |
| Tested model | `claude-opus-5-5` |
| Scorer | `claude-sonnet-5-5` |
| Harness | `tests/run_prompt_cases.py` and `tests/score_prompt_cases.py`: Anthropic API, the loaded text as the system prompt, no tools, max_tokens 64,000, streamed; RI-01 two samples; no turn truncated |
| Run label | R2 (`20261125-R2`), finished 19:56 KST |
| Reviewer | Michael Paik, 25 November 2026 (KST); concurs per case with the session review below |

| Case | Scorer verdict | Element | Session review | Reason |
| --- | --- | --- | --- | --- |
| RI-01 sample 1 | FAIL | (11) every Tolerance cell one value | Concur, model behavior (K7) | R-02a reads "Within at the point estimate (0.10 ≤ 0.20); the upper credible bound of 0.445 would exceed": two values in one cell |
| RI-01 sample 1 | | (5) Criticality names the matrix cell | Concur | R-01a names no matrix cell ("no single cell"), where the matrix is supplied |
| RI-01 sample 2 | PASS | (11) every Tolerance cell one value | **Dissent to FAIL,** model behavior (K7) | R-01a's cell follows its label with a test of the tolerance ("The failure probability (10%) exceeds 5% ...") that element (11) puts in the combined-exposure lines, on Michael Paik's ruling of 25 November 2026 (KST). R-04's "n/a: invalid" is not counted (case defect C1) |
| RI-02 | FAIL | (4) a row whose risk fails B2 reads n/a with the reason | Concur, model behavior (K8) | R-03 fails B2, but its Timeframe reads "25 Oct 2026: Short". Its Tolerance "n/a: not valid" is not counted (C1). Every Tolerance cell of a valid risk reads `Unknown/Insufficient data`: no tolerance supplied by the model |
| RI-03 | FAIL | (4) a row whose risk fails B2 reads n/a with the reason | Concur on element (4), model behavior (K8) | R-03 fails B2; its Uncertainty reads "n/a" with no reason and its Timeframe gives a reason unrelated to B2. The scorer's main ground, B3's sentence that the risk "would escalate one band" if a matrix were supplied, is not counted: element (11) governs the Criticality cells, which name no band, cell or escalation (ruling of 25 November 2026). No matrix supplied by the model |
| All cases | | (8) Required Close last | Concur with the scorer's met | OUTCOME was the last line of every scored turn (K3's fix held); later driver rows repeat by reference (K2's fix held) |

**Counts, run R2.** Scorer: 1 PASS, 3 FAIL, 0 unscorable, 0 truncated (samples). Session review: 1 dissent to FAIL (RI-01 sample 2); after review 0 PASS, 4 FAIL; by case 0 of 3. Every sample's scorer evidence and judgment calls were read. Critical cases RI-02 and RI-03 failed (ACCEPTANCE.md (b)); RI-01 failed ((c), 0 of 1). **Acceptance: not accepted.** Each fix is ruled at the Gate 1 of 30 November 2026 and retried once on 3 December 2026 (Test Thursday).

**Previous run.**

**Run R1, 26 October 2026 (KST).** The logged run of prompt v1.7.0 that the account requires when a rule changes, read under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). Evidence: [evidence/transcripts-2026-10-26-R1/](evidence/transcripts-2026-10-26-R1/README.md). Configuration:

| Field | Entry |
| --- | --- |
| Instruction text | [risk-informed-prompt.md](risk-informed-prompt.md) v1.7.0, everything below its horizontal rule, 23,073 bytes, Secure Hash Algorithm 256-bit (SHA-256) digest `4263af696112a4bd01a22ec540838e317c9e9c8f759892f1c31bd6d317864645`; repository HEAD `a2a459f` (v1.7.1) |
| Tested model | `claude-opus-5-5` |
| Scorer | `claude-sonnet-5-5` |
| Harness | As run T5: Anthropic API, the instruction text as the system prompt, no tools, max_tokens 64,000, streamed; cases RI-01 and RI-02 unchanged; no turn truncated |
| Run label | R1 (`20261026-R1`), finished 10:13 KST |
| Reviewer | Michael Paik, 26 October 2026 (KST); concurs per case with the session review below |

| Case | Scorer verdict | Element | Session review | Reason |
| --- | --- | --- | --- | --- |
| RI-01 | FAIL | (11) every Tolerance cell one value | Concur, instrument defect (K1) | R-01a reads "Within at the point estimate (10% ≤ 20%); the upper bound and the aggregate (CE-1) exceed": the cell tests the risk alone and in aggregate, as R-02a did in run T5 |
| RI-01 | | (8) Required Close last | Concur, instrument defect (K3) | The turn ends with "Final liability rests with the human decision-maker." after OUTCOME |
| RI-01 | | all other elements | Concur with the scorer's met | Half-open bands, the matrix arithmetic and escalation on both conditions held; BOTH classified with Phase A first; driver rows read "as R-01a" |
| RI-02 | PASS | (8) Required Close last | **Dissent to FAIL,** instrument defect (K3) | The turn ends with "*Final liability rests with the human decision-maker.*" after OUTCOME. The scorer passed the line as the instrument's sign-off and failed the same line in RI-01; run T5 failed RI-02 on it |
| RI-02 | | all other elements | Concur with the scorer's met | MANAGE with no Phase A; Tolerance in force and every Tolerance cell `Unknown/Insufficient data`; the missing tolerance in GAPS; driver rows repeat by reference ("as R-01a", "as R-02a"); R-03 fails B2 and is not scored |

**Counts, run R1.** Scorer: 1 PASS, 1 FAIL, 0 unscorable, 0 truncated. Session review: 1 dissent to FAIL (RI-02, element (8)); after review 0 PASS, 2 FAIL. Both failures are instrument defects already open (K1, K3); their disposition is a fix in the next text, which needs its own run; K2 did not recur. **Acceptance: not accepted.** Open cases: RI-01, RI-02. Reviewer: Michael Paik, 26 October 2026 (KST), concurs per case.

**Earlier run.**

**Run T5, 18 October 2026 (KST).** Configuration:

| Field | Entry |
| --- | --- |
| Instruction text | [risk-informed-prompt.md](risk-informed-prompt.md) v1.6.0, everything below its horizontal rule, 23,098 bytes, SHA-256 `978a7594bc005b442f15c72300d03c06a5fa475448d88fc643ea14b9c0fe9251` |
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

**Current text.** Prompt v1.9.0 (23 November 2026, second release of the day) keeps the v1.8.0 text and adds one Scoring Convention rule: a matrix's product or sum of levels bands a risk and does not measure it. Loaded text, the text between the first and the last horizontal rule without the blank lines next to either: 24,274 bytes, SHA-256 `2355229a4330d0b3b5fcebe316ebc2dfa88b14058b57935202a1f42829065e5a`. Prompt v1.8.0 (earlier the same day) fixed K1 to K6 in the text and moved the closing line below the last horizontal rule, outside the loaded text (23,689 bytes, SHA-256 `6a011782efdc1531108c2746a16f7539319596cc375310c858dd651d0e137132`); it was never run. Run R2 (25 November 2026), above, ran v1.9.0 on [tests/prompt-cases.md](tests/prompt-cases.md): **not accepted.**

**Earlier text.** Prompt v1.7.0 narrowed limb (b) of the high-uncertainty test to the likelihood score. Run R1 of 26 October 2026, above, ran it: **not accepted.**

The RI-01 transcript is published as [examples/sample-run-transcript.md](examples/sample-run-transcript.md), labeled as a generated run that failed its case.

## 4. Known defects

K1 to K3 were recorded from run T5; K4 to K6 from the independent review of 20 October 2026. v1.7.0 changed one rule (limb (b)) and fixed none of them. Run R1 (26 October 2026) showed K1 in RI-01 and K3 in both cases again; K2 did not recur. **Prompt v1.8.0 (23 November 2026) fixes all six in the text** (the last column below); each fix stays untested until a logged run of v1.8.0. Run R2 (25 November 2026) of v1.9.0, which keeps those fixes, recorded K7, K8 and the case defect C1.

| ID | Defect | Text | Effect | Fix in v1.8.0 |
| --- | --- | --- | --- | --- |
| K1 | The Tolerance column does not say whether it tests the risk alone or in aggregate with the risks that share a requirement | "Within, Exceeds or `Unknown/Insufficient data`, against the Tolerance in force" | A requirement-level tolerance shared by several risks yields a compound cell (RI-01, R-02a) | The Tolerance cell tests the risk alone; a tolerance several risks share is tested in aggregate in the combined-exposure lines below the table |
| K2 | The register format does not say what a second or later driver row carries in the risk-level columns (Likelihood to Criticality) | "a risk with several drivers takes one row per driver (R-01a, R-01b), and its risk statement appears in the first of them only" | One run repeats by reference ("as R-01a"), another writes `n/a`; two runs are not comparable on those cells | A later driver row reads `as R-01a` in the Risk statement column and from Valid to Tolerance, and states its own Driver, Disposition, Owner and Track |
| K3 | "Every response ends with these five items" sits in a text whose own last line is the closing line "Final Liability rests with the Human." | Required Close; the final line of the prompt | The model appends a closing line after OUTCOME (both cases), and the line it appends varies the doctrine wording ("Final liability rests with the human decision-maker.") | "OUTCOME is the last line of every response. Nothing follows it"; the closing line sits below the last horizontal rule, outside the loaded text |
| K4 | B5 names a section that does not exist; B4 is "Disposition" | "Trigger conditions that reopen Analyze or Plan" | A reader or model cannot tell which section a trigger reopens | "reopen Analyze (B3) or Disposition (B4)" |
| K5 | A Scoring Convention sentence has no verb | "Never false precision, and never a band the matrix does not support." | The rule reads as a fragment; its intent (no false precision, no band the matrix does not support) is clear but not stated as an instruction | "Never report false precision, and never report a band the matrix does not support." |
| K6 | B4 assigns one disposition per driver, but Accept "Applies to the overall posture, not to individual drivers" (deferred item A21: permit Accept per driver) | "Assign one per driver"; the Accept bullet | The two rules pull against each other; the register records Accept in a posture line below the table | B4 names the per-driver dispositions; Accept is recorded once, for the overall posture, in the posture line below the register |
| K7 | Found by run R2 (25 November 2026): the Tolerance cell carries more than its label, either two values or a test of the tolerance after the label | The register's Tolerance column; element (11) of RI-01 and RI-02 | RI-01 fails in both samples (R-02a in sample 1, R-01a in sample 2) | Ruled at the Gate 1 of 30 November 2026: the cell holds the label alone, and any reasoning sits in Basis or the combined-exposure lines |
| K8 | Found by run R2 (25 November 2026): a row whose risk fails B2 does not read n/a with the reason in Uncertainty and Timeframe | B3 and the register format | RI-02 and RI-03 fail on R-03 | Ruled at the Gate 1 of 30 November 2026: one exact form for every cell of such a row, "n/a: fails B2 (reason)" |
| C1 | Case defect, found by run R2 (25 November 2026): element (11) of RI-01 and RI-02 does not exempt a row whose risk fails B2, as elements (4) and (5) do | tests/prompt-cases.md, RI-01 and RI-02 | "n/a" in such a row's Tolerance cell reads as a failure; not counted in run R2 on Michael Paik's ruling of 25 November 2026 (KST) | Ruled at the Gate 1 of 30 November 2026: element (11) gains the exemption |

## 5. Run log

| Run | Date (KST) | Prompt | Model | Scorer | max_tokens | Result | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T5 first attempt | 18 Oct 2026 | v1.6.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 16,000 | Not exercised: no text returned in any turn | [RI-01](evidence/transcripts-2026-10-18-T5/RI-01-run1-truncated.md), [RI-02](evidence/transcripts-2026-10-18-T5/RI-02-run1-truncated.md) |
| T5 | 18 Oct 2026 | v1.6.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 64,000 | RI-01 FAIL, RI-02 FAIL; not accepted | [RI-01](evidence/transcripts-2026-10-18-T5/RI-01.md), [RI-02](evidence/transcripts-2026-10-18-T5/RI-02.md) |
| R1 | 26 Oct 2026 | v1.7.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 64,000 | Scorer RI-01 FAIL, RI-02 PASS; after review both FAIL (K1, K3); not accepted | [RI-01](evidence/transcripts-2026-10-26-R1/RI-01.md), [RI-02](evidence/transcripts-2026-10-26-R1/RI-02.md) |
| R2 | 25 Nov 2026 | v1.9.0 | `claude-opus-5-5` | `claude-sonnet-5-5` | 64,000 | Scorer RI-01 FAIL (1 of 2 samples PASS), RI-02 FAIL, RI-03 FAIL; after review all FAIL (K7, K8); not accepted | [evidence/transcripts-2026-11-25-R2/](evidence/transcripts-2026-11-25-R2/README.md) |

---

Final Liability rests with the Human.
