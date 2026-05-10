---
name: social-media-municipal-style
description: Drafts platform-tailored social media posts in a neutral, public-records-safe municipal voice with what-not-to-post guardrails. Use when a PIO, communications coordinator, or department social media account owner needs posts for a city announcement, event, or service notice across Facebook, X/Twitter, Instagram, LinkedIn, or Nextdoor.
---

# Social Media — Municipal Style

> Drafts platform-tailored posts in a neutral municipal voice that holds up under public records requests and avoids the most common political and legal pitfalls. Built for PIOs and the staff who run the city's social accounts.

## When to Use

- "Draft Facebook and Twitter posts about the road closures starting next week."
- "Need an Instagram post for the library's summer reading kickoff."
- "Nextdoor post about the boil-water notice — I need it conservative."
- "LinkedIn post announcing the new finance director."
- "Three platform variations on the Fire Station #3 groundbreaking."
- A press release just went out and the social team needs aligned post-outs.
- A service disruption, road closure, or weather event requires rapid platform-specific posts.

## Inputs Needed

Required:

- Topic in one sentence
- Platform(s) requested: Facebook, X/Twitter, Instagram, LinkedIn, Nextdoor (request more than one if cross-posting)
- Urgency: routine, time-sensitive, or urgent
- Audience: general public, parents, business community, residents in a specific area
- Tone target: informational, celebratory, cautionary, somber

Optional:

- Press release the post should align with
- Suggested image type or asset on hand
- Hashtag policy or campaign hashtags
- Posting schedule preference (single post vs. recurring cadence)
- Contested-topic flag (rezoning, rate adjustments, controversial votes) — triggers extra neutrality and the "what NOT to post" callout

If the platform list, audience, or topic is unclear, ask before drafting. Do not draft posts about contested matters without confirming the city's adopted position or neutral framing.

## Process

1. Confirm platforms requested and the urgency level.
2. Identify any contested-topic flags (election season, pending litigation, rate adjustments, personnel matters, officer-involved incidents). For flagged topics, route to the talking-points-writer skill first and use this skill only for the neutral announcement post.
3. Draft 2–3 variations per requested platform within each platform's character and format conventions.
4. Pair each post with: recommended image type (or "no image / text-only"), hashtag set, and a suggested posting time window.
5. Add a "What NOT to Post" callout for the topic — explicit guardrails for what could create liability, public records exposure, or political risk.
6. If part of a series (multi-week road project, multi-day event, ongoing service disruption), suggest a posting cadence.
7. Apply the municipal voice guardrails in `references/municipal-voice-tone-guide.md` — neutrality, no endorsements, no in-thread defamation responses, public records awareness.

## Output Format

Plain markdown. One block per platform. No emoji unless the city's brand voice permits (use sparingly even then).

```
TOPIC: [One-line summary]
URGENCY: [Routine / Time-sensitive / Urgent]
ALIGNED WITH: [Press release or other source, if any]

---

FACEBOOK (post limit ~63,206 chars; practical 100–300 words)

Variation 1:
[Post text]
Image recommendation: [type]
Hashtags: [#cedarridgetx #cityservices etc.]
Suggested time: [day / time window]

Variation 2: [...]

---

X / TWITTER (280 chars)

Variation 1:
[Post text + URL]
Image recommendation: [type]
Hashtags: [in-line within char limit]
Suggested time: [...]

Variation 2: [...]

---

INSTAGRAM (caption practical 125–250 words; visual-first)

Variation 1:
[Caption]
Image / carousel recommendation: [type]
Hashtags: [end of caption, 5–10 max]
Suggested time: [...]

---

LINKEDIN (1,300–3,000 chars; professional audience)

Variation 1:
[Post text]
Image recommendation: [type]
Suggested time: [weekday mornings]

---

NEXTDOOR (no character limit; neighborhood audience)

Variation 1:
[Post text — Nextdoor reads more like a neighbor-to-neighbor note than
a broadcast post. Lead with what residents need to know.]
Suggested time: [...]

---

POSTING CADENCE (if applicable)
[Recommended schedule across the campaign window]

---

WHAT NOT TO POST
- [Guardrail 1 — specific to this topic]
- [Guardrail 2]
- [Guardrail 3]
- [Always: do not respond to defamatory comments in-thread; document
  and route to legal if needed]

Drafted with AI assistance, reviewed by [Name, Title] before posting.
```

Tone: neutral, civically appropriate, plain. Department voice may vary slightly (Library can be warmer; Police is more neutral; Fire is reassuring; Public Works is operational). Across all platforms: no superlatives, no editorializing, no endorsement language.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Public records — social media is records:** Posts, comments, DMs, and moderation actions on official accounts are public records under Tex. Gov't Code Ch. 552, retained per Texas State Library Local Government Retention Schedule (GR 1050-26). Use an archiving tool (ArchiveSocial, Hootsuite, Smarsh) for all official accounts. Deletion of citizen comments may raise First Amendment forum concerns (*Davison v. Randall*, *Lindke v. Freed*).

**First Amendment forum doctrine:** Official accounts that allow comments likely create a limited public forum. Viewpoint-based comment removal or user blocking is risky. The adopted moderation policy should govern every action; document each one.

**Political activity:** Do not endorse candidates or use city accounts for partisan messaging. The federal Hatch Act may apply to employees in federally funded positions. Tex. Elec. Code § 255.003 prohibits use of public funds for political advertising.

**Defamation:** Do not respond to allegedly defamatory comments in-thread. Screenshot, preserve in archive, route to the City Attorney. Do not delete unless moderation policy authorizes.

**ADA accessibility:** Provide alt text on every image. Use camelCase hashtags (#CedarRidgeTX) so screen readers parse correctly. Reviewed transcripts or burned-in captions on video.

**Bilingual posts:** For jurisdictions with significant Spanish-speaking populations (5% or greater LEP), publish parallel Spanish posts. Cedar Ridge-style cities should treat bilingual posts as default for service-critical announcements.

**Crisis posts:** Do not use this skill alone for crisis comms. Use crisis-comms-template for holding statements and updates.

## References

- See `references/municipal-voice-tone-guide.md` for municipal voice guardrails: endorsement avoidance, neutrality on contested council matters, defamation handling, public records implications under Tex. Gov't Code Ch. 552, and escalation criteria to legal.

## Examples

- See `examples/street-overlay-road-closures.md` for a worked example: three platform-tailored post variations announcing road closures for the Cedar Ridge street overlay project, with recommended weekly posting cadence during construction.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
