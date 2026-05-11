---
name: infrastructure-condition-report
description: Drafts a written infrastructure condition report summarizing inspection data for a specific asset or asset class — pavement, water mains, sanitary sewer, stormwater, bridges, facilities — to support CIP planning, council presentations, or grant applications. Use when a public works director, asset manager, or city engineer's office has inspection data and prior reports in hand and needs an operational narrative wrapped around the engineer's findings.

---

# Infrastructure Condition Report

> Drafts an infrastructure condition report from inspection data for a specific asset class — pavement, water mains, sewer, stormwater, bridges, facilities — for CIP planning, council, or grants. Built for public works staff who have the engineer's data and need the operational narrative.

## When to Use

- "Draft the FY2026 pavement condition report covering all city-maintained lane-miles."
- "Build a condition report on the four lift stations using last quarter's inspection data."
- "We need a sewer collection system condition report for the SRF loan application."
- "Council wants a five-year retrospective on water main break trends."
- "Write the condition section of the bridge report from the TxDOT NBI scores."
- Engineer or qualified inspector has produced the data. User needs a council-ready or grant-ready narrative wrapped around it.

This skill drafts the operational and policy narrative. Substantive engineering judgments — whether a structure is safe, what hydraulic capacity remains, what design life is achievable — must come from a licensed professional engineer under the Texas Engineering Practice Act.

## Inputs Needed

Required:

- Asset class and inventory — total quantity (lane-miles, linear feet, count of structures).
- Inspection methodology and date — PCI survey, CCTV, hydraulic model, NBI inspection.
- Condition data — distribution by rating tier or raw scores with key tier breakpoints.
- Prior report or baseline data for trend.
- Operational implications the engineer has identified.
- Author engineer's name and license number (P.E. number for any structural or hydraulic conclusion).

Optional:

- Geographic breakdown — by council district, sub-area, drainage basin, pressure zone.
- O&M cost history tied to the asset class.
- Capital programs tied to the asset class — current overlay program, CIP line items.
- Grant or loan program the report supports — SRF, BIL formula funds, TxDOT category, FEMA BRIC.
- Photos, geographic exhibits, or appendices the engineer wants included.

If raw inspection data is provided without an engineer's conclusions, ask. The skill drafts narrative around engineering conclusions, not in place of them.

## Process

1. Restate inventory and methodology in plain language with the engineer of record named.
2. Present findings by tier. Pavement: Good (PCI 71-100), Fair (56-70), Poor (41-55), Failed (0-40). Water mains: break rate per mile per year by material and age cohort. Bridges: NBI sufficiency rating tiers.
3. Break findings by geography or sub-area where data supports it. Council members read condition reports through their district's lens.
4. Compare to prior baseline. Trend is more valuable than snapshot.
5. Translate findings into CIP implications. Engineer identifies what is needed; the report names the capital programs that address it.
6. Translate findings into O&M implications — crack-seal cycles, leak detection cadence, valve exercising, inspection intervals.
7. Recommend next inspection per ASTM, TxDOT, EPA, or city policy interval.
8. Add Caveats and Limitations — scope, methodology limits, data confidence, deferrals.
9. Add the engineer's signature and license block — substantive judgments attributed to the P.E. of record.
10. Add the AI-assisted draft notation.

## Output Format

Plain markdown. Six to twelve pages. Tone: factual, plain, decision-ready.

```
[CITY] INFRASTRUCTURE CONDITION REPORT
[ASSET CLASS] — [REPORTING PERIOD]
[Date]

Prepared by: [Author]
Engineer of record: [Name, P.E.], License No. [____]
Reviewed by: [Public Works Director]

1. EXECUTIVE SUMMARY
   [Half page. Inventory, headline distribution, top finding,
   top recommendation.]

2. ASSET CLASS AND INVENTORY
   [Quantity, geographic extent, age cohort, material breakdown.]

3. METHODOLOGY
   [Inspection standard cited (ASTM, NBI, EPA, AWWA), survey
   window, sampling, who conducted it.]

4. FINDINGS BY SUB-AREA
   [Distribution tables by sub-area or council district.
   Quantitative findings only.]

5. TREND ANALYSIS
   [Comparison to prior baseline. Direction of change. Drivers
   the engineer identifies.]

6. IMPLICATIONS FOR CIP
   [Capital programs the findings support. Link to current CIP
   line items by name. The decision is the council's.]

7. IMPLICATIONS FOR O&M
   [Adjustments to crack-seal, leak detection, inspection cadence,
   valve exercising, etc.]

8. RECOMMENDED NEXT INSPECTION
   [Interval and methodology, with citation to controlling
   standard or city policy.]

9. CAVEATS AND LIMITATIONS
   [Scope, data confidence, items deferred to separate report.]

10. ENGINEER OF RECORD
    [Name, P.E., License No., signature, date, seal where required.]

AI-assisted draft, reviewed by [Public Works Director].
```

Length: six to twelve pages depending on asset class breadth and sub-area detail. Tone: plain, decision-ready, no marketing.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Engineering Practice Act (Tex. Occ. Code Ch. 1001):** Engineering conclusions must be made by a Texas-licensed P.E. and signed and sealed where the product constitutes the practice of engineering. The narrative wrapper around the engineer's data is operational drafting, not engineering judgment. Substantive conclusions are attributed to the P.E. of record.

**Standards cited:** ASTM D6433 (pavement); FHWA / TxDOT NBI (bridges); AWWA M11, M28 (water mains); EPA SSO control practices; city policy. Cite precisely.

**Public records (Tex. Gov't Code Ch. 552):** Condition reports are public. Drafts may be exempt under § 552.111 until finalized. Critical infrastructure information may be excepted under § 552.155 — coordinate with the city attorney before publishing location-specific vulnerability data.

**Grant and council use:** Reports for SRF, BIL, FEMA BRIC follow the funding agency's content requirements; the body content here is portable.

**Retention:** 10 years per Texas State Library Local Government Retention Schedule PW Item 5050-04, longer when part of a project or grant file.

## References

- Standard scoring tier breakpoints by asset class appear in the Process section.

## Examples

- See `examples/cedar-ridge-pavement-condition-report-2025.md` for a Cedar Ridge 2025 pavement condition report covering 87 lane-miles of city-maintained roads, with PCI distribution (52% Good, 23% Fair, 18% Poor, 7% Failed), identifying the FY2026 overlay program as the right operational response, recommending a 10-year resurfacing cycle for the worst quartile.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
