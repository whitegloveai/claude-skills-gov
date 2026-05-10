---
name: crisis-comms-template
description: Drafts initial holding statements and follow-up update templates for a public crisis (boil-water, severe weather, public safety incident, infrastructure failure, cybersecurity incident), with internal coordination notes and an all-clear template. Use when a PIO, city manager's office, or emergency management coordinator needs rapid, accurate crisis messaging that aligns with incident command.
---

# Crisis Communications Template

> Drafts a crisis communications package: holding statement, scheduled updates, all-clear, and internal coordination note. Built for PIOs and emergency management coordinators working under time pressure and chain-of-command discipline.

## When to Use

- "We just got a boil-water notice. Draft the holding statement now."
- "Major water main break flooding three blocks. PD has the area closed."
- "Cyber incident — ransomware on utility billing. Need a holding statement."
- "Severe weather watch upgraded to warning. Draft the activation package."
- "Officer-involved shooting downtown. Need a holding statement."
- A public crisis has occurred and the city must communicate within 30 minutes with verified facts.
- An incident command structure is forming and comms must align with the lead agency.

## Inputs Needed

Required:

- Incident type (boil-water, gas leak, cyber, severe weather, infrastructure failure, public safety)
- Scope: residents, geographic area
- Verified status: only what incident command has confirmed
- Known unknowns
- Lead agency, spokesperson, channels

Optional:

- Prior incident comms patterns
- Bilingual flag (mandatory for service-critical crises in significant LEP jurisdictions)
- Regulatory notice requirements (TCEQ; HHSC; FCC alerts)

If verified facts, lead agency, or spokesperson alignment is unclear, ask. Do not speculate.

## Process

1. Identify incident type and pull the matching pattern from `references/crisis-comms-holding-statement-patterns.md`.
2. Confirm verified facts only. Unconfirmed information stays in "known unknowns."
3. Confirm chain of command: lead agency, spokesperson, sign-off authority.
4. Draft Holding Statement (within 30 minutes) in three parts: what we know, what we are doing, next update.
5. Draft Update 1 (within 2 hours), Update 2 (within 12 hours or as warranted), and the All-Clear template.
6. Draft Internal Coordination Note — ICS alignment, no-speculation reminder, public records reminder, social moderation note.
7. Incorporate required regulatory language (TCEQ boil-water text is mandated; Tex. Bus. & Comm. Code Ch. 521 may apply to cyber).
8. Mark each template with a spokesperson sign-off field.

## Output Format

Plain markdown. Internal package, to be filled in and approved by incident command before each release. No emoji. Plain, calm, factual.

```
CRISIS COMMUNICATIONS PACKAGE — [INCIDENT TYPE]

Incident: [Brief description]
Activated: [TIMESTAMP] | Lead agency: [Agency]
Incident commander: [Name] | Spokesperson: [Name]
Bilingual required: [Yes / No]

---

HOLDING STATEMENT (release within 30 minutes)
For release at: ____   Approved by: ____

The City of [City] is responding to [incident, verified only].
[Area / residents affected.] [What is being done.] [Citizen
guidance.] [When the next update will be issued.]
For updates: [URL] | [Social] | [Mass notification].
Accessibility: [PHONE].
En espanol: [Spanish translation.]

---

UPDATE 1 (within 2 hours)
For release at: ____   Approved by: ____

UPDATED [TIMESTAMP]: [Refined facts.] [Actions since initial.]
[Updated citizen guidance.] [Resources.] [Next update.]
En espanol: [Spanish translation.]

---

UPDATE 2 (within 12 hours or as warranted)
For release at: ____   Approved by: ____

UPDATED [TIMESTAMP]: [Refined facts.] [Progress.] [Continued
guidance.] [Next update.]
En espanol: [Spanish translation.]

---

ALL-CLEAR STATEMENT
For release at: ____   Approved by: ____

UPDATED [TIMESTAMP]: The [incident] is resolved as of [time].
[What this means for residents.] [Continued precautions.]
[Thanks to responders, mutual aid, residents.] [Optional: report
damage, recovery resources, council briefing date.]
En espanol: [Spanish translation.]

---

INTERNAL COORDINATION NOTE (NOT FOR RELEASE)

1. Spokesperson: [Name]. Other staff do not speak to press
   independently.
2. Verified facts only. No speculation on cause, casualties,
   damage, or timing.
3. Social: post pre-approved updates; do not respond
   substantively in-thread; document moderation; route
   defamatory comments to PIO and City Attorney.
4. Mass notification: [system], activated by [approval level],
   coordinated with [agency].
5. Public records: every communication is a record under Tex.
   Gov't Code Ch. 552; drafts may be exempt under § 552.111;
   assume disclosure.
6. ICS alignment: conforms to adopted ICS structure.
7. Regulatory notices: [TCEQ / HHSC / state] handled by [lead].
8. Council: receives updates simultaneously with the public,
   plus an internal briefing from City Manager. Council does not
   speak independently to press.
9. Bilingual: every release goes out in English and Spanish
   simultaneously, reviewed by [reviewer].

AI-assisted draft, reviewed by [Name, Title] and incident command.
```

Length: 800–1,500 words for the full package.

Tone: calm, factual, third-person. No reassurance that could be falsified later. No blame. No speculation. No timing promises the incident cannot keep.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Verified facts only:** The largest cause of crisis comms failure is releasing unverified information. If a fact has not been confirmed by the incident commander, it does not go in the statement.

**Incident command:** Crisis comms align with ICS under NIMS. Tex. Gov't Code Ch. 418 (Texas Disaster Act) governs state and local emergency management. Multi-agency incidents use a Joint Information Center.

**Public records (Tex. Gov't Code Ch. 552):** Every internal communication is a record. Drafts may be exempt under § 552.111; assume disclosure. After-action reviews are subject to disclosure.

**TCEQ boil-water:** TCEQ prescribes specific notice language under 30 TAC § 290.46 when pressure drops below 20 psi. Use the prescribed text exactly; deviation creates regulatory exposure.

**Cyber incidents:** Tex. Bus. & Comm. Code Ch. 521 requires notice to affected individuals when sensitive personal information is exposed. Coordinate with legal, IT, and DIR before public disclosure.

**Officer-involved incidents:** Cleared by chief and City Attorney. Do not name involved officers initially. Do not characterize the incident.

**Bilingual and ADA:** For service-critical crises in LEP jurisdictions, bilingual is operationally mandatory; machine translation alone is insufficient. Video needs captions; web posts need alt text; robocalls need TTY. ADA Title II applies.

**Mass notification:** Local systems (CodeRED, Everbridge, RAVE) follow city policy with thresholds in the emergency operations plan.

## References

- See `references/crisis-comms-holding-statement-patterns.md` for proven holding statement structures for the most common municipal crises: boil-water, gas leak, cyber incident, severe weather, officer-involved incident. Each pattern with do's, don'ts, and the pivot from holding to fuller communication.

## Examples

- See `examples/boil-water-notice-template.md` for a Cedar Ridge boil-water notice crisis comms package, including TCEQ notice requirements summary and bilingual statement structure.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
