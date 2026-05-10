---
name: system-of-record-mapper
description: Documents a municipal system of record (SOR) including authority, data classification, integrations, retention, access controls, and disaster recovery posture. Use when a CIO, records officer, or department director needs a standardized SOR record for the city's data inventory, audit responses, vendor risk reviews, or public records intake.
---

# System of Record Mapper

> Produces a one-stop SOR document that captures what a system is, what data it holds, who can touch it, how long it retains, how it backs up, and what public records implications it carries. Built for the records officer mapping the city's data estate and the CIO answering an auditor in 24 hours.

## When to Use

- "Document the permit management system as an SOR for the data inventory."
- "Auditor wants a system map for the financial general ledger."
- "Records officer is building the city's data inventory. Map every SOR."
- "Police RMS migration is up for procurement; we need the SOR record for the legacy system."
- "Council asked which systems hold PII. Build the SOR table for every system that does."
- A TPIA request requires staff to identify which systems hold responsive records.

## Inputs Needed

Required:

- System name and version.
- Vendor (or "in-house") and hosting model (on-premises, SaaS, IaaS).
- Primary data classes (Public, Internal, Confidential, Restricted) and regulated overlays (PII, PHI, CJIS, financial-account data, election data).
- Authority for the data: statutory (cite Texas Local Government Code, Tex. Gov't Code, Tex. Tax Code, federal mandate) or operational (City policy).
- Integrations: upstream sources, downstream consumers, batch and real-time interfaces.
- Retention requirement: TSLAC schedule item and any sectoral overlay (CJIS, HIPAA, IRS).
- System owner (business owner), data steward, and IT contact.
- Access roles or groups, MFA posture, privileged access controls.

Optional:

- Audit logging configuration and retention.
- Backup posture: frequency, retention, immutability, geographic separation.
- DR posture: RPO, RTO, last DR exercise result.
- Public records implications: known TPIA-responsive scope, redaction patterns, § 552.139 / § 552.108 considerations.
- Whether the system is a designated SOR (single authoritative source) or a system of engagement / system of report.

If the data classification or authority is missing, ask. Those two inputs anchor every other section.

## Process

1. Confirm the system is the *authoritative* source for the data class. If it is not, document it as a system of engagement or report and identify the upstream SOR.
2. Identify the legal authority. Cite the statute or policy that authorizes collection. Utility billing: Tex. Loc. Gov't Code Ch. 552; tax records: Tex. Tax Code; police: relevant penal-code authority and agency general orders.
3. Classify data elements. Mark PII, PHI, CJIS, financial-account, election, biometric. Cross-reference the City's Data Classification Policy.
4. Document data flow. Upstream sources (intake, integrations) and downstream consumers (reporting, vendor sync, council packets). Note cross-jurisdictional sharing.
5. Set retention. Cite the TSLAC schedule item by code. Layer federal or state overlays (HIPAA 6 years; CJIS audit logs per FBI policy; IRS per § 6001).
6. Document access controls: roles, group source (AD, IdP), MFA, privileged access, review cadence.
7. Document audit logging, backups, DR posture.
8. Identify public records implications under Tex. Gov't Code Ch. 552.
9. Date and sign. Set the next review date.

## Output Format

```
SYSTEM OF RECORD
City of [ENTITY] — [System Name] (Version)
SOR No. [SOR-NNN]
Reviewed: [Date] by [Name, title]
Next review: [Date]

1. SYSTEM OVERVIEW
- Purpose, business owner, IT contact, vendor and hosting model.
- SOR status: Authoritative SOR | System of engagement | System of report.

2. AUTHORITY FOR DATA
- Statutory or policy basis with specific citations.

3. DATA CLASSIFICATION
- Class: Public | Internal | Confidential | Restricted
- Regulated overlays: PII | PHI | CJIS | financial-account | election | biometric

4. DATA ELEMENTS (high-level table)
| Element | Class | Regulated marker | Notes |
|---|---|---|---|
| [field] | [class] | [marker] | [e.g., SSN — § 521.002] |

5. INTEGRATIONS
Upstream: [source → frequency → mechanism]
Downstream: [destination → frequency → mechanism]

6. RETENTION
- Primary schedule: TSLAC Local Government Retention Schedule [Series], Item [Item No.]
- Sectoral overlay: [if any — HIPAA, CJIS, IRS]
- Disposition trigger and method.

7. ACCESS CONTROLS
- Roles and groups (source of truth)
- MFA posture
- Privileged access controls
- Access review cadence

8. AUDIT LOGGING
- Events logged, retention, integrity controls (immutable, write-once)

9. BACKUP AND DR POSTURE
- Backup frequency, retention, geographic separation, immutability
- RPO and RTO
- Last DR exercise date and result

10. PUBLIC RECORDS IMPLICATIONS
- Categories likely public
- Categories excepted (with statutory citation)
- Redaction patterns

11. INCIDENT REPORTING TRIGGERS
- Conditions that route to security-incident-classifier

12. CHANGE LOG
| Version | Date | Author | Change |
|---|---|---|---|
```

Length: 3–6 pages.

Tone: factual, table-forward, no speculation.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system*. This skill produces a static SOR document; § 552.051 is not engaged. Annotate *"AI-assisted draft, reviewed by [staff title]"* per city AI use policy.

**TSLAC retention:** TSLAC Local Government Retention Schedules are the controlling authority for cities under Tex. Loc. Gov't Code Ch. 203. Common schedules: GR, TX, FN, PW, CC, HR, SD, UT. Identify by series and item number.

**Public records (Tex. Gov't Code Ch. 552):** the SOR itself is a public record. Data within the system may be excepted under § 552.101 (confidential by other law), § 552.108 (law enforcement), § 552.117 (employee personal information), § 552.130 (driver's license), § 552.137 (member-of-public emails), § 552.139 (network security), or other Ch. 552 exceptions. Section 10 documents patterns; it does not pre-decide any specific request.

**CJIS Security Policy:** SORs holding criminal justice information are subject to additional access, audit, and personnel-screening requirements. Sections 7 and 8 should reflect CJIS requirements when in scope.

**HIPAA:** SORs holding PHI under a covered component (ambulance billing, group health plan) are subject to 45 C.F.R. Parts 160 and 164.

**Tex. Bus. & Comm. Code § 521.002 sensitive personal information:** any SOR holding SSN, driver's license, government-issued ID, or financial-account-plus-security-code in combination with name is in scope for § 521.053 breach notification. Mark these elements in Section 4 to drive incident classification.

**FTC Safeguards Rule (16 C.F.R. Part 314):** utility billing SORs with credit-extension features may be in scope.

## References

- This skill defers to the City's Data Classification Policy and to TSLAC retention schedules for authoritative class and retention values. The SOR record is the snapshot, not the policy source.

## Examples

- See `examples/permit-management-system-sor.md` for a worked example: SOR for the City of Cedar Ridge permit management system, including the data flow from intake through review through Council action and TSLAC-aligned retention. The system holds the Z-2026-04 zoning case file referenced across the planning plugin.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
