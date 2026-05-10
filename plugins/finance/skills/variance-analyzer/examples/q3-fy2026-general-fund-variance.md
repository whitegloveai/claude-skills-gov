# Example: Q3 FY2026 General Fund Variance Memo — City of Cedar Ridge

This is a worked example for the variance-analyzer skill. It uses the fictional City of Cedar Ridge, TX. The same fiscal year is referenced in the council-ops examples (the June 9, 2026 council meeting includes an FY2026 budget amendment public hearing).

## Input

- **Entity:** City of Cedar Ridge, TX
- **Fund:** General Fund
- **Period:** Q3 FY2026 (Jan 1, 2026 – Mar 31, 2026); reporting at the end of Q3 with nine months of YTD activity
- **FY2026 adopted budget:** $24,840,000 revenue, $24,712,000 expenditure
- **Q3 YTD actual (75 percent of year elapsed):**
  - Revenue: $19,128,200 (77.0 percent of budget)
  - Expenditure: $18,866,400 (76.3 percent of budget)
- **Materiality threshold:** 10 percent of line and $50,000
- **Prior-year Q3 YTD:** Revenue $17,940,100; Expenditure $17,612,800
- **Known operational drivers:**
  - Police overtime overage driven by two extended homicide investigations and unfilled patrol vacancies
  - Capital outlay underrun driven by delayed delivery of two pieces of fleet equipment
  - Sales tax tracking 6.4 percent above prior year
  - Property tax collections complete at 99.1 percent
  - Building permit revenue softening on multifamily slowdown
- **Encumbrances at Q3 end:** $1,415,000 open POs and contracts

## Output

```
MEMORANDUM

TO:       Daniel Ahn, City Manager
          Cedar Ridge City Council Finance Committee
FROM:     M. Rivera, Finance Director
DATE:     April 22, 2026
SUBJECT:  General Fund Variance Analysis — Q3 FY2026

EXECUTIVE SUMMARY

Through Q3 of FY2026 the General Fund is performing ahead of budget on
revenue and within tolerance on expenditure. Total revenue of
$19,128,200 reflects 77.0 percent of the adopted $24,840,000 budget,
ahead of the 75 percent linear pace. Total expenditure of $18,866,400
reflects 76.3 percent of the adopted $24,712,000 budget, slightly
above pace driven by police overtime. The fund is projected to end
FY2026 with a positive operating result of $310,000 to $360,000, which
keeps unassigned fund balance above the 90-day reserve floor. The
single most important issue is the structural police overtime overage,
which staff recommends addressing through a budget amendment and a
recruiting plan refresh.

MATERIAL VARIANCES — REVENUE

1. Sales tax — $186,400 over budget (4.8 percent F YTD)
   Driver: Local sales activity outperformed adopted assumptions,
   particularly in the food service and building materials categories
   tracked by the Comptroller's allocation reports. Trend, not timing.
   Likely partially recurring; staff is monitoring whether the building
   materials lift is tied to a specific multifamily project that will
   wind down in Q4.

2. Building permit revenue — $84,200 under budget (14.6 percent U YTD)
   Driver: Multifamily permit activity slowed in late Q2 and Q3. Single-
   family activity is flat. This appears to be a trend, not timing, and
   correlates with regional financing conditions. Likely recurring into
   FY2027 absent a project pipeline change.

3. Court fines and fees — $52,800 under budget (11.2 percent U YTD)
   Driver: Reduced citation volume due to two patrol vacancies and a
   shift toward warnings during the staffing gap. Likely partially
   recurring while vacancies remain.

MATERIAL VARIANCES — EXPENDITURE

1. Police overtime — $214,600 over budget (38.7 percent U YTD)
   Driver: Two extended homicide investigations consumed approximately
   $74,000 in overtime in Q2 and Q3 (one-time). The remaining $140,600
   reflects coverage of three patrol vacancies (recurring while
   vacancies remain). Department recommends a $190,000 budget amendment
   and an accelerated lateral hiring incentive.

2. Capital outlay — $168,000 under budget (52.1 percent F YTD)
   Driver: Delayed manufacturer delivery of one ambulance chassis and
   one street sweeper. Both are on order with confirmed delivery in
   Q4 or early FY2027. Timing variance, not trend. Full encumbrance is
   captured in the $1,415,000 open PO balance; year-end actual will
   approach budget.

3. Workers' compensation premium — $58,400 over budget (16.2 percent U
   YTD)
   Driver: The TML Risk Pool experience modifier increased on renewal
   in October due to two prior-year claims. Recurring through the
   current policy year; will moderate in FY2027 if claims experience
   improves.

4. Personnel services (general government) — $112,000 under budget
   (6.8 percent F YTD)
   Driver: Vacancies in the Planning Director, IT Analyst, and Building
   Inspector roles for portions of the year. Recoveries from FY2025
   compensated absences accrual contributed an additional $18,000.
   Partial recurring; positions are expected to be filled in Q4.

YTD TREND

General Fund revenue is running 6.6 percent ahead of prior-year YTD,
driven primarily by sales tax and a stronger property tax collection
rate. Expenditure is running 7.1 percent ahead of prior-year YTD, of
which 4.0 percent reflects the council-approved compensation
adjustment and 1.1 percent reflects insurance and benefit cost
increases. The remaining 2.0 percent is concentrated in police
overtime. Excluding police overtime, expenditure growth is in line
with revenue growth.

PROJECTED YEAR-END

Staff projects FY2026 will close with revenue of $24,950,000 to
$25,030,000 (favorable to budget by $110,000 to $190,000) and
expenditure of $24,650,000 to $24,720,000 (favorable to budget by
roughly break-even to $62,000) before the recommended amendments
below. Projected operating result is favorable by $310,000 to
$360,000 versus the adopted budget. Projected unassigned fund balance
at September 30, 2026 is $5,820,000, equal to approximately 86 days
of operating expenditure, above the 75-day policy floor but below the
90-day target. Capital outlay encumbrances will carry forward into
FY2027 on the two delayed fleet purchases.

RECOMMENDED ACTIONS

1. Bring forward a budget amendment under Tex. Loc. Gov't Code
   § 102.0065 to increase the Police Department overtime appropriation
   by $190,000 and reallocate $190,000 from the General Fund
   contingency reserve.
2. Schedule a Finance Committee briefing on police staffing and the
   lateral hiring incentive proposal before the June council meeting.
3. Encumber the FY2026 fleet POs for carry-forward into FY2027 to
   preserve the appropriation.
4. Review the building permit revenue assumption used in the FY2027
   proposed budget; the current trajectory suggests reducing the
   adopted FY2026 estimate by approximately 8 percent for the FY2027
   baseline.

WATCH LIST

- Court fines and fees — monitor through Q4; recovery depends on
  patrol staffing.
- Workers' compensation experience modifier — quarterly risk pool
  reports should be reviewed.
- Sales tax — confirm whether the food service lift continues into
  Q4 or normalizes; this affects the FY2027 baseline.
- Property tax delinquencies — through Q3 the delinquency rate is
  0.9 percent, which is within tolerance; revisit at June 30.

cc: Department heads (General Fund); Internal Auditor
```

## Notes for the User

- The $190,000 budget amendment referenced here aligns with the
  June 9, 2026 council meeting's Item 5a (the public hearing on a
  FY2026 budget amendment for street maintenance reallocation in the
  council-ops example uses a different reallocation amount; the two
  amendments would be packaged separately).
- The 90-day fund balance target reflects the city's adopted reserve
  policy; confirm the current policy version before transmittal.
- Encumbrance treatment follows the city's budgetary basis. The ACFR
  will report encumbrances as commitments rather than expenditures.
- This memo was prepared with AI assistance and reviewed by Finance
  Director Rivera before transmittal.
```
