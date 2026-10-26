# Changelog

All notable changes to this repository are documented here. Versioning follows [Semantic Versioning](https://semver.org/). The README and this file version in lockstep; prior versions are superseded, never silently overwritten.

## v1.7.2 (2026-10-26)

Patch release, record only. **Run R1 logged:** prompt v1.7.0 on `claude-opus-5-5`, scored by `claude-sonnet-5-5`, max_tokens 64,000, the cases of run T5 unchanged. Scorer: RI-01 FAIL, RI-02 PASS. Session review: RI-01 concur (K1, K3); RI-02 dissent to FAIL, because its turn ends with a closing line after OUTCOME, the line the scorer failed in RI-01 and run T5 failed in RI-02 (K3). **Not accepted** under `ACCEPTANCE.md` in the `rolldabones` repository; reviewer Michael Paik concurring per case. K1 and K3 recur; K2 did not. No rule in the prompt changed. `tests.md` (Last run, known defects, run log, status) and the README status line updated; transcripts in `evidence/transcripts-2026-10-26-R1/`. Prepared with Claude, approved by Michael Paik.

## v1.7.1 (2026-10-26)

Patch release. Acceptance restated as a tolerance: the tests file is now read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), names its critical cases and records the instrument's status under that rule (not accepted: v1.7.0 has no run; v1.6.0 failed both cases); the README carries the same status below its masthead. No rule in the instrument changed and no run was made; the edits are to the test record and the front door. Train A of the whole-account review of 24 October 2026 (KST); prepared with Claude, approved by Michael Paik.

## v1.7.0 (2026-10-20)

Minor, because one rule changes what a run must produce. Independent review of 20 October 2026; changes made with Claude, approved by Michael Paik. Dates are Korea Standard Time (KST).

- **Prompt rule (RID-03).** Limb (b) of the high-uncertainty test in `risk-informed-prompt.md` now reads the likelihood score only. Consequence is scored on labels without descriptors and almost always rests on judgment, so in both T5 runs every valid risk met limb (b) on consequence and the test did not discriminate. The prompt is re-versioned 1.6.0 to 1.7.0 (masthead and amendment line) and is **not accepted pending a logged run**. New digest of the text below the first horizontal rule: 23,073 bytes, SHA-256 `4263af696112a4bd01a22ec540838e317c9e9c8f759892f1c31bd6d317864645`. The T5 records still describe v1.6.0.
- **Known defects disclosed (RID-06, RID-07, RID-08, RID-10).** `tests.md` section 4 adds K4 (B5 names a "Plan" section that does not exist), K5 (a Scoring Convention sentence is a fragment) and K6 (per-driver disposition against posture-level Accept, deferred item A21). The README gains a Known defects paragraph listing K1 to K6. None is fixed in the prompt, because each fix is a new text and needs a new run.
- **Test record (RID-01).** `tests.md` adds a dated note beside the 19 October concurrence: RI-01 shows the Bias Check and closing-line behaviors charged to RI-02 on elements (6) and (8). The recorded scoring and concurrence stand.
- **Evidence README (RID-02, RID-11, RID-18).** Records the completed review of 19 October 2026, notes that the RI-01 pass condition's "examples/sample-run.md" means `examples/sample-run-transcript.md`, and describes the `../Claude outputs/...` paths in the summary files as the maintainer's local paths. Transcripts and summaries are unchanged.
- **README claims qualified (RID-04, RID-05, X-08).** Registers from two runs line up in format; score reproducibility is untested. The only tested configuration was not accepted, and the output needs a budget above 16,000 tokens. The master-prompt neighbor line no longer claims shared conventions that prompt does not carry.
- **README lineage cited (RID-19).** National Aeronautics and Space Administration (NASA) *Risk-Informed Decision Making Handbook* (NASA/SP-2010-576, v1.0, April 2010) and *NASA Risk Management Handbook* (NASA/SP-2011-3422, v1.0, November 2011).
- **Wording (RID-09, RID-15).** "Below the first horizontal rule" in the prompt masthead and README; ERM, KST, SHA-256 and P80 spelled out at first use.
- **How to Cite and `CITATION.cff` (RID-16).** No change: How to Cite keeps the publisher, GRC Solutions Korea, as in every repository of this account. `CITATION.cff` carries none because Citation File Format 1.2.0 has no top-level publisher key.
- **Earlier entries' references (RID-12).** Entries below refer to records kept outside this repository: the maintainer's whole-account review of 15 October 2026 (its document sections, reviewer report 13 and item numbers such as A18, B8 and C1), the account-maintenance runbook, its guard classes (E3 checks that the README, How to Cite and `CITATION.cff` carry one version; E4 checks version tokens in the README) and the `CITATION.cff` house form (D-C1) that the v1.4.2 entry describes. "Ruling 7 of 15 October 2026" is the rule that shipped changelog entries are left as written.
- README masthead, How to Cite, `CITATION.cff` and the `tests.md` masthead to v1.7.0.
- Findings applied: RID-01, RID-02, RID-03, RID-04, RID-05, RID-06, RID-07, RID-08, RID-09, RID-10, RID-11, RID-12, RID-15, RID-18, RID-19 and X-08. RID-16 (How to Cite keeps the account's publisher form), RID-13 and RID-14 (spelling and a serial comma in shipped entries) and RID-17 (the acceptance rule stays as published for v1.6.0) take no change.
- Shipped entries below are left as written.

## v1.6.2 (2026-10-20)

- LICENSE: two defects against the Creative Commons legal code corrected (the space in 'ShareAlike. In'; the CC0 sentence of the closing notice). Operative terms unchanged.
- README masthead, How to Cite and `CITATION.cff` to v1.6.2. `risk-informed-prompt.md` and the `tests.md` masthead are unchanged.

## v1.6.1 (2026-10-19)

Patch, from the weekly maintenance sweep of 19 October 2026 (KST) and Michael Paik's review of the T5 runs, completed 19 October 2026 (KST), on which he concurs with the scoring as recorded. No change to `risk-informed-prompt.md`; the tested configuration stays prompt v1.6.0.

- **Run T5 reviewed.** `tests.md` records the reviewer in the configuration table and the counts line. Not accepted, as before: RI-01 and RI-02 fail; K1 to K3 stay open.
- README masthead, `tests.md` masthead, How to Cite and `CITATION.cff` to v1.6.1.

## v1.6.0 (2026-10-18)

Minor. Session T5 of the whole-account review of 15 October 2026 (doc section 5; reviewer report 13, items A18, A19, A20 and B8). **Amendment note, 18 October 2026 (KST):** the working prompt is re-versioned 1.5.1 to 1.6.0 because four rules change what a run must produce. A run under v1.5.1 can disagree with a run under v1.6.0 on a likelihood level at 33 or 66 percent, on an escalation and on whether a risk exceeds tolerance.

- **Likelihood bands half-open.** "2 Unlikely (10 to 33), 3 Possible (33 to 66)" put 33 and 66 in two bands each. Every band now includes its lower bound and excludes its upper bound, the last band also including 100, and the convention is stated beside the scale: 33 percent is Possible and 90 percent is Near-certain. A range that crosses a boundary is reported as a range of levels.
- **High uncertainty and short timeframe defined.** The default escalation ("escalate one band when uncertainty is high and the timeframe to act is short") turned on two undefined words. Uncertainty is now high when a score's credible range spans three or more levels or the score rests on no F1 or F2 Fact; the timeframe is short when action becomes impossible before the next scheduled register review. With no review scheduled the test is Unknown and no escalation is made. A risk in the top band is not escalated further. B3's bare "Uncertainty band." now says what the band is.
- **Tolerance in force.** B3 tested drivers against "a tolerability threshold" and B4 asked whether residual "exceeds tolerance", but tolerance was set only at A5, which a MANAGE-only matter never runs. The Provenance block gains a Tolerance in force line (from A5, else as supplied, else `Unknown/Insufficient data`); B3 and B4 test against it, and where it is Unknown no risk is said to exceed or fall within tolerance and the gap is carried.
- **Fixed register format.** B1 to B5 fixed no output form, so two runs could not be compared. Phase B now returns one table with fourteen named columns in a fixed order, one row per driver, with Accept recorded in a posture line below the table because it applies to the posture and not to a driver. The INPUT section lists the inputs that make runs comparable, and two Pre-send Verification items check the new rules.
- **README:** a What to supply block listing the eight inputs, the matrix contents the prompt needs and what happens when one is missing.
- **First logged run (run T5, 18 October 2026, KST).** `tests.md` added with two fictional cases (RI-01, a fully supplied BOTH matter; RI-02, MANAGE only with no tolerance), an acceptance rule, the run, its known defects and a run log. The v1.6.0 prompt, loaded as everything below its horizontal rule (SHA-256 `978a7594bc005b442f15c72300d03c06a5fa475448d88fc643ea14b9c0fe9251`), ran on `claude-opus-5-5` through the Anthropic API with no tools at max_tokens 64,000 and was scored by `claude-sonnet-5-5`; LLM scoring is developer testing, not independent assurance. A first attempt at max_tokens 16,000 returned no text in any turn and is recorded as not exercised. Scorer: RI-01 FAIL, RI-02 FAIL. Session review: RI-01 failed on one compound Tolerance cell (instrument defect K1) and on labels in two invalid-risk rows (case defect: the prompt applies those tests to valid risks only); RI-02 failed on content after OUTCOME (instrument defect K3), on `n/a` in the risk-level cells of driver rows (instrument defect K2) and on Bias Check labels with appended text (model behavior). Half-open bands, the matrix arithmetic, the escalation test and the Unknown-tolerance handling held in both. **Not accepted;** reviewer pending (Michael Paik). K1 to K3 are recorded, not fixed: a text change needs a new run.
- **`examples/sample-run-transcript.md`** reproduces RI-01's input and output verbatim, labeled as a generated run that failed its case on two named elements, not an exemplar. Transcripts of both attempts are in `evidence/transcripts-2026-10-18-T5/`, copied byte for byte with the closing line appended. The README's file table and What to supply block point to both files.
- Findings by class: A18, A19, A20 and B8 (register column specification, What to supply and the sample run) confirmed and edited; none already fixed, none not reproducible.
- Deferred: A21 (permit Accept per driver) is not taken here, because it changes which dispositions a driver may carry; the register records Accept in the posture line, as the rule stands. K1 to K3 wait for the next text release and its run.
- Shipped entries below are left as written (ruling 7 of 15 October 2026).

## v1.5.1 (2026-10-17)

Patch. Session T3 of the whole-account review of 15 October 2026 (doc section 8; reviewer report 13, items C1 and C2). **Amendment note, 17 October 2026 (KST):** the working prompt is re-versioned 1.5.0 to 1.5.1 for punctuation and spelling only. No rule, threshold, band, template or required output changed.

- Seventeen serial commas removed from `risk-informed-prompt.md`, the instrument that states the house style it now keeps, and one from the README's How to use paragraph.
- "Judgemental" and "Modelling" in the uncertainty-type table corrected to "Judgmental" and "Modeling", matching "modeling" two rows below.
- Shipped entries below are left as written (ruling 7 of 15 October 2026). The half-open band boundaries and the sample run are session T5's.

## v1.5.0 (2026-09-08)

The instrument required a criticality band it never defined, and now requires the matrix that defines one. **Minor, not patch:** this changes what the instrument requires of its user. An analysis that ran to completion under v1.4.2 with an invented band will, under v1.5.0, stop at the likelihood and consequence pair and report a gap. That is a change in required input and in output, not in wording.

Standing item 14, registered 7 September 2026 in `account-maintenance/RUNBOOK.md` section 8 and remediated here.

### The defect

The Scoring Convention defined likelihood 1 to 5 and consequence 1 to 5, then instructed the model to take a position on a 5 by 5 matrix and to escalate one band under stated conditions, **without defining the bands or the cell-to-band mapping anywhere in the prompt**. Neighbouring instructions required the arithmetic to be shown and the criticality to be present before the response could be returned. The model had to invent both the band set and the mapping, and then present the invention as scored output, inside an instrument whose own Pre-send Verification requires that **"No quantitative claim exceeds the evidence"** and whose Rule for Ambiguity says **"Do not produce false precision."** The contradiction is internal, and it is the argument for this fix.

### Struck

- ~~"**Criticality:** position on the 5 by 5 matrix. Default combination rule: take the matrix band, then escalate one band when uncertainty is high **and** the timeframe to act is short. State which cells you used."~~ **STRUCK.** It directed a band assignment against a matrix that did not exist in the instrument, and an escalation between bands that were never named.
- ~~"Use this convention unless you state and justify a different one. Report bands, not false precision."~~ **STRUCK.** "Report bands" was an unconditional instruction to produce the thing the prompt did not define.
- ~~"**Criticality ranking** using the Scoring Convention below. State the combination rule and show the arithmetic."~~ **STRUCK.** It required arithmetic unconditionally, so the absence of a matrix could not be reported without failing the instruction.
- ~~"Phase B: every valid risk has likelihood, consequence, criticality and a disposition per driver."~~ **STRUCK.** A Pre-send gate that could not be passed by a correct `Unknown/Insufficient data` answer.
- ~~"Scoring convention stated, with arithmetic shown."~~ **STRUCK.** Same defect in the Pre-send Verification list.
- ~~"**Version 1.4.0 - 2026-07-15.**" in the masthead of `risk-informed-prompt.md`~~ **STRUCK.** The operative file carried v1.4.0 through the v1.4.1 and v1.4.2 releases. Its bytes were unchanged across both, so the lag was true of the file and false of the repository, and no guard in the account reads that line. See "Second defect" below.

### Changed

- **The organization's approved risk matrix is now a required input.** It is named in the Provenance block with its source and the date of the version used, alongside the stakes band and any pinned numeric thresholds, which is where this instrument already records what an analysis was scored against.
- **Where a matrix is supplied**, the criticality bullet requires the cell, the band that matrix assigns to that cell, and the arithmetic. The one-band escalation for high uncertainty with a short timeframe survives as the default **only where the supplied matrix states no combination rule of its own**, and the escalation and both triggering conditions must be stated.
- **Where no matrix is supplied**, the analysis reports `Unknown/Insufficient data`, stops at the likelihood and consequence pair, assigns no band, and adds the matrix to the GAPS list with the input that would close it. Risks may still be ranked against each other on the pair, and the ranking is stated as carrying no band. This routes into the existing `Unknown/Insufficient data` and GAPS machinery rather than adding new machinery.
- **Both Pre-send Verification lines recast** so that a correct no-matrix answer passes the gate: criticality is now "a criticality band from a named matrix **or** `Unknown/Insufficient data` recorded in its place", and the arithmetic is required "where a matrix was supplied".
- **README how-to-use paragraph** now states the new required input, because it described behaviour that has changed.

### Deliberately not done

- **No default matrix, and no illustrative one either.** Band boundaries are a statement of risk appetite: the organization's to set, and neither the analyst's nor the model's to infer from a scale. An example matrix printed in this prompt would be adopted as a default by every reader who has none, which reinstates the defect with a disclaimer attached. The prompt now says so in its own text, in one line, so that a reader who looks for an example finds the reason there is not one. **This is recorded as a judgment that a later reader may reverse, not as an oversight.**
- **B4's "If residual still exceeds tolerance" and B3's "tolerability threshold" are unchanged.** They were read for the same defect and do not carry it: risk tolerance is stated by the user at A5 and is a different object from a matrix band. Recorded so that a later reader does not treat this fix as under-scoped.

### Second defect, found by reading rather than by the registration

The standing item named "one bullet in one file". **Five lines carried the defect, in three sections**, and a sixth line was a version lag: the criticality bullet, the Scoring Convention lead-in, the B3 criticality ranking bullet and both Pre-send Verification lines. Fixing only the registered bullet would have left the Pre-send gate demanding a band the corrected bullet refuses to invent, which is a worse state than the defect. **Registered line references are a starting point for the search, never its scope.**

The masthead lag is a guard blind spot, registered against the toolchain rather than fixed here: class E4 reads version tokens in `README.md` only, and E3 reads the README and `CITATION.cff`. **No guard in this account reads the version line of an operative prompt file**, so `risk-informed-prompt.md` sat two releases behind its own repository for eight weeks and every sweep reported the repository clean.

## v1.4.2 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- All other files in this repository are unchanged byte for byte.

## v1.4.1 (2026-08-13)

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v1.4.0 (2026-07-15)

Ecosystem integration and structure release under the repository improvement program. Three-part semantic versioning applies from this release.

### Added
- risk-informed-prompt.md: the operative prompt in a standalone file so it can be copied without documentation overhead, on the master-prompt repository pattern. The operative text (ROLE through Rule for Ambiguity and the closing line) is carried over verbatim; no operative provision is changed.
- Part of the ecosystem section in the README linking the canonical ECOSYSTEM.md in the profile repository plus four nearest neighbors (RedCap-01, RedCap-00, master-prompt-for-in-house-legal-and-compliance, grc).
- LICENSE.md (CC BY-NC-SA 4.0, the ecosystem default) and a README License section.
- Formal version header (v1.4.0, date, license, CHANGELOG link) replacing the bare "Version 1.3." line.
- CHANGELOG.md (this file).

### Changed
- README rewritten as a landing page (what it is, how to use, repository table, ecosystem, license); the prompt itself moved to risk-informed-prompt.md.

### Fixed
- Stray upload-artifact link removed from the first line of the README (the same defect class fixed in grc-workbook v4.0.1).

### Superseded
- The v1.3 single-file README (the tag chain preserves it as the historical record).

## v1.3 (baseline, date not recorded)

Pre-existing repository state, reconstructed: a single README carrying the front matter (how to use, version and lineage note) and the full working prompt for risk-informed decision making (Phase A, select) and continuous risk management (Phase B, manage), with provenance block, evidence tiering (F1 to F3), fixed scoring convention, quality gate and Required Close. Versions 1.0 through 1.2 predate this repository's records and are not reconstructed.

Final Liability rests with the Human.
