# Example: Cedar Ridge Utility Billing Ransomware Classification

Worked example output of the `security-incident-classifier` skill for a fictional ransomware incident at the City of Cedar Ridge, TX.

**Inputs provided:**

- Event: Encryption of the production utility billing database and file shares. Ransom note dropped on shares at 03:42. Discovery at 06:15 by the on-call SOC analyst.
- Affected systems: UtilityWorks SaaS-adjacent on-prem billing application, the supporting MS SQL database, and the customer-correspondence file share.
- Data involved: Approximately 14,200 active customer records — name, service address, account number, billing history. Bank ACH routing/account numbers for ~3,800 customers enrolled in auto-pay.
- Impact: Availability — high. Integrity — high (encrypted). Confidentiality — moderate to high (exfiltration claim in the ransom note, not yet verified).
- Discovery time: 2026-04-22 06:15 CT. Event start estimated 2026-04-22 03:42 CT.
- Threat actor signal: Targeted; ransom note attributes to a known double-extortion group.
- Vendor involvement: UtilityWorks application vendor.
- Insurance: Cedar Ridge Texas Municipal Cyber Pool, Policy CMC-2026-0148.
- Law enforcement: Not yet engaged.

---

# CYBERSECURITY INCIDENT CLASSIFICATION

**City of Cedar Ridge, Texas — Incident ID CR-IR-2026-0007**
**Classified by:** Vihaan Joshi, CIO (Incident Commander)
**Classification time:** 2026-04-22 07:10 CT
**Status:** Confirmed

## 1. EVENT SUMMARY

At approximately 03:42 CT on April 22, 2026, threat actors deployed file-encrypting malware against the City's utility billing application, database, and supporting file shares. A ransom note dropped at 03:51 claims data exfiltration in addition to encryption. Encryption is confirmed. Exfiltration claim is unverified pending log review. The application is offline; the database is unrecoverable from primary storage and is being restored from immutable backup. Estimated population in scope: 14,200 active customer records, including ACH bank data on approximately 3,800 auto-pay customers.

## 2. SEVERITY

**Sev 1 — Critical.**

Rationale: confirmed encryption with high availability and integrity impact on a public-utility billing system; sensitive personal information in scope (ACH financial account data on 3,800 Texas residents); targeted threat actor; council-relevant public impact.

## 3. CATEGORY

Ransomware (primary). Data exfiltration (suspected, unverified).

## 4. AFFECTED DATA

| Class | Volume (approx) | Regulated markers |
|---|---|---|
| Customer name, address, account, usage history | 14,200 | PII |
| ACH routing and account number | 3,800 | PII; "sensitive personal information" under Tex. Bus. & Comm. Code § 521.002 |
| Internal correspondence file share | ~6 GB | Mixed; some attorney-client privilege expected |
| No CJIS data in scope | — | — |
| No PHI in scope | — | — |

## 5. NOTIFICATION TRIGGERS

| Recipient | Statutory / contractual basis | Timeline | Status |
|---|---|---|---|
| Cyber insurance carrier (TML Cyber Pool) | Policy CMC-2026-0148 condition precedent | Immediate | Notification sent 07:25 |
| Breach counsel (via carrier) | Carrier appointment | At carrier direction | Pending |
| Texas DIR | Tex. Gov't Code § 2054.1125 alignment; insurance condition | 48 hours | Pending |
| City Manager (Daniel Ahn) | Local governance | Within 1 hour | Notified 06:40 |
| City Attorney | Local governance | Within 1 hour | Notified 06:55 |
| City Council | Local governance; § 551.089 closed-session brief | Within 24 hours | Special meeting requested for 04/23 |
| Affected Texas residents (≥3,800 with ACH data) | Tex. Bus. & Comm. Code § 521.053(b) | Not later than 60 days from determination | Pending counsel approval and verification |
| Texas Attorney General | Tex. Bus. & Comm. Code § 521.053(i) (≥250 affected) | Not later than 60 days from determination | Pending |
| FBI / CISA | Voluntary | ASAP | Pending; recommend StopRansomware report |
| UtilityWorks (vendor) | Master services agreement § 12 | Immediate | Notified 06:55 |
| Texas Municipal League (insurance pool) | Pool membership | Per pool guidance | Tied to carrier notification |

## 6. CONTAINMENT — FIRST 90 MINUTES

- [x] Isolate utility billing servers and SQL host from network; preserve VM state
- [x] Take immutable backup repository read-only; verify backup integrity hashes
- [x] Rotate all service account credentials touching the affected subnet
- [x] Disable user sessions on affected accounts; require fresh MFA enrollment
- [x] Place legal hold on EDR, firewall, AD, and mail security logs
- [x] Open Incident Commander chronology in IR ticket CR-IR-2026-0007
- [ ] Engage carrier-appointed breach counsel and forensics
- [ ] Identify and document indicators of compromise

## 7. FORENSICS PRESERVATION

- Preserve EDR telemetry — current retention 90 days; in scope.
- Preserve firewall logs — current retention 14 days; risk of rollover; extend immediately.
- Preserve email security gateway logs — current retention 30 days; in scope.
- Do not log into any affected accounts to inspect. Use out-of-band methods.
- Chain of custody for any images: hash on capture, log custodian, store in case folder \\evidence\CR-IR-2026-0007 with restricted ACL.

## 8. COMMUNICATIONS HOLD

External communications held pending counsel review. Internal communications limited to need-to-know via the incident channel. Public utility-billing system status page may carry a generic "services temporarily unavailable" message under prior policy authority; no specifics until breach counsel approval.

Council briefing on 04/23 will be in closed session under Tex. Gov't Code § 551.089 (security audit/assessment) and § 551.071 (consultation with attorney), with action items returned to open session.

## 9. NEXT-STEPS OWNER

Vihaan Joshi, CIO — Incident Commander.

Backup IC: Maria Salinas, Information Security Manager.

---

**Drafting notes (not part of the official classification):**

This Sev 1 classification triggers the maximum notification fan-out. The combination of (a) confirmed encryption on a public-utility-serving system, (b) ACH financial account data on more than 250 Texas residents, and (c) a credible (though unverified) exfiltration claim places this incident in the highest-impact tier under both the city's internal scale and the § 521.053 notification statute.

The classification expressly anchors on Tex. Bus. & Comm. Code § 521.053 (not TPIA under Tex. Gov't Code Ch. 552). Cross-reference to TPIA appears only in the public records analysis for the investigation file (§ 552.108 and § 552.139 exceptions).

Cross-skill linkage: a finance-side impact assessment of receivables interruption should follow under the `finance` plugin's variance and revenue analysis workflows once the billing system is restored.

AI-assisted draft, reviewed by Vihaan Joshi, CIO.
