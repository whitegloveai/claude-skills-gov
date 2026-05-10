---
name: public-hearing-notice
description: Drafts the three-part public hearing notice package (newspaper publication, mailed notice to nearby property owners, and posted-sign content) for a planning matter under Tex. Loc. Gov't Code Ch. 211 or Ch. 212. Use when a planner or city secretary is preparing the statutory notice for a rezoning, special-use permit, variance, plat, or similar land-use hearing.
---

# Public Hearing Notice

> Produces the full notice package for a planning hearing in one shot, so the city does not get a § 211.011 writ overturned on a notice defect. Built for planners and city secretaries who run hearings on tight calendars.

## When to Use

- "Draft the public hearing notices for Case Z-2026-04, the Pecan Street rezoning."
- "I need the three-part notice package for a variance hearing on the corner lot at 503 Hickory."
- "Set up the plat hearing notices for the Live Oak Crossing replat."
- "Generate the newspaper notice, mailed notices, and posted-sign content for the SUP hearing."
- A planning case is scheduled for a public hearing and the city must publish, mail, and (per local ordinance) post notice before the hearing date.

## Inputs Needed

Required:

- Case type and case number
- Subject property: address, legal description, acreage
- Current and proposed status (e.g., zoning change from X to Y)
- Hearing body, date, time, and location
- Statutory basis for the notice
- Newspaper of general circulation and target publication date
- Mailing list source and number of owners (most recent approved municipal tax roll, owners within statutory radius — typically 200 feet)
- City secretary name
- Posted-sign requirement under local code, if any

Optional: courtesy email to a neighborhood association or HOA (not a statutory substitute); Spanish translation per local policy.

If the user has not provided the controlling statute or the hearing body, ask before drafting.

## Process

1. Confirm the case type and the controlling statute. Zoning amendments and SUPs are noticed under Tex. Loc. Gov't Code § 211.007. Variances are noticed under § 211.009(d). Plats and replats are noticed under Tex. Loc. Gov't Code § 212.0095 where applicable, or per local subdivision ordinance.
2. Confirm timing. Newspaper publication for zoning matters: at least 15 days before the hearing. Mailed notice for zoning matters: at least 10 days before the hearing. Local codes may require longer notice; comply with the more stringent rule.
3. Draft the newspaper notice. Identify the city, the case, the property by address and legal description, the request, the hearing body, the date, time, and location of the hearing, and where the application may be reviewed.
4. Draft the mailed notice. Same content as the newspaper notice, addressed personally to each owner of record from the most recent approved tax roll. Include a return address for written comments and protest petitions.
5. Draft the posted-sign content if the local code requires posting. The sign identifies the case, property, proposed change, hearing date and time, and a contact number.
6. Build the city secretary's verification block for each component.
7. Flag any ancillary notice (e.g., comprehensive plan amendment notice under separate statute).

## Output Format

Plain markdown delivered as three labeled documents within one file. Each document is publication-ready.

```
PART 1 — NEWSPAPER PUBLICATION NOTICE
(For publication in [Newspaper] on [Date], at least 15 days
before the hearing)

NOTICE OF PUBLIC HEARING
CITY OF [City], TEXAS

[Hearing body] will hold a public hearing on [Date] at
[Time] at [Location] to consider:

Case Number: [Z-YYYY-NN]
Property:    [Address; legal description; acreage]
Request:     [From X to Y; or other request]
Authority:   Tex. Loc. Gov't Code § [citation]

The application is available at [Office] during regular
business hours. Written comments may be submitted to
[Address] before the hearing.


PART 2 — MAILED NOTICE TO PROPERTY OWNERS

Mailed [Date] to [N] owners within 200 feet per the most
recently approved [County] Appraisal District tax roll. Use
the same content as Part 1 plus the addressee block, return
address, and written-comment instructions.


PART 3 — POSTED-SIGN CONTENT
(Posted on the property under [local code section] at least
[N] days before the hearing)

PUBLIC HEARING NOTICE — [Hearing body], City of [City]
Case: [Case number]    Request: [Brief]
Hearing: [Date and time]    Location: [Location]
Information: [Phone]


CERTIFICATION OF NOTICE
I, [City Secretary], City Secretary of the City of [City],
certify that:
   (a) The Part 1 notice was published in [Newspaper] on
       [Date], not less than 15 days before the hearing.
   (b) The Part 2 notices were mailed first-class on [Date],
       not less than 10 days before the hearing, to [N]
       owners on the most recently approved tax roll.
   (c) The Part 3 sign was posted on [Date] under [local
       code section].

____________________________________
[City Secretary], City Secretary
```

Length: typically 2–3 pages.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Notice defects are the most common reversal ground:** A zoning decision may be set aside on writ of certiorari under Tex. Loc. Gov't Code § 211.011 if notice was defective. Verify dates and keep the publisher's affidavit and certified mailing list in the case file.

**Tax roll currency:** § 211.007 ties the mailing list to the most recently approved municipal tax roll. Pull the list as of the mailing date and document the source.

**Posted sign and Spanish translation:** Neither is required by state law for zoning notice; both may be required by local policy. Confirm the local code.

**Fair Housing Act:** If the case touches group housing, supportive housing, or another use serving a protected class under 42 U.S.C. § 3601 et seq., describe the use accurately and avoid editorializing. Coordinate with the city attorney.

**Public records and retention:** The notice and certified mailing list are public records under Tex. Gov't Code Ch. 552. Notice records retain permanently with the case file under Texas State Library Local Government Retention Schedule DC.

## References

- This skill ships without a separate references file. The controlling references are the Local Government Code sections, the local zoning and subdivision ordinances, and the county appraisal district tax roll.

## Examples

- See `examples/z-2026-04-public-hearing-notices.md` for a worked example: the full three-part notice package for Case Z-2026-04, the rezoning at 1100 Pecan Street in the City of Cedar Ridge, with mailed notice to property owners within 200 feet.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
