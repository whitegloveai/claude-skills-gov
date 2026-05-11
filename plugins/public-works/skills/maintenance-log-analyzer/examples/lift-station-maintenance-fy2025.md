CITY OF CEDAR RIDGE PUBLIC WORKS — WASTEWATER COLLECTION
WASTEWATER LIFT STATION MAINTENANCE ANALYSIS, FY2025

Prepared by: Adelina Cortez, Wastewater Superintendent
Reviewed: Renata Hsu, Public Works Director; Stephen Kovac, P.E. (consulting)
Period: October 1, 2024 to September 30, 2025

*AI-assisted draft, reviewed by Adelina Cortez, Wastewater Superintendent.*

## 1. Asset Class and Inventory Summary

Cedar Ridge operates six wastewater lift stations. All discharge to the regional WWTP via force mains.

| Station | In service | Pump count | Rated life remaining (yrs) | Tier |
|---|---|---|---|---|
| LS-1 (Main Street) | 2011 | 2 | ~10 | Good |
| LS-2 (Hillcrest) | 2008 | 2 | ~7 | Fair |
| LS-3 (Industrial Park) | 1998 | 2 | 0 (past) | Poor |
| LS-4 (Brookside) | 2017 | 2 | ~17 | Good |
| LS-5 (Pecan Hills) | 2014 | 2 | ~14 | Good |
| LS-6 (River Road) | 2003 | 2 | ~3 | Fair |

## 2. Methodology

Source data: Cityworks corrective and PM work orders FY2025, plus the SCADA alarm log. Included: corrective work, planned PMs that uncovered defects, and operator-initiated repairs. Excluded: routine PMs with no defect (counted only for completion). Data quality gap: pre-2022 records are partially paper; long-term MTBF trend is calculated only on the FY2022 forward window.

## 3. Top Recurring Failure Modes

| Failure mode | Count | % of corrective work | Affected assets |
|---|---|---|---|
| Pump clog / rag binding | 21 | 38% | LS-3 (12), LS-2 (4), others (5) |
| Control panel fault | 9 | 16% | LS-3 (6), LS-6 (3) |
| Float / level sensor failure | 7 | 13% | LS-2 (3), LS-3 (2), LS-6 (2) |
| Pump motor fault | 6 | 11% | LS-3 (4), LS-6 (2) |
| Valve / check failure | 5 | 9% | various |
| Other | 7 | 13% | various |

## 4. Mean Time Between Failures

| Station | MTBF FY2025 (days) | MTBF FY2024 | Trend |
|---|---|---|---|
| LS-1 | 162 | 175 | Stable |
| LS-2 | 78 | 88 | Slightly worsening |
| LS-3 | 22 | 31 | Worsening |
| LS-4 | 240 | 250 | Stable |
| LS-5 | 198 | 210 | Stable |
| LS-6 | 64 | 70 | Slightly worsening |

## 5. Cost Trend

| Station | FY2025 maintenance cost | Replacement cost estimate | Ratio |
|---|---|---|---|
| LS-1 | $14,200 | $850,000 | 1.7% |
| LS-2 | $32,100 | $850,000 | 3.8% |
| LS-3 | $118,400 | $1,400,000 | 8.5% (5-yr cumulative 31%) |
| LS-4 | $9,400 | $1,000,000 | 0.9% |
| LS-5 | $12,800 | $1,000,000 | 1.3% |
| LS-6 | $24,000 | $900,000 | 2.7% |

LS-3 by itself absorbed 56% of total wastewater lift station corrective spending in FY2025.

## 6. End-of-Life Signals

**LS-3 (Industrial Park):**

- Failure frequency rising (MTBF 22 days, down from 31)
- Same component repeatedly: pump impellers fouled and binding; control panel relays failing
- OEM end-of-support: 1998 control panel manufacturer discontinued the relay rack in 2021; replacements are secondary-market only
- Past rated life by ~10 years
- Two sanitary sewer overflow near-misses in FY2025 attributable to control panel faults during wet weather

**LS-6 (River Road):**

- Approaching but not yet at end-of-life. Continued operation through FY2028 is reasonable with the PM adjustments below.

## 7. Reliability and Safety Concerns

LS-3 is the principal availability and TPDES compliance risk in the collection system. The two near-miss SSOs in FY2025 are documented in the TPDES quarterly noncompliance reporting log. A failure during a heavy rain event with both pumps offline is a credible scenario based on the FY2025 history, and the Industrial Park basin has no upstream gravity capacity to absorb a multi-hour outage.

## 8. Recommendations — CIP

1. **Prioritize LS-3 for full station replacement in the FY2027 CIP** (planning and design in FY2026, construction in FY2027). Estimated $1.4M. Funding candidates include TWDB Clean Water State Revolving Fund and utility rate revenue. See companion CIP entry (LS-3 Replacement).
2. **Schedule LS-6 control panel refurbishment** in the FY2028 CIP at an estimated $180,000. This is a refurbishment, not a station replacement.

Engineering certification of station sizing and pump selection on the LS-3 replacement will be provided by the design engineer under seal.

## 9. Recommendations — Preventive Maintenance Adjustments

1. **Increase wet well cleaning frequency at LS-2 and LS-3** from quarterly to monthly until LS-3 is replaced. The rag binding pattern is consistent with reduced cleaning intervals being effective.
2. **Add a quarterly relay inspection at LS-3 and LS-6** with a defined replace-on-condition threshold rather than waiting for failure.
3. **Add operator-readable runtime totals to SCADA exports** so future analyses can compute cost per pump-hour.

## 10. Caveats and Next Steps

Sizing and hydraulic analysis for the LS-3 replacement requires a preliminary engineering report (PER) sealed by a licensed Texas P.E. Operational conclusions in this memo do not substitute for that PER. The FY2026 budget should include $80,000 for the PER and design start.
