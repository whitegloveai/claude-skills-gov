---
name: emergency-comms-drafter
description: Drafts the operational emergency communication itself — a shelter-in-place order, evacuation order, all-clear, road-closure, or boil-water advisory — in the required statutory or operational format, in English and Spanish, for CodeRED, IPAWS/WEA, social, and posted notice. Use when an OEM coordinator, PIO, water system operator, or chief is releasing an operational notice to the public on a confirmed incident.
---

# Emergency Comms Drafter

> Drafts the operational emergency message itself — shelter-in-place, evacuation, all-clear, road closure, or boil-water — in the required format. Built for OEM staff, PIOs, and water operators issuing public notices on a confirmed incident.

## When to Use

- "Draft the boil-water notice for the Pecan pressure zone — TCEQ-compliant, English and Spanish."
- "Shelter-in-place message for the chemical spill on Highway 90."
- "Evacuation order for the apartment fire on Cypress."
- "All-clear and lift-notice package once water test results clear."
- "Road closure notice for bridge inspection on Main Street — 48 hours."
- A confirmed incident requires a public notice. User has verified facts and a recommended action and needs the message in CodeRED, IPAWS/WEA, social, and posted formats.

This skill produces the operational notice itself. For the holding statement and message architecture around the notice, use `communications/crisis-comms-template`.

## Inputs Needed

Required:

- Incident type — shelter-in-place, evacuation, all-clear, road closure, boil-water, lift notice, other.
- Geographic scope — addresses, pressure zone, neighborhood, intersection, radius.
- Confirmed facts only. What is verified, by whom, as of when.
- Recommended citizen action — specific behaviors.
- Channels to distribute — CodeRED, IPAWS/WEA, social, website, posted, media release.
- Authorized sender.
- Estimated duration and next-update time.

Optional:

- Bilingual scope beyond English/Spanish (other LEP languages, ASL video).
- ADA reasonable modifications path.
- Cross-jurisdictional coordination — county OEM, TDEM, TCEQ, neighboring city, school district.
- TCEQ Public Notification Rule template or LEPC / Tier II considerations.

If facts are not verified, ask before drafting. Emergency notices are public records and a wrong fact in writing is a long-tail problem.

## Process

1. Confirm incident type and the controlling format. Boil-water uses the TCEQ template under 30 TAC § 290.46(q). IPAWS/WEA is 360 characters (90 legacy). CodeRED SMS is 160 characters or longer voice.
2. Reduce to verified facts. Two paragraphs maximum on what is known. No speculation, no unconfirmed cause, no individual names without authorization.
3. State the citizen action in plain imperatives. "Do not drink the water." "Shelter in place until further notice." "Boil two full minutes before drinking, cooking, or making ice."
4. Add a duration and a next-update commitment with a specific time.
5. Add an authorized sender and a contact channel — main line, OEM hotline, website URL.
6. Render in each required format: long form (website, posted notice, door hanger, media release); CodeRED SMS; CodeRED voice script (45 to 60 seconds); IPAWS/WEA where criteria are met; social post.
7. Produce a Spanish translation of each render, reviewed by a fluent translator before release.
8. For boil-water, append TCEQ-required language verbatim (boil time, alternative sources, susceptible populations, contact, lift-notice commitment) and confirm public water system ID and operator signature line.
9. Add the AI-assisted draft notation and route to the named authorizer before release.

## Output Format

Plain markdown. One package containing all renders. No emoji. No flourishes.

```
EMERGENCY NOTICE — [INCIDENT TYPE]
[CITY / AGENCY]
Issued: [Date, Time, Time Zone]
Status: [Active / All-Clear / Lift Notice]
Authorized by: [Name, Title]

1. LONG-FORM NOTICE (English)
   [Header, geographic scope, recommended action, what is known,
   duration, next update, contact.]

2. CODERED SMS (160 char)
   [Plain action + URL.]

3. CODERED VOICE SCRIPT (45-60 sec)
   [Read-aloud cadence, plain English.]

4. IPAWS / WEA MESSAGE (360 char, where applicable)
   [Geographic, action, source, time.]

5. SOCIAL POST
   [First-screen lede + full text.]

6. SPANISH RENDERS
   6a. Long-form (Spanish)
   6b. SMS (Spanish)
   6c. Voice script (Spanish)
   6d. IPAWS/WEA (Spanish)
   6e. Social (Spanish)

7. STATUTORY OR OPERATIONAL APPENDIX (where applicable)
   [TCEQ Public Notification Rule language for boil-water; or
   LEPC Tier II reference; or other required format.]

AI-assisted draft, reviewed by [Name, Title].
Reviewed by translator: [Name].
Final approval to release: [Name, Title, Time].
```

Length: long-form 250 to 500 words; SMS 160 char; voice 45-60 sec; IPAWS 360 or 90 char.

Tone: factual, calm, imperative. No softening hedges. State what is happening and what to do.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Channel-level AI disclosure:** If the city delivers this notice through an AI-driven interactive channel (an IVR with synthetic voice, an SMS chatbot, an AI-driven hotline), Tex. Bus. & Comm. Code § 552.051 disclosure attaches at the channel level. The message drafted here is not the trigger; the delivery channel is.

**Boil-water notices:** 30 TAC § 290.46(q) requires TCEQ-approved language within 24 hours of the triggering event, with description, action, alternatives, susceptible populations, contact. The lift notice requires confirming bacteriological samples and TCEQ approval. The system's Public Water System ID and operator must appear.

**IPAWS / WEA:** Use only when criteria are met under the FEMA IPAWS Operating Standard — imminent threat to life or property within a specific geography. WEA bodies are 360 characters (90 legacy). Test before live use.

**Disaster declarations:** A mayor's local disaster declaration under Tex. Gov't Code Ch. 418 triggers TDEM reporting and may unlock mutual aid and emergency procurement authority. The notice is separate from the declaration but often paired.

**Public information (Tex. Gov't Code Ch. 552):** Emergency notices are public. Drafts may be exempt under § 552.111 until released. Internal incident command records may be exempt under § 552.108 or § 552.101.

**ADA / language access:** Reasonable modifications path on request. Spanish translation is operational standard in LEP neighborhoods; ASL video where feasible for life-safety messages.

**Retention:** Per Texas State Library Local Government Retention Schedule PS, Item 6075-04 (Emergency Management Records), longer if tied to a federally declared disaster or litigation hold.

## References

- See `references/emergency-message-statutory-formats.md` for the boil-water template under 30 TAC § 290.46(q), CodeRED and WEA limits, IPAWS message structure, LEPC / Tier II, and TCEQ-mandated language.

## Examples

- See `examples/boil-water-advisory-package.md` for a boil-water advisory package for a single pressure zone, with initial notice, CodeRED short version, follow-up updates, lift notice, and TCEQ Public Notification Rule language, English and Spanish.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
