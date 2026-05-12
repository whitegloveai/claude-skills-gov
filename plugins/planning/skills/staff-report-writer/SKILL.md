---
name: staff-report-writer
description: Drafts the planning staff report for P&Z or City Council with case background, applicable regulations, surrounding context, staff analysis, findings, and a recommendation. Use when a planner is assembling the staff report that will go in the P&Z or council packet for a zoning, plat, variance, or special-use case under Tex. Loc. Gov't Code Ch. 211 or Ch. 212.
---

# Staff Report Writer

> Produces the planning staff report that anchors a packet, walks the body through the case, and stands up as an exhibit on appeal. Built for planners who already did the work and need the finished document.

## When to Use

- "Draft the staff report for the rezoning case going to P&Z next Tuesday."
- "I need the staff report for the plat approval."
- "Write up the variance staff report for the ZBA on June 18."
- "Put together a staff report for the SUP at 215 Elm for the council packet."
- A planning case is on the agenda and the staff report must be in the packet by the city's posting deadline.

## Inputs Needed

Required:

- Case number and case type (rezone, SUP, PD, plat, replat, variance, comp plan amendment)
- Hearing body (P&Z, ZBA, City Council)
- Hearing date
- Applicant and property owner
- Subject property: address, legal description, acreage, current zoning, current use
- The specific request
- Applicable code sections and the comp plan reference
- Surrounding context (zoning and use on each side)
- The substantive staff analysis (this is the input that does most of the work; if it is not provided, the skill cannot draft a report)
- Recommendation (approval, approval with conditions, denial, deferral)
- List of attachments to be referenced (vicinity map, site plan, application, narrative, notices, public comment log)

Optional:

- Prior staff actions on the case (P&Z recommendation if council is the hearing body)
- Conditions of approval if conditional approval is recommended
- Public hearing record if hearings have already occurred at a prior body

If the user has not provided the substantive analysis or the recommendation, ask before drafting. The staff report is a vehicle for analysis already done; it is not the place where the analysis happens.

## Process

1. Identify the case type and the controlling statutory framework. Rezoning and SUP cases proceed under Tex. Loc. Gov't Code Ch. 211; plats under Ch. 212; variances under § 211.009.
2. Build the cover page. Case number, hearing date, hearing body, applicant, property, request, and the bottom-line recommendation. The cover page should let a council member who reads only the first page know the case and the recommendation.
3. Draft Background. Three to six paragraphs identifying the property, the applicant, the prior history on the parcel if any, and what brought the case forward.
4. Draft Applicable Regulations. Identify the controlling code provisions and comp plan references with specific citations.
5. Draft Surrounding Context. North, south, east, west — zoning and use on each side.
6. Draft Staff Analysis. This is the substantive section. Walk through the criteria the body must consider and present the facts that bear on each.
7. Draft Findings. Each finding states the criterion, the supporting facts, and the conclusion. Findings are not opinions; they are evidence-based statements.
8. Draft Recommendation. State the recommended action and tie it to the findings. If conditional approval is recommended, list the conditions.
9. Build the Attachments list. Identify each attachment by exhibit letter or number.
10. Sign and date. Identify the preparing planner and the reviewing director.

## Output Format

Plain markdown. The cover page is a compact block; the body is the report. No emoji.

```
PLANNING STAFF REPORT

COVER PAGE
==========
Case Number:         [Z/V/SP-YYYY-NN]
Hearing Body:        [P&Z / ZBA / City Council]
Hearing Date:        [Date]
Applicant:           [Name]
Property:            [Address; acreage]
Request:             [Brief]
Staff Recommendation: [Approval / Approval with Conditions /
                       Denial / Deferral]

BODY
====
1. BACKGROUND
2. APPLICABLE REGULATIONS
3. SURROUNDING CONTEXT
4. STAFF ANALYSIS
5. FINDINGS
6. RECOMMENDATION
7. CONDITIONS (if recommending approval with conditions)
8. ATTACHMENTS

   Exhibit A: Vicinity map
   Exhibit B: [etc.]

PREPARED BY:         [Name and title]
DATE:                [Date]
REVIEWED BY:         [Planning Director]
DATE:                [Date]
```

Length: typically 4–10 pages depending on case complexity. A routine plat may be 2–3 pages; a contested rezoning may be 8–12.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Quasi-judicial exhibit risk:** The staff report is the primary planning exhibit in any record on appeal. Zoning decisions are reviewable by writ of certiorari under Tex. Loc. Gov't Code § 211.011 with a 10-day deadline. Plat decisions are reviewable under Tex. Loc. Gov't Code § 212.0099. Variance decisions are reviewable under § 211.011 through the ZBA pathway. The report must read as a coherent document on its own.

**Findings of fact:** Findings are not editorial. A finding states the criterion, the facts in the record that support the criterion, and the conclusion. A staff report that recommends approval without findings keyed to criteria is procedurally weak. A staff report that recommends denial without findings is more vulnerable still.

**Fair Housing Act considerations:** Cases involving group housing, supportive housing, or any use serving a protected class under 42 U.S.C. § 3601 et seq. require careful language. The staff analysis must address the use on its planning merits without language that could be read as a proxy for discrimination. Route those cases through the city attorney.

**Public records:** Staff reports are public records under Tex. Gov't Code Ch. 552 once posted with the agenda packet. Drafts are exempt under § 552.111 (agency memoranda) until posted.

**Retention:** Staff reports retain permanently with the case file under Texas State Library Local Government Retention Schedule DC.

## References

- This skill ships without a separate references file. Pull into context the city's zoning ordinance, comp plan, the substantive analysis already done by the planner, and the relevant Local Government Code chapters when running the report.

## Examples

- See `examples/z-2026-04-staff-report.md` for a worked example: a staff report for a fictional rezoning case going to City Council on June 9, 2026. This pairs with the zoning-narrative-writer and public-hearing-notice examples in this plugin to form a complete case file.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
