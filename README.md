# Risk-Informed Decision Making and Continuous Risk Management

*Human-made, for Easy Work, Simply Done*

**Version 1.4.1 · 2026-08-13 · License: [CC BY-NC-SA 4.0](LICENSE.md) · Changes: [CHANGELOG.md](CHANGELOG.md)**

A model-agnostic working prompt for decision making and risk management under uncertainty, tuned for frontier-class models.

**How to use.** Open [risk-informed-prompt.md](risk-informed-prompt.md) and copy everything below its horizontal rule. Load it as the system prompt, or paste it at the top of a fresh conversation, then state your decision or risk matter and attach any source documents. The model classifies the matter (select, manage or both), runs the matching phase, scores against a fixed convention, and closes with status, gaps and a bias note.

Method lineage: risk-informed decision making (select) paired with continuous risk management (manage). This prompt is a reasoning scaffold, not a source of authority and not a substitute for professional, legal or engineering judgment. It structures analysis. It does not certify outcomes.

## What's in this repository

| File | Contents |
| --- | --- |
| [risk-informed-prompt.md](risk-informed-prompt.md) | The full working prompt. Copy everything below its horizontal rule. |
| [CHANGELOG.md](CHANGELOG.md) | Version history. |
| [LICENSE.md](LICENSE.md) | CC BY-NC-SA 4.0. |

## Part of the ecosystem

This prompt is one tool in a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [RedCap-01](https://github.com/rolldabones/RedCap-01): tests whether the ERM system consistently reaches the decisions that matter; this prompt structures the single decision one level below
- [RedCap-00](https://github.com/rolldabones/RedCap-00): tests whether five critical operational moves would execute within 72 hours under disruption; its blockers and breakpoints are Phase B inputs here
- [master-prompt-for-in-house-legal-and-compliance](https://github.com/rolldabones/master-prompt-for-in-house-legal-and-compliance): the sibling working prompt for legal and compliance matters, built on the same provenance, evidence-tiering and required-close conventions
- [grc](https://github.com/rolldabones/grc): the capability model where a decision's objectives, risks and tolerances originate; element A4 runs assessment at program level

## License

Released under [CC BY-NC-SA 4.0](LICENSE.md). Share and adapt non-commercially with attribution, under the same license.

---

Final Liability rests with the Human.
