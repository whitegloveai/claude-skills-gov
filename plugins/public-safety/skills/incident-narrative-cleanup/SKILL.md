---
name: incident-narrative-cleanup
description: Restructures and copy-edits an officer, EMT, or firefighter incident narrative into a clean chronological report without altering facts. Use when a peace officer, paramedic, or fire officer needs help producing a grammatically sound, well-organized narrative for a Texas agency report, with a reviewer-notes section that flags internal contradictions, missing checklist items, and weak phrasing the author can address before submission.
---

# Incident Narrative Cleanup

> Cleans up grammar, structure, and completeness of a sworn incident narrative without changing what the author wrote. The officer's facts and voice are sovereign; this skill is a copy editor.

## When to Use

- "Run my narrative through the cleanup. Don't change what I said."
- "I wrote this at 0300, please tighten it up before I submit."
- "Flag anything that looks inconsistent so I can fix it myself."
- An officer, EMT, or firefighter has drafted a raw narrative and needs structural and grammatical review before the report is finalized in the records management system.
- A supervisor wants a consistency check on a subordinate's narrative before approval, with flags rather than rewrites.
- The narrative will be used in a TPIA release, a deposition, or a grand jury presentation, and must read cleanly while preserving the author's substance.

## Inputs Needed

Required:

- The author's raw narrative, in full, exactly as written.
- Incident type (burglary, MVA, structure fire, EMS run, mental health call, etc.).
- Agency report template or completeness checklist (Cedar Ridge PD uses initial response, observations, actions, statements, evidence, disposition).

Optional:

- Statute framing (e.g., Tex. Penal Code § 30.02 for burglary), so reviewer notes can flag missing elements without inserting them.
- Known recipients (prosecutor, civil discovery, internal affairs) so reviewer notes can prioritize testimony-critical fixes.
- BWC or CAD timestamps if the author wants consistency checked (the skill flags discrepancies; it does not edit the author's stated times).

If the author has not provided the raw narrative in full, ask for it. Do not work from a summary.

## Process

1. Read the raw narrative end to end before editing. Identify the author's voice and terminology. Preserve them.
2. Reorder into chronological structure: Initial Response, Observations, Actions Taken, Statements, Evidence Collected, Disposition. Reordering is permitted only when meaning is preserved; if ambiguous, leave it and flag.
3. Copy-edit for grammar, spelling, and punctuation. Replace passive voice only where the subject is unambiguous. Do not invent a subject.
4. Replace vague phrases with the author's specific facts stated elsewhere in the narrative. If the fact is not present, flag the vagueness.
5. Standardize times (24-hour clock), names (Last, First), and addresses, using exactly what the author wrote. Do not change a name's spelling.
6. Identify internal contradictions in dates, times, names, vehicles, sequence of events. Do not resolve. Flag with conflicting passages quoted.
7. Identify missing checklist items for the agency template and incident type. Flag as gaps.
8. Identify phrasing that would weaken testimony: hedge words, conclusory statements without observational support, characterizations that read as opinion. Flag, do not delete.
9. Produce a "Cleaned Narrative" and a "Reviewer Notes" section. The reviewer notes are working notes for the author and do not appear in the submitted report.

## Output Format

Plain markdown. Two distinct sections. The cleaned narrative reads as a submittable report; the reviewer notes are working-paper marginalia for the author.

```
CLEANED NARRATIVE — [Case number] — [Date of incident]
Author: [Rank Last name, badge]
Reviewing structure (not facts): AI-assisted cleanup, [date]

INITIAL RESPONSE
[Dispatch information, arrival time, weather/light conditions if author noted
them, scene description on arrival.]

OBSERVATIONS
[Author's observations on arrival, in chronological order, with author's
specific facts preserved.]

ACTIONS TAKEN
[Numbered chronological steps the author took, in the author's words,
tightened for grammar.]

STATEMENTS
Witness 1 — [Name, Last, First; DOB]
[Author's record of the statement, in the author's words.]

Witness 2 — [Name]
[Author's record.]

Suspect — [Name]
[Author's record, with Miranda notation if the author included it.]

EVIDENCE COLLECTED
[List, with item numbers and chain-of-custody notations the author provided.]

DISPOSITION
[Author's stated disposition, charges if filed, transport, referral.]

---

REVIEWER NOTES (NOT FOR SUBMISSION)

Internal contradictions:
- [Quoted passage 1] conflicts with [Quoted passage 2]. Author should
  resolve before submission.

Possible missing checklist items:
- [Item from agency template, not found in narrative].

Phrasing that could weaken testimony:
- [Quoted phrase] reads as conclusory; consider restating with the
  underlying observation.

Spelling and grammar corrections applied:
- [Brief log so the author can verify nothing of substance was changed.]

AI-assisted cleanup, reviewed by [author rank and name].
```

Length: cleaned narrative tracks the raw input. Reviewer notes are 100 to 400 words.

Tone: matches the author's tone. Reviewer notes are neutral and specific.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Substance is sovereign:** This skill must not add facts, remove facts, or reorder chronology in a way that changes meaning. The author retains sole authority over substance and is responsible for verifying nothing material changed before submission.

**Public records (Tex. Gov't Code Ch. 552):** The final narrative is a public record subject to TPIA with the law enforcement carve-outs under § 552.108. Working drafts and reviewer notes may be exempt under § 552.111 until the report is finalized. Reviewer notes should not be retained in the case file.

**Brady, Giglio, impeachment:** Reviewer-notes flags about hedges, conclusory statements, or contradictions give the author the chance to fix issues defense counsel will exploit on cross-examination under *Brady v. Maryland* and *Giglio v. United States*. The skill surfaces issues; it does not erase them.

**Civil service:** Tex. Loc. Gov't Code Ch. 143 and Tex. Gov't Code Ch. 614 procedures apply to discipline arising from report deficiencies. Reviewer notes are not a finding.

**Retention:** Incident reports retain under the Texas State Library Local Government Retention Schedule PS, generally five years or longer depending on offense and disposition.

## References

- See `references/report-writing-checklist.md` for a section-by-section completeness checklist tied to common Texas Penal Code offenses, EMS run-report fields, and NFIRS fire-incident reporting categories.

## Examples

- See `examples/burglary-narrative-cleanup.md` for a Cedar Ridge PD burglary narrative authored by Officer J. Holloway, with the raw narrative, the cleaned narrative, and reviewer notes flagging two minor inconsistencies for the officer to resolve before RMS submission.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
