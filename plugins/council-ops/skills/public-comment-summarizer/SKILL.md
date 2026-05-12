---
name: public-comment-summarizer
description: Condenses a city council public comment session into a neutral, public-records-safe summary for the meeting record. Use when a clerk or council aide needs to convert raw comment transcripts or notes into a summary suitable for inclusion in minutes or a packet.
---

# Public Comment Summarizer

> Produces a neutral, factual summary of public comment that holds up as part of the public record. Built for clerks and aides who need a usable record without editorializing or chilling speech.

## When to Use

- "Summarize last night's public comment for the minutes."
- "We had 14 speakers at the budget hearing — give me a clean summary by topic."
- "Draft a summary of public comment from the rezoning hearing for the staff report."
- "I need a one-page summary of the comments on the short-term rental ordinance."
- The clerk is preparing a record where the full transcript is too long but speaker substance must be preserved.

## Inputs Needed

Required:

- The meeting context: which meeting, which item(s) the comment relates to
- Source material: a transcript, a list of speaker registration cards with notes, or a recording summary
- List of speakers (names as registered, in the order they spoke)

Optional but improves accuracy:

- Each speaker's stated topic from the registration card
- Time each speaker began (helpful when cross-referencing recording)
- Whether the speaker indicated for, against, or neutral on a specific posted item
- Any written comments submitted that should be referenced

If speaker names are missing or partial, ask. Public comment is part of the public record — names matter.

## Process

1. Read the source material end to end before drafting. Note the dominant themes.
2. Group comments by topic where possible. If 6 of 10 speakers addressed the budget and 4 addressed unrelated matters, the summary follows that structure.
3. For each topic, write a short paragraph that conveys the substance of what speakers said. Use neutral verbs (*stated*, *expressed*, *raised*, *requested*, *opposed*, *supported*) — not characterizing verbs (*ranted*, *complained*, *attacked*).
4. Where speakers identifiably took a position on a posted item, include a count: "Of [N] speakers on Item 5b, [X] expressed support, [Y] opposed, and [Z] did not state a position."
5. Use direct quotation only when a single phrase is essential to convey the substance and paraphrase would distort it. Keep quotes under 20 words.
6. Do not characterize the speaker's tone, motive, or state of mind. The record reports what was said, not how it landed.
7. Note any procedural events (a speaker yielding time, the chair calling time, requests for translation, written submissions filed during the period).
8. Close with a line stating that the full recording is available under the city's public records policy.

## Output Format

Plain markdown, suitable to be pasted into minutes or a staff report. Length: typically half a page to one page.

```
PUBLIC COMMENT SUMMARY
[Meeting type and date]

Total speakers registered: [N]
Total speakers heard: [N]
Written comments submitted: [N]

By Topic:

[Topic 1] ([N] speakers)
[2–4 sentence neutral summary of the substance.]

[Topic 2] ([N] speakers)
[Same pattern.]

Position Counts on Posted Items:

  Item [X]: [N] in support, [N] in opposition, [N] no stated position.

Procedural Notes:
[Any time-keeping, translation requests, written submissions, or
yielded time.]

Speakers (in order heard):
1. [Name], [registered topic]
2. [Name], [registered topic]
...

The full recording of the public comment period is retained under the
City's records management program and is available through the City
Secretary's office under Tex. Gov't Code Ch. 552.
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**First Amendment / Viewpoint Neutrality:** A summary that selectively omits or characterizes speakers based on their viewpoint can chill speech and create legal exposure. Treat all speakers' substance evenhandedly. If one speaker is summarized in two sentences, opposing speakers should not be summarized in half a sentence.

**Texas Open Meetings Act (Tex. Gov't Code § 551.007):** The Council may not deliberate or take action on items raised during public comment that are not on the agenda. The summary is part of the meeting record but the comments themselves do not authorize council action.

**Public Records (Tex. Gov't Code Ch. 552):** Speaker names and the substance of their public comments are public records. The summary itself is a public record once filed in the meeting record. Speakers who provide an address from the dais provide it knowingly; the city should not redact addresses given in open meeting unless the speaker is in a protected class (judge, peace officer) under Tex. Gov't Code § 552.117 — even then, the original recording reflects what was said.

**Retention:** Public comment summaries included in approved minutes are permanent. Speaker registration cards are typically retained 2 years (Texas State Library Local Government Retention Schedule GR, Item 1000-26 series).

**Plain language and accessibility:** The summary should be readable at roughly an 8th-grade level so it serves the public, not just lawyers.

## Examples

- See `examples/budget-hearing-comments.md` for a worked example: summary of public comment at a FY26 budget hearing with 6 speakers across four topics.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
