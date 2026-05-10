---
name: audit-response-helper
description: Drafts management responses to external audit findings (independent financial audit, Single Audit, or state audit) for inclusion in the audit report or follow-up letter. Use when a finance director, controller, or department head must respond to a draft finding with a concur/disagree statement, corrective action plan, timeline, and responsible person.
---

# Audit Response Helper

> Drafts the management response to an external audit finding. Built for finance staff under deadline to return responses to the external auditor before the audit report is finalized.

## When to Use

- "Draft the management response to this draft audit finding on travel reimbursement controls."
- "We have a Single Audit compliance finding on Davis-Bacon documentation — write the corrective action plan."
- "Convert this auditor finding into a concur-with-comment management response."
- "Draft the response to the state audit recommendation on procurement."
- "Write the corrective action plan for the bank reconciliation finding from FY2025."
- An external auditor has issued a draft finding under GAAS, GAGAS, or the Uniform Guidance, and the finance director has a deadline to return management responses before the report goes final.

## Inputs Needed

Required:

- Audit type: independent financial audit, Single Audit under 2 C.F.R. Part 200 Subpart F, state audit (SAO), or risk-pool agreed-upon procedures
- The verbatim finding text (Condition, Criteria, Cause, Effect, Recommendation as the auditor wrote it)
- Finding category: material weakness, significant deficiency, control deficiency, compliance, questioned cost, other matter
- Department or function (e.g., Finance, HR, Police, a specific federal program)
- Root cause assessment from the department (what actually happened)
- Proposed corrective action with realistic dates
- Responsible person (name and title) and the implementation owner

Optional:

- Prior-year status if this is a repeat finding
- Auditor-provided dollar amount of questioned cost (Single Audit findings only)
- Federal program identifying information: Assistance Listing number, federal awarding agency, pass-through entity, award identifying number
- Whether the finding will trigger a corrective action plan submission to the federal agency

If the user has not provided the verbatim finding text or the proposed corrective action, ask before drafting.

## Process

1. Identify the audit framework. GAAS findings accept a narrative response; Single Audit findings under 2 C.F.R. § 200.512(b) require structured response elements; state audits often dictate a template.
2. Read the finding carefully. Condition–Criteria–Cause–Effect–Recommendation is the spine the response should answer.
3. Decide the response position: *concur*, *concur with comment*, or *disagree* (rare; reserved for factual errors and routed through a partner-level conversation first).
4. Draft the Response section. Three to five sentences. Acknowledge the condition, state the position, reference the corrective action.
5. Draft the Corrective Action Plan. Each action has a deliverable, a responsible person, and a target date. Avoid "we will consider."
6. Draft the Implementation Timeline. Calendar dates, not "Q3."
7. Draft the Responsible Person line. Name, title, one alternate. Required for Single Audit responses.
8. Draft Preventive Controls. The control that will be added or strengthened. A finding without a control change usually repeats next year.

## Output Format

Plain markdown response, one block per finding. Tone: direct, factual, no defensiveness. The reader is the audit partner finalizing the report.

Length: 200 to 500 words per finding. Structure for Single Audit findings (required elements at 2 C.F.R. § 200.512(b)):

```
MANAGEMENT RESPONSE — FINDING [#]

Finding Reference: [Auditor-assigned number, e.g., 2025-001]
Type: [Material Weakness / Significant Deficiency / Compliance / Other]
Federal Program (if applicable): [Name; Assistance Listing #;
  Awarding Agency; Pass-through Entity; Award ID]
Questioned Cost (if any): $[amount]
Repeat Finding: [Yes — prior year reference / No]

Response Position: [Concur / Concur with Comment / Disagree]

RESPONSE

[3–5 sentences. Acknowledge condition, state position, reference
corrective action.]

CORRECTIVE ACTION PLAN

[Action 1 — what will be done, by whom, by when.]
[Action 2 — what will be done, by whom, by when.]
[Action 3 — what will be done, by whom, by when.]

IMPLEMENTATION TIMELINE

| Action | Target Date | Responsible |
|---|---|---|

PREVENTIVE CONTROLS

[The control that will be added or strengthened to prevent
recurrence.]

RESPONSIBLE PERSON

Primary: [Name], [Title]
Alternate: [Name], [Title]
```

For non-Single-Audit findings, omit the Federal Program, Questioned Cost, and Repeat Finding lines unless directly relevant.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Audit standards:**

- GAAS (AICPA) governs independent financial audits.
- GAGAS (the Yellow Book) governs financial audits that include federal awards and most government-conducted audits.
- 2 C.F.R. Part 200 Subpart F governs the Single Audit (federal expenditures of $1,000,000 or more in a fiscal year for fiscal years beginning on or after October 1, 2024). The Schedule of Findings and Questioned Costs follows the format at § 200.515(d), and management responses follow § 200.512(b)(3).
- Tex. Gov't Code Ch. 321 governs the State Auditor's Office.

**Findings categorization:** *Material weakness* (reasonable possibility of material misstatement); *significant deficiency* (less severe but worth attention); *control deficiency / other matter* (management letter only); *compliance finding* (Single Audit noncompliance); *questioned cost* (federal award cost the auditor questions).

**Single Audit corrective action plan:** Under 2 C.F.R. § 200.511(c), the auditee prepares a CAP for each finding listing the contact person, planned corrective action, and anticipated completion date. The federal awarding agency or pass-through entity may issue a management decision under § 200.521 within six months of FAC acceptance.

**Public records:** The audit report, including management responses, is a public record under Tex. Gov't Code Ch. 552 when accepted by the city council. Drafts circulated between management and the auditor before acceptance may be exempt under § 552.111.

**Retention:** Audit reports retain permanently per Texas State Library Local Government Retention Schedule GR, Item 1025-30. Single Audit working papers retain for 3 years from final closeout under 2 C.F.R. § 200.334.

**Verify before sending to the auditor:** The verbatim finding language matches the auditor's draft; the responsible person has read and approved the response; the corrective action timeline is achievable; the preventive control is named (not generic).

## References

- See `references/uniform-guidance-2cfr200-summary.md` (in `grant-application-drafter/references`) for the Single Audit framework and Subpart F requirements.

## Examples

- See `examples/two-findings-fy2025.md` for a worked example: Cedar Ridge FY2025 management responses to two findings — a significant deficiency in travel reimbursement controls and a Single Audit compliance finding on Davis-Bacon documentation.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
