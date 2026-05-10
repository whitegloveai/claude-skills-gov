# NIST CSF 2.0 and NIST SP 800-53 Rev. 5 Mapping for Common Municipal IT Policies

This reference maps the IT policy topics most often adopted by Texas cities to NIST CSF 2.0 functions and the NIST SP 800-53 Rev. 5 control families that should anchor the policy statement. Use it to verify framework coverage during policy drafting and review.

## NIST CSF 2.0 — six functions

- **Govern (GV)** — organizational context, risk management strategy, roles, oversight. New in CSF 2.0.
- **Identify (ID)** — asset management, business environment, governance, risk assessment.
- **Protect (PR)** — access control, awareness and training, data security, IP and processes, maintenance, protective technology.
- **Detect (DE)** — anomalies and events, continuous monitoring, detection processes.
- **Respond (RS)** — response planning, communications, analysis, mitigation, improvements.
- **Recover (RC)** — recovery planning, improvements, communications.

## Policy-to-control mapping

| Policy topic | Primary CSF function | Key 800-53 Rev. 5 families | Notes |
|---|---|---|---|
| Acceptable Use | PR.AT, GV.PO | AC-2, AC-8, AT-2, PL-4 | Tie to personnel manual for sanctions. |
| Password and Authentication | PR.AA | IA-2, IA-5, IA-11 | NIST SP 800-63B for the technical standard. MFA required for privileged and remote access. |
| Access Control | PR.AA, PR.DS | AC-2, AC-3, AC-5, AC-6 | Least privilege; periodic access reviews. |
| Bring Your Own Device (BYOD) | PR.AC, PR.DS | AC-19, AC-20, CM-7 | Address mobile device management, e-discovery, and stipend. |
| Remote Access | PR.AA, PR.PT | AC-17, SC-8, SC-12 | VPN or zero-trust gateway; MFA mandatory. |
| Data Classification | ID.AM, PR.DS | MP-2, SC-28, RA-2 | Define classes: Public, Internal, Confidential, Restricted (CJIS/PHI/PCI). |
| Generative AI Use | GV.OC, GV.RM, PR.DS | PM-30, SI-4, AC-22 | Reference NIST AI RMF 1.0 and the Generative AI Profile. TRAIGA cross-reference required. |
| Incident Response | RS.MA, RS.AN, RS.CO | IR-1 through IR-8 | NIST SP 800-61 as procedural reference. DIR reporting per Tex. Gov't Code § 2054.1125. |
| Vendor Management | GV.SC, ID.SC | SA-9, SA-12, SR-3 | Reference vendor risk questionnaire and BAA/DPA templates. |
| Change Management | PR.IP | CM-3, CM-4, CM-5 | Tie to ITIL change advisory board or equivalent. |
| Vulnerability Management | ID.RA, PR.IP, DE.CM | RA-5, SI-2, SI-3 | Define SLA per severity (critical 7 days, high 30, medium 90). |
| Logging and Monitoring | DE.CM, DE.AE | AU-2, AU-3, AU-6, AU-12 | Tie retention to TSLAC and any CJIS or HIPAA logging mandates. |
| Physical Security | PR.AC, PR.IP | PE-2, PE-3, PE-6 | Server rooms, network closets, badge access. |
| Backup and Recovery | RC.RP, RC.IM | CP-9, CP-10, SI-13 | Define RPO and RTO per system class. Immutable backups for ransomware resilience. |

## Regulated-data overlays

When a policy touches regulated data, layer the relevant federal or state requirements on top of the NIST baseline:

- **CJIS** — FBI CJIS Security Policy v5.9 (or current). Applies to police records, dispatch, and any system that touches criminal justice information. Requires advanced authentication, audit logging, and personnel screening.
- **HIPAA** — 45 C.F.R. Parts 160 and 164. Applies if the city operates a covered component (utility-billing PHI does not normally qualify; ambulance billing and group health plans typically do).
- **FTC Safeguards Rule** — 16 C.F.R. Part 314. Cities operating utility billing where the city extends credit may be a "financial institution" under the rule.
- **Privacy Act of 1974** — 5 U.S.C. § 552a. Applies only to federal records; not directly applicable to cities but useful as a structural reference.
- **Tex. Bus. & Comm. Code § 521** — Texas Identity Theft Enforcement and Protection Act. Breach notification for sensitive personal information.
- **Tex. Bus. & Comm. Code Ch. 552 (TRAIGA)** — AI use disclosure and prohibited uses; effective January 1, 2026.

## TX-RAMP scope note

Tex. Gov't Code Ch. 2059 establishes the Texas Risk and Authorization Management Program (TX-RAMP) for cloud services consumed by Texas state agencies. **Cities are not directly subject to TX-RAMP** by statute. However, many Texas cities have voluntarily adopted TX-RAMP Level 1 or Level 2 as a procurement floor for SaaS, IaaS, and PaaS services because the certification rides on FedRAMP and SOC 2 evidence that vendors already produce. A vendor management policy should state whether TX-RAMP authorization is required, preferred, or considered alongside other certifications.

## Texas DIR alignment

Tex. Gov't Code Ch. 2054 vests information resource management authority in the Department of Information Resources. DIR publishes the Texas Cybersecurity Framework, which maps to NIST CSF. Cities that align with the Texas Cybersecurity Framework gain access to DIR shared services and pricing.

Tex. Gov't Code § 2054.1125 requires reporting of certain cybersecurity incidents. While the direct statutory reporting obligation lies on state agencies, DIR encourages voluntary reporting from cities; many cyber insurance policies now require DIR notification as a coverage condition.

## How to use this mapping

1. Identify the policy topic and find its row.
2. Confirm the primary CSF function — that drives the section ordering of the policy.
3. Pull the 800-53 control identifiers into the policy statement comment column.
4. Layer regulated-data overlays if the policy touches CJIS, PHI, or financial data.
5. Note any TX-RAMP or DIR cross-references in the related documents section.
