---
name: variance-request-analyzer
description: Analyzes a variance request against the statutory unique-hardship criteria in Tex. Loc. Gov't Code § 211.009 and produces a written staff memo with findings on each criterion and a staff recommendation. Use when a planner or development services reviewer is preparing the staff memo for a Zoning Board of Adjustment variance hearing.
---

# Variance Request Analyzer

> Produces the staff memo behind a variance recommendation, with findings tied criterion by criterion to § 211.009. Built for planners and ZBA liaisons who need defensible reasoning in a record that will outlive the hearing.

## When to Use

- "Analyze the setback variance request at 503 Hickory and write the staff memo."
- "Run a variance analysis on this side-yard reduction request for the ZBA."
- "I need findings on each statutory criterion for a height variance hearing next month."
- "Draft the staff recommendation memo for the variance at the corner of Elm and 4th."
- A variance application is scheduled for a Zoning Board of Adjustment hearing under Tex. Loc. Gov't Code § 211.008, and staff needs the substantive memo.

## Inputs Needed

Required:

- Case number
- Subject property: address, legal description, lot size, lot shape (including any unusual configuration), topography, and existing structures
- Property zoning
- The specific code provision the applicant seeks to vary
- The deviation requested (e.g., "reduction of side-yard setback from 10 feet to 5 feet")
- The applicant's claimed hardship
- Surrounding properties and any similar conditions
- Alternatives the applicant has considered or could have considered (redesign, smaller scope, different orientation)
- Public input received

Optional:

- Survey or site plan showing the proposed variance footprint
- Prior variance history on the property
- Whether the hardship was created by the applicant's own action (relevant under § 211.009(a)(3))

If the user has not provided the code section being varied, the lot's unique characteristic, or the alternatives analysis, ask before drafting. A variance memo without those three elements is not defensible.

## Process

1. Confirm the controlling authority. Variances are decided by the Zoning Board of Adjustment under Tex. Loc. Gov't Code § 211.008–.011. Substantive criteria are in § 211.009 and in the local zoning ordinance.
2. Restate the request in plain language. Identify the code provision, the dimensional standard required, and the deviation proposed.
3. Describe the property's unique physical characteristic. The hardship must arise from a condition unique to the property — typically lot shape, lot size, topography, or location. Generic neighborhood conditions are not unique hardships.
4. Walk through each statutory criterion under § 211.009 and the local ordinance equivalent, in order:
   (a) Special conditions and circumstances unique to the property that do not result from the actions of the applicant.
   (b) Literal interpretation of the ordinance deprives the applicant of rights commonly enjoyed by other properties in the same district.
   (c) Granting the variance will not confer a special privilege not enjoyed by other properties.
   (d) The variance is the minimum necessary to make possible reasonable use of the land.
   (e) Granting the variance will be consistent with the spirit of the ordinance and substantial justice will be done.
5. For each criterion, write a finding: state the criterion, state the facts, state the conclusion. Do not write conclusions without facts.
6. Address self-created hardship explicitly. A hardship created by the applicant — for example, by subdividing a parcel into a configuration that no longer fits the ordinance — generally does not support a variance.
7. State the staff recommendation. The recommendation must be tied to the findings. If staff finds the criteria are met, recommend approval (with conditions where appropriate). If not, recommend denial and identify which criterion failed.

## Output Format

Plain markdown. No emoji. Headers in this order:

```
VARIANCE ANALYSIS MEMO

CASE NUMBER:       [V-YYYY-NN]
PROPERTY:          [Address; legal description; lot size]
ZONING:            [Zone]
APPLICANT:         [Name]
HEARING BODY:      Zoning Board of Adjustment
HEARING DATE:      [Date]

1. REQUEST SUMMARY
2. PROPERTY CHARACTERISTICS
3. APPLICABLE STANDARDS
4. FINDINGS ON EACH STATUTORY CRITERION
   4a. Special conditions unique to the property and not
       self-created (§ 211.009(a)(3) and local code)
   4b. Literal interpretation would deprive the applicant of
       rights commonly enjoyed by others in the same district
   4c. Variance does not confer a special privilege
   4d. Variance is the minimum necessary
   4e. Variance is consistent with the spirit of the ordinance
       and substantial justice will be done
5. ALTERNATIVES ANALYSIS
6. PUBLIC INPUT
7. STAFF RECOMMENDATION
   [ ] Approval
   [ ] Approval with conditions
   [ ] Denial
   Conditions (if approval):
   Rationale tied to findings:

PREPARED BY:       [Name and title]
DATE:              [Date]
```

Length: typically 2–4 pages. Findings should read as findings: criterion, facts, conclusion.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Tex. Loc. Gov't Code § 211.009 standard:** The Texas variance standard is strict. A variance authorizes deviation from a specific dimensional standard because of a unique property condition. The ZBA cannot grant a use variance — only an area or dimensional variance. Use variances require a rezoning.

**Quasi-judicial proceeding:** ZBA decisions must rest on competent evidence in the record. § 211.011 provides for judicial review by writ of certiorari within 10 days. Findings matter.

**Supermajority vote:** Tex. Loc. Gov't Code § 211.008(c) requires the affirmative concurring vote of 75% of ZBA members to grant a variance.

**Fair Housing Act considerations:** A reasonable accommodation request under 42 U.S.C. § 3604(f)(3)(B) of the Fair Housing Act is governed by federal fair-housing law, not the § 211.009 unique-hardship standard. Route those cases to the city attorney.

**Public records and retention:** Variance applications, memos, and decisions are public records under Tex. Gov't Code Ch. 552. Case files retain permanently under Texas State Library Local Government Retention Schedule DC.

## References

- This skill ships without a separate references file. The controlling references are Tex. Loc. Gov't Code §§ 211.008–.011 and the local zoning ordinance variance criteria. Pull these into context when running the analysis.

## Examples

- See `examples/setback-variance-corner-lot.md` for a worked example: variance analysis for a 5-foot side-yard setback reduction on a corner lot in the City of Cedar Ridge, finding the unique-hardship standard met because the corner lot has two front yards under the code.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
