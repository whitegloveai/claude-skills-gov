---
name: variance-analyzer
description: Drafts a budget-to-actual variance memo for a monthly or quarterly financial report. Use when a finance director, budget analyst, or department head needs to explain material variances by line item or category, project year-end, and recommend corrective action for the council's monthly or quarterly financial review.
---

# Variance Analyzer

> Drafts a budget-to-actual variance memo. Built for finance staff turning a budget vs actual report into a narrative the council and city manager will actually read.

## When to Use

- "Draft the Q3 variance analysis for the General Fund."
- "Write the variance memo for the monthly financial report — flag anything over 10 percent."
- "Explain the police overtime overage and the capital outlay underrun in the FY2026 mid-year report."
- "I need a memo for the City Manager on the Water Fund variances for the quarter."
- "Convert this budget vs actual spreadsheet into a written variance analysis with year-end projections."
- The finance director presents monthly or quarterly results to the council under Tex. Loc. Gov't Code § 103.001 and needs uniform variance commentary across funds.

## Inputs Needed

Required:

- Entity name, fund, and reporting period (e.g., "City of Cedar Ridge, General Fund, Q3 FY2026" or "Month ended April 30, 2026")
- Budget vs actual figures by line item or by category, with both period and year-to-date columns
- Materiality threshold (commonly 10 percent and $25,000, or whatever the city's financial policies specify)
- Prior-period trend context — at minimum prior-year YTD for the same period
- The department contact who can confirm operational drivers

Optional:

- Budget amendments approved during the period that affect the comparison baseline
- Encumbrances at period end (open POs, contracts) that affect projected year-end
- Known nonrecurring items (a one-time settlement payment, a FEMA reimbursement)
- The city's adopted reserve policy (so the memo can flag fund balance impacts)

If the user has not provided a materiality threshold or the prior-period context, ask before drafting. Without those the memo will either flag every line or miss the items the council actually needs to see.

## Process

1. Confirm period, fund, and materiality threshold. Apply a two-test rule by default: a variance is "material" if it exceeds the percentage threshold (e.g., 10 percent) AND the dollar threshold (e.g., $25,000). Both tests must trip.
2. Compute period and YTD variances for revenue and expenditure categories. For revenue, favorable means actual is above budget; for expenditure, favorable means actual is below budget. Label every variance F or U.
3. Identify the top three to seven material variances, balanced between revenue and expenditure. Avoid a memo that is only bad news or only good news.
4. For each material variance, draft one paragraph: the variance amount and percent, the driver (operational explanation), whether it is timing or trend, and whether it is recurring or one-time. The department contact must verify the driver.
5. Build a YTD Trend section: how the run-rate compares to prior year and to budget. Two to four sentences.
6. Project year-end: extrapolate based on YTD, encumbrances, and known nonrecurring items. State the projected favorable or unfavorable variance and the projected fund balance impact.
7. Draft Recommended Actions: budget amendments to bring forward, line items to monitor, departments to coordinate with. Be specific.
8. Build a Watch List: items not yet material but trending. Two to four bullet points.

## Output Format

Plain markdown memo. Tone: factual, plain, no hedging language. The reader is the city manager, finance committee, or council.

Length: 600 to 1,200 words for a single fund; longer when multiple funds are combined. Structure:

```
MEMORANDUM

TO:       [Recipient — City Manager / Finance Committee / Council]
FROM:     [Finance Director name and title]
DATE:     [Date of memo]
SUBJECT:  [Fund] Variance Analysis — [Period] FY[year]

EXECUTIVE SUMMARY
[3–5 sentences: the headline numbers, whether the fund is on track,
the projected year-end position, and the single most important issue.]

MATERIAL VARIANCES — REVENUE
1. [Revenue line] — $X over/under budget ([Y%] F/U)
   Driver: [operational explanation]. [Recurring/one-time]. [Timing/trend].

MATERIAL VARIANCES — EXPENDITURE
1. [Expense line] — $X over/under budget ([Y%] F/U)
   Driver: [operational explanation]. [Recurring/one-time]. [Timing/trend].

YTD TREND
[How the run-rate compares to prior year and to budget. Two to four
sentences.]

PROJECTED YEAR-END
[Projected favorable or unfavorable variance to budget. Projected
ending fund balance and policy implications.]

RECOMMENDED ACTIONS
1. [Specific action — budget amendment, transfer, freeze]
2. [Specific action]

WATCH LIST
- [Item not yet material but trending]
- [Item not yet material but trending]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas financial reporting:**

- Tex. Loc. Gov't Code § 103.001 requires the city to keep a system of accounts and provide periodic financial reports.
- Tex. Loc. Gov't Code § 102.0065 requires notice and a public hearing before the council adopts a budget amendment. A variance memo that recommends an amendment must build the timeline in.
- The Public Funds Investment Act, Tex. Gov't Code Ch. 2256, requires the city to report investment performance. Variance memos covering investment income should reconcile to the Ch. 2256 quarterly investment report.

**GASB considerations:** Variance analysis is a budgetary basis exercise, not a GAAP exercise. Encumbrances are treated as expenditures for budget but as commitments for GAAP. Disclose the basis explicitly so the council does not try to tie the variance memo to the most recent ACFR. Year-end projections should reference GASB 54 fund balance classifications when discussing reserve impacts.

**Public records:** The variance memo is a public record under Tex. Gov't Code Ch. 552 once it is transmitted to the council or placed in a posted packet. Internal drafts may be exempt under § 552.111 (agency memoranda) until transmitted.

**Retention:** Monthly and quarterly financial reports retain for 5 years per Texas State Library Local Government Retention Schedule GR, Item 1025-32 (Financial Reports — Periodic).

**Verify before transmittal:** All figures tie to the city's general ledger trial balance at period end. Department drivers are confirmed by the department head, not assumed. Year-end projections are documented with the underlying assumptions.

## References

- See `references/gasb-framework-summary.md` (in `budget-narrative-writer/references`) for fund-type framework and budgetary-basis distinctions.

## Examples

- See `examples/q3-fy2026-general-fund-variance.md` for a worked example: a Q3 FY2026 General Fund variance memo for the fictional City of Cedar Ridge, TX.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
