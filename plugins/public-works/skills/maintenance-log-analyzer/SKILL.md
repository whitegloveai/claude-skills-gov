---
name: maintenance-log-analyzer
description: Reviews equipment or facility maintenance logs for trends, recurring failures, and asset condition signals that should inform capital planning. Use when a fleet manager, water utility superintendent, facilities manager, or public works director needs a written analysis of maintenance history to support CIP decisions or preventive maintenance changes.
---

# Maintenance Log Analyzer

> Turns a maintenance log into a written analysis with trends, recurring failure modes, and a clear signal of which assets are approaching end-of-life. Built for fleet, utility, and facility managers preparing CIP requests and preventive maintenance changes.

## When to Use

- "Pull together the FY2025 lift station maintenance analysis. Renata wants to know which station goes into the CIP first."
- "We've been chasing the same HVAC failures at City Hall for two years. What does the log actually say?"
- "Fleet log analysis for the heavy trucks — which units are no longer cost-effective to keep?"
- "Traffic signal cabinet maintenance review for the FY2027 budget."
- "Water meter replacement justification: what does our test bench data show on the AMR units installed in 2014?"
- A manager is moving from "I think we need to replace this" to a written memo that decisionmakers can act on.

## Inputs Needed

Required:

- Entity name, asset class, and reporting period
- Maintenance log (or summary) with work date, asset ID, work type (PM or corrective), failure mode or task code, labor hours, parts cost, and downtime
- Asset inventory: ID, install or in-service date, manufacturer/model where available

Optional:

- Manufacturer's expected service life or industry benchmark life
- Replacement cost estimate per asset
- Operator complaints or safety incidents associated with specific assets
- Prior analyses or condition assessments
- Operating context (run hours, cycles, miles)

If the user has not provided the asset class, the period, or at least one usable failure mode code or description per record, ask before drafting. A log of "repair done" with no detail cannot drive analysis.

## Process

1. Confirm asset class and period. Mixing asset classes weakens the analysis.
2. Group corrective work by failure mode. The top three to five modes usually drive the narrative.
3. Compute mean time between failures (MTBF) per asset where the log supports it. Median time between corrective events is more honest than mean when one asset is an outlier.
4. Compute trailing 12-month cost per asset (labor + parts). Sort descending. Highlight assets whose annual cost exceeds 60% of replacement cost — a common decision threshold for replace-versus-repair.
5. Identify end-of-life signals: rising failure frequency, repeat failures of the same component, obsolete parts that are no longer manufactured, vendor end-of-support announcements, accumulated hours or cycles beyond rated life.
6. Note reliability and safety concerns separately from cost. A station that fails on a Sunday night during a rain event is operationally worse than one that fails reliably on Tuesday mornings.
7. Translate the data into two outputs: CIP recommendations (replace or refurbish) and preventive maintenance adjustments (more frequent task, different vendor, different lubricant).
8. Flag anything that needs a P.E. or licensed operator review before being treated as a conclusion.

## Output Format

Plain markdown, two to four pages. Tone: analytical, candid. Numbers in tables; narrative in short paragraphs that connect the numbers to a decision.

```
[ENTITY] PUBLIC WORKS — [ASSET CLASS]
MAINTENANCE LOG ANALYSIS, [PERIOD]

Prepared by: [Name, title]
Period: [start] to [end]

1. ASSET CLASS AND INVENTORY SUMMARY
   - Asset count: [n]
   - Age range: [oldest] to [newest]
   - Inventory table (ID, age, condition tier if known)

2. METHODOLOGY
   - Data source(s), reporting tool, period
   - What was included, what was excluded, known data quality gaps

3. TOP RECURRING FAILURE MODES
   | Failure mode | Count | % of corrective work | Affected assets |
   |---|---|---|---|

4. MEAN TIME BETWEEN FAILURES (where computable)
   | Asset | MTBF (days) | Trend (improving / stable / worsening) |
   |---|---|---|

5. COST TREND
   | Asset | Trailing 12-mo cost | Replacement cost estimate | Cost/replacement ratio |
   |---|---|---|---|

6. END-OF-LIFE SIGNALS
   [Narrative on which assets are showing the textbook signs and why.]

7. RELIABILITY AND SAFETY CONCERNS
   [Separate from cost. Calls out availability risk, public safety, regulatory.]

8. RECOMMENDATIONS — CIP
   [Specific assets recommended for replacement or refurbishment, with rough
   priority and rough cost.]

9. RECOMMENDATIONS — PREVENTIVE MAINTENANCE ADJUSTMENTS
   [Specific PM tasks to add, drop, or change frequency on.]

10. CAVEATS AND NEXT STEPS
    [Data quality notes; what would tighten the analysis next year.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Engineering scope:** Conclusions about whether an asset is structurally deficient, hydraulically inadequate, electrically unsafe, or otherwise out of compliance with applicable codes require engineering judgment under the Texas Engineering Practice Act and must come from a licensed Texas P.E. This skill drafts the operational analysis around the data; engineering conclusions belong to the engineer.

**Regulatory context for utility assets:**

- Public water systems are regulated under Tex. Health & Safety Code Ch. 341 and 30 T.A.C. Ch. 290. Conclusions touching on regulatory compliance must involve the licensed water operator and, where relevant, the consulting engineer.
- Wastewater systems are regulated under Tex. Water Code Ch. 26 and 30 T.A.C. Ch. 217 (design criteria) and Ch. 305 (TPDES permits). Sanitary sewer overflow data and root-cause discussion should align with the TPDES permit reporting framework.

**Public records (Tex. Gov't Code Ch. 552):** Maintenance logs and analyses are generally public. Security-sensitive utility infrastructure data may be subject to § 418.183 (Homeland Security Chapter) review before public release.

**Retention:** Equipment maintenance records retain through the life of the asset plus 3 years under Texas State Library Local Government Retention Schedule PW, Item 5050. Capital planning analyses retain 10 years.

**Verify before distribution:** That data quality caveats are visible, that asset IDs are correct, and that the engineering conclusions are reviewed and concurred by the appropriate licensed professional.

## References

- See `references/end-of-life-signals-checklist.md` for the standard signal checklist used in Section 6 (rising failure frequency, parts obsolescence, accumulated hours, OEM end-of-support, repeat component failure).

## Examples

- See `examples/lift-station-maintenance-fy2025.md` for a worked example: the Cedar Ridge FY2025 wastewater lift station maintenance analysis covering six stations, identifying Station 3 as the CIP priority due to recurring pump failures and an aging control panel.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
