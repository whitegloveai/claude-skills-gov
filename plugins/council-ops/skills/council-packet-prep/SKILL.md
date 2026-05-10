---
name: council-packet-prep
description: Assembles a city council packet from a posted agenda — drafts the cover memo, attachment index, and packet completeness checklist. Use when the city manager's office or city secretary is preparing the packet for council and needs a single artifact that ties agenda items to required attachments.
---

# Council Packet Prep

> Drafts the cover memo, attachment index, and a completeness checklist for a council packet. Built for city manager's office staff who assemble packets the Friday before a Tuesday meeting and need to know nothing is missing.

## When to Use

- "We have the agenda for next Tuesday — build me the packet cover memo and index."
- "Run a completeness check on the June 9 packet before I send it to council."
- "Draft the cover memo from the City Manager for this packet."
- "What attachments should be in this packet given the agenda?"
- The city secretary is finalizing the packet and wants the cover materials in standard format.

## Inputs Needed

Required:

- The posted (or near-final) agenda
- List of agenda items that require packet support, with item type for each (contract, zoning, budget, public hearing, resolution, ordinance, appointment, report, etc.)
- Known attachments and their preparers (e.g., "Item 5b: P&Z staff report — Planning Director Okafor")
- City Manager name (signs the cover memo)

Optional:

- Page-numbering plan if the city uses paginated packets (cover memo is page 1; attachments follow)
- Distribution list (council members, mayor, city manager, attorney, secretary, web posting)
- Any time-sensitive items the City Manager wants flagged in the cover memo

## Process

1. Read the agenda. Note which items need packet support and which are routine (e.g., adjournment doesn't).
2. For each agenda item that needs support, identify the standard attachments based on item type. Use `references/standard-packet-attachments.md`.
3. Draft the cover memo: from the City Manager to the Mayor and Council, dated the Friday before the meeting, summarizing the agenda and flagging items that warrant attention.
4. Build the attachment index: a table mapping Item # → packet pages → attachment description → preparer.
5. Run the completeness checklist: for each item type, verify required attachments are present. Flag any gap as an Outstanding Item.
6. Note items that require statutory notice attachments (zoning notice, budget notice, tax rate notice) — those notices belong in the packet so council can verify compliance.
7. Note items where the City Attorney has not signed off — flag as a blocker.
8. Format the output so the City Secretary can copy-paste it as the front matter of the packet.

## Output Format

Three sections in order:

1. **Cover memo** (City Manager to Mayor and Council)
2. **Attachment index** (table)
3. **Packet completeness checklist** with any Outstanding Items

```
TO:        Mayor [Name] and Members of the City Council
FROM:      [Name], City Manager
DATE:      [Friday before meeting]
SUBJECT:   [Meeting type] — [Meeting date]

The packet for the [DATE] [meeting type] is attached. Total pages: [N].

ITEMS WARRANTING ATTENTION
[2–4 bullet points highlighting the most consequential items.]

CHANGES SINCE THE AGENDA WAS POSTED
[Any item updates, withdrawn items, supplements, or material changes.
"None" if there are none.]

EXECUTIVE SESSION NOTE
[Reminder of the executive session topics and any preparatory materials
included separately.]

I am available before the meeting if any member would like to discuss
any item.

ATTACHMENT INDEX

Item #   Pages    Description                                    Preparer
[6a]     [21–34]  [Memo, bid tabulation, draft contract, ...]    [Name]
...

PACKET COMPLETENESS CHECKLIST

[Item Type]      Required Attachments        Present?    Notes
Contract         Memo + redlined contract    Yes / No    [...]
Zoning           Staff report + plat + ...   Yes / No    [...]

OUTSTANDING ITEMS
- [Item] — Owner: [Name] — Due: [Date]
- [Item] — Owner: [Name] — Due: [Date]

[If no outstanding items: "Packet is complete."]
```

Length: cover memo half a page; index 1–2 pages; checklist half a page.

Tone: businesslike, neutral, brief. The City Manager's voice in the cover memo is professional and direct.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Open Meetings Act (Tex. Gov't Code Ch. 551):** The packet does not substitute for the posted agenda. The agenda, not the packet, controls the legal scope of items the council may consider.

**Public Records (Tex. Gov't Code Ch. 552):**

- Items in the packet are public records once distributed to council, even before the meeting. Many cities post the packet on the website at the same time as the agenda.
- Some cities maintain certain packet attachments as confidential (executive session memos, personnel files, attorney-client privileged memos under § 552.107). These should not be in the public packet — they go in a separate executive session packet.
- Items submitted by individuals (e.g., applicant materials in a zoning case) may include personal information; redaction may be required under § 552.117 (peace officer addresses) or § 552.130 (driver's license numbers) before public posting.

**Retention:** Adopted council packets are part of the meeting record and retain permanently with the minutes (Texas State Library Local Government Retention Schedule GR, Item 1000-25 / 1000-26).

**Attorney-client privilege:** Memos prepared by the City Attorney specifically for executive session deliberation should NOT be in the public packet. Route them separately to council under cover of a privileged memo.

## References

- See `references/standard-packet-attachments.md` for a by-item-type list of required and recommended packet attachments, including statutory drivers.

## Examples

- See `examples/cedar-ridge-packet-cover.md` for a worked example: cover memo and attachment index for the same Cedar Ridge regular meeting used in the agenda-builder example.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
