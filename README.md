# Risk-Informed Decision Making and Continuous Risk Management

*Human-made, for Easy Work, Simply Done*

**Version 1.9.1 · 2026-11-25 · License: [CC BY-NC-SA 4.0](LICENSE.md) · Changes: [CHANGELOG.md](CHANGELOG.md)**

**Acceptance status at version 1.9.1 ([ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 25 November 2026, KST):** Not accepted. Run R2 (25 November 2026) of prompt v1.9.0 passed 0 of 3 cases after review. The rule against supplying a missing tolerance or risk matrix held in both critical cases; every case failed on the register's form: a Tolerance cell carrying more than its label (K7) and the cells of a row whose risk fails B2 (K8). No version of the prompt has an accepted run. The account's status table is in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md#instrument-status).

A model-agnostic working prompt for decision making and risk management under uncertainty, tuned for frontier-class models. The current prompt text was run once, in run R2 (25 November 2026), and not accepted; its suite is [tests/prompt-cases.md](tests/prompt-cases.md) and its record is [tests.md](tests.md), which names the prompt version each run tested. Two earlier texts were tested on `claude-opus-5-5`, in runs T5 (18 October 2026) and R1 (26 October 2026); neither was accepted.

**How to use.** Open [risk-informed-prompt.md](risk-informed-prompt.md) and copy everything between its first and its last horizontal rule. Load it as the system prompt, or paste it at the top of a fresh conversation, then state your decision or risk matter and attach any source documents. The model classifies the matter (select, manage or both), runs the matching phase and scores against a fixed convention. It will not assign a criticality band without your organization's approved risk matrix: supply it as an input, or the analysis stops at the likelihood and consequence pair and records the matrix as a gap. Every response closes with status, gaps and a bias note. Allow an output budget above 16,000 tokens: in testing, a 16,000-token limit returned no text in any turn, and 64,000 completed the run.

Method lineage: risk-informed decision making (select) paired with continuous risk management (manage), after two handbooks of the National Aeronautics and Space Administration (NASA): *NASA Risk-Informed Decision Making Handbook* (NASA/SP-2010-576, v1.0, April 2010) and *NASA Risk Management Handbook* (NASA/SP-2011-3422, v1.0, November 2011). NASA's technical reports server marks the second superseded by Version 2.0 (as at 23 November 2026); the lineage cites v1.0. The risk-statement template and the Accept, Mitigate, Watch, Research, Elevate and Close dispositions come from the second. The Scoring Convention's rule that a matrix's product or sum of levels bands a risk and measures nothing follows L. A. Cox, "What's Wrong with Risk Matrices?", *Risk Analysis* 28(2): 497 to 512 (2008), and D. W. Hubbard, *The Failure of Risk Management*, 2nd ed. (Wiley, 2020). This prompt is a reasoning scaffold, not a source of authority and not a substitute for professional, legal or engineering judgment. It structures analysis. It does not certify outcomes.

## What to supply

The prompt runs on less and says what it lacked. Two runs can be compared only when they start from the same inputs, and then only in format: run R2 ran RI-01 twice, in two fresh sessions, to test whether the scores repeat; both samples failed after review, on different cells ([tests.md](tests.md) section 3). Supply these, each with its source:

1. **The matter** in one or two sentences, and whether you must choose among alternatives (SELECT), manage a choice already made (MANAGE) or both.
2. **The decision-maker** and their authority to decide.
3. **Requirements or objectives**, each with its direction of goodness, and every imposed constraint with its source (law, contract, policy or instruction).
4. **The alternatives**, each with its defining assumptions (SELECT only).
5. **The risk tolerance** each requirement is held to, for example cost at the 90th-percentile forecast. A MANAGE-only matter has no Phase A to set one, so supply it here, or the analysis reports that no risk could be tested against tolerance.
6. **The approved risk matrix**: its likelihood and consequence scales, the band each cell falls in, the combination rule if it has one, its source and the date of the version used. Without it no criticality band is assigned.
7. **The horizon** for likelihood and **the date of the next scheduled register review**, which sets the short-timeframe test for escalation.
8. **Source documents and data**, named, and any numeric thresholds your organization pins to the stakes bands.

Anything not supplied is marked `Unknown/Insufficient data` and listed under GAPS with the input that would close it; the model does not fill it in. Phase B returns its risks in the fixed register format the prompt specifies, so registers from two runs line up in format, column by column. [examples/sample-run-transcript.md](examples/sample-run-transcript.md) shows a full run on a fictional matter, and [tests.md](tests.md) records where that run and a second one departed from the format.

**Known defects.** Prompt v1.8.0 fixes in the text the six defects listed in [tests.md](tests.md) section 4. The Tolerance cell tests a risk alone, and a shared tolerance is tested in aggregate below the table (K1). A later driver row repeats its first row by reference (K2). OUTCOME is the last line of every response, and the closing line sits outside the loaded text (K3). B5 names B3 and B4 (K4). The Scoring Convention sentence is an instruction (K5). Accept is recorded once, for the overall posture (K6). In run R2 (25 November 2026) OUTCOME was the last line of every scored turn (K3) and later driver rows repeated by reference (K2), while Tolerance cells still carried more than their label (K7, [tests.md](tests.md) section 4). Read output on those points with care.

## What's in this repository

| File | Contents |
| --- | --- |
| [risk-informed-prompt.md](risk-informed-prompt.md) | The full working prompt. Copy everything between its first and its last horizontal rule. |
| [tests.md](tests.md) | The acceptance status, the Critical cases line, the runs logged so far, the known defects and the run log. |
| [tests/](tests/prompt-cases.md) | The suite, three cases with their literal run inputs, and the harness that runs and scores it. |
| [examples/sample-run-transcript.md](examples/sample-run-transcript.md) | One generated run on a fictional matter, input and output verbatim. It failed its case on two named elements and is not an exemplar. |
| evidence/ | The transcripts of every logged run, copied byte for byte: [run T5](evidence/transcripts-2026-10-18-T5/README.md) and [run R1](evidence/transcripts-2026-10-26-R1/README.md). |
| [CHANGELOG.md](CHANGELOG.md) | Version history. |
| [LICENSE.md](LICENSE.md) | CC BY-NC-SA 4.0. |

## Part of the ecosystem

This prompt is one tool in a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [RedCap-01](https://github.com/rolldabones/RedCap-01): tests whether enterprise risk management (ERM) improves decisions that determine objective achievement; this prompt structures the single decision one level below
- [RedCap-00](https://github.com/rolldabones/RedCap-00): tests whether five critical operational moves would execute within 72 hours under disruption; its blockers and breakpoints are Phase B inputs here
- [master-prompt-for-in-house-legal-and-compliance](https://github.com/rolldabones/master-prompt-for-in-house-legal-and-compliance): the sibling working prompt for legal and compliance matters
- [grc](https://github.com/rolldabones/grc): the capability model where a decision's objectives, risks and tolerances originate; element A4 runs assessment at program level

## How to Cite

> Paik, Son-U Michael. *Risk-Informed Decision Making and Continuous Risk Management*, v1.9.1. GRC Solutions Korea, 2026. https://github.com/rolldabones/risk-informed-decision-making-prompt

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Released under [CC BY-NC-SA 4.0](LICENSE.md). Share and adapt non-commercially with attribution, under the same license.

Commercial use, including a Client's use in its own operations, is set out in [LICENSING.md](https://github.com/rolldabones/rolldabones/blob/main/LICENSING.md).

---

Final Liability rests with the Human.
