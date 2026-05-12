---
name: capital-improvement-plan-drafter
description: Drafts a Capital Improvement Plan (CIP) project entry — scope, problem statement, phased cost estimate, funding strategy, and schedule. Use when a public works director, engineer, or budget officer needs a complete CIP narrative for a specific project that will go into the city's capital budget document.
---

# Capital Improvement Plan Drafter

> Drafts the project narrative for a single CIP entry. Built for directors and engineers who have the technical inputs and need a clean, decisionmaker-ready writeup for the capital budget book.

## When to Use

- "Draft the CIP entry for the Lift Station 3 replacement — $1.4M, CWSRF candidate."
- "We need a CIP writeup for the Downtown sidewalk reconstruction program for the FY2027 capital budget."
- "Build the project narrative for the public safety radio system replacement."
- "Convert this engineer's memo into a CIP entry the finance director can drop into the budget book."
- "We're submitting a TWDB application; I need the project narrative version of the CIP entry."
- A director is moving from "we should do this project" to a CIP entry that can survive review by the finance director, the city manager, the council, and the bond underwriter.

## Inputs Needed

Required:

- Project name and asset class
- Scope summary
- Problem statement with supporting data (condition assessment, work order history, complaint volume, regulatory letter)
- Cost range or estimate with confidence level (planning-level, design-level, or bid-ready)
- Funding source candidates
- Schedule constraints

Optional:

- Environmental or regulatory considerations (TCEQ, USACE, FEMA floodplain, MS4, archaeological)
- Operational impact during construction
- Operating cost impact post-completion (O&M increase or decrease)
- Coordination with adjacent projects
- Council district or service area context

If the user has not provided a cost estimate (even a range), a scope, or a funding source candidate, ask before drafting. CIP entries without those three are not entries; they are wish list items.

## Process

1. Confirm asset class and tier. Different asset classes interact with different regulatory and funding regimes (water with TCEQ and TWDB; transportation with TxDOT and MPO; parks with TPWD; broadband with NTIA).
2. Draft Scope and Problem Statement. The problem statement should connect to data: condition rating, failure frequency, regulatory letter, complaint volume.
3. Draft Goals and Outcomes in measurable language. "Restore reliable service" is weak; "Achieve 99.9% availability and remove the station from the TPDES noncompliance log" is strong.
4. Draft Project Phases. The standard sequence is planning/PER, design, bid and award, construction, and closeout. For some projects, environmental review or right-of-way acquisition is a separate phase.
5. Draft the Cost Estimate by phase with a stated confidence level. Planning-level estimates carry a ±30% band and should say so.
6. Draft the Funding Strategy. Cite the statute or program authority for each source. See `references/cip-funding-source-summary.md`.
7. Draft the Schedule with key milestones tied to funding cycles (TWDB intended use plan, council CIP adoption, bond election dates if applicable).
8. Draft Environmental and Regulatory Considerations — name the specific permits and consultations.
9. Draft Operational Impact (during construction) and Operating Cost Impact (after). Operating impact matters to finance; construction impact matters to the city manager and council.

## Output Format

Plain markdown, two to four pages per project. Tone: complete, professional, neutral. Numbers in tables; narrative tight.

```
[ENTITY] CAPITAL IMPROVEMENT PLAN
[PROJECT NUMBER] — [PROJECT TITLE]

Asset class: [class]
Council district / service area: [if applicable]
Project manager: [name, title]

1. SCOPE
   [Two to four paragraphs: what is being built, where, and to what standard.]

2. PROBLEM STATEMENT
   [Why this project is needed. Cite the condition data, the failure history,
   the regulatory driver, or the growth demand. Be specific.]

3. GOALS AND OUTCOMES
   [Three to five measurable outcomes.]

4. PROJECT PHASES
   - Planning / PER
   - Design (preliminary, final)
   - Bid and award
   - Construction
   - Closeout and warranty

5. COST ESTIMATE
   | Phase | Cost | Confidence band |
   |---|---|---|
   Total: $[amount]

6. FUNDING STRATEGY
   [Source(s) with statutory authority and program citation, share, and any
   matching requirement.]

7. SCHEDULE
   | Milestone | Target |
   |---|---|

8. ENVIRONMENTAL AND REGULATORY CONSIDERATIONS
   [Specific permits, consultations, and the agency that issues them.]

9. OPERATIONAL IMPACT DURING CONSTRUCTION
   [What residents and operations will experience and how it will be managed.]

10. OPERATING COST IMPACT (POST-COMPLETION)
    [Annualized change in O&M, FTEs, and energy.]

11. PROJECT TEAM
    [Owner, project manager, design engineer (P.E. seal), construction
    manager, key external agencies.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Engineering scope:** Engineering certifications, sizing, hydraulic and structural design require a licensed Texas P.E. under the Texas Engineering Practice Act. This skill drafts the operational narrative around the engineer's data and conclusions; it does not certify engineering work. The "Project Team" section should name the responsible P.E.

**Funding statutes (most common):**

- General obligation bonds — Tex. Gov't Code Ch. 1331
- Certificates of obligation — Tex. Loc. Gov't Code § 271.045 et seq.
- Revenue bonds — utility revenue financings under city charter and Tex. Gov't Code Ch. 1502
- Impact fees — Tex. Loc. Gov't Code Ch. 395 (with the required Land Use Assumptions and Capital Improvements Plan)
- TIRZ — Tex. Tax Code Ch. 311
- Type A / Type B sales tax — Tex. Loc. Gov't Code Ch. 504 and Ch. 505
- TWDB Clean Water State Revolving Fund / Drinking Water State Revolving Fund — Tex. Water Code Ch. 15
- TxDOT TASA, BIL programs, CDBG infrastructure set-asides

**Public records (Tex. Gov't Code Ch. 552):** CIP entries are public records on adoption. Pre-adoption drafts and internal memoranda may be exempt under § 552.111.

**Retention:** Adopted CIP documents retain permanently under Texas State Library Local Government Retention Schedule, Item 1000-19 (Capital Improvement Plans). Project files retain through asset life plus 3 years.

**Verify before submission:** Cost confidence band is stated, the funding strategy cites the right statute, environmental triggers are listed, and the responsible P.E. is named.

## References

- See `references/cip-funding-source-summary.md` for a concise summary of common municipal CIP funding sources and their statutory authority.

## Examples

- See `examples/lift-station-3-replacement-cip.md` for a worked example: a Lift Station 3 replacement CIP entry, $1.4M, funded through a combination of utility rate revenue and TWDB CWSRF. Surfaced from the lift station maintenance log analysis.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
