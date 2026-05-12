---
name: business-retention-survey-analyzer
description: Analyzes BR&E (Business Retention and Expansion) survey results, identifies risk signals and opportunity targets, and produces a board-ready analysis memo with recommended follow-up visits. Use when an EDC executive, BR&E coordinator, or chamber partner has completed a survey cycle and needs to convert responses into a prioritized action plan and watch list.
---

# Business Retention Survey Analyzer

> Reads a BR&E survey dataset and produces an analysis memo that flags imminent expansion signals, retention risk, workforce themes, and a prioritized follow-up list. Built for the ED director who runs the BR&E program with limited staff and needs to act on what the data says.

## When to Use

- "Analyze the FY2026 BR&E survey results."
- "Pull the retention risks and expansion signals out of these 60 responses."
- "Identify which businesses need a follow-up visit in the next 30 days."
- "Build the workforce themes section for the EDC board memo."
- "Cross-reference this year's survey to last year's baseline."

## Inputs Needed

Required:

- Survey responses, free-form and structured. Common formats: CSV export from the survey platform, a structured spreadsheet, or interview write-ups.
- Reporting period (typically fiscal year or calendar year)
- Universe definition: which businesses were targeted, how the response rate is calculated, and the survey instrument used.

Optional but valuable:

- Prior-year survey results for trend comparison
- Business demographics: NAICS sector, employee count, years in community, ownership stage
- Free-form interview notes from in-person visits
- Workforce board sector reports for cross-reference
- Local sales tax trend data by sector

If the user has not provided the response set, ask before drafting. The skill cannot infer findings from sector profiles alone.

## Process

1. Confirm the universe and the response rate. State both clearly in the memo. A 60% response rate with a defined universe is more meaningful than a 95% response rate on a self-selected sample.
2. Classify each response on three axes: (a) operating health (stable, growing, contracting), (b) expansion signal (none, exploring, planning, imminent), and (c) retention risk (none, watch, concern, imminent).
3. Identify expansion signals using concrete indicators: capacity at or above 90%, recent capital purchases, plans to add shifts, hiring difficulty for specific roles, recent customer wins. Note the specific signal by business.
4. Identify retention risks using concrete indicators: utility or facility constraints driving relocation consideration, ownership transition without succession plan, lease expiration in the next 24 months without renewal commitment, primary customer loss, regulatory or workforce constraints that cannot be addressed locally.
5. Pull supply chain insights. Note where local businesses are sourcing from out of state, whether local suppliers exist, and where supplier development could yield local content.
6. Pull workforce and training insights. Cluster the workforce signals by occupation, sector, and skill level. Identify two or three themes that the workforce board or community college could act on.
7. Build the Recommended Visits and Outreach list. Prioritize by signal strength and decision window. For each, name the business, the signal, and the suggested outreach owner and timeline.
8. Build the Watch List. Lower-urgency businesses where signals warrant tracking but not immediate action.
9. State the limitations honestly. A survey reflects what respondents disclose, not the underlying truth. Identify any non-response that materially limits the analysis.

## Output Format

Plain markdown analysis memo. Sections in this order:

1. Reporting Period and Universe
2. Response Summary (response rate, distribution by sector, response method)
3. Sector Health Indicators
4. At-Risk Businesses (with specific red flags by business)
5. Expansion Opportunities (with specific signals by business)
6. Supply Chain Insights
7. Workforce and Training Insights
8. Recommended Visits and Outreach (ranked)
9. Watch List
10. Limitations

Length: 5 to 10 pages depending on universe size.

Tone: candid, specific, and protective of business confidentiality. Where the memo will be distributed beyond the ED office, anonymize at-risk findings or aggregate them. Where the memo is internal only, name names so the EDC can act.

The analysis memo distinguishes clearly between two audiences:

- **Internal working memo** — names specific businesses, signals, and actions.
- **Board-distributed version** — anonymized or aggregated for at-risk findings. Specific businesses for expansion signals are typically named only with the business's consent.

Always draft both versions when the user asks for a board memo.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Business confidentiality:** BR&E survey responses include sensitive operational and financial information that businesses share in confidence. Treat individual responses as confidential. Aggregate where possible. When sharing the memo beyond the ED office, redact business names from at-risk findings unless the business has agreed to disclosure.

**Public records implications:** A BR&E memo is a public record under Tex. Gov't Code Ch. 552 unless an exception applies. Some content may be eligible for withholding under § 552.131 (economic development information) where disclosure would harm the governmental body's competitive position. The exception is narrow and time-limited; substantive findings typically become public over time. Plan distribution accordingly.

**Retention:** BR&E survey results and analysis memos retain consistent with the local government's adopted retention schedule, typically aligned to the Texas State Library Local Government Retention Schedule.

**Avoid commitments:** The memo identifies opportunities and risks. Any incentive or assistance offered to an individual business through BR&E is subject to the same Tex. Loc. Gov't Code Ch. 380 process as a recruitment incentive: council action in open meeting.

## References

- See `references/br-e-signal-taxonomy.md` for a working taxonomy of expansion signals and retention risk indicators with the underlying survey questions that surface each.

## Examples

- See `examples/cedar-ridge-br-e-fy2026-analysis.md` for an analysis of a FY2026 BR&E survey covering 42 manufacturing and 18 professional services businesses, with three imminent expansion signals, two retention risk flags (one capacity-driven, one ownership-transition-driven), and three workforce themes for the EDC's regional training partnership.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
