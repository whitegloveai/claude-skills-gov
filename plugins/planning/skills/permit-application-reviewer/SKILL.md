---
name: permit-application-reviewer
description: Reviews a submitted permit application for completeness and code compliance, then returns a clear next-step decision (approve, approve with conditions, deny, or incomplete). Use when a building inspector, planner, or development services reviewer needs a written review memo for a permit submittal that will go into the case file under the Tex. Loc. Gov't Code Ch. 245 vested rights framework.
---

# Permit Application Reviewer

> Produces a permit review memo that tells the applicant where they stand and tells the next reviewer what was checked. Built for staff working through a submittal queue under deadline.

## When to Use

- "Review this building permit submittal for the residential addition at 411 Magnolia."
- "Check the sign permit submittal against the sign code and tell me what's missing."
- "I have a special event permit submittal for the fall festival — run the review."
- "Review the fence permit submittal and write up the next-step memo."
- "This is a re-submittal of last month's permit; tell me whether the comments were addressed."
- A submittal has been logged in, the application fee is paid, and staff needs a written review document for the case file.

## Inputs Needed

Required:

- Permit type (building, sign, fence, special event, demolition, certificate of occupancy, etc.)
- Permit number and submittal date
- Property address and owner
- Applicant or contractor name and license number where applicable
- List of documents received with the submittal
- Applicable code references (city building code adoption ordinance, sign code, zoning ordinance, etc.)
- The completeness checklist the city uses for this permit type

Optional:

- Prior review comments if this is a re-submittal
- Conditions of any underlying zoning approval (SUP, PD, site plan)
- HOA or deed restriction notes the applicant has provided (these are not enforceable by the city but inform staff awareness)

If the user has not provided the checklist for this permit type or the applicable code section, ask before drafting.

## Process

1. Confirm the permit type and pull the applicable checklist and code sections. The Texas Building Code, as adopted locally, governs building permits; sign permits and fence permits typically follow chapters of the local development code.
2. Inventory the submittal. List each document received with reference numbers (sheet numbers, exhibit letters). Note submittal date and any prior submittal dates if this is a re-submittal.
3. Run the completeness check. Compare received documents to the checklist line by line. If a required item is missing, identify the exact item and the checklist line.
4. Run the code compliance review. For each applicable code section, identify what was reviewed and any discrepancies. Cite the section number and edition (e.g., 2021 IBC § 1009 means egress).
5. If this is a re-submittal, address each prior comment in order: was the comment resolved, partially resolved, or not addressed.
6. List any conditions of approval that would be carried into the permit if issued.
7. Choose one decision: approve, approve with conditions, deny, or incomplete — return for additional information. The decision must match the findings of the review. Do not approve a submittal with missing required items.
8. Sign and date. Identify the next responsible reviewer if the permit requires multiple reviews (planning, building, fire, public works).

## Output Format

Plain markdown. No emoji. Headers in this order:

```
PERMIT REVIEW MEMO

PERMIT NUMBER:     [BLD/SGN/FNC-YYYY-NNNN]
PERMIT TYPE:       [Building / Sign / Fence / etc.]
PROPERTY:          [Address]
OWNER:             [Name]
APPLICANT:         [Name; contractor license number if applicable]
SUBMITTAL DATE:    [Date]
SUBMITTAL CYCLE:   [First submittal / Second submittal / etc.]

1. APPLICATION SUMMARY
2. COMPLETENESS CHECK
   2a. Documents received
   2b. Items missing (with checklist line numbers)
3. CODE COMPLIANCE REVIEW
   3a. [Code section] — [reviewed / discrepancy]
   3b. [Code section] — [reviewed / discrepancy]
   (continue)
4. RESPONSE TO PRIOR COMMENTS (re-submittals only)
5. CONDITIONS (if approval is recommended)
6. DECISION
   [ ] Approve
   [ ] Approve with conditions
   [ ] Deny
   [ ] Incomplete — return for additional information

REVIEWER:          [Name and title]
DATE:              [Date]
NEXT REVIEWER:     [Discipline and name, if applicable]
```

Length: typically 1–3 pages for a routine permit; longer for complex submittals. Use plain numerals for code sections (e.g., "2021 IBC § 1009.1"). The memo should be specific enough that the applicant can fix what is wrong without a phone call.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Vested rights — Tex. Loc. Gov't Code Ch. 245:** Treat carefully what is documented as a "complete" application. Under Ch. 245, the regulations in effect when the first complete application in a project is filed govern the project. A "complete" determination locks in the applicable rules. If the submittal is missing required items and is not complete, the review memo should say so and identify the items, so the date the application becomes complete is documented. Coordinate with the city attorney before applying Ch. 245 in a contested case.

**Quasi-judicial exhibit risk:** A denial or conditional approval may be appealed administratively under the city's procedures and, in some cases, judicially. The review memo becomes part of the record. Cite the code accurately and document the discrepancy in enough specificity that another reviewer could verify it independently.

**Public records:** Permit applications and review memos are public records under Tex. Gov't Code Ch. 552, with certain exemptions for personal information of the applicant under § 552.137 (email addresses of members of the public). Redact accordingly when responding to a public records request.

**Retention:** Permit files generally retain in accordance with Texas State Library Local Government Retention Schedule BC (Building, Construction, Inspection, Permits). Most building permit files retain for the life of the structure plus 10 years; check the schedule for the specific permit type.

## References

- This skill ships without a separate references file. The controlling reference for any specific permit is the city's adopted code and the submittal checklist for that permit type. Pull those documents into context when running the review.

## Examples

- See `examples/residential-addition-permit-review.md` for a worked example: review of a building permit submittal for a residential addition, returning an "incomplete — return for additional information" decision with three missing items and one code discrepancy.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
