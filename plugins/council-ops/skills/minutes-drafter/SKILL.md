---
name: minutes-drafter
description: Drafts clean, public-records-safe city council meeting minutes from raw recordings, livestream transcripts, or note-taker drafts. Use when a city secretary or clerk needs to convert source material into the formal minutes for council approval.
---

# Minutes Drafter

> Turns raw meeting source material into draft minutes ready for review by the city secretary, mayor, and city attorney. Built for clerks who would otherwise spend a full day transcribing.

## When to Use

- "Here's the transcript from last night's council meeting — draft the minutes."
- "I have my notes plus the recording. Build me a minutes draft."
- "Convert this Zoom transcript into council minutes for the special meeting."
- "Need a clean minutes draft to send to the City Attorney for review before next council."
- The city secretary is preparing minutes for the next council meeting's consent agenda.

## Inputs Needed

Required:

- The agenda for the meeting (so the order and item captions match)
- Source material: a transcript, recording summary, or note-taker draft
- Vote tallies on each action item (mover, second, ayes, nays, abstentions, absentees)
- Attendance roll: who was present, who was absent, who arrived late or left early

Optional but improves accuracy:

- Executive session entry/exit times and a one-line description of what was deliberated (the action taken in open session must be in the minutes; the deliberation itself is not)
- A summary of public comment (or pull from the public-comment-summarizer skill)
- City Attorney's notes on any motions that were amended or substituted on the floor

If the user has not provided vote tallies or attendance, ask before drafting; minutes without these are not usable.

## Process

1. Read the agenda first. The minutes mirror the agenda's order. Use the same item captions.
2. Draft the opening: meeting type, date, time, place, and presiding officer.
3. Build the attendance roll. Note arrival or departure times for any member who was not present for the full meeting.
4. For each agenda item, draft a short narrative followed by the action taken. Use this pattern:
   *Caption.* Brief one- to three-sentence description of the discussion and any speakers. Motion by ___, seconded by ___. Vote: Ayes — ___; Nays — ___; Abstain — ___; Absent — ___. **Motion carried** (or *failed*, or *tabled*).
5. Summarize public comment neutrally. Name speakers (public comment is a public record). Do not characterize speakers' motives. Limit verbatim quotes; paraphrase substance.
6. For executive session, record the time the council recessed into closed session, the statutory citation(s), the time the council returned to open session, and any action taken in open session. Do NOT record what was said in closed session.
7. Note adjournment time.
8. Add a signature block for the mayor and city secretary.
9. Flag for human review: any motion where the source material is ambiguous, any item where the vote tally appears not to match members present, any executive session item where the open-session action is unclear.

## Output Format

Plain markdown minutes with the following structure:

```
[ENTITY NAME]
[GOVERNING BODY] MINUTES — [MEETING TYPE]
[DATE], [START TIME]
[LOCATION]

ATTENDANCE
Present: [members]
Absent: [members]
Also Present: [city manager, attorney, secretary, other staff]

CALL TO ORDER
[Presiding officer] called the meeting to order at [time] and confirmed
a quorum was present.

INVOCATION AND PLEDGES OF ALLEGIANCE
[One sentence.]

PUBLIC COMMENT
[Neutral summary, naming speakers and topics. 1–2 paragraphs.]

CONSENT AGENDA
On a motion by [member], seconded by [member], the Council approved the
consent agenda items 4a through 4c. Vote: Ayes — [list]; Nays — none.
Motion carried [N–0].

PUBLIC HEARING — [Item caption]
[Narrative, 2–4 sentences. Note opening of hearing, staff presentation,
public comment received during the hearing, closing of hearing.]
On a motion by ___, seconded by ___, the Council [action]. Vote: Ayes — ___;
Nays — ___; Abstain — ___; Absent — ___. Motion [carried/failed].

REGULAR BUSINESS — [Item caption]
[Same pattern.]

EXECUTIVE SESSION
The Council recessed into executive session at [time] under Tex. Gov.
Code §§ [citations]. The Council reconvened in open session at [time].

ACTION ON EXECUTIVE SESSION ITEMS
[List action(s) taken or note that no action was taken.]

ADJOURNMENT
There being no further business, [presiding officer] adjourned the
meeting at [time].

___________________________________
[Mayor name], Mayor

ATTEST:

___________________________________
[City Secretary name], City Secretary
```

Length: typically 2–5 pages. Tone: neutral, factual, plain. Past tense throughout.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Open Meetings Act (Tex. Gov't Code Ch. 551):**

- § 551.021 — A governmental body shall keep minutes or make a recording of each open meeting.
- § 551.022 — The minutes/recording is a public record.
- § 551.103 — Certified agenda or recording of closed sessions must be maintained for at least two years; this is separate from the open-session minutes and is **not** drafted by this skill. Closed-session content stays in the certified agenda or recording, not the public minutes.

**Public Records (Tex. Gov't Code Ch. 552):** The minutes are a public record once approved by council. Drafts before approval are working papers and may be exempt under § 552.111.

**Retention:** Minutes are permanent under the Texas State Library Local Government Retention Schedule GR, Item 1000-25 (Meeting Minutes).

**Verify before posting:** Vote tallies match members present; speakers' names spelled correctly; statutory citations for executive session match the agenda.

## References

- See `references/roberts-rules-quick-reference.md` for the parliamentary terminology and vote thresholds used in standard motion language.

## Examples

- See `examples/minutes-cedar-ridge-regular.md` for a worked example: minutes for the regular meeting used in the agenda-builder example.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
