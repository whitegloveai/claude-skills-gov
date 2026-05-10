# Example: Cedar Ridge AI Use Case Intake — Generative AI Agenda Drafting

Worked example output of the `ai-governance-checklist` skill for the City of Cedar Ridge's adoption of a generative AI tool used by the council-ops `agenda-builder` skill to draft city council agendas.

**Inputs provided:**

- Use case: Use of the WhitegloveAI Claude Skills Library `agenda-builder` skill (operating on Claude for Enterprise) for first-draft preparation of City Council meeting agendas.
- Owner: City Secretary's Office (Janelle Roth, City Secretary); IT liaison: Vihaan Joshi, CIO.
- Scope: Production deployment, City Secretary's Office only, two-user pilot expanding to office-wide after 90 days.
- Citizen impact: No direct citizen interaction. Output is a draft document reviewed and edited by the City Secretary before posting.
- Data inputs: Agenda items submitted by departments (Confidential), prior meeting agendas (Public), executive session statutory cites (Public).
- Data outputs: Markdown agenda draft delivered to the City Secretary's queue; no direct posting to public website.
- Automation level: Advisory; human-in-the-loop required by skill design and by Cedar Ridge IT-014.
- Evaluation metrics: Accuracy of statutory citations (target 100%); time to first draft (target <10 minutes); editor edit-distance per draft (track baseline).
- Procurement: Claude for Enterprise license under existing master agreement (no new procurement).

---

# AI USE CASE INTAKE

**City of Cedar Ridge, Texas — Intake No. AI-2026-007**
Submitted by: Janelle Roth, City Secretary; sponsored by Vihaan Joshi, CIO
Date: 2026-03-04
**Status: Approved with conditions**

## 1. USE CASE IDENTIFICATION

Title: City Secretary AI Agenda Drafting — `agenda-builder` skill.
Version: 1.0 (Claude Skills Library v1.0, council-ops plugin).
Summary: City Secretary's Office will use the `agenda-builder` skill running on the City's Claude for Enterprise tenancy to produce first-draft agendas for City Council regular, special, and emergency meetings. The skill is one of 65 skills in the WhitegloveAI Claude Skills Library for Local Government adopted by the City under Council Resolution R-2026-08.

## 2. OWNER AND STAKEHOLDERS

- Sponsoring department: Office of the City Secretary.
- Business owner: Janelle Roth, City Secretary.
- IT contact: Vihaan Joshi, CIO.
- Privacy officer liaison: Karen Ledbetter, City Attorney's Office.
- Records management liaison: Jessica Aldridge, Records Management Officer.

## 3. PURPOSE AND DECISION AUTHORITY

The City Secretary spends approximately 4 hours per cycle drafting agendas from intake forms received from departments. The `agenda-builder` skill produces a first draft in under 10 minutes, including statutory citation suggestions for executive sessions and public hearings. The City Secretary retains all decision authority. The skill informs no public-facing decision; it produces a draft for staff editing.

## 4. CITIZEN INTERACTION SCREEN — § 552.051 TRIGGER

| Question | Answer | Rationale |
|---|---|---|
| A. Direct citizen interaction with AI? | **No** | The skill produces a static document. Citizens do not interact with the skill or its output during drafting. |
| B. AI informs/makes a decision affecting citizen rights/benefits/status? | **No** | The City Council makes meeting decisions. The AI output is a draft document, not a decision input. |
| C. Could a reasonable citizen mistake this AI for a human? | **No** | The output is a posted agenda over the City Secretary's signature. The drafting tool is not visible to citizens. |

**Result:** § 552.051 disclosure is not engaged. Route to transparency-best-practice plan in Section 11.

## 5. RISK CLASSIFICATION

**Medium-Low.**

Drivers:
- Citizen impact: indirect (TOMA-compliant agendas are central to lawful governance), but mediated entirely by staff review.
- Data class: Confidential agenda intake inputs; no PII, PHI, or CJIS.
- Automation level: Advisory; high human review.
- Reversibility: High — draft errors caught at City Secretary review before posting; further protected by 72-hour posting window and TOMA correction practice.

## 6. NIST AI RMF FUNCTION ALIGNMENT

- **Govern (GV-1.1, GV-3.2, GV-6.1)** — Use governed by Cedar Ridge IT-014 (Generative AI AUP). Process documented in this intake. Vendor risk addressed via the underlying Claude for Enterprise contract reviewed under intake AI-2026-001.
- **Map (MP-1.1, MP-2.2)** — Purpose (agenda drafting) and users (City Secretary's Office) documented. System documentation: WhitegloveAI Claude Skills Library SKILL.md, council-ops/agenda-builder.
- **Measure (MS-1.3, MS-2.5, MS-2.7)** — Metrics defined: statutory citation accuracy, time-to-first-draft, editor edit-distance. Validity reviewed at 90 days. Security inherited from Claude for Enterprise tenancy.
- **Manage (MG-1.1, MG-4.1)** — Benefits-and-impacts determination on record (this intake). Post-deployment monitoring weekly for first 90 days, monthly thereafter.

## 7. GENERATIVE AI PROFILE CROSS-CUTS

- **GV-1.1** — Confidentiality protected by Claude for Enterprise data handling terms (no training on customer data).
- **MP-2.2** — Skill documentation in the library is the model card equivalent.
- **MS-1.3** — Hallucination risk specifically measured via statutory citation accuracy metric.
- **MG-1.1** — Determination: benefits (8x speed; improved citation hygiene) outweigh negative impacts (low) given Advisory automation and 100% staff review.

## 8. DATA INPUTS AND OUTPUTS

- Inputs: Agenda intake forms (Confidential, departmental email or shared drive). Prior agendas (Public). Statutory cite library (Public, maintained by City Attorney's Office).
- Outputs: Markdown draft to the City Secretary's secure drafting queue. No outbound transmission to other systems or publication channels.

## 9. AUTOMATION LEVEL

Advisory. The City Secretary reviews and edits every draft. No automated posting.

## 10. PERFORMANCE MEASUREMENT AND REVIEW

| Metric | Target | Cadence |
|---|---|---|
| Statutory citation accuracy | 100% pre-edit | Per agenda |
| Time to first draft | < 10 minutes | Per agenda |
| Editor edit-distance | Tracked; no target | Per agenda |
| User satisfaction | Quarterly survey | Quarterly |
| TOMA notice complaints | Zero attributable to AI drafting | Continuous |

Review: 30, 60, 90 days; quarterly thereafter; full re-intake on skill version change.

## 11. TRAIGA APPLICABILITY AND DISCLOSURE PLAN

**§ 552.051 not triggered.** Transparency best-practice plan:

- Adopted agendas distributed to the public carry the existing City Secretary certification block under § 551.043 / § 551.056; no AI footer is required on the posted public artifact.
- Internal drafts circulated to the governing body or department heads will carry a notation: *"AI-assisted draft, reviewed by [City Secretary]."*
- The AI use case is listed on the City's public AI Use Case Inventory (intake AI-2026-007).
- Plain-language description on city website's "AI at Cedar Ridge" page.

Substantial-compliance posture under § 552.057: documented in Section 6 above with specific NIST AI RMF subcategory citations.

## 12. PUBLIC RECORDS AND RETENTION

- AI drafts pre-posting: working drafts, excepted under Tex. Gov't Code § 552.111 (agency memoranda) until adoption. Retain 90 days per IT-017 logging standard.
- Adopted agendas: permanent retention per TSLAC Schedule GR, Item 1000-26 (Meeting Notices and Agendas). Adopted agendas are the only artifact distributed publicly.
- Prompts and outputs: retained in the Claude for Enterprise tenancy per IT-017 (logs) and IT-014 § 4.7 (substantive prompts retained with the resulting record).

## 13. INCIDENT REPORTING

Triggers for routing to the `security-incident-classifier`:
- Confabulated or incorrect statutory citation that reaches a posted agenda.
- Confidentiality leak of pre-draft intake content.
- Outage during the 72-hour posting window.

## 14. APPROVAL PATH

Risk classification Medium-Low. Approval authority: IT Steering Committee for record; CIO and City Secretary for sign-off. AI literacy training (HB 3512) completion by all users before access provisioning.

## 15. APPROVAL AND CONDITIONS

Approved 2026-03-12 by IT Steering Committee.

Conditions:
1. 90-day pilot scope (2 users, City Secretary's Office) before office-wide rollout.
2. 30/60/90-day metric review.
3. Re-intake on any change to the underlying `agenda-builder` skill major version.
4. Annual review at the AI Use Case Inventory cycle.

Next review: 2026-06-12 (90 days).

---

**Drafting notes (not part of the official intake):**

Cross-skill linkage: this intake also covers the council-ops `minutes-drafter`, `public-comment-summarizer`, and `decision-memo-writer` skills as a cohort because they share the same risk profile (advisory, internal, no citizen interaction, Confidential-class inputs). The finance `budget-narrative-writer` and planning `staff-report-writer` skills require their own intakes given the higher impact of those outputs.

The intake is annotated *AI-assisted draft, reviewed by Janelle Roth, City Secretary, and Vihaan Joshi, CIO* per IT-014.
