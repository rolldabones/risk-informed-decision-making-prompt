# Risk-Informed Decision Making and Continuous Risk Management

*Human-made, for Easy Work, Simply Done*

**Version 1.7.0 · 2026-10-20 · License: [CC BY-NC-SA 4.0](LICENSE.md) · Changes: [CHANGELOG.md](CHANGELOG.md)**

A model-agnostic working prompt for decision making and risk management under uncertainty, tuned for frontier-class models. The only configuration tested so far, the previous prompt text on `claude-opus-5-5`, was not accepted, and the current text is not accepted pending a logged run; see [tests.md](tests.md).

**How to use.** Open [risk-informed-prompt.md](risk-informed-prompt.md) and copy everything below its first horizontal rule. Load it as the system prompt, or paste it at the top of a fresh conversation, then state your decision or risk matter and attach any source documents. The model classifies the matter (select, manage or both), runs the matching phase and scores against a fixed convention. It will not assign a criticality band without your organization's approved risk matrix: supply it as an input, or the analysis stops at the likelihood and consequence pair and records the matrix as a gap. Every response closes with status, gaps and a bias note. Allow an output budget above 16,000 tokens: in testing, a 16,000-token limit returned no text in any turn, and 64,000 completed the run.

Method lineage: risk-informed decision making (select) paired with continuous risk management (manage), after the National Aeronautics and Space Administration (NASA) *Risk-Informed Decision Making Handbook* (NASA/SP-2010-576, v1.0, April 2010) and *NASA Risk Management Handbook* (NASA/SP-2011-3422, v1.0, November 2011). The risk-statement template and the Accept, Mitigate, Watch, Research, Elevate and Close dispositions come from the second. This prompt is a reasoning scaffold, not a source of authority and not a substitute for professional, legal or engineering judgment. It structures analysis. It does not certify outcomes.

## What to supply

The prompt runs on less and says what it lacked. Two runs can be compared only when they start from the same inputs, and then only in format: no case has yet been run twice to test whether the scores repeat. Supply these, each with its source:

1. **The matter** in one or two sentences, and whether you must choose among alternatives (SELECT), manage a choice already made (MANAGE) or both.
2. **The decision-maker** and their authority to decide.
3. **Requirements or objectives**, each with its direction of goodness, and every imposed constraint with its source (law, contract, policy or instruction).
4. **The alternatives**, each with its defining assumptions (SELECT only).
5. **The risk tolerance** each requirement is held to, for example cost at the 90th-percentile forecast. A MANAGE-only matter has no Phase A to set one, so supply it here, or the analysis reports that no risk could be tested against tolerance.
6. **The approved risk matrix**: its likelihood and consequence scales, the band each cell falls in, the combination rule if it has one, its source and the date of the version used. Without it no criticality band is assigned.
7. **The horizon** for likelihood and **the date of the next scheduled register review**, which sets the short-timeframe test for escalation.
8. **Source documents and data**, named, and any numeric thresholds your organization pins to the stakes bands.

Anything not supplied is marked `Unknown/Insufficient data` and listed under GAPS with the input that would close it; the model does not fill it in. Phase B returns its risks in the fixed register format the prompt specifies, so registers from two runs line up in format, column by column. [examples/sample-run-transcript.md](examples/sample-run-transcript.md) shows a full run on a fictional matter, and [tests.md](tests.md) records where that run and a second one departed from the format.

**Known defects.** The prompt still carries the open defects listed in [tests.md](tests.md) section 4. The Tolerance cell does not say whether it tests a risk alone or with the risks that share its requirement (K1). The register does not say what a second or later driver row carries in the risk-level columns (K2). The prompt's own last line invites a closing line after the Required Close (K3). B5 names a "Plan" section that does not exist (K4). One Scoring Convention sentence is a fragment (K5). B4 assigns a disposition per driver while Accept applies only to the overall posture (K6). Read output on those points with care.

## What's in this repository

| File | Contents |
| --- | --- |
| [risk-informed-prompt.md](risk-informed-prompt.md) | The full working prompt. Copy everything below its first horizontal rule. |
| [tests.md](tests.md) | The two test cases, the acceptance rule, the last run, its known defects and the run log. |
| [examples/sample-run-transcript.md](examples/sample-run-transcript.md) | One generated run on a fictional matter, input and output verbatim. It failed its case on two named elements and is not an exemplar. |
| [evidence/](evidence/transcripts-2026-10-18-T5/README.md) | The transcripts of every logged run, copied byte for byte. |
| [CHANGELOG.md](CHANGELOG.md) | Version history. |
| [LICENSE.md](LICENSE.md) | CC BY-NC-SA 4.0. |

## Part of the ecosystem

This prompt is one tool in a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [RedCap-01](https://github.com/rolldabones/RedCap-01): tests whether the enterprise risk management (ERM) system consistently reaches the decisions that matter; this prompt structures the single decision one level below
- [RedCap-00](https://github.com/rolldabones/RedCap-00): tests whether five critical operational moves would execute within 72 hours under disruption; its blockers and breakpoints are Phase B inputs here
- [master-prompt-for-in-house-legal-and-compliance](https://github.com/rolldabones/master-prompt-for-in-house-legal-and-compliance): the sibling working prompt for legal and compliance matters
- [grc](https://github.com/rolldabones/grc): the capability model where a decision's objectives, risks and tolerances originate; element A4 runs assessment at program level

## How to Cite

> Paik, Son-U Michael. *Risk-Informed Decision Making and Continuous Risk Management*, v1.7.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/risk-informed-decision-making-prompt

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Released under [CC BY-NC-SA 4.0](LICENSE.md). Share and adapt non-commercially with attribution, under the same license.

---

Final Liability rests with the Human.
