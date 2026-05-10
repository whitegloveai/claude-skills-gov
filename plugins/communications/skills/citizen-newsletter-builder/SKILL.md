---
name: citizen-newsletter-builder
description: Drafts a monthly or quarterly citizen newsletter with cover note, council-decision recap, upcoming events calendar, departmental highlights, and contact sidebar. Use when a PIO, city manager's office, or communications coordinator needs to assemble the recurring city newsletter for distribution by mail, email, or web post.
---

# Citizen Newsletter Builder

> Drafts a citizen newsletter with section structure, calls to action, and recurring layout. Built for communications staff producing the city's regular touchpoint with residents.

## When to Use

- "Draft the July citizen newsletter. Council just adopted the budget."
- "Build the Q3 newsletter for the utility-bill mail insert."
- "I have department updates. Pull them into a newsletter."
- "Draft the post-election newsletter recapping the bond vote."
- "Need a special edition on the water restrictions."
- A scheduled monthly or quarterly newsletter is due.
- A milestone event warrants a special edition.

## Inputs Needed

Required:

- Period (e.g., "July 2026" or "Q3 FY2026")
- Distribution channel(s): utility bill insert, email, website, mailed copy, social media post-out
- Council decisions to recap (titles, dates, outcomes — drawn from the prior meeting's minutes or agenda)
- Upcoming events list with dates, times, locations
- Departmental updates received from each department (raw bullets are fine; the skill structures them)

Optional:

- Mayor or city manager column topic for the cover note
- Featured project (capital improvement, grant award, recognition)
- Recurring sections to include (budget update, code reminder, public safety tip, water conservation, severe weather prep)
- Bilingual flag for Spanish summary box
- Page-count target (typical: 4 pages for utility-bill insert; 6–8 pages for mailed edition)

If the period, channel, or departmental updates are missing, ask before drafting. Do not invent council decisions or quantitative results.

## Process

1. Confirm the period, distribution channel, and target page count.
2. Draft the cover note (mayor's or city manager's column) — 200–300 words, conversational, no editorializing on contested matters, signed by the named official.
3. Build the "What Council Decided" recap — bulleted list of actions from the last meeting(s) with a one-line description per item and the date. Reference ordinance, resolution, or contract numbers when available.
4. Build the "Coming Up" calendar — chronological list of public meetings, hearings, deadlines, and events for the period ahead. Include date, time, location, and a one-line note on what residents need to know.
5. Pull departmental highlights into 50–100 word blocks each, in a consistent order (public works, parks, library, public safety, finance, planning). Use raw department bullets as source material; do not embellish.
6. Insert recurring sections as needed (see `references/municipal-newsletter-section-templates.md`).
7. Add the "How to Reach Us" sidebar — main phone, after-hours line, online portal URLs, social handles, ADA accommodation note.
8. Add Spanish summary box if jurisdiction policy calls for bilingual.
9. Place the AI-assistance notation in the colophon if city policy adopts it.

## Output Format

Plain markdown structured for layout staff to typeset, or for direct paste into the city's CMS or email template. No emoji unless the city's adopted brand voice permits.

```
[CITY NAME] CITIZEN NEWSLETTER
[Period — e.g., July 2026]

FROM THE CITY MANAGER / MAYOR
[200–300 word column. Plain, civically appropriate. Sign-off:
[Name], [Title]]

WHAT COUNCIL DECIDED
At the [date] regular meeting, the Cedar Ridge City Council:
- [Action 1 — short description, vote count if contested]
- [Action 2]
- [Action 3]
Full minutes and meeting video are available at [URL].

COMING UP
[Chronological list. Format: Date — Event — Location — One-line note.]

DEPARTMENTAL UPDATES

PUBLIC WORKS
[50–100 words on operations, projects, service notes.]

PARKS AND RECREATION
[50–100 words on programs, facilities, registration.]

LIBRARY
[50–100 words on programming, hours, collections.]

PUBLIC SAFETY
[50–100 words on community engagement, safety reminders.]

FINANCE AND ADMINISTRATION
[50–100 words on budget, utility billing, transparency.]

PLANNING AND DEVELOPMENT
[50–100 words on permits, projects, public hearings.]

[FEATURED PROJECT OR PROGRAM]
[150–250 word feature on a capital project, grant, or program.]

[RECURRING SECTION — choose from template library]

EN ESPANOL
[Optional 150-word Spanish summary of the issue's main points.]

HOW TO REACH US
City Hall: [phone] | [hours]
After-hours emergency: [phone]
Online portal: [URL]
[Social media handles]
ADA accommodations: [phone/email and 48-hour notice request]

[Colophon: published by, edition number, "AI-assisted draft, reviewed
by [Name, Title]" if city policy adopts the notation.]
```

Length: typically 1,500–3,000 words depending on format. Utility-bill inserts run shorter; mailed editions longer.

Tone: warm-neutral, civically appropriate, accessible to an 8th-grade reading level. Concrete numbers and dates over adjectives.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Accuracy and verification:** The "What Council Decided" section is the highest-risk part. Cross-check against the official minutes (council-ops minutes-drafter), not staff recollection. Vote counts and dollar amounts must be verified before publication.

**ADA accessibility:** Online newsletters must meet WCAG 2.1 AA. PDFs should be tagged with proper reading order, headings, and alt text. Mailed editions should use at least 12-point body type. Provide a large-print version on request.

**Spanish translation:** For jurisdictions with significant Spanish-speaking populations (5% or greater LEP under DOJ guidance), include a Spanish summary box at minimum. Cedar Ridge-style cities with ~30% Spanish-speaking households should publish a fully bilingual edition.

**Plain language:** Target 8th-grade reading level. Spell out acronyms on first use. Replace bureaucratese with plain verbs. Use specific dollar amounts and dates, not "significant investment" or "in the near future."

**Political neutrality:** A municipal newsletter is not a campaign vehicle. The mayor's or manager's column may share priorities and gratitude, but should not endorse, criticize, or position the city on contested partisan questions. Election-period editions should be reviewed against Tex. Elec. Code § 255.003 prohibitions on use of public funds for political advertising.

**Public records:** The published newsletter is a public record under Tex. Gov't Code Ch. 552. Drafts may be exempt under § 552.111 until published. Reader feedback is also a public record.

## References

- See `references/municipal-newsletter-section-templates.md` for reusable 50–100 word boilerplate templates for: budget update, capital project update, code enforcement reminder, public safety tip, water conservation tip, and severe weather prep.

## Examples

- See `examples/cedar-ridge-july-2026-newsletter.md` for a worked example: the City of Cedar Ridge July 2026 newsletter (post-budget-adoption issue) with manager column, council decisions from the June 9 meeting, street overlay project update, and parks summer programming.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
