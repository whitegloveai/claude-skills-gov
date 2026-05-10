# Example: Cedar Ridge Permit Management System — SOR Record

Worked example output of the `system-of-record-mapper` skill for the City of Cedar Ridge permit management system. This is the same SaaS reviewed under the `vendor-risk-questionnaire` example (PermitPath Inc.) and holds the Z-2026-04 zoning case referenced across the planning plugin.

**Inputs provided:**

- System: PermitPath SaaS, deployed January 2026.
- Vendor / hosting: PermitPath Inc., multi-tenant SaaS on AWS us-east-1 and us-west-2.
- Data classes: Confidential (applicant PII, property records, case notes); Internal (staff workflow); Public (filed applications post-public-notice; council action records).
- Authority: Tex. Loc. Gov't Code Ch. 211 (zoning), Ch. 212 (subdivision), and the Cedar Ridge Code of Ordinances Ch. 18 (Land Development).
- Integrations: GIS (ArcGIS Enterprise, bidirectional), Tyler Munis financial (fees, one-way to finance), Granicus agenda management (case packets for Planning Commission and Council), city email (outbound notifications).
- Retention: TSLAC Schedule PD (Planning and Development), various items.
- Owner: Planning Director Carmen Ruiz.
- IT contact: Vihaan Joshi, CIO.

---

# SYSTEM OF RECORD

**City of Cedar Ridge, Texas — PermitPath (v2026.04)**
**SOR No. SOR-031**
Reviewed: 2026-05-01 by Vihaan Joshi, CIO; Jessica Aldridge, Records Management Officer
Next review: 2027-05-01

## 1. SYSTEM OVERVIEW

- Purpose: Permit application intake, plan review workflow, inspections scheduling, and zoning case management.
- Business owner: Carmen Ruiz, Planning Director.
- IT contact: Vihaan Joshi, CIO.
- Vendor / hosting: PermitPath Inc., multi-tenant SaaS, AWS us-east-1 (primary) and us-west-2 (DR).
- SOR status: **Authoritative SOR** for permit and zoning case data. System of report for parcel data (authoritative SOR is GIS).

## 2. AUTHORITY FOR DATA

- Tex. Loc. Gov't Code Ch. 211 (zoning regulation and procedure).
- Tex. Loc. Gov't Code Ch. 212 (subdivision regulation).
- Tex. Loc. Gov't Code Ch. 245 (vested rights for permits).
- Cedar Ridge Code of Ordinances Ch. 18 (Land Development Code).
- Adopted under Council Ordinance O-2025-44 (procurement and operational policy).

## 3. DATA CLASSIFICATION

- Primary class: Confidential (PII), with Public-class records after notice and adoption.
- Regulated overlays: PII; no PHI; no CJIS.

## 4. DATA ELEMENTS

| Element | Class | Regulated marker | Notes |
|---|---|---|---|
| Applicant name | Confidential | PII | Subject to Tex. Gov't Code § 552 access on application file once public |
| Applicant address, phone, email | Confidential | PII | Email of member of public excepted under § 552.137 if applicant requests |
| Driver's license number | Restricted | § 521.002 sensitive personal information | Collected only when identity verification required |
| Property address and parcel ID | Public | — | Authoritative SOR is GIS; replicated here |
| Application content | Confidential to Public | — | Becomes Public after notice publication |
| Plan documents and drawings | Confidential to Public | Copyright considerations | § 552.110 may except proprietary contractor information |
| Staff review notes | Internal | — | § 552.111 (agency memoranda) deliberative process |
| Fee payment status | Confidential | Financial transaction | Card data not stored in system; tokenized via Munis |
| Council action records | Public | — | Permanent retention |

## 5. INTEGRATIONS

**Upstream:**
- ArcGIS Enterprise (parcel boundary refresh, daily batch).
- City email (citizen intake, real-time).

**Downstream:**
- Tyler Munis financial (fee posting, real-time webhook).
- Granicus agenda management (case packets, batch on Planning Commission and Council meeting cycle).
- Public web portal (read-only published cases via API).
- Email notifications to applicants (system-generated).

No cross-jurisdictional sharing.

## 6. RETENTION

- Primary schedule: TSLAC Local Government Retention Schedule PD.
  - Item 5050-01 (Building Permit Files): 10 years after expiration or final inspection.
  - Item 5100-01 (Zoning Case Files including hearings and decisions): Permanent.
  - Item 5125-04 (Subdivision Plat Files): Permanent.
- Sectoral overlays: none.
- Disposition trigger: case closure / permit closeout. Method: certified disposition by Records Management Officer; vendor purges data via signed deletion certificate upon disposition direction.

## 7. ACCESS CONTROLS

- Roles sourced from City IdP via SAML SSO (group-based, Active Directory).
- Role tiers: Reader, Applicant Liaison, Reviewer, Approver, Administrator.
- MFA: required for all users (City IT-005 policy and vendor MFA configuration).
- Privileged access: vendor PAM with City CIO approval for production data access; logged.
- Access reviews: quarterly by Planning Director with IT facilitation.

## 8. AUDIT LOGGING

- Events logged: authentication, role changes, record create/update/delete, document upload/download, search of sensitive elements (driver's license), API calls.
- Retention: 365 days in system; exported monthly to City SIEM (Splunk Cloud), 3-year retention.
- Integrity: write-once on SIEM side; vendor uses append-only audit table.

## 9. BACKUP AND DR POSTURE

- Backups: hourly snapshots; daily full; 35-day retention; cross-region replication us-east-1 → us-west-2; immutable backup repository.
- RPO: 1 hour. RTO: 4 hours.
- Last DR exercise: vendor test 2025-10-08 met objectives. City-side failover exercise scheduled 2026-09-15.

## 10. PUBLIC RECORDS IMPLICATIONS

- **Public records:** posted public notices; adopted zoning ordinances; council action records; final approved permits; inspection results.
- **Excepted records (with citation):**
  - § 552.111 — staff review notes and deliberative process content pre-decision.
  - § 552.117 — employee personal information of City reviewers.
  - § 552.130 — driver's license numbers.
  - § 552.137 — email addresses of members of the public, where requested withheld.
  - § 552.110 — proprietary contractor / applicant business information where claimed.
- TPIA responsive scope: Planning Department is the records custodian; PermitPath case-export and document-export reports support response within statutory windows.

## 11. INCIDENT REPORTING TRIGGERS

- Compromise of applicant PII at rest, in transit, or by exfiltration.
- Unauthorized release of pre-decision deliberative content.
- Loss of integrity of council action records.
- Vendor-side incident notification.
- Any compromise affecting the active Z-2026-04 zoning case file or other high-attention cases.

## 12. CHANGE LOG

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-05-01 | V. Joshi, J. Aldridge | Initial SOR record post-deployment |

---

**Drafting notes (not part of the official SOR record):**

This SOR consolidates the vendor risk assessment (SOR-031 maps to vendor questionnaire AI-2026-007's underlying procurement record) and the system inventory. The Z-2026-04 case file referenced in the planning plugin's `zoning-narrative-writer` and `staff-report-writer` skill examples lives here. Incident response on this system feeds the `security-incident-classifier` and would trigger council briefing under Tex. Gov't Code § 551.089 for the security dimension of any compromise.

The SOR is annotated *AI-assisted draft, reviewed by Vihaan Joshi, CIO, and Jessica Aldridge, Records Management Officer* per Cedar Ridge IT-014.
