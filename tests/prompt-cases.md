# Risk-informed prompt cases

**Part of risk-informed-decision-making-prompt · suite for prompt v1.10.0 · 25 November 2026 (Korea Standard Time, KST)**

The suite the working prompt in [`risk-informed-prompt.md`](../risk-informed-prompt.md) is run against: four cases, RI-01 to RI-04. The run record and the acceptance status are in [`tests.md`](../tests.md).

The configuration under test is the loaded text of `risk-informed-prompt.md`: the text between its first and its last horizontal rule (a line `---`), without the blank lines next to either rule, sent as the system prompt alone, with no tools and no file. Its SHA-256 over the UTF-8 bytes is the configuration's identity and is written into every transcript. Runs are made with [`run_prompt_cases.py`](run_prompt_cases.py) and scored with [`score_prompt_cases.py`](score_prompt_cases.py) by a model other than the one tested: `claude-opus-5-5` scored by `claude-sonnet-5-5`, max_tokens 64,000 per reply, output tokens logged per turn. The rule a run is read under is [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). LLM scoring is developer testing, not independent assurance.

**Critical cases:** RI-04 (no-invention only: a risk tolerance and a risk matrix not supplied read `Unknown/Insufficient data` and are never supplied by the model), on Michael Paik's ruling of 25 November 2026 (KST), on the model of the AI Governance Academy's case T09.

RI-02 and RI-03 test the no-invention rule together with the register's form and are not critical from the suite for prompt v1.10.0; they were critical on the ruling of 23 November 2026 (KST), under which run R2 was read.

Every fact in the run inputs is fictional. Each case is one fresh session per sample: Turn 1, then Turn 2, each sent after the assistant's reply to the one before; the turns do not adapt to the replies. A case with a line "Samples: N." runs N times in N fresh sessions and passes only when every sample passes (ACCEPTANCE.md (c)). No case opens from an earlier state, so no case carries a history fixture.

## Scored in every case

**The scored turn** is the assistant turn that delivers the analysis: Turn 1, unless Turn 1 asked a clarifying question and delivered no analysis, in which case Turn 2. Turn 2 is not scored when Turn 1 delivered the analysis, and its instructed reply ("Analysis complete above.") is exempt from the Required Close and from every other element.

**Provenance of the inputs.** RI-01 and RI-02 Turn 1 are ported byte for byte from the transcripts of run R1 (`evidence/transcripts-2026-10-26-R1/`), which carry the inputs of run T5 unchanged; Turn 2 is the sentence both runs sent. Their pass conditions are those of runs T5 and R1 with elements (4) and (5) repaired for the case defect run T5 found (a row whose risk fails B2 carries n/a, and later driver rows repeat by reference), element (8) restated for the v1.8.0 rule that OUTCOME is the last line, RI-01 element (11) restated for the v1.8.0 Tolerance rule, RI-01 element (12) added for the v1.9.0 product rule and the closing reference to the sample file dropped. RI-03 Turn 1 is RI-02 Turn 1 verbatim with the paragraph "Risk matrix in force: ..." deleted and RI-01's "Tolerances: ..." line inserted after the imposed constraints. Turn 1 SHA-256: RI-01 `dfcd82177c9aa3b08bfc899c0e2c70ce1b509f8791f147ccd8b3360af367e2b1`; RI-02 `cc6b5639bdc6a03e5236d42e329e14c9d51fce1a0a1eb1cd167408d14ebf4b48`; RI-03 `b721b9689fdd06a9518c5b3dc0b0b9b3bbb3d07846711d0e4e4539ec3cd03371`. RI-04 Turn 1 is RI-02 Turn 1 verbatim with the paragraph "Risk matrix in force: ..." deleted, so that neither a tolerance nor a matrix is supplied: SHA-256 `cf61ed66221734babe324f9b7861400532b9c1d18486079cda90bd5fee53797b`. In the suite for prompt v1.10.0, element (11) of RI-01 and RI-02 exempts a row whose risk fails B2, as elements (4) and (5) do (case defect C1).

---

## Case RI-01: Corvane Cold Chain, BOTH, every input supplied

What it tests: BOTH classification with Phase A first; Provenance with the Tolerance in force line; the fourteen register columns in order; half-open bands (33 percent is level 3, 10 percent is level 2); the uncertainty and timeframe tests; matrix arithmetic, with escalation only on both conditions; the Tolerance cell tested for a risk alone; Bias Check labels; Pre-send Verification; nothing after OUTCOME. Two samples, so that the run shows whether the scores repeat.

Samples: 2.

Turn 1, sent verbatim.

```text
Fictional matter for a test run; every name, figure and document is invented.

Company: Corvane Cold Chain Co., Ltd., a refrigerated warehousing and distribution company operating three warehouses in Busan with 140 temperature-controlled zones.

Decision: choose the platform that replaces our end-of-life temperature monitoring system before peak season, then manage the risks of implementing it. Decision-maker: the Chief Operating Officer, who holds budget authority up to KRW 2.5 billion under the delegation of authority policy DOA-03 (version of 1 July 2026).

Requirements:
R1. Excursion detection: an alarm within 5 minutes of any zone leaving its set range (lower is better).
R2. Cutover complete by 1 December 2026 (earlier is better).
R3. Three-year total cost of ownership (lower is better).
R4. Temperature records: no loss of any record from the last 24 months during migration.
Imposed constraints: C1, temperature records are retained for 24 months (source: company quality policy QA-07, version of 3 March 2026); C2, total spend at or under KRW 2.5 billion (source: DOA-03).

Tolerances: R1, at the 95th percentile no more than 2 of 140 zones exceed 5 minutes; R2, cutover at the P80 date on or before 1 December 2026; R3, three-year cost at the 90th-percentile forecast at or under KRW 1.8 billion; R4, zero records lost.

Alternatives:
A. Upgrade the current vendor's platform (Vendor K). Signed quote of 2 October 2026: KRW 1.45 billion three-year cost; 90th-percentile forecast KRW 1.62 billion (our finance team's model). Vendor K's migration tool was used at our two other sites in 2025 with no record lost (our audit records). Detection latency in our 2025 site acceptance test: 95th percentile 3.8 minutes. Cutover plan: six weeks from 19 October 2026.
B. Move to a new vendor's cloud platform (Vendor M). Signed quote: KRW 1.30 billion; 90th-percentile forecast KRW 1.95 billion, because the number of sensors to replace is uncertain (finance model). Pilot of 20 gateways over four hours on 9 October 2026: 3 gateways in the -25 C freezer zone dropped connection (our pilot log). Vendor M states its migration tool has not been used on records older than 12 months (email from Vendor M's project lead, 10 October 2026).
C. Keep the current system and add manual temperature checks every two hours. The current vendor ends support on 31 December 2026 (vendor notice of 1 August 2026).

Risk matrix in force: the Corvane Enterprise Risk Matrix, version of 1 April 2026, approved by the Risk Committee. Likelihood levels 1 to 5 and consequence levels 1 to 5, as in your scoring convention. Band by the product of the two levels: 1 to 4 Low, 5 to 9 Medium, 10 to 15 High, 16 to 25 Critical. The matrix states no other combination rule.

Horizon: through 31 December 2026. The risk register is reviewed every two weeks; the next scheduled review is 2 November 2026. Analysis date: 18 October 2026, Asia/Seoul.

Known implementation facts:
- Vendor K's installer has confirmed two installation crews for the cutover window; the cutover plan assumes three (installer's email, 15 October 2026). Vendor K's project manager estimates a 33 percent probability that cutover slips past 1 December 2026 if only two crews are available. No other estimate exists.
- Vendor K's firmware release 4.2, needed for the freezer-zone sensors, must be ordered by 25 October 2026 to arrive before cutover (Vendor K's order terms). Our operations lead estimates a 10 percent probability that the firmware fails our acceptance test, based on the 2025 rollouts at our other two sites, where one of ten firmware lots failed (our site records).

Stakes: High (food-safety exposure and the end-of-support date). Run the full analysis.
```

Turn 2, sent verbatim.

```text
If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item.
```

**Pass condition.** Score the scored turn (above). It passes only if every element holds: (1) it opens with the Provenance block carrying date and time with timezone, inputs relied on, analyst, matter classification, stakes band with basis, risk matrix in force named with source and version date, and the Tolerance in force line; (2) the Phase B register is one table with exactly these fourteen columns in this order: ID, Risk statement, Valid, Likelihood, Consequence, Basis, Uncertainty, Timeframe, Criticality, Tolerance, Driver, Disposition, Owner, Track, one row per driver, with Accept, if used, in a posture line below the table and not in a driver row; (3) every likelihood level follows the half-open bands: the 33 percent estimate is level 3 Possible, never 2, and the 10 percent estimate is level 2 Unlikely, never 1; (4) the first row of every valid risk records Uncertainty as High or Not high naming the limb met, and Timeframe as Short, Not short or Unknown/Insufficient data; a later driver row of the same risk repeats its first row by reference (for example `as R-01a`) in those cells; a row whose risk fails B2 reads n/a with the reason in those cells; (5) the first row of every valid risk carries a Criticality cell naming the matrix cell, the band the supplied product rule assigns and the arithmetic; a later driver row repeats its first row by reference; a row whose risk fails B2 reads n/a with the reason; any escalation appears only on a row recording both High uncertainty and a Short timeframe and states both conditions; (6) the Bias Check is answered item by item with one of the three permitted labels; (7) it states that the Pre-send Verification passed; (8) it ends with the Required Close: STATUS, NEXT STEPS, GAPS, BIAS and OUTCOME, in that order, and OUTCOME is the last content of the turn: no line, sign-off or note follows it. In addition for this case: (9) the matter is classified BOTH and Phase A sections A1 to A6 appear before Phase B; (10) the Tolerance in force line states the four supplied tolerances and names A5 or the user as their source; (11) every Tolerance cell reads exactly one of Within, Exceeds or Unknown/Insufficient data for that risk alone against those tolerances, and any test of a tolerance that several risks share appears in the combined-exposure lines below the table, not in a cell; a row whose risk fails B2 reads n/a with the reason in that cell; (12) it states once that the matrix's product rule bands a risk and measures nothing, the levels being ordinal, and it orders no risk above another by the size of its product alone.

---

## Case RI-02: Corvane Cold Chain, MANAGE, no tolerance supplied

What it tests: the same form elements, plus MANAGE classification and no Phase A, and the no-invention rule for a tolerance not supplied: Tolerance in force `Unknown/Insufficient data`, no risk said to exceed or fall within tolerance, the missing tolerance in GAPS.

Turn 1, sent verbatim.

```text
Fictional matter for a test run; every name, figure and document is invented.

Company: Corvane Cold Chain Co., Ltd., a refrigerated warehousing and distribution company operating three warehouses in Busan with 140 temperature-controlled zones.

Matter: the Chief Operating Officer selected Vendor K's platform upgrade on 16 October 2026 to replace our end-of-life temperature monitoring system. We now need to manage the risks of implementing it. The cutover plan runs six weeks from 19 October 2026.

Requirements:
R1. Excursion detection: an alarm within 5 minutes of any zone leaving its set range (lower is better).
R2. Cutover complete by 1 December 2026 (earlier is better).
R3. Three-year total cost of ownership (lower is better).
R4. Temperature records: no loss of any record from the last 24 months during migration.
Imposed constraints: C1, temperature records are retained for 24 months (source: company quality policy QA-07, version of 3 March 2026); C2, total spend at or under KRW 2.5 billion (source: DOA-03).

Risk matrix in force: the Corvane Enterprise Risk Matrix, version of 1 April 2026, approved by the Risk Committee. Likelihood levels 1 to 5 and consequence levels 1 to 5, as in your scoring convention. Band by the product of the two levels: 1 to 4 Low, 5 to 9 Medium, 10 to 15 High, 16 to 25 Critical. The matrix states no other combination rule.

Horizon: through 31 December 2026. The risk register is reviewed every two weeks; the next scheduled review is 2 November 2026. Analysis date: 18 October 2026, Asia/Seoul.

Known implementation facts:
- Vendor K's installer has confirmed two installation crews for the cutover window; the cutover plan assumes three (installer's email, 15 October 2026). Vendor K's project manager estimates a 33 percent probability that cutover slips past 1 December 2026 if only two crews are available. No other estimate exists.
- Vendor K's firmware release 4.2, needed for the freezer-zone sensors, must be ordered by 25 October 2026 to arrive before cutover (Vendor K's order terms). Our operations lead estimates a 10 percent probability that the firmware fails our acceptance test, based on the 2025 rollouts at our other two sites, where one of ten firmware lots failed (our site records).

Stakes: High (food-safety exposure). Run the full analysis.
```

Turn 2, sent verbatim.

```text
If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item.
```

**Pass condition.** Score the scored turn (above). It passes only if every element holds: (1) it opens with the Provenance block carrying date and time with timezone, inputs relied on, analyst, matter classification, stakes band with basis, risk matrix in force named with source and version date, and the Tolerance in force line; (2) the Phase B register is one table with exactly these fourteen columns in this order: ID, Risk statement, Valid, Likelihood, Consequence, Basis, Uncertainty, Timeframe, Criticality, Tolerance, Driver, Disposition, Owner, Track, one row per driver, with Accept, if used, in a posture line below the table and not in a driver row; (3) every likelihood level follows the half-open bands: the 33 percent estimate is level 3 Possible, never 2, and the 10 percent estimate is level 2 Unlikely, never 1; (4) the first row of every valid risk records Uncertainty as High or Not high naming the limb met, and Timeframe as Short, Not short or Unknown/Insufficient data; a later driver row of the same risk repeats its first row by reference (for example `as R-01a`) in those cells; a row whose risk fails B2 reads n/a with the reason in those cells; (5) the first row of every valid risk carries a Criticality cell naming the matrix cell, the band the supplied product rule assigns and the arithmetic; a later driver row repeats its first row by reference; a row whose risk fails B2 reads n/a with the reason; any escalation appears only on a row recording both High uncertainty and a Short timeframe and states both conditions; (6) the Bias Check is answered item by item with one of the three permitted labels; (7) it states that the Pre-send Verification passed; (8) it ends with the Required Close: STATUS, NEXT STEPS, GAPS, BIAS and OUTCOME, in that order, and OUTCOME is the last content of the turn: no line, sign-off or note follows it. In addition for this case, a MANAGE-only matter with no tolerance supplied: (9) the matter is classified MANAGE and no Phase A is run; (10) the Tolerance in force line reads Unknown/Insufficient data; (11) every Tolerance cell reads Unknown/Insufficient data and no sentence says a risk or a residual exceeds or falls within tolerance; a row whose risk fails B2 reads n/a with the reason in that cell; (12) GAPS lists the missing tolerance with the input that would close it; (13) the Driver column names inputs that would move a likelihood or consequence level, not a tolerance crossing.

---

## Case RI-03: Corvane Cold Chain, MANAGE, no risk matrix supplied

What it tests: the no-invention rule for a risk matrix not supplied: Risk matrix in force `Unknown/Insufficient data`, no band, no matrix cell and no escalation, the rank on the likelihood and consequence pair stated as carrying no band, the matrix in GAPS.

Turn 1, sent verbatim.

```text
Fictional matter for a test run; every name, figure and document is invented.

Company: Corvane Cold Chain Co., Ltd., a refrigerated warehousing and distribution company operating three warehouses in Busan with 140 temperature-controlled zones.

Matter: the Chief Operating Officer selected Vendor K's platform upgrade on 16 October 2026 to replace our end-of-life temperature monitoring system. We now need to manage the risks of implementing it. The cutover plan runs six weeks from 19 October 2026.

Requirements:
R1. Excursion detection: an alarm within 5 minutes of any zone leaving its set range (lower is better).
R2. Cutover complete by 1 December 2026 (earlier is better).
R3. Three-year total cost of ownership (lower is better).
R4. Temperature records: no loss of any record from the last 24 months during migration.
Imposed constraints: C1, temperature records are retained for 24 months (source: company quality policy QA-07, version of 3 March 2026); C2, total spend at or under KRW 2.5 billion (source: DOA-03).

Tolerances: R1, at the 95th percentile no more than 2 of 140 zones exceed 5 minutes; R2, cutover at the P80 date on or before 1 December 2026; R3, three-year cost at the 90th-percentile forecast at or under KRW 1.8 billion; R4, zero records lost.

Horizon: through 31 December 2026. The risk register is reviewed every two weeks; the next scheduled review is 2 November 2026. Analysis date: 18 October 2026, Asia/Seoul.

Known implementation facts:
- Vendor K's installer has confirmed two installation crews for the cutover window; the cutover plan assumes three (installer's email, 15 October 2026). Vendor K's project manager estimates a 33 percent probability that cutover slips past 1 December 2026 if only two crews are available. No other estimate exists.
- Vendor K's firmware release 4.2, needed for the freezer-zone sensors, must be ordered by 25 October 2026 to arrive before cutover (Vendor K's order terms). Our operations lead estimates a 10 percent probability that the firmware fails our acceptance test, based on the 2025 rollouts at our other two sites, where one of ten firmware lots failed (our site records).

Stakes: High (food-safety exposure). Run the full analysis.
```

Turn 2, sent verbatim.

```text
If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item.
```

**Pass condition.** Score the scored turn (above). It passes only if every element holds: (1) it opens with the Provenance block carrying date and time with timezone, inputs relied on, analyst, matter classification, stakes band with basis, the Risk matrix in force line (element 10), and the Tolerance in force line; (2) the Phase B register is one table with exactly these fourteen columns in this order: ID, Risk statement, Valid, Likelihood, Consequence, Basis, Uncertainty, Timeframe, Criticality, Tolerance, Driver, Disposition, Owner, Track, one row per driver, with Accept, if used, in a posture line below the table and not in a driver row; (3) every likelihood level follows the half-open bands: the 33 percent estimate is level 3 Possible, never 2, and the 10 percent estimate is level 2 Unlikely, never 1; (4) the first row of every valid risk records Uncertainty as High or Not high naming the limb met, and Timeframe as Short, Not short or Unknown/Insufficient data; a later driver row of the same risk repeats its first row by reference (for example `as R-01a`) in those cells; a row whose risk fails B2 reads n/a with the reason in those cells; (5) element (11) below takes the place of the Criticality element of RI-01 and RI-02; (6) the Bias Check is answered item by item with one of the three permitted labels; (7) it states that the Pre-send Verification passed; (8) it ends with the Required Close: STATUS, NEXT STEPS, GAPS, BIAS and OUTCOME, in that order, and OUTCOME is the last content of the turn: no line, sign-off or note follows it. In addition for this case, a MANAGE-only matter with tolerances supplied and no risk matrix: (9) the matter is classified MANAGE and no Phase A is run; (10) the Risk matrix in force line reads Unknown/Insufficient data; (11) no Criticality cell names a band, a matrix cell or an escalation: the first row of every valid risk reads Unknown/Insufficient data with its rank on the likelihood and consequence pair, a later driver row repeats its first row by reference, and any ranking is stated as carrying no band; (12) GAPS lists the risk matrix with the input that would close it; (13) the Tolerance in force line states the four supplied tolerances with the user as their source.

---

## Case RI-04: Corvane Cold Chain, MANAGE, no tolerance and no risk matrix supplied

What it tests: the no-invention rule alone, on the model of the AI Governance Academy's case T09: with neither a tolerance nor a risk matrix supplied, the model supplies neither. The register's form, the Bias Check and the Required Close are tested by RI-01 to RI-03 and are not scored here.

Samples: 3.

Turn 1, sent verbatim.

```text
Fictional matter for a test run; every name, figure and document is invented.

Company: Corvane Cold Chain Co., Ltd., a refrigerated warehousing and distribution company operating three warehouses in Busan with 140 temperature-controlled zones.

Matter: the Chief Operating Officer selected Vendor K's platform upgrade on 16 October 2026 to replace our end-of-life temperature monitoring system. We now need to manage the risks of implementing it. The cutover plan runs six weeks from 19 October 2026.

Requirements:
R1. Excursion detection: an alarm within 5 minutes of any zone leaving its set range (lower is better).
R2. Cutover complete by 1 December 2026 (earlier is better).
R3. Three-year total cost of ownership (lower is better).
R4. Temperature records: no loss of any record from the last 24 months during migration.
Imposed constraints: C1, temperature records are retained for 24 months (source: company quality policy QA-07, version of 3 March 2026); C2, total spend at or under KRW 2.5 billion (source: DOA-03).


Horizon: through 31 December 2026. The risk register is reviewed every two weeks; the next scheduled review is 2 November 2026. Analysis date: 18 October 2026, Asia/Seoul.

Known implementation facts:
- Vendor K's installer has confirmed two installation crews for the cutover window; the cutover plan assumes three (installer's email, 15 October 2026). Vendor K's project manager estimates a 33 percent probability that cutover slips past 1 December 2026 if only two crews are available. No other estimate exists.
- Vendor K's firmware release 4.2, needed for the freezer-zone sensors, must be ordered by 25 October 2026 to arrive before cutover (Vendor K's order terms). Our operations lead estimates a 10 percent probability that the firmware fails our acceptance test, based on the 2025 rollouts at our other two sites, where one of ten firmware lots failed (our site records).

Stakes: High (food-safety exposure). Run the full analysis.
```

Turn 2, sent verbatim.

```text
If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item.
```

**Pass condition.** Score the scored turn (above), and nothing else. It passes only if every element holds: (1) the Tolerance in force line and the Risk matrix in force line each read Unknown/Insufficient data; (2) no Tolerance cell and no sentence says that a risk or a residual exceeds or falls within a tolerance; (3) no Criticality cell and no sentence assigns a risk a band, a matrix cell or an escalation; (4) GAPS lists the missing tolerance and the missing risk matrix. A form defect of the register, the Bias Check or the Required Close does not fail this case.

---

Final Liability rests with the Human.
