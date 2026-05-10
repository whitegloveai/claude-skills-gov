---
name: open-meetings-compliance-checker
description: Reviews a posted Texas city council or governing body agenda against TOMA (Tex. Gov't Code Ch. 551) notice and content requirements and flags issues before posting. Use when a city secretary needs a pre-posting compliance check on agenda timing, subject specificity, executive session citations, and ancillary notices.
---

# Open Meetings Compliance Checker

> Pre-posting review of a Texas governing body agenda against the Texas Open Meetings Act. Built for city secretaries, deputy clerks, and city attorneys clearing an agenda before the 72-hour clock.

## When to Use

- "Run this agenda against TOMA before I post it tomorrow morning."
- "I'm not sure this executive session caption is specific enough. Check it."
- "The mayor added an item at the last minute. Is the timing still compliant?"
- "We have a zoning hearing on this agenda. Did we cover all the ancillary notices?"
- "The city attorney wants a compliance check on the special meeting agenda before posting."
- Any agenda that has not yet been posted and that staff want reviewed under Tex. Gov't Code Ch. 551.

## Inputs Needed

Required:

- Agenda text in full, including header, item captions, and any executive session items
- Intended posting date and time
- Meeting date and time
- Meeting type: regular, special, or emergency
- Governing body (city council, planning and zoning commission, board of adjustment, EDC board, etc.)

Optional:

- City population (drives § 551.056 internet posting obligation, generally for cities with population 48,000 or more)
- Whether the city posts on a physical bulletin board and a website
- Any special-notice items the user is already tracking (zoning, tax rate, budget, bond)
- Notes on items added in the 72 hours before posting

If meeting type or posting time is missing, ask. The compliance windows depend on both.

## Process

1. **Posting timeline check.** Compute the gap between posting time and meeting time. Regular and special meetings require 72 hours under Tex. Gov't Code § 551.043. Emergency meetings require at least 1 hour under § 551.045 with a written supplemental notice and stated emergency. Cities with population 48,000 or more must also post on the city website under § 551.056. Flag any timing gap, holiday-weekend conflict, or missing internet posting.
2. **Subject specificity check.** Test each caption against the § 551.041 subject-notice standard. Flag vague captions ("Discuss city business," "Other matters") and recommend tightened language.
3. **Executive session citation check.** Verify each closed-session item cites a specific § 551.07x exception matching the subject. Common exceptions: § 551.071 (attorney), § 551.072 (real property), § 551.074 (personnel), § 551.076 (security devices), § 551.087 (economic development).
4. **Public comment compliance.** Confirm comment is offered under § 551.007 and that speaker rules are reasonable and viewpoint-neutral.
5. **Special-notice items.** Identify items with ancillary notice obligations: zoning (Tex. Loc. Gov't Code Ch. 211), tax rate (Tex. Tax Code Ch. 26), budget (Tex. Loc. Gov't Code § 102.0065), elections (Tex. Election Code). Note the controlling statute and deadline for each.
6. **Member-requested items.** Confirm any items requested under § 551.041 / § 551.0411 are reflected.
7. **Reconvene language.** If executive session is on the agenda, confirm a clear reconvene-in-open-session item and an action item if action is contemplated.
8. **Posting certification.** Confirm the certification block has placeholders for date, time, and signature.
9. **Pass / Fail summary.** Issue *PASS*, *PASS WITH RECOMMENDED FIXES*, or *FAIL*. For any FAIL, state the issue, citation, and recommended fix.

## Output Format

A compliance review memo, approximately one to two pages, organized by the check categories above. Each finding is keyed to a specific item by number so the user can fix in place.

```
TOMA COMPLIANCE REVIEW — [ENTITY], [MEETING TYPE] [DATE]

Reviewed by: [reviewer]
Review date: [date]
Intended posting: [date / time]
Meeting time: [date / time]

1. Posting timeline check
   [Findings — pass / fail with citation]

2. Subject specificity check
   [Per-item findings, keyed to item number]

3. Executive session citation check
   [Per-item findings]

4. Public comment compliance
   [Findings]

5. Special-notice items
   [List of items that trigger ancillary notice with the controlling
   statute and deadline; confirm each ancillary notice is on track]

6. Member-requested items
   [Findings]

7. Reconvene and action language
   [Findings]

8. Posting certification block
   [Findings]

OVERALL FINDING: [PASS / PASS WITH RECOMMENDED FIXES / FAIL]

Recommended fixes (paste-ready language):
  - Item [N]: replace "[old]" with "[new]" because [citation].
  - [...]

Next steps before posting:
  1. [...]
  2. [...]
```

Tone: factual, neutral, specific. Every finding cites the controlling statute. No editorializing about the substance of the agenda items.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Open Meetings Act (Tex. Gov't Code Ch. 551):**

- § 551.041 / § 551.042 — Subject-notice standard; council may not deliberate or act on non-posted items.
- § 551.043 / § 551.045 — Regular/special meetings 72-hour posting; emergency meetings 1-hour with written supplemental notice.
- § 551.056 — Website posting for cities with population 48,000 or more.
- §§ 551.071–551.090 — Executive session exceptions; each closed item must cite the specific section.
- § 551.007 — Public comment; rules must be reasonable and viewpoint-neutral.

**Ancillary notice statutes commonly on city agendas:** zoning (Tex. Loc. Gov't Code Ch. 211 — mailed 10 days, published 15 days), budget (Tex. Loc. Gov't Code § 102.0065 — 10 days), tax rate (Tex. Tax Code §§ 26.05, 26.06), election (Tex. Election Code Ch. 4).

**Retention:** The posted agenda and posting certification retain permanently under TSLAC Schedule GR, Item 1000-26.

**Verify before posting:** That all ancillary notices have run, that the city attorney has cleared any executive session caption involving litigation, and that the posting certification will be signed at the moment of posting (not pre-signed).

## References

- See the agenda-builder skill's `references/toma-agenda-sections.md` (in the council-ops plugin) for a section-by-section TOMA taxonomy and the executive session exceptions catalog. This skill applies that taxonomy as a compliance check.

## Examples

- See `examples/cedar-ridge-agenda-review.md` for a worked example: a pre-posting review of the Cedar Ridge City Council June 9, 2026 regular meeting agenda referenced in the agenda-builder example. Result: pass with two recommended fixes (a specificity tightening on a regular business item and a citation correction in the posting block).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
