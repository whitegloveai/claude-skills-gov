---
name: records-retention-classifier
description: Classifies a local government document against the Texas State Library and Archives Commission (TSLAC) Local Government Records Retention Schedules. Use when a clerk, records manager, or department staff needs to determine the schedule, item number, retention period, and disposition for a record.
---

# Records Retention Classifier

> Classifies a single document or a batch against the TSLAC Local Government Records Retention Schedules and recommends a disposition. Built for clerks and records management staff during routine cleanup, audit preparation, or end-of-fiscal-year purges.

## When to Use

- "I have a stack of public works documents. Tell me what schedule each one falls under."
- "How long do we have to keep this contract?"
- "Can we destroy these utility billing records?"
- "Classify this work order log against the TSLAC schedules."
- "We're closing out the FY2025 file room. Run these through the retention schedule."
- Before any disposition decision (destroy, archive, transfer to TSLAC). Texas Local Government Code § 203.041 requires every local government to follow a records control schedule approved by TSLAC before destroying any record.

## Inputs Needed

Required:

- Document description (what is the record, what does it contain, what action does it document)
- Originating department (clerk, public works, finance, police, planning, etc.)
- Document date or date range
- Format: paper, electronic, microfilm, audio/video recording

Optional:

- Whether the record is currently subject to a litigation hold or pending TPIA request (overrides routine disposition)
- Whether the record has been declared archival by the city
- Whether the record contains a state or federal grant trail (federal grant retention may extend the TSLAC minimum)
- The city's adopted records control schedule reference number if it deviates from TSLAC

If the originating department or document date is missing, ask before classifying. Departmental context drives which TSLAC schedule applies.

## Process

1. Identify the TSLAC schedule that governs the originating department or record type. See `references/tslac-schedule-families.md` for the families: GR (General), LC (Local Counsel and Governing Body), PS (Public Safety), HR, FN (Financial), TX (Tax), UT (Utility), PW (Public Works).
2. Within that schedule, locate the item number that best describes the record. TSLAC item numbers are stable across revisions and are the load-bearing citation in any disposition log.
3. State the retention period using the TSLAC formula: "AC + N years" (after closing), "FE + N years" (after fiscal year end), "US + N years" (after useless or obsolete), "PERM" (permanent), or "LIFE" (life of the underlying asset).
4. Identify factors that extend retention beyond the TSLAC minimum: federal grant audit trails, litigation hold, pending or anticipated TPIA request, or archival declaration.
5. Recommend a disposition: *destroy* (retention met, no holds), *archive* (declared archival or permanent items), *retain* (retention not yet run), or *hold* (litigation or TPIA hold in place).
6. Provide the citation block for the disposition log: schedule, item number, retention period, retention authority, and the eligibility date.
7. Flag records that should be referred to the city attorney before disposition: contracts with ongoing obligations, records under any hold, records with potential evidentiary value, and any record where the responsible department disagrees with the classification.

## Output Format

A classification entry per record, formatted as a structured block suitable for pasting into the city's records management system or disposition log.

```
RECORD CLASSIFICATION

Document: [short description]
Originating department: [department]
Document date: [date or date range]
Format: [paper / electronic / microfilm / A/V]

TSLAC schedule: [GR / LC / PS / HR / FN / TX / UT / PW]
Item number: [e.g., 1000-26]
Item title: [TSLAC item title]
Retention period: [e.g., FE + 5]
Retention authority: TSLAC Schedule [letter], Item [number]; Tex. Loc.
  Gov't Code § 203.041

Eligibility date: [computed date the record becomes disposable]
Holds or extensions: [none / federal grant audit period / litigation
  hold / pending TPIA / archival declaration]

Recommended disposition: [destroy / archive / retain / hold]
Notes: [any review needed before disposition]
```

For a batch input, produce one block per record, in the order received, followed by a one-line summary at the end stating how many records map to each disposition recommendation.

Tone: factual, precise. No editorial commentary. Citations use the full TSLAC schedule letter and item number; do not abbreviate.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Statutory framework:**

- Tex. Loc. Gov't Code § 203.041 — Must follow a TSLAC-approved schedule before destroying any record.
- Tex. Loc. Gov't Code § 203.044 — Destruction outside the schedule is a Class A misdemeanor.
- Tex. Loc. Gov't Code Ch. 201 — Records management responsibilities and the RMO role.
- Tex. Gov't Code § 441.158 — TSLAC authority to issue local-government schedules.

**Holds override schedule:** A litigation hold, an active TPIA request under Tex. Gov't Code Ch. 552, or an audit hold under federal grant rules suspends disposition until the hold is lifted. Disposition of records subject to any hold may constitute spoliation, may waive privilege, or may breach federal grant terms.

**Federal grant overlay:** Records that document expenditure of federal funds retain for the longer of the TSLAC schedule and the period required by 2 C.F.R. § 200.334 (three years from the final expenditure report, longer for certain categories). Identify federal grant records during classification, not after.

**Verify before disposing:** That the schedule version cited is current (TSLAC publishes revisions periodically); that no hold is active; that the recommended disposition is documented in the city's disposition log and signed by the records management officer.

## References

- See `references/tslac-schedule-families.md` for an overview of the TSLAC Local Government Records Retention Schedule families (GR, LC, PS, HR, FN, TX, UT, PW) with the typical record types each covers.

## Examples

- See `examples/mixed-public-works-documents.md` for a worked example: classification of five documents from Cedar Ridge public works (work order log, change order, service contract, traffic study, retired pump test report).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
