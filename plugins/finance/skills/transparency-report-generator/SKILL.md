---
name: transparency-report-generator
description: Drafts a Texas Comptroller Transparency Stars-style disclosure summary for a city's website. Use when a finance director, public information officer, or web team is publishing or updating a transparency page that consolidates the city's financial, contract, debt, and pension disclosures into a citizen-readable narrative.
---

# Transparency Report Generator

> Drafts the disclosure summary that lives on a city's transparency web page. Built for finance staff and PIOs who need to publish the city's Transparency Stars-style narrative without restating every spreadsheet.

## When to Use

- "Draft the FY2025 transparency summary for the city website."
- "Update the Traditional Finances section after the audit is final."
- "Write the citizen-facing narrative for our Transparency Stars submission."
- "Convert these FY data sheets into a plain-language transparency disclosure."
- "Refresh the debt obligations section for our annual transparency page."
- The Texas Comptroller's Transparency Stars program is being pursued or maintained; the city wants the public-facing page to read clearly and tie cleanly to the underlying disclosures.

## Inputs Needed

Required:

- Entity name and fiscal year
- Total revenue and total expenditure for the FY by major fund
- Outstanding debt at FY end by type (GO, certificates of obligation, revenue bonds, capital leases)
- Top-tier contract list (typically over a posted threshold) and the procurement disclosure source
- Pension plan participation (TMRS, ERS, or local actuarial plan) and the most recent funded ratio
- Property tax adopted rate components (M&O and I&S splits) under Tex. Tax Code Ch. 26

Optional:

- Economic development incentive disclosures (Ch. 380/381 agreements)
- Hotel occupancy tax and other dedicated revenue summaries
- Tax abatement disclosures (Statement 77 — Tax Abatement Disclosures under GASB 77)
- A check register or vendor payment summary location
- Links to the city's adopted budget, ACFR, and quarterly investment report

If the user has not provided the FY year and the total revenue/expenditure figures, ask before drafting.

## Process

1. Confirm the fiscal year and whether the underlying ACFR is final or pending. If pending, label estimates as "unaudited" and commit to a refresh date.
2. Identify the five Transparency Stars categories: Traditional Finances, Contracts and Procurement, Economic Development, Public Pensions, and Debt Obligations.
3. Draft Traditional Finances: total revenue and expenditure by major fund, year-over-year change, plain-language explanation. Reference the ACFR and adopted budget.
4. Draft Contracts and Procurement: vendor payment summary, link to the check register, top-N contracts list, and the city's procurement standards (LGC Ch. 252, Ch. 2269, Ch. 176 conflict filings).
5. Draft Economic Development: Tex. Loc. Gov't Code Ch. 380/381 agreements with named beneficiary, term, maximum incentive, and performance criteria. Tax abatements disclosed under GASB 77.
6. Draft Public Pensions: plan participation, contribution rate, most recent funded ratio, valuation date. State plans report to the Texas Pension Review Board.
7. Draft Debt Obligations: outstanding principal by issue, debt service coverage for revenue debt, bond ratings, EMMA continuing disclosure link. Tie to Tex. Loc. Gov't Code § 140.0045.
8. Draft header and navigation; include source-document dates.

## Output Format

Plain markdown. Tone: plain language, citizen-readable. The reader is a curious resident, a journalist, or a credit analyst.

Length: 1,000 to 2,000 words for the main page. Long tables and raw data should remain in linked source files (the budget book, the ACFR, the investment report).

```
CITY OF [NAME] FY[YEAR] FINANCIAL TRANSPARENCY
Last updated: [Date]   Source documents: [list]

OVERVIEW
[2–3 sentences orienting the reader.]

1. TRADITIONAL FINANCES
[Total revenue, total expenditure, year-over-year change, plain-
language explanation. Link to ACFR and adopted budget.]

2. CONTRACTS AND PROCUREMENT
[Vendor payment summary, top contracts, procurement standards, link
to check register and bid postings.]

3. ECONOMIC DEVELOPMENT
[Ch. 380/381 agreements, GASB 77 tax abatements, the named
beneficiaries and performance terms.]

4. PUBLIC PENSIONS
[Plan, contribution rate, funded ratio, valuation date, link to
PRB filings.]

5. DEBT OBLIGATIONS
[Outstanding principal by issue, ratings, EMMA link, debt service
schedule reference.]

CONTACT
[Finance Director contact info and the records request portal link.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas transparency framework:**

- Texas Comptroller of Public Accounts — Transparency Stars program. Voluntary recognition for cities, counties, school districts, and special districts that post specified financial information online. Five categories: Traditional Finances, Contracts and Procurement, Economic Development, Public Pensions, and Debt Obligations.
- Tex. Loc. Gov't Code § 140.008 — annual financial reporting by cities, counties, and special districts that issue debt.
- Tex. Loc. Gov't Code § 140.0045 — annual debt obligation reporting; cities of population 5,000+ must post outstanding debt information annually on the city website.
- Tex. Tax Code Ch. 26 — truth-in-taxation; the no-new-revenue and voter-approval tax rates must be calculated and posted; tax-rate notices governed by §§ 26.04–26.18.
- Tex. Gov't Code Ch. 2256 (Public Funds Investment Act) — quarterly investment reports.
- Texas Pension Review Board reporting under Tex. Gov't Code Ch. 801 for defined benefit pension plans.

**GASB linkage:** Transparency disclosures should be consistent with the GASB-compliant ACFR. GASB 77 (Tax Abatement Disclosures) requires disclosure of tax abatements granted by the reporting government and those granted by other governments that reduce the city's revenue. GASB 84 covers fiduciary activities. The Schedule of Long-Term Debt in the ACFR is the source for the Debt Obligations section.

**Public records:** All transparency disclosures are public records under Tex. Gov't Code Ch. 552. The page itself is a city-published document and is permanently in the city's records system. Underlying source documents (the ACFR, the budget book, the investment reports, the EMMA filings) are independently available.

**Retention:** Transparency disclosures retain permanently per Texas State Library Local Government Retention Schedule GR, Item 1025-22 (Adopted Budget) for budget-derived content; ACFRs retain permanently under GR, Item 1025-26. The web page itself is captured under the records of agency operation.

**Verify before publishing:** Every number on the page ties to an underlying source document; debt obligation figures match the most recent § 140.0045 filing; pension funded ratio matches the most recent actuarial valuation cited; contact and records request portal links work.

## References

- See `references/gasb-framework-summary.md` (in `budget-narrative-writer/references`) for fund-type framework. The Texas Comptroller Transparency Stars page at comptroller.texas.gov contains the current criteria checklist.

## Examples

- See `examples/cedar-ridge-fy2025-transparency-summary.md` for a worked example: a FY2025 transparency summary for a fictional Texas city.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
