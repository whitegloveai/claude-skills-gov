# Emergency Message Statutory and Operational Formats

This reference is for drafters. It collects the required formats and character limits for the five most common Texas municipal emergency notices. Verify against current TCEQ, FEMA IPAWS, and carrier specifications before issuing live messages — limits and templates change periodically.

---

## 1. Boil-Water Notice — 30 TAC § 290.46(q)

TCEQ requires public water systems (PWS) to issue a boil-water notice when bacteriological contamination is suspected or confirmed, when pressure drops below 20 psi in any portion of the distribution system, or when other conditions in 30 TAC § 290.46(q) are met. The system must use TCEQ-approved language and issue notice within 24 hours of the triggering event.

### Required content

1. A clear description of the situation.
2. Specific actions consumers should take, including:
   - Bring all water to a vigorous rolling boil for at least two (2) minutes before using for drinking, cooking, ice, food preparation, brushing teeth, or any other consumption.
   - Use bottled or boiled water for infant formula and for immunocompromised persons.
3. The population most at risk (infants, elderly, immunocompromised).
4. A description of the cause and the estimated time the advisory will remain in effect.
5. Steps the system is taking to correct the problem.
6. A contact name, phone number, and address for questions.
7. The public water system identification number (PWS ID).
8. The signature or printed name of the responsible operator.

### Required notice methods (any combination as appropriate)

- Door hangers on each affected service connection.
- Hand-delivered notices.
- Posted notices in conspicuous locations.
- Local broadcast media (radio, TV).
- Local newspaper.
- Direct telephone notification (CodeRED or equivalent).
- Posted on the system's public website.

### Lift-notice requirements

Two consecutive bacteriological samples taken 24 hours apart must be free of total coliform bacteria. TCEQ approval is required before lifting. The lift notice must use approved language and follow the same delivery channels as the initial notice. Maintain a record of the bacteriological results and the lift-notice issuance in the PWS file for at least three (3) years (longer if part of a TCEQ enforcement file).

### TCEQ-approved standard language (reproduce verbatim on the notice)

> "Due to [cause], the [PWS Name, PWS ID] is advising all customers in [affected service area] to boil all tap water used for drinking, cooking, making ice, brushing teeth, or washing dishes. Bring water to a vigorous rolling boil and continue boiling for at least two (2) minutes. In lieu of boiling, customers may purchase bottled water or obtain water from another suitable source. When it is no longer necessary to boil the water, the public water system officials will notify customers that the water is safe to drink."

> "Once the boil-water notice is no longer in effect, the public water system will issue a notice to customers that rescinds the boil-water notice in a manner similar to this notice."

---

## 2. CodeRED / Emergency Notification System

CodeRED is a private mass-notification service used by most Texas municipalities. It supports voice, SMS, and email. Limits vary by carrier and message type.

### SMS body

- **160 characters** for a single-segment SMS (standard GSM encoding).
- **70 characters** for messages containing non-GSM characters (e.g., extended characters in some Spanish-language text).
- Multi-segment messages are split by carrier; segmentation can affect delivery order on some networks.

### Voice script

- **45 to 60 seconds** at conversational pace is the operational target.
- Synthetic voice with a known recognizable identifier ("This is a message from the City of [Name].") at the start.
- Repeat the core action at the end.

### Email

- Subject under 60 characters.
- Plain-text body required for accessibility.
- HTML body optional. Avoid images-only messages.

---

## 3. IPAWS — Integrated Public Alert and Warning System

IPAWS is the federal interoperability layer (FEMA) that allows authorized alerting authorities to send messages through Wireless Emergency Alerts (WEA), Emergency Alert System (EAS), NOAA Weather Radio, and internet alerts. Use is restricted to authorized alerting authorities operating under an approved IPAWS Memorandum of Agreement with FEMA.

### WEA body limits

- **360 characters** for WEA 2.0 (most modern devices).
- **90 characters** for legacy WEA on older devices.
- Body must include: a what (event), a where (geographic area), a who (sending authority), and a when (time and duration).
- WEA is one-way. Citizens cannot reply. Include a follow-up channel (URL or city number).

### Event codes

Use the appropriate Common Alerting Protocol (CAP) event code. Common municipal codes:

- **SPW** — Shelter in Place Warning.
- **EVI** — Evacuation Immediate.
- **CEM** — Civil Emergency Message.
- **LAE** — Local Area Emergency.

### Testing

Test in IPAWS Lab before any live use. Local jurisdictions are responsible for accuracy and geographic targeting.

---

## 4. Road Closure Notices

No single statutory format. Operational best practice:

- Header: "Road Closure — [Roadway] — [Date/Time Begin] to [Date/Time End]."
- Identify the controlling agency (city Public Works, TxDOT, county) and the closure reason.
- Identify detour route by named street.
- Identify access for emergency vehicles and residents within the closure.
- Identify contact for questions.
- If closure affects a state highway, coordinate with the TxDOT Area Office and the District Public Information Officer.

---

## 5. LEPC / Tier II — Emergency Planning and Community Right-to-Know Act

Under EPCRA Tier II reporting (42 U.S.C. § 11022 and 40 CFR Part 370), facilities storing reportable quantities of hazardous chemicals file annual Tier II reports with the State Emergency Response Commission (SERC), the Local Emergency Planning Committee (LEPC), and the local fire department.

In an emergency, the LEPC and the local fire department are the primary points for chemical hazard information. Emergency comms drafters should:

- Coordinate with the LEPC chair or designee before issuing a notice that names a specific chemical or facility.
- Use the chemical's common name and a one-sentence plain-language hazard description.
- Identify the recommended action (shelter in place, evacuate, distance).
- Include the LEPC and fire department contact for questions.
- Do not publish facility-specific Tier II data inconsistent with site-security protections that may be invoked under Tex. Gov't Code § 552.155 (homeland security) or applicable federal restrictions.

---

## 6. ADA, language access, and accessibility

- ADA Title II: reasonable modifications path on request. Provide alternate formats (large print, braille, audio) on request.
- LEP Executive Order 13166 and equivalent state guidance: meaningful access for limited-English-proficient populations. Spanish is operational standard in most Texas LEP neighborhoods. Other languages where the population warrants.
- ASL video for life-safety messages where feasible. Caption all video. Provide a transcript.
- Web posting: WCAG 2.1 Level AA. Plain-text fallback for any image. Adequate color contrast.

---

## 7. Drafter checklist before release

- [ ] Facts verified by named source within the agency.
- [ ] Geographic scope clear and bounded (no ambiguity at the edges).
- [ ] Recommended action stated as imperative.
- [ ] Duration and next-update time stated.
- [ ] Authorized sender identified.
- [ ] Contact channel(s) for citizen questions identified.
- [ ] English and Spanish renders complete; translator named.
- [ ] Statutory format requirements satisfied (boil-water, IPAWS event code).
- [ ] Channel-specific character limits respected.
- [ ] AI-assisted draft notation present.
- [ ] Final authorizer named and approval logged with timestamp.
- [ ] Record retained in incident file per TSLAC retention schedule.
