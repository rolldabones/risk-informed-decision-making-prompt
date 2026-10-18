# risk-informed-sample RI-01

**Tested model:** claude-opus-5-5 · **Scorer:** claude-sonnet-5-5 (LLM scoring, developer testing, not independent assurance) · **Run:** 2026-10-18 10:55 KST · **max_tokens:** 16000

**Rule:** Scoring Convention, quoted: "Every band includes its lower bound and excludes its upper bound (the last band also includes 100), so each probability falls in exactly one band: 33 percent is Possible and 90 percent is Near-certain." Register format: "Phase B returns its risks in one table with exactly these columns, in this order and under these headings." Required Close: "Every response ends with these five items." FIRST MOVE: "BOTH if the matter spans selection and implementation. Run Phase A, then carry its surviving and residual risks into Phase B as the starting register."

**Pass condition:** Score the assistant turn that delivers the analysis (the first turn, unless it asked a clarifying question, in which case the second). It passes only if every element holds: (1) it opens with the Provenance block carrying date and time with timezone, inputs relied on, analyst, matter classification, stakes band with basis, risk matrix in force named with source and version date, and the Tolerance in force line; (2) the Phase B register is one table with exactly these fourteen columns in this order: ID, Risk statement, Valid, Likelihood, Consequence, Basis, Uncertainty, Timeframe, Criticality, Tolerance, Driver, Disposition, Owner, Track, one row per driver, with Accept, if used, in a posture line below the table and not in a driver row; (3) every likelihood level follows the half-open bands: the 33 percent estimate is level 3 Possible, never 2, and the 10 percent estimate is level 2 Unlikely, never 1; (4) every register row records Uncertainty as High or Not high naming the limb met, and Timeframe as Short, Not short or Unknown/Insufficient data; (5) every Criticality cell names the matrix cell, the band the supplied product rule assigns and the arithmetic, and any escalation appears only on a row recording both High uncertainty and a Short timeframe and states both conditions; (6) the Bias Check is answered item by item with one of the three permitted labels; (7) it states that the Pre-send Verification passed; (8) it ends with the Required Close: STATUS, NEXT STEPS, GAPS, BIAS and OUTCOME, in that order, as the last content of the turn. In addition for this case: (9) the matter is classified BOTH and Phase A sections A1 to A6 appear before Phase B; (10) the Tolerance in force line states the four supplied tolerances and names A5 or the user as their source; (11) every Tolerance cell reads Within, Exceeds or Unknown/Insufficient data against those tolerances. This case's transcript is the source of examples/sample-run.md.

## Transcript

### Turn 1, user

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

### Turn 1, assistant (stop_reason max_tokens)



### Turn 2, user

If your previous reply was the complete analysis, reply only: Analysis complete above. Otherwise proceed on the facts given and deliver the full analysis; record anything missing as an open item.

### Turn 2, assistant (stop_reason max_tokens)



## Score

**Verdict: FAIL.** The pass condition requires the delivering turn to contain a Provenance block, a fourteen-column register, correct likelihood banding, a Bias Check and a Required Close. Neither assistant turn contains any content, so no element is met and the missing-Required-Close fail indicator is present. The case therefore fails.

---

Final Liability rests with the Human.
