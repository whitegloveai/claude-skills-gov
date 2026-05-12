---
name: grant-application-drafter
description: Drafts a federal or state grant application narrative against a published NOFO (Notice of Funding Opportunity). Use when a grants manager, finance director, or project sponsor needs to convert a project concept and an NOFO into a compliant application narrative organized to the funder's required sections.
---

# Grant Application Drafter

> Drafts a grant application narrative organized to match the NOFO sections. Built for grant writers and project managers who must produce a competitive, compliance-ready application under deadline.

## When to Use

- "Draft the application narrative for the TxDOT TASA grant — here's the NOFO and the project description."
- "Write the federal CDBG application narrative for the new senior center project."
- "Convert this project concept into a competitive application against the EPA Brownfields NOFO."
- "Draft the need statement and the work plan for our state grant application."
- "We're applying for a USDA Rural Development grant — produce a narrative against the FY2026 NOFO."
- A grants manager is assembling an application package on grants.gov, eGrants, or a state portal and needs the narrative sections drafted to the NOFO's exact rubric.

## Inputs Needed

Required:

- NOFO/RFP source: agency name, program name, CFDA or Assistance Listing number, NOFO number, application deadline, page limits, required sections
- Project description: scope, location, beneficiaries, total cost, requested amount, match
- Organizational background: applicant entity, fiscal capacity, recent audits, grant management track record
- Project team and partners (with letters of support if available)
- Evaluation plan: measurable outcomes and the data sources

Optional:

- Prior-year grant performance with the same funder
- Pre-application or letter-of-intent feedback
- Environmental review status (NEPA, THC review, Section 106) and procurement readiness
- Sustainability plan beyond the grant period
- Cost-benefit or return-on-investment analysis

If the user has not provided the NOFO or the project budget, ask before drafting. NOFO-blind narratives score poorly.

## Process

1. Read the NOFO. Identify the rubric: required sections, page limits, font and margin rules, scoring criteria with point allocations, and any priority points (e.g., for rural communities, low-income census tracts, or disadvantaged community designation).
2. Map the project to the NOFO's stated priorities. If the NOFO names a specific outcome or population, anchor the narrative to that language.
3. Draft the Need / Problem Statement: data-supported description of the problem, the affected population, and the consequences of inaction. Use the most recent ACS, census, or sector-specific data.
4. Draft the Project Approach: scope, methodology, and how the approach addresses the problem. Cite evidence base where the NOFO requires it.
5. Draft Goals and Objectives using SMART format: Specific, Measurable, Achievable, Relevant, Time-bound. One goal with two to four objectives is typical; do not over-proliferate.
6. Draft the Work Plan and Timeline: tasks, deliverables, responsible party, start and end dates. Tie tasks to objectives.
7. Draft the Evaluation Plan: how progress and outcomes will be measured, the data sources, the reporting schedule, and the third-party evaluator if applicable.
8. Draft the Budget Narrative: line-by-line justification matching the SF-424A or equivalent budget form. Document match source (cash or in-kind) and the indirect cost rate (de minimis 10 percent under 2 C.F.R. § 200.414 if no negotiated rate).
9. Draft Organizational Capacity: applicant authority, fiscal capacity, audit history, single audit status, similar projects completed.
10. Draft Sustainability: post-grant operating plan, identified non-grant revenue, partnership commitments. Cross-check page limits and remove anything that does not score.

## Output Format

Plain markdown organized to match the NOFO's section order. Tone: confident, factual, evidence-led. The reader is a federal or state reviewer scoring against a rubric.

Length: dictated by the NOFO page limit. For a typical 15-page narrative, 6,000 to 8,000 words. Structure example:

```
[APPLICANT NAME]
[PROGRAM NAME] — Application Narrative
[NOFO #] | Assistance Listing [#]
Submitted: [Date]

PROJECT TITLE: [Title]
TOTAL PROJECT COST: $[amount]   FEDERAL/STATE REQUEST: $[amount]   MATCH: $[amount]

NEED / PROBLEM STATEMENT
[Data-supported problem, affected population, consequence of inaction.]

PROJECT APPROACH
[Scope, methodology, evidence base.]

GOALS AND OBJECTIVES
Goal 1: [Statement]
  Objective 1.1 (SMART): [Statement]
  Objective 1.2 (SMART): [Statement]

WORK PLAN AND TIMELINE
| Task | Deliverable | Responsible | Start | End |
|---|---|---|---|---|
| 1.1 | [Deliverable] | [Party] | [Date] | [Date] |

EVALUATION PLAN
[Performance measures, data sources, reporting cadence, third-party evaluator if any.]

BUDGET NARRATIVE
[Line-by-line justification keyed to SF-424A or state budget form.]
[Indirect cost rate basis and source.]
[Match source(s), cash vs. in-kind, documentation.]

ORGANIZATIONAL CAPACITY
[Fiscal capacity, audit history, single audit status, prior grant performance.]

SUSTAINABILITY
[Post-grant operating plan, non-grant revenue, partnership commitments.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate. Some federal NOFOs are beginning to require AI use disclosure in the application itself — check the NOFO before submission.

**Federal grant rules:**

- 2 C.F.R. Part 200 (Uniform Guidance) governs cost principles (Subpart E), audit requirements (Subpart F — Single Audit threshold currently $1,000,000 in federal expenditures), and procurement standards (§§ 200.317–200.327).
- 2 C.F.R. § 200.414 permits a de minimis indirect cost rate of 10 percent of modified total direct costs if the applicant has no negotiated rate.
- 2 C.F.R. § 200.331 governs subrecipient vs. contractor determinations for any subawards.
- Federal funding accountability requires registration in SAM.gov and a UEI before submission.
- See `references/uniform-guidance-2cfr200-summary.md` for the cost principles, audit, and procurement framework.

**Texas-specific overlays:** The Texas Grant Management Standards (TxGMS), administered by the Comptroller's office, apply to state grants and to federal pass-through grants administered by Texas agencies.

**Public records:** The application is a public record under Tex. Gov't Code Ch. 552 once submitted. Drafts may be exempt under § 552.111 (agency memoranda) until transmittal.

**Retention:** Grant application files retain for 3 years after grant closeout under 2 C.F.R. § 200.334 and per Texas State Library Local Government Retention Schedule GR, Item 1050.

**Verify before submission:** Page limits, font size and margins, SAM.gov registration current, UEI active, environmental review status accurate, match commitments documented in writing from partners.

## References

- See `references/uniform-guidance-2cfr200-summary.md` for the federal Uniform Guidance framework — cost principles, audit threshold, procurement standards, and indirect cost rate options.

## Examples

- See `examples/txdot-tasa-cedar-ridge-sidewalks.md` for a worked example: a TxDOT Transportation Alternatives Set-Aside (TASA) application from a fictional Texas city for $850,000 in safe-routes-to-school sidewalks.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
