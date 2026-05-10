---
name: site-plan-summary
description: Summarizes a submitted site plan against the city's dimensional standards, parking and landscape requirements, drainage and access standards, and any conditions of underlying zoning approval. Use when a planner or development review committee staff member needs a written site plan review memo for staff sign-off, P&Z review, or a development review committee meeting.
---

# Site Plan Summary

> Produces the site plan review memo that goes into the case file and onto the agenda. Built for planners who have walked the plan with the engineer and need to put the analysis on paper.

## When to Use

- "Summarize the site plan for the mixed-use project at 800 Live Oak Drive."
- "Run a site plan review on the proposed convenience store at 1500 FM 1200."
- "I need a development review committee memo for the apartment site plan at Cedar Crossing."
- "The Planning Commission is reviewing this site plan next week — write the memo."
- A site plan has been submitted, fee paid, and a multi-discipline review (planning, engineering, fire, public works) has produced comments that need to be summarized in a single memo.

## Inputs Needed

Required:

- Project name and case number
- Property address, legal description, and zoning
- Proposed use(s) and gross floor area
- Lot size in acres or square feet
- Site plan sheets received (typically C-1 through C-8 or similar)
- Building footprint dimensions and height
- Parking count proposed
- Landscape plan summary (street trees, parking lot interior, buffer requirements)
- Drainage analysis summary
- Access points (driveway count, location, type)
- Photometric plan summary if exterior lighting is proposed
- Any variances or waivers requested
- Underlying zoning case conditions, if any

Optional:

- Traffic impact analysis findings
- Tree survey and tree mitigation calculations
- Phasing plan
- Easement encumbrances on the property

If the user has not provided the zoning, the dimensional standards table for that zone, or the parking and landscape requirements, ask before drafting.

## Process

1. Confirm the zoning and pull the dimensional standards for the zone (setbacks, height, lot coverage, floor area ratio, density limits if residential).
2. Build the zoning compliance table. List each standard required, the value proposed, and a compliance status (compliant / non-compliant / waiver requested).
3. Run the parking analysis. Count the required parking by use under the city's parking ordinance; compare to provided. Note any shared parking arrangements or off-site agreements.
4. Run the landscaping compliance. Address street trees, parking lot interior landscaping, perimeter buffers, screening requirements where commercial abuts residential, and any tree preservation or mitigation.
5. Summarize the drainage analysis. Note pre-development and post-development runoff, the detention or retention strategy, and the design storm. If a fee-in-lieu is proposed, note the amount.
6. Address access and circulation. Number and location of driveways, distance from intersections, internal circulation, fire lane compliance, and emergency vehicle access.
7. Summarize the photometric plan. Note maximum footcandle at the property line, fixture cutoff classification, and compliance with any dark-sky overlay.
8. List variances and waivers explicitly. Each must identify the standard, the proposed deviation, and the procedural path (administrative waiver, Zoning Board of Adjustment, P&Z, council).
9. List recommended conditions of approval. Tie each condition to a specific finding above.
10. State the staff recommendation: administrative approval, approval with conditions, deferral, or denial.

## Output Format

Plain markdown. The compliance table is a markdown table. No emoji.

```
SITE PLAN REVIEW MEMO

CASE NUMBER:       [SP-YYYY-NN]
PROJECT NAME:      [Name]
PROPERTY:          [Address; legal description; acreage]
ZONING:            [Zone]
PROPOSED USE:      [Use(s) and floor area]
APPLICANT:         [Name]

1. PROJECT SUMMARY

2. ZONING COMPLIANCE TABLE

   | Standard           | Required | Proposed | Status      |
   |--------------------|----------|----------|-------------|
   | Front setback      |          |          |             |
   | Side setback       |          |          |             |
   | Rear setback       |          |          |             |
   | Maximum height     |          |          |             |
   | Maximum lot cover  |          |          |             |
   | Floor area ratio   |          |          |             |
   | Density (if resi)  |          |          |             |

3. PARKING ANALYSIS
   3a. Required by use
   3b. Provided
   3c. Compliance status

4. LANDSCAPING COMPLIANCE
   4a. Street trees
   4b. Parking lot interior
   4c. Perimeter buffers
   4d. Tree preservation/mitigation

5. DRAINAGE AND STORMWATER

6. ACCESS AND CIRCULATION

7. PHOTOMETRIC / LIGHTING

8. VARIANCES OR WAIVERS REQUESTED

9. RECOMMENDED CONDITIONS OF APPROVAL

10. STAFF RECOMMENDATION

PREPARED BY:       [Name and title]
DATE:              [Date]
DRC REVIEW DATE:   [Date]
```

Length: typically 3–6 pages depending on project size and complexity.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Vested rights — Tex. Loc. Gov't Code Ch. 245:** Site plans are within the scope of Ch. 245. The regulations in effect when the first complete application in the project was filed govern the site plan review. Document the project's first-application date so a later regulatory change does not erroneously control the review.

**Subdivision interaction — Tex. Loc. Gov't Code Ch. 212:** If the site plan accompanies a plat or replat, Ch. 212 procedural requirements apply to the plat in parallel. The site plan memo should reference but not substitute for the plat review.

**Engineer of record:** The site plan must be sealed by a licensed Texas professional engineer. The review memo identifies the engineer of record but does not certify the engineering; the engineer's seal carries that certification.

**Retention:** Site plan case files are retained permanently under Texas State Library Local Government Retention Schedule DC, Item 1100-08 (Site Plan and Plat Files).

**Quasi-judicial exhibit risk:** Where site plan approval requires P&Z or council action, the memo becomes part of the record on any administrative or judicial appeal. Citations must be accurate.

## References

- This skill ships without a separate references file. The controlling references are the city's zoning ordinance dimensional standards, the parking and landscape ordinances, the drainage manual, and any overlay district requirements. Pull these into context when running the review.

## Examples

- See `examples/cedar-ridge-mixed-use-site-plan.md` for a worked example: site plan review memo for a 2.4-acre mixed-use development at 800 Live Oak Drive in the City of Cedar Ridge, with 12,000 sf retail on the ground floor and 32 residential units above.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
