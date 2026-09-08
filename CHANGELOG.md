# Changelog

All notable changes to this repository are documented here. Versioning follows [Semantic Versioning](https://semver.org/). The README and this file version in lockstep; prior versions are superseded, never silently overwritten.

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
