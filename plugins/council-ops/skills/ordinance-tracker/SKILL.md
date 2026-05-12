---
name: ordinance-tracker
description: Creates and maintains a tracking record for a proposed Texas city ordinance through introduction, public hearings, two readings, and codification. Use when a city secretary or council aide needs a single source of truth for where an ordinance stands and what's needed next.
---

# Ordinance Tracker

> Produces a one-page tracking record for a proposed ordinance and updates it as the ordinance moves through the legislative process. Built for clerks who manage 20+ ordinances at once and need to know what's outstanding without flipping through emails.

## When to Use

- "Create a tracker for the new short-term rental ordinance."
- "Update the tracker on the tree preservation ordinance — first reading happened last night."
- "What's the status of every pending ordinance heading into the August agenda?"
- "Build me the tracking record for Ord. 2026-22."
- A new ordinance is being introduced and the clerk wants the tracking record set up before the first packet.

## Inputs Needed

Required:

- Ordinance title (working title is fine before assignment)
- Ordinance number (or "TBD")
- Sponsoring council member or department
- Brief summary of effect (one paragraph)
- Type: zoning, budget/financial, regulatory, organizational, or other (this drives the procedural requirements)
- Key dates known to date

Optional but improves accuracy:

- Charter requirements specific to this city (some home-rule charters require two readings; some require publication after passage; emergency ordinances often need a supermajority)
- Statutory requirements specific to the ordinance type (zoning hearings under LGC Ch. 211, budget under LGC Ch. 102, impact fees under LGC Ch. 395, etc.)
- Any companion resolutions or interlocal agreements
- Department leads and the City Attorney's review status

## Process

1. Identify the ordinance type. The procedural checklist depends on it. Zoning, budget, tax-related, and impact-fee ordinances each have their own statutory requirements; general regulatory ordinances follow the city's charter.
2. Build the initial tracking record with sections: Status, History, Outstanding Items, Next Required Action, Statutory References, Related Documents.
3. For Status, use one of these states: Drafting, Introduced, First Reading Scheduled, First Reading Passed, Public Hearing Scheduled, Public Hearing Held, Second Reading Scheduled, Adopted, Effective, Codified, Failed, Withdrawn.
4. For History, record each event in chronological order with a date and a one-line description. Never delete history — only append.
5. For Outstanding Items, list every action that must occur before the next status change, with the responsible party.
6. For Next Required Action, name the single most-immediate action and its deadline.
7. For Statutory References, list the controlling statutes for the ordinance type and any procedural deadlines (e.g., zoning notice 10 days before hearing, budget notice as required by Local Gov. Code § 102.0065).
8. For Related Documents, list packet memos, staff reports, public notices, and any companion resolutions with their dates.
9. When updating, append to History; revise Outstanding Items, Next Required Action, and Status.

## Output Format

Plain markdown, one page in length, suitable to be saved as a standing file the clerk updates over weeks.

```
ORDINANCE TRACKER — [TITLE]

Ordinance Number:        [number or TBD]
Type:                    [zoning / budget / regulatory / organizational / other]
Sponsor:                 [council member or department]
Status:                  [current state]
Date Introduced:         [date]
City Attorney Review:    [Not started / Pending / Approved as to form]

SUMMARY OF EFFECT
[One paragraph, plain language. Who or what is affected, and how.]

HISTORY
[YYYY-MM-DD] — [Event] — [Brief detail]
...

OUTSTANDING ITEMS
- [Item] — Owner: [Name/Role] — Due: [Date]
- [Item] — Owner: [Name/Role] — Due: [Date]

NEXT REQUIRED ACTION
[The single most-immediate action and its deadline.]

STATUTORY REFERENCES
- [Citation] — [What it requires]
- [Citation] — [What it requires]

RELATED DOCUMENTS
- [Document] — [Date] — [Location/packet reference]
- [Document] — [Date] — [Location/packet reference]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Procedural compliance varies by ordinance type:**

- **Zoning (Tex. Loc. Gov't Code Ch. 211):** Notice 15 days before P&Z hearing, mailed notice to property owners within 200 ft, three-fourths affirmative vote required if ≥20% of property owners protest under § 211.006(d).
- **Budget (Tex. Loc. Gov't Code Ch. 102):** Public hearing required before adoption; notice published per § 102.0065.
- **Tax rate (Tex. Tax Code Ch. 26):** Specific notice and hearing requirements when rate exceeds the no-new-revenue rate or the voter-approval rate.
- **Impact fees (Tex. Loc. Gov't Code Ch. 395):** Capital improvements plan, advisory committee, public hearing.
- **Annexation (Tex. Loc. Gov't Code Ch. 43):** Service plan, hearings, notice requirements.
- **Emergency ordinances:** Charter-specific; many home-rule charters require a supermajority and a written finding of emergency.
- **Two readings:** Many home-rule charters require two readings before adoption. General-law cities follow Tex. Loc. Gov't Code Title 2 procedures.

**Public Records (Tex. Gov't Code Ch. 552):** The tracker, once distributed in a packet or beyond a working group, is a public record. Drafts within a working group may be exempt under § 552.111.

**Retention:** Adopted ordinances retain permanently (Texas State Library Local Government Retention Schedule GR, Item 1000-23). Working files for unadopted ordinances retain 2 years after final disposition.

**Codification:** Once an ordinance is adopted, the city's code publisher (commonly Municode or American Legal) needs the certified ordinance to integrate into the code. Track the codification step in History.

## References

This skill does not require a separate reference file; the SKILL.md captures the procedural framework. Reference the agenda-builder skill's `toma-agenda-sections.md` for posting requirements when the ordinance comes up at a meeting.

## Examples

- See `examples/tree-preservation-ordinance.md` for a worked example: tracking record for a tree preservation ordinance from introduction through adoption.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
