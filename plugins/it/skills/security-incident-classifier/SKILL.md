---
name: security-incident-classifier
description: Classifies a cybersecurity event by severity, category, and external notification trigger, and produces an initial response action list. Use when an IT director, SOC analyst, or city manager needs a fast, defensible classification of a confirmed or suspected incident to drive the right notification, containment, and forensic-preservation steps.
---

# Security Incident Classifier

> Turns a chaotic event into a structured classification with severity, category, notification triggers, and the first-90-minutes response actions. Built for the IT director who has to brief the city manager in 30 minutes.

## When to Use

- "Utility billing looks encrypted. Classify this and tell me who I have to call."
- "Phishing led to MFA-bypass login on a finance account. Severity?"
- "A vendor told us they had a breach that may include our data."
- "Someone walked off with an unencrypted laptop containing personnel files."
- "SOC flagged anomalous traffic to a known C2 IP from the police network."
- The city manager needs a written classification to decide on council notification, AG notification, and external communications.

## Inputs Needed

Required:

- Event description (what happened, in plain language).
- Affected systems and asset criticality.
- Data involved: classification level (Public, Internal, Confidential, Restricted) and regulated categories (PII, PHI, CJIS, financial account data, election data).
- Impact dimensions: availability, integrity, confidentiality — each rated as none, low, moderate, or high.
- Discovery time and event start time (if known).
- Threat actor signal (internal user, external opportunistic, targeted, vendor compromise, unknown).

Optional:

- Cyber insurance carrier and policy number (for early notification).
- Whether law enforcement is already engaged.
- Vendor or third-party involvement.
- Election-system or public-safety nexus (triggers additional notifications).

If data classification or impact dimensions are missing, ask before classifying. An incomplete classification produces the wrong notification list.

## Process

1. Validate facts. Distinguish *confirmed* from *suspected*. If suspected, classify conservatively and recommend a triage step before public notification.
2. Determine severity (Sev 1–4) using `references/severity-and-notification-matrix.md`. Anchor on the highest impact dimension and the regulated-data overlay.
3. Determine category: malware/ransomware, phishing/BEC, account compromise, insider, physical (lost or stolen device), vendor/third-party, denial of service, web defacement, data exfiltration, or system failure with security implications.
4. List affected data classes with PII/PHI/CJIS/financial markers.
5. Identify notification triggers and timelines: Tex. Bus. & Comm. Code § 521.053; Tex. Gov't Code § 2054.1125 (DIR alignment); CJIS Security Policy if applicable; HIPAA Breach Notification Rule if PHI; vendor and insurance triggers.
6. Generate the first-90-minutes response action list: isolation, credential rotation, log preservation, evidence chain of custody, communication holds, ticketing.
7. Add forensics preservation reminder: do not power down if memory is needed; do not log into compromised accounts to "check"; preserve logs before retention rotates them off.
8. Flag council briefing trigger and public-communications hold-or-release decision point.

## Output Format

```
CYBERSECURITY INCIDENT CLASSIFICATION
City of [ENTITY] — [Incident ID]
Classified by: [Name, title]
Classification time: [Timestamp]
Status: Confirmed | Suspected

1. EVENT SUMMARY
[2–4 sentence summary. What, when, scope.]

2. SEVERITY
Sev [1|2|3|4] — [Definition]
Rationale: [Impact and data-class drivers]

3. CATEGORY
[Primary category, with secondary tag if hybrid]

4. AFFECTED DATA
| Class | Volume (approx) | Regulated markers |
|---|---|---|
| [class] | [count] | [PII/PHI/CJIS/etc.] |

5. NOTIFICATION TRIGGERS
| Recipient | Statutory / contractual basis | Timeline | Status |
|---|---|---|---|
| Cyber insurance carrier | Policy condition precedent | Immediate | [Done/Pending] |
| Texas DIR | Tex. Gov't Code § 2054.1125 alignment | 48 hours | Pending |
| City Manager and Council | Local governance | [As required] | Pending |
| Affected citizens | Tex. Bus. & Comm. Code § 521.053 | No later than 60 days | Pending |
| Texas Attorney General | Tex. Bus. & Comm. Code § 521.053(i) if ≥ 250 affected | 60 days | Pending |
| FBI / CISA | Voluntary (CISA encouraged) | ASAP | Pending |
| Vendor | Contract | Immediate | Pending |
| HHS OCR | HIPAA Breach Rule if PHI | 60 days | Pending |
| FBI CJIS Systems Officer | CJIS Security Policy | Immediate | Pending |

6. CONTAINMENT — FIRST 90 MINUTES
- [ ] Isolate affected systems from network without powering down
- [ ] Preserve volatile memory if applicable
- [ ] Rotate credentials for affected accounts
- [ ] Disable compromised user sessions
- [ ] Place legal hold on related logs and email
- [ ] Open incident ticket with chronology

7. FORENSICS PRESERVATION
- Preserve logs that may rotate off (firewall, EDR, identity provider, mail security gateway).
- Do not log into compromised accounts to inspect.
- Document chain of custody for any imaged systems.

8. COMMUNICATIONS HOLD
[Default: hold all external communications until counsel approves. Internal communications limited to need-to-know.]

9. NEXT-STEPS OWNER
[Name, title — typically the CIO or designated incident commander]
```

Length: 2–4 pages. Tone: factual, time-stamped.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system*. This skill produces a static internal classification document; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged. Mark *"AI-assisted draft, reviewed by [Incident Commander]"* per city AI use policy.

**Texas Identity Theft Enforcement and Protection Act:** Tex. Bus. & Comm. Code § 521.053 requires notification to affected Texas residents of a breach of sensitive personal information without unreasonable delay and no later than the 60th day after determination. If 250 or more Texas residents are affected, notify the Texas Attorney General. Definitions of "sensitive personal information" and "breach of system security" are at § 521.002.

**DIR cybersecurity reporting:** Tex. Gov't Code § 2054.1125 governs reporting by state agencies; the direct obligation does not run on cities, but DIR encourages voluntary reporting and many cyber insurance policies require DIR notification as a coverage condition. Use 48 hours as a planning target.

**CJIS Security Policy:** If criminal justice information is involved, FBI CJIS Security Policy governs notification to the CJIS Systems Officer. CJIS notification is separate from and additional to § 521.053 notification.

**HIPAA:** If PHI is involved and the City operates a covered component (e.g., ambulance billing, group health plan), 45 C.F.R. §§ 164.400–414 requires notification of individuals, HHS OCR, and in some cases the media.

**Public records:** The classification document and the investigation file are public records under Tex. Gov't Code Ch. 552, subject to § 552.108 (law enforcement) and § 552.139 (computer network security) exceptions. Coordinate redactions with the city attorney.

**Retention:** Investigation files retain per TSLAC schedule SD (law-enforcement nexus) or GR (administrative).

## References

- See `references/severity-and-notification-matrix.md` for the severity definitions, response time targets, and a side-by-side notification matrix keyed to statutes and contracts.

## Examples

- See `examples/utility-billing-ransomware.md` for a worked example: a Sev 1 ransomware incident on a city utility billing system with multiple notification triggers (cyber insurance, DIR, council, customers under § 521.053, AG, vendor, FBI/CISA).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
