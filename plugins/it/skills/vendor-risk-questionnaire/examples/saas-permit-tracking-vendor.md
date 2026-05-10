# Example: Cedar Ridge Permit-Tracking SaaS Vendor Review

Worked example output of the `vendor-risk-questionnaire` skill for a fictional SaaS permit-tracking vendor under evaluation by the City of Cedar Ridge, TX.

**Inputs provided:**

- Vendor: PermitPath Inc., Austin, TX
- Service: Cloud-hosted permit and zoning case management; replaces incumbent on-prem system; data flows from intake portal to staff review, council action, and TSLAC-aligned retention.
- Service model: SaaS, multi-tenant
- Data class: Confidential (PII on applicants and property owners; no PHI; no CJIS). System will host Z-2026-04 and successor zoning case files.
- Certifications claimed: SOC 2 Type II; no FedRAMP; no TX-RAMP; no HITRUST.
- Status: New procurement under interlocal cooperative purchasing.
- Contract value: $54,000/year; three-year initial term.

---

# VENDOR RISK QUESTIONNAIRE

**City of Cedar Ridge, Texas — PermitPath Inc.**
Service: Cloud permit and zoning case management | Data class: Confidential (PII)
Reviewed by: Maria Salinas, Information Security Manager
Review date: 2026-04-30
**Disposition: Approve with conditions**

## EXECUTIVE SUMMARY

PermitPath Inc. is a Texas-based SaaS provider of permit and zoning case management software, multi-tenant, hosted on AWS US-East and US-West. The product satisfies functional requirements for the Planning Department and integrates with Cedar Ridge's identity provider. Security posture is adequate for a Confidential PII workload but has three gaps that must be remediated or contractually addressed before award.

**Top three risks:**
1. No FedRAMP and no TX-RAMP authorization. SOC 2 Type II is the only third-party attestation.
2. Subprocessor list discloses subprocessor names but not geographic location of subprocessor staff with potential City data access.
3. Vendor lacks a standalone DPA template; current data protection terms are in the MSA security exhibit only.

**Required contractual provisions:**
- DPA with City as data controller; 60-day notice on subprocessor changes; geographic disclosure of subprocessor support staff.
- 48-hour breach notification clause to City CIO with content specification (scope, affected data, vendor response).
- Annual audit right on reasonable notice; vendor cooperation with carrier-appointed forensics in the event of an incident.
- Insurance minimums: $5M cyber, $2M E&O, $1M general liability.

**Disposition rationale:** Approve subject to executed DPA and the contractual provisions above. Move SOC 2 evidence review to annual. Reassess at renewal in 36 months; if TX-RAMP Level 1 becomes available by then, require it.

## 1. COMPANY AND SERVICE OVERVIEW

| # | Question | Response | Source | Gap |
|---|---|---|---|---|
| 1.1 | Legal entity, jurisdiction | PermitPath Inc., Delaware C-corp, principal office Austin TX | Vendor RFI Q.A1 | None |
| 1.2 | Years in business; financial indicators | 8 years; ~140 employees; Series B | Vendor RFI Q.A2; Crunchbase | None |
| 1.3 | Service architecture | Multi-tenant SaaS on AWS us-east-1 (primary), us-west-2 (DR) | SOC 2 § II.A | None |

## 2. DATA HANDLING AND CLASSIFICATION

- City data in scope: applicant PII (name, address, contact), property records, application content, staff review notes, council decisions.
- Residency at rest: AWS us-east-1 and us-west-2 (United States).
- Vendor's internal classification: maps to "Customer Data — Confidential" tier.
- Retention: vendor retains for term + 90 days post-termination; City retains primary retention authority via export.
- Data return: JSON export + PDF case packages on termination.

**Gap: Low.** Confirm 90-day post-termination retention window in DPA; require irrevocable deletion certificate.

## 3. SECURITY CERTIFICATIONS

| Certification | Status | Notes |
|---|---|---|
| SOC 2 Type II | Yes — current report dated 2026-01-15, auditor Big Four firm | Two exceptions: late patching on a non-production system; one logging gap remediated by report date. Acceptable. |
| ISO 27001 | No | Not pursued; vendor states "on the SOC 2 path" |
| FedRAMP | No | Vendor stated "not on roadmap" |
| TX-RAMP | No | Vendor stated awareness; will pursue Level 1 if requested by Texas customers |
| HITRUST / PCI / CJIS | N/A | Not in scope for this data class |

**Gap: High.** No FedRAMP or TX-RAMP. Cedar Ridge currently treats TX-RAMP as preferred, not required, for non-CJIS workloads. Approvable on SOC 2 Type II alone; flag for renewal reassessment.

## 4. ACCESS CONTROLS AND AUTHENTICATION

- MFA: required for admin; configurable for end users (Cedar Ridge will require).
- SSO via SAML 2.0 (Cedar Ridge IdP integration confirmed in proof-of-concept).
- RBAC with audit trail; admin actions logged 1 year.
- PAM: vendor uses just-in-time elevation; access requires manager approval and is logged.
- Background checks: criminal and education verification on all personnel; 100% of vendor staff.

**Gap: Low.** Acceptable.

## 5. ENCRYPTION

- In transit: TLS 1.2 minimum, TLS 1.3 supported; ciphers per Mozilla intermediate.
- At rest: AES-256, AWS KMS managed keys; BYOK not offered.
- Backups encrypted at rest; logs encrypted in S3 with separate key.

**Gap: Medium.** No BYOK. Accept for this data class; revisit if scope expands to financial data.

## 6. VULNERABILITY MANAGEMENT

- Annual third-party pen test; most recent report 2025-11-20, two medium findings remediated.
- Daily scans (DAST and SCA); critical SLA 7 days; high 30 days; medium 90 days.
- SDLC: branch protection, peer review, SAST in pipeline.
- SBOM available on request.

**Gap: Low.** Acceptable.

## 7. INCIDENT RESPONSE AND NOTIFICATION

- Documented IR plan; tested annually.
- Customer notification: vendor's default contract language commits to "without undue delay" — too vague.
- Forensics: cooperation pledged; full forensics support is a paid professional service unless a confirmed customer-impact breach.
- 24-month history: one Sev 2 (BEC against vendor staff; no customer data); zero customer-data incidents.

**Gap: Critical.** "Without undue delay" is not adequate. Require 48-hour notification clause to City CIO with content specification. **Must remediate before award.**

## 8. BUSINESS CONTINUITY AND DR

- RPO 1 hour, RTO 4 hours.
- Backups every hour; retained 35 days; replicated to us-west-2.
- Annual DR exercise; last test 2025-10-08 met objectives.
- Multi-region failover supported.

**Gap: Low.** Acceptable for this workload.

## 9. SUBPROCESSORS

- Subprocessor list provided: AWS, Datadog, Twilio, Stripe, three named consulting firms.
- Flow-down obligations stated in vendor's terms; City has no direct privity.
- Notification on subprocessor changes: 30 days; objection right limited to material changes.
- **Geographic disclosure of subprocessor support staff: not provided.**

**Gap: High.** Subprocessor list lacks geographic detail. City data may be accessible to non-U.S. support staff. Require disclosure of subprocessor support-staff geography in DPA; require advance notice on staff geography changes.

## 10. DATA RESIDENCY

- Primary: AWS us-east-1; DR: us-west-2; support center: Austin, TX with some staff in Pune, India.
- Cross-border transfer: support-staff access from Pune.
- Remote access: VPN, MFA, session recording.

**Gap: Medium.** India support access requires a contractual cross-border transfer mechanism and a documented data-minimization control (no PII to chat tools, etc.). Address in DPA.

## 11. CONTRACTUAL PROVISIONS REQUIRED

- [ ] DPA executed with the gaps above resolved — **must remediate**
- [x] BAA — not applicable
- [ ] 48-hour breach notification clause — **must remediate (Critical)**
- [ ] Audit rights annual on reasonable notice — request
- [ ] Indemnification floor $5M for vendor-caused breach
- [ ] Insurance minimums confirmed; certificates due at execution
- [ ] Right to terminate for material security failure
- [x] Data return and deletion at termination — vendor agrees

## 12. DECISION

Approve with conditions. Procurement may proceed to negotiation. Award is conditional on executed DPA addressing the Critical and High gaps above. Re-review at first renewal, with a strong preference for TX-RAMP Level 1 by 2029.

---

**Drafting notes (not part of the official questionnaire):**

This SaaS holds the same case data the planning department's `staff-report-writer` and `zoning-narrative-writer` skills will operate on (e.g., the Z-2026-04 case file). Coordination across plugins is by data system, not by skill.

The questionnaire is annotated *AI-assisted draft, reviewed by Maria Salinas, Information Security Manager* per Cedar Ridge IT-014.
