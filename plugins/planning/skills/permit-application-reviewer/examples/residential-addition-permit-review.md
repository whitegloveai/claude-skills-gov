# Example: Permit Review Memo — Residential Addition

This is a worked example for the permit-application-reviewer skill. It uses the fictional City of Cedar Ridge, TX. The output is a first-cycle review memo returning the submittal as incomplete.

## Input

- **Permit type:** Building — residential addition
- **Permit number:** BLD-2026-0317
- **Submittal date:** May 6, 2026
- **Property:** 411 Magnolia Avenue, Cedar Ridge, TX 75000
- **Owner:** Brandon and Tessa Whitley
- **Applicant/contractor:** Hill Country Custom Builders, LLC; Texas RBC #45221
- **Scope of work submitted:** 320-square-foot bedroom addition at the rear of an existing 1,840-sf single-family residence; matching slab-on-grade foundation, 2x6 wood framing, asphalt shingle roof
- **Documents received:**
  - Permit application form, signed and dated May 6, 2026
  - Site plan (Sheet C-1)
  - Floor plan (Sheet A-1)
  - Foundation plan (Sheet S-1)
  - Wall sections (Sheet A-3)
  - Energy compliance affidavit
  - Contractor license certification
- **Documents NOT received (per the city's residential addition checklist):**
  - Roof framing plan
  - Elevations on all four sides
  - Survey showing existing improvements and the addition footprint
- **Applicable code:** 2021 International Residential Code as adopted by City of Cedar Ridge Ordinance 2022-08; Cedar Ridge Code of Ordinances Ch. 18, Building Regulations; Ch. 24, Zoning (R-1 dimensional standards)
- **Zoning check:** Property is zoned R-1. R-1 rear setback is 20 feet. The site plan shows the rear face of the addition at 17 feet from the rear property line.

## Output

```
PERMIT REVIEW MEMO

PERMIT NUMBER:     BLD-2026-0317
PERMIT TYPE:       Building — Residential Addition
PROPERTY:          411 Magnolia Avenue, Cedar Ridge, TX 75000
OWNER:             Brandon and Tessa Whitley
APPLICANT:         Hill Country Custom Builders, LLC
                   Texas RBC #45221
SUBMITTAL DATE:    May 6, 2026
SUBMITTAL CYCLE:   First submittal

1. APPLICATION SUMMARY

The applicant proposes a 320-square-foot bedroom addition at the
rear of an existing 1,840-square-foot single-family residence at
411 Magnolia Avenue. The work includes a matching slab-on-grade
foundation, 2x6 wood framing, and matching asphalt shingle roof.
The property is zoned R-1 Single-Family Residential.

2. COMPLETENESS CHECK

   2a. Documents received
       - Permit application, signed and dated May 6, 2026
       - Site plan (Sheet C-1)
       - Floor plan (Sheet A-1)
       - Foundation plan (Sheet S-1)
       - Wall sections (Sheet A-3)
       - Energy compliance affidavit
       - Contractor license certification

   2b. Items missing per the Residential Addition Submittal
       Checklist (Cedar Ridge Form BLD-101, Revision 2024-03):

       - Item 5: Roof framing plan. The submittal includes wall
         sections but no plan view of the roof framing showing
         rafter or truss layout, ridge and valley locations, and
         connection details to the existing structure.

       - Item 7: Elevations on all four sides. The submittal does
         not include elevations. Four sides are required.

       - Item 11: Boundary survey showing existing improvements
         and the addition footprint, sealed by a Texas-registered
         surveyor. The submittal includes a site plan drawn by
         the designer but not a sealed survey.

3. CODE COMPLIANCE REVIEW

   3a. Zoning — Cedar Ridge Code of Ordinances Ch. 24 (R-1
       dimensional standards). Discrepancy. R-1 requires a
       20-foot rear setback. The site plan (Sheet C-1) shows the
       rear face of the addition at 17 feet from the rear
       property line, which is 3 feet short of the required
       setback. The applicant has two options: (i) redesign the
       addition to meet the 20-foot rear setback, or (ii) apply
       for a setback variance to the Zoning Board of Adjustment
       under Tex. Loc. Gov't Code § 211.009 and the city's
       variance procedures.

   3b. 2021 IRC § R301 (Design criteria). Reviewed. Framing
       species and grade noted on Sheet S-1 are acceptable.

   3c. 2021 IRC § R302 (Fire-resistant construction). Reviewed.
       The addition is more than 5 feet from any adjacent
       structure. No fire-resistant separation required.

   3d. 2021 IRC § R401 (Foundations). Reviewed. The foundation
       plan calls for a 4-inch slab on grade with No. 4 bars at
       16 inches on center each way and a 12-inch by 24-inch
       perimeter beam. Acceptable.

   3e. 2021 IRC § R807 (Attic access). Cannot fully review
       without the roof framing plan. Pending the resubmittal.

4. RESPONSE TO PRIOR COMMENTS

Not applicable — first submittal.

5. CONDITIONS

Not applicable at this submittal cycle.

6. DECISION

   [ ] Approve
   [ ] Approve with conditions
   [ ] Deny
   [X] Incomplete — return for additional information

Applicant must submit:
   (a) Roof framing plan (Checklist Item 5).
   (b) Elevations on all four sides (Checklist Item 7).
   (c) Boundary survey, sealed by a Texas-registered surveyor,
       showing existing improvements and the proposed addition
       footprint (Checklist Item 11).
   (d) Resolution of the R-1 rear setback discrepancy, either
       by redesign or by applying for a variance.

REVIEWER:          Marcus Webb, Building Plans Examiner
DATE:              May 9, 2026
NEXT REVIEWER:     Adaeze Okafor, AICP, Planning Director —
                   for zoning sign-off after the setback issue
                   is resolved.

AI-assisted draft, reviewed by Building Plans Examiner Marcus Webb.
```

## Notes for the User

- The clock under Tex. Loc. Gov't Code Ch. 245 begins when the application is complete. This submittal is not complete; the review memo documents the missing items so the date of completion can be established on the resubmittal.
- Cedar Ridge's Building Plans Examiner runs the building review; the Planning Director runs the zoning review. The decision routes the file appropriately.
- If the applicant elects to pursue a variance instead of redesigning, the variance application is a separate case and follows the procedures in the variance-request-analyzer skill in this plugin.
