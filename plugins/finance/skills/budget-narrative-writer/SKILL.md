---
name: budget-narrative-writer
description: Drafts the narrative section of a department's annual budget submission for a Texas city. Use when a department head, budget analyst, or finance director needs to translate prior-year actuals, current-year performance, and FY+1 priorities into the written sections of a budget book that the council and the public will read.
---

# Budget Narrative Writer

> Drafts the narrative portion of a department's annual budget submission. Built for budget analysts and department heads turning numbers and goals into the prose that lives in the adopted budget book.

## When to Use

- "Draft the FY2026 budget narrative for the Parks Department."
- "I have the prior-year actuals and the FY+1 ask. Write the program summary the council will read."
- "Help me write the performance measures section for the Police Department budget."
- "Translate this list of departmental goals and KPIs into a budget narrative."
- "We added two FTEs in the Code Enforcement budget. Draft the Significant Changes section."
- The finance director is assembling the proposed budget under Tex. Loc. Gov't Code Ch. 102 and needs uniform narrative quality across departments.

## Inputs Needed

Required:

- Entity name and department (e.g., "City of Cedar Ridge, Parks and Recreation")
- Fiscal year being budgeted (e.g., FY2026 = Oct 1, 2025 – Sept 30, 2026)
- Prior-year actuals (FY-just-ended), current-year adopted budget and YTD actuals, and the FY+1 ask, by program or major category
- Departmental mission statement and two to five strategic goals
- Three to six performance measures with prior-year actuals and FY+1 targets
- Any significant changes — FTE additions or reductions, capital asks, mandate-driven costs, fee changes

Optional:

- Outyear (FY+2 and FY+3) considerations or known cost drivers
- Legislative or regulatory impacts (e.g., new state-mandated reporting, federal grant requirements)
- Council-adopted strategic plan priorities to align against
- A prior-year narrative to mirror in voice and structure

If the user has not provided prior-year actuals or the strategic goals, ask before drafting. Without the numbers the narrative will read as marketing copy.

## Process

1. Confirm scope: department, fiscal year, fund type (general fund, enterprise, internal service, special revenue), and total budget size. Fund type drives the GASB presentation framework — see `references/gasb-framework-summary.md`.
2. Verify the numbers tie. Prior-year actuals plus current-year YTD plus encumbrances should reconcile to the figures provided. Flag any line where the FY+1 ask is more than a 10 percent change from the current adopted budget without an explanation.
3. Draft the Strategic Context section: mission, alignment to council priorities, and the operating environment for the coming year.
4. Draft FY-just-ended Accomplishments: three to six specific accomplishments tied to the prior-year budget commitments. Use past tense and measurable results.
5. Draft FY+1 Priorities: three to five priorities for the budget year. Each priority states the activity, the resource required, and the expected outcome.
6. Draft Performance Measures: a compact table with prior-year actuals and FY+1 targets. Mix input, output, and outcome measures.
7. Draft Significant Changes: FTE additions or reductions, capital outlay above the city's capitalization threshold, mandate compliance costs, and any reorganization. Each change states the dollar impact and the rationale.
8. Draft Outyear Considerations: known cost drivers in FY+2 and FY+3 (e.g., debt service step-ups, expiring grants, equipment replacement cycles).

## Output Format

Plain markdown. Tone: factual, plain, neutral. No marketing language. The reader is a council member skimming the budget book the weekend before adoption.

Length: 700 to 1,400 words for a mid-sized department; longer for departments with multiple divisions. Structure:

```
[DEPARTMENT NAME]
FY[YEAR] Proposed Budget Narrative
Fund: [General Fund / Enterprise / etc.]
Total Proposed: $[amount]   FTEs: [count]

STRATEGIC CONTEXT
[2–4 paragraphs: mission, council priority alignment, operating environment.]

FY[year-just-ended] ACCOMPLISHMENTS
- [Accomplishment with measurable result]
- [Accomplishment with measurable result]
- [Accomplishment with measurable result]

FY[YEAR] PRIORITIES
1. [Priority name] — [activity, resource, outcome]
2. [Priority name] — [activity, resource, outcome]
3. [Priority name] — [activity, resource, outcome]

PERFORMANCE MEASURES
| Measure | FY[prior] Actual | FY[current] Projected | FY[year] Target |
|---|---|---|---|
| [Measure] | [#] | [#] | [#] |

SIGNIFICANT CHANGES FROM FY[CURRENT]
- [Change with dollar impact and rationale]
- [Change with dollar impact and rationale]

OUTYEAR CONSIDERATIONS (FY+2 AND FY+3)
[1–2 paragraphs on known cost drivers, expiring grants, equipment replacement, debt service step-ups.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas budget law:**

- Tex. Loc. Gov't Code Ch. 102 governs city budget adoption: budget officer files proposed budget 30 days before tax levy; public hearing required; council adopts before fiscal year begins.
- Tex. Tax Code Ch. 26 sets the truth-in-taxation timeline and notice requirements when tax rate increases are involved. Budget narratives that depend on a tax rate increase must reconcile to the Ch. 26 timeline.
- Tex. Loc. Gov't Code § 102.0065 requires notice and a hearing for budget amendments.

**GASB framework:** Government budgets are not financial statements, but the categorization of funds in the budget should mirror the city's fund structure under GASB 34 and GASB 54 (fund balance classification). The CAFR/ACFR will present the adopted budget side-by-side with actuals; consistency between budget narrative and the audited statements is expected. See `references/gasb-framework-summary.md`.

**Public records:** Proposed and adopted budgets are public records under Tex. Gov't Code Ch. 552. Draft narratives circulated within the city manager's office before submission to council may be exempt under § 552.111 (agency memoranda) until released.

**Retention:** Adopted budgets retain permanently under the Texas State Library Local Government Retention Schedule GR, Item 1025-22.

**Verify before submission:** All dollar figures tie to the budget worksheets; performance measures match what is actually tracked in the city's performance reporting system; FTE counts reconcile to the position control roster.

## References

- See `references/gasb-framework-summary.md` for the fund-type framework, key GASB statements affecting municipal budget presentation, and the difference between budgetary and GAAP basis.

## Examples

- See `examples/cedar-ridge-parks-fy2026-narrative.md` for a worked example: the Parks and Recreation Department FY2026 budget narrative for the fictional City of Cedar Ridge, TX.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
