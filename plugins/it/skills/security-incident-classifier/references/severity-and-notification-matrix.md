# Severity and Notification Matrix

This reference accompanies the `security-incident-classifier` skill. It defines the four-tier severity scale, the response-time targets at each tier, and the external notification triggers keyed to statute and contract. Use it during classification and during after-action review.

## Severity definitions

### Sev 1 — Critical

Confirmed compromise or unavailability with **high** impact on confidentiality, integrity, or availability of a system processing Restricted or Confidential data, OR a confirmed breach of sensitive personal information, OR a confirmed compromise of CJIS data, election data, public-safety dispatch, or financial transaction systems.

- **Response time target:** Incident Commander engaged within 30 minutes; executive notification within 60 minutes.
- **Council briefing:** Required, normally within 24 hours.
- **Public communications:** Hold by default. Release only after counsel review.

Examples: ransomware on utility billing or finance; confirmed exfiltration of HR records; loss of CAD/911 availability.

### Sev 2 — High

Significant suspected or confirmed event with **moderate** impact on a regulated or business-critical system, OR confirmed compromise of an individual high-privilege account, OR confirmed phishing/BEC with monetary loss potential.

- **Response time target:** Incident Commander engaged within 2 hours; executive notification within 4 hours.
- **Council briefing:** As warranted; brief the City Manager.
- **Public communications:** Hold pending investigation outcome.

Examples: BEC attempt on accounts payable; confirmed account takeover of department director; targeted malware on a single workstation with privileged access.

### Sev 3 — Moderate

Confirmed event with **low** impact, OR widespread suspected event that has not been confirmed.

- **Response time target:** Standard ticketing; same-business-day triage.
- **Council briefing:** None unless escalated.
- **Public communications:** None.

Examples: phishing email reaching multiple users with no confirmed click; malware quarantined by EDR on a low-privilege workstation; isolated misuse without data exposure.

### Sev 4 — Low

Minor security hygiene event, policy violation without exposure, or false positive.

- **Response time target:** Routine.
- **Council briefing:** None.
- **Public communications:** None.

Examples: lost MFA token recovered the same day; password sharing reported by manager; isolated phishing click with no credential compromise.

## Notification triggers — when each applies and the timeline

| Recipient | Trigger | Statute / contract | Timeline | Notes |
|---|---|---|---|---|
| Cyber insurance carrier | Any Sev 1 or 2 with potential coverage implication | Policy condition precedent | Immediate (within hours) | Late notice is the most common coverage forfeiture. |
| Texas DIR | Cybersecurity incident with state-data nexus or per cyber insurance condition | Tex. Gov't Code § 2054.1125 alignment | 48 hours (planning target) | Direct obligation runs on state agencies; cities align voluntarily. |
| City Manager | Any Sev 1 or 2 | Local governance | Within 1 hour (Sev 1) or 4 hours (Sev 2) | Same hour for Sev 1. |
| City Council | Sev 1 with public-impact dimension | Local governance and TOMA disclosure planning | Within 24 hours (briefing) | Coordinate with city attorney on closed-session under Tex. Gov't Code § 551.089 (security). |
| Affected Texas residents | Breach of sensitive personal information | Tex. Bus. & Comm. Code § 521.053(b) | Without unreasonable delay; no later than 60 days from determination | Method and content per § 521.053(d). |
| Texas Attorney General | Breach affecting 250 or more Texas residents | Tex. Bus. & Comm. Code § 521.053(i) | No later than 60 days from determination | Online submission per OAG portal. |
| FBI / CISA | Cybercrime, ransomware, nation-state indicators | Voluntary; CISA strongly encouraged | ASAP | CISA's StopRansomware reporting is the simplest channel. |
| Vendor or service provider | Compromise indicators involving vendor systems or credentials | Contract | Immediate | Triggers vendor's own breach response and possibly BAA/DPA notification obligations. |
| HHS OCR | Breach of unsecured PHI | HIPAA Breach Notification Rule, 45 C.F.R. §§ 164.400–414 | Individuals within 60 days; OCR within 60 days (>500 affected) or annual log (<500); media if >500 in a state | Only if City operates a HIPAA covered component. |
| FBI CJIS Systems Officer | Compromise of criminal justice information | FBI CJIS Security Policy | Immediate | Triggers FBI involvement and audit. |
| Texas Secretary of State | Election system incident | Election Code and SOS guidance | Immediate | Election-system nexus elevates to Sev 1 regardless of size. |

## Key statutory language to cite verbatim

- **Tex. Bus. & Comm. Code § 521.053(b):** notification "as quickly as possible" and "not later than the 60th day after the date on which the person determines that the breach occurred."
- **Tex. Bus. & Comm. Code § 521.053(i):** AG notification "if a breach … requires notification of at least 250 residents of this state."
- **Tex. Bus. & Comm. Code § 521.002:** definitions of "breach of system security" and "sensitive personal information."
- **Tex. Gov't Code § 2054.1125:** state-agency reporting framework that informs the city's voluntary 48-hour target.
- **Tex. Gov't Code § 552.139:** TPIA exception for "information that relates to computer network security."
- **Tex. Gov't Code § 552.108:** TPIA exception for law enforcement records.
- **Tex. Gov't Code § 551.089:** TOMA closed-session authority for security audits and assessments.

## Defining "sensitive personal information" under § 521.002

Sensitive personal information is, in summary, a Texas resident's first name or initial and last name in combination with one or more of: SSN, driver's license number or government-issued ID number, or financial account or card number with any required security code. Health information and biometric data are also included under § 521.002(a)(2). The classifier should treat any of those combinations as triggering § 521.053.

## Post-classification checkpoints

1. Counsel concurrence on the notification list before any external notice is sent.
2. Cyber insurance carrier appointment of forensics or breach counsel.
3. Council briefing under § 551.089 closed session if litigation or further compromise risk exists.
4. Hand-off to records management for retention of the investigation file.
