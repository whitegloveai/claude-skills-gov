---
name: agenda-builder
description: Drafts a TOMA-compliant Texas city council meeting agenda from a list of items. Use when a city secretary, council aide, or city manager's office needs to produce a posted agenda for a regular, special, or emergency meeting that meets Tex. Gov't Code Ch. 551 notice and content requirements.
---

# Agenda Builder

> Drafts a posted council meeting agenda that satisfies the Texas Open Meetings Act. Built for city secretaries and council aides assembling agendas under deadline.

## When to Use

- "Build me a draft agenda for the May 12 regular council meeting."
- "I have these 8 items going to council next week — put them in agenda form."
- "Draft a special meeting agenda. We need an executive session on the city manager's evaluation."
- "Convert this list of items into a TOMA-compliant agenda."
- "We have an emergency meeting tomorrow on the boil-water notice — draft the agenda."
- A meeting must be posted at least 72 hours in advance under Tex. Gov't Code § 551.043 and the user is preparing the posting.

## Inputs Needed

Required:

- Entity name (e.g., "City of Cedar Ridge")
- Meeting type: regular, special, or emergency
- Meeting date and time
- Meeting location (physical address; note any video conferencing under § 551.127)
- List of agenda items, each with: short title, one- to three-line description, presenter/sponsor

Optional:

- Executive session topics with the relevant § 551.07x exception
- Public hearing items with the controlling statute (LGC, zoning, budget, etc.)
- Consent agenda items (routine, non-controversial)
- Any items requested by individual council members under § 551.041 / § 551.0411
- Whether the meeting will be broadcast or video-conferenced

If the user has not provided meeting type, posting deadline, or executive session statutory citations, ask before drafting.

## Process

1. Confirm meeting type and verify the posting timeline. Regular and special meetings need 72 hours; emergency meetings need at least 1 hour with a written supplemental notice and a stated reason for the emergency under § 551.045.
2. Draft the header block: entity name, governing body, meeting type, date, time, location, and a posting timestamp placeholder for the city secretary to fill in at posting.
3. Order agenda items in the standard sequence: call to order, invocation/pledge, public comment, consent agenda, public hearings, regular business, executive session, reconvene/action, adjournment.
4. For each public hearing, cite the controlling statute (e.g., LGC § 102.006 for budget; LGC Ch. 211 for zoning).
5. For each executive session topic, cite the specific § 551.07x exception (most commonly § 551.071 attorney consultation, § 551.072 real property, § 551.074 personnel).
6. Write item descriptions with enough specificity to satisfy the § 551.041 "subject" notice standard. Vague captions like "Discuss city business" do not comply.
7. Add a TOMA posting certification block at the end for the city secretary's signature and posting timestamp.
8. Flag any item that may require additional notice (zoning hearings under LGC Ch. 211, tax rate hearings under Tax Code Ch. 26, etc.) so the user can verify ancillary postings.

## Output Format

Plain markdown agenda with the following sections in order. No emoji. No flourishes.

```
[ENTITY NAME]
[GOVERNING BODY]
[MEETING TYPE] MEETING AGENDA
[DATE], [TIME]
[LOCATION]

Posted: [DATE/TIME — to be filled by City Secretary at posting]

1. CALL TO ORDER

2. INVOCATION AND PLEDGES OF ALLEGIANCE
   [Note on prayer practice: invocations should be voluntary and not endorsed
   by the council. Consider rotating clergy or moment of silence to avoid
   Establishment Clause concerns. Pledge to the United States flag and the
   Texas flag.]

3. PUBLIC COMMENT
   The Council will hear public comment on items on this agenda and on
   matters of public concern under Tex. Gov't Code § 551.007. Each speaker
   is allotted [X] minutes. Speakers must complete a public comment form.
   The Council may not deliberate or take action on items not posted under
   § 551.042.

4. CONSENT AGENDA
   The following items are considered routine and will be acted on by a
   single motion. Any council member may pull an item for separate
   consideration.
   4a. [Item]
   4b. [Item]

5. PUBLIC HEARINGS
   5a. [Hearing title — Statutory citation]

6. REGULAR BUSINESS / INDIVIDUAL CONSIDERATION
   6a. [Item — discussion and possible action]

7. EXECUTIVE SESSION
   The Council may convene in closed executive session under the following
   provisions of the Texas Open Meetings Act:
   7a. § 551.071 — Consultation with attorney regarding [subject]
   7b. § 551.074 — Personnel matters: [position]

8. RECONVENE IN OPEN SESSION AND ACTION ON EXECUTIVE SESSION ITEMS

9. ADJOURNMENT

CERTIFICATION OF POSTING
I, [Name], City Secretary of the [City Name], certify that this agenda
was posted on the bulletin board at City Hall at [Address] and on the
City's internet website at [URL] on [DATE] at [TIME], not less than 72
hours before the scheduled meeting time, in accordance with Tex. Gov.
Code § 551.043 and § 551.056.

___________________________________
[Name], City Secretary
```

Length: approximately 1–3 pages depending on number of items.

Tone: neutral, plain, no editorializing. Item descriptions describe the action, not its merits.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Open Meetings Act (Tex. Gov't Code Ch. 551):**

- § 551.041 — Notice must state time, place, and subject of each item.
- § 551.043 — Regular and special meetings require posting at least 72 hours in advance.
- § 551.045 — Emergency meetings require 1-hour notice with written supplemental notice of the emergency.
- § 551.056 — Internet posting required for cities of 48,000+.
- § 551.07x — Executive sessions require specific citation.

**Public Records:** The posted agenda is public under Tex. Gov't Code Ch. 552. Drafts may be exempt under § 552.111 until posted.

**Retention:** Posted agendas retain permanently per TSLAC Schedule GR Item 1000-26.

**Verify before posting:** Statutory citations, meeting time/place, and any required ancillary notices (tax rate hearings, zoning notices).

## References

- See `references/toma-agenda-sections.md` for a section-by-section taxonomy of the Texas Open Meetings Act and the executive session exceptions catalog.

## Examples

- See `examples/regular-meeting-cedar-ridge.md` for a worked example: a full regular meeting agenda for the fictional City of Cedar Ridge, TX with 9 items including a budget amendment public hearing, a zoning case, and an executive session.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
