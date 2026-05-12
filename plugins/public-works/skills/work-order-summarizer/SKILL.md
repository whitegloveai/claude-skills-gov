---
name: work-order-summarizer
description: Summarizes a batch of public works work orders into a weekly or monthly operations report for the public works director or city manager. Use when a division supervisor, public works director, or city manager's office needs a written summary of work order activity with KPIs, recurring issues, and recommendations.
---

# Work Order Summarizer

> Turns a batch of work orders into a readable operations report. Built for public works supervisors and directors who need to brief the city manager without spending half a day pivoting a spreadsheet.

## When to Use

- "Summarize the May work orders for the streets division — Renata wants it in the Friday packet."
- "Pull together a weekly ops report from the work order export."
- "We had 120 work orders last month. What were the patterns?"
- "I need a one-page summary of facility maintenance work orders for the council budget workshop."
- "Build the monthly fleet work order summary for the city manager's report."
- A division is producing routine internal reporting on completed and open work orders and wants narrative on top of the numbers, not a CSV dump.

## Inputs Needed

Required:

- Entity name, division, and reporting period
- Work order export or list (each item should have a category, status, open and close dates, location or asset, and a short description)
- KPIs of interest (default: total volume, completion rate, cycle time, backlog, recurring locations)

Optional:

- Staffing levels and known absences during the period
- Equipment downtime events (mower out, vactor truck in shop)
- Weather events that affected operations
- Carryover projects flagged for the period (overlay program prep, hydrant flushing, leaf collection)
- Prior period data for trend comparison

If the user has not provided the period, the division, or at least a count and category breakdown, ask before drafting.

## Process

1. Confirm period and scope. Weekly summaries focus on what changed; monthly summaries focus on KPIs and recurring themes.
2. Tabulate volume by category and status. Categories typically include potholes, signs and markings, drainage and culvert, water leaks and main breaks, sewer calls, dead animal, signal and streetlight, sidewalk, facility, fleet, and other.
3. Compute cycle time per category where dates are available. Median is more useful than mean when a few stale tickets distort the average.
4. Identify backlog: open work orders aged beyond the division's target response time. Group by category and age band (0–7 days, 8–30, over 30).
5. Spot recurring locations. If the same block appears three or more times in 90 days, flag it as a hot spot and recommend a diagnostic look (drainage, base failure, illegal dumping pattern).
6. Note staffing and equipment constraints that affected throughput.
7. Surface items the city manager or director should see: anything political (school zones, council districts), anything safety-relevant, anything that points to a capital need.
8. Recommend two to four operational adjustments grounded in the data, not boilerplate.

## Output Format

Plain markdown, one to three pages depending on volume. Tone: operational, plain, no editorializing. Numbers in tables; narrative in short paragraphs.

```
[ENTITY] PUBLIC WORKS — [DIVISION]
[PERIOD] WORK ORDER SUMMARY

Prepared by: [Name, title]
Period: [start] to [end]

1. SUMMARY KPIs
   - Work orders received: [n]
   - Work orders closed: [n] ([completion %])
   - Open at period end: [n] (carryover [n], new [n])
   - Median cycle time (closed): [days]
   - Backlog over target SLA: [n]

2. WORK BY CATEGORY
   | Category | Received | Closed | Open | Median cycle time |
   |---|---|---|---|---|

3. NOTABLE ITEMS
   [Three to six narrative bullets covering high-visibility work, safety items,
   council-district patterns, or items requiring follow-up.]

4. CYCLE TIME AND BACKLOG
   [What's moving on time; what isn't; aging breakdown.]

5. RECURRING ISSUES / HOT SPOTS
   [Locations with three or more requests in 90 days, with a one-line
   diagnostic hypothesis.]

6. STAFFING AND EQUIPMENT NOTES
   [Vacancies, leave, equipment downtime that affected the numbers.]

7. TRENDS
   [Period-over-period or year-over-year where comparison data exists.]

8. RECOMMENDATIONS
   [Two to four. Specific, actionable, division-level decisions.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Engineering scope:** This skill summarizes routine operational work. Anything requiring engineering judgment under the Texas Engineering Practice Act — recommending a structural fix, determining whether a pipe failure mode is systemic, certifying that an installation meets code — must be reviewed and signed by a licensed Texas P.E. The skill drafts the operational narrative; engineering conclusions belong to the engineer.

**Public records (Tex. Gov't Code Ch. 552):** Work order data and operations reports are generally public records. Personally identifying information of citizens who submitted requests may be redacted under § 552.117 or § 552.137 depending on context.

**Retention:** Operational reports retain 3 years under Texas State Library Local Government Retention Schedule PW (Public Works), Item 5025-01 (Routine Operations Reports). Underlying work order records retain 2 years.

**Verify before distribution:** That counts match the source data, that named locations are accurate, and that recommendations align with what the director is willing to act on.

## References

- Standard work order categories are listed in the Output Format section. Division-specific category lists should be maintained locally.

## Examples

- See `examples/cedar-ridge-streets-may-2026-work-orders.md` for a worked example: a Streets Division May 2026 monthly work order summary, with overlay program prep flagged, three pothole hot spots identified, two equipment downtime events, and a scheduling recommendation tied to the FY2026 overlay contractor mobilization.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
