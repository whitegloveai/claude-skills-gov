---
name: ai-governance-checklist
description: Drafts an AI use-case intake form aligned with NIST AI RMF 1.0, the NIST Generative AI Profile, TRAIGA, and the GovAI Coalition's use case template. Use when a CIO, AI governance lead, or department director needs to intake a proposed AI use case for risk classification, control mapping, and approval routing before deployment.
---

# AI Governance Checklist

> Produces an AI use case intake form that captures purpose, risk, control alignment, TRAIGA applicability, and the approval path. Built for the AI governance lead who needs a record of every AI tool in the city's environment that will hold up to council scrutiny and a TRAIGA enforcement review.

## When to Use

- "Planning wants AI to draft staff reports. Intake the use case."
- "HR is piloting AI résumé screening. Run it through governance."
- "Council asked for an inventory of every AI use case in the city."
- "Vendor is offering an AI citizen chatbot. Does this trigger TRAIGA disclosure?"
- "Evaluating the agenda-builder skill for the City Secretary's Office."
- The city's AI use policy requires intake before procurement, deployment, or pilot.

## Inputs Needed

Required:

- Use case description in plain language.
- Owner and stakeholders (sponsoring department, business owner, IT contact).
- Scope (pilot or production; user population; data classes).
- Citizen impact: does the use case put a citizen in direct interaction with AI? Does it inform or make a decision affecting a citizen's rights, benefits, or legal status?
- Data inputs (what is ingested; classification level) and outputs (what is produced; destination).
- Automation level: advisory, substantial-assist, or autonomous.
- Evaluation metrics.

Optional:

- Vendor name and procurement status.
- Existing intake number if reopening.
- Vendor AI fact sheet for pre-population.

If citizen impact or automation level is missing, ask. Those two inputs determine § 552.051 disclosure and prohibited-use screening.

## Process

1. Confirm citizen interaction. **Section 4 of the form surfaces the direct question: "Does this AI place a citizen in direct interaction with an AI system?"** The answer routes the use case into the disclosure plan.
2. Classify risk against the city's AI Risk Tiers (Low, Medium, High, Prohibited). Anchor on citizen impact, data class, automation level, and reversibility.
3. Map the use case to NIST AI RMF 1.0 functions (Govern, Map, Measure, Manage) and identify the relevant subcategories. See `references/nist-ai-rmf-functions-mapping.md`.
4. Apply NIST Generative AI Profile cross-cuts if generative AI is involved (GV-1.1, MP-2.2, MS-1.3, MG-1.1 at minimum).
5. Evaluate TRAIGA applicability. Yes routes to § 552.051 disclosure plan. No routes to the transparency-best-practice plan. Both document the policy basis.
6. Document the public records and retention plan: what AI-generated content is a public record, storage, TSLAC schedule item.
7. Define performance metrics and review cadence. Higher-risk quarterly; lower-risk annual.
8. Define the incident reporting trigger.
9. Specify the approval path. Low: AI Governance Lead. Medium: IT Steering Committee. High: City Manager and Council. Prohibited: not approved.

## Output Format

```
AI USE CASE INTAKE
City of [ENTITY] — Intake No. [AI-YYYY-NNN]
Submitted by: [Name, title] | Date: [Date]
Status: Draft | Under review | Approved | Approved with conditions | Not approved

1. USE CASE IDENTIFICATION — title, version, 2–4 sentence summary.

2. OWNER AND STAKEHOLDERS — sponsoring department, business owner, IT
   contact, privacy officer liaison, records management liaison.

3. PURPOSE AND DECISION AUTHORITY — problem solved; what decision the
   AI informs or makes; who retains decision authority.

4. CITIZEN INTERACTION SCREEN — § 552.051 TRIGGER
   A. Direct citizen-AI interaction? [Yes / No]
   B. AI informs or makes a decision affecting citizen rights, benefits,
      or legal status? [Yes / No]
   C. Could a citizen mistake the AI for a human? [Yes / No]
   Any Yes routes to § 552.051 disclosure plan in § 11.

5. RISK CLASSIFICATION — Low | Medium | High | Prohibited.
   Drivers: citizen impact, data class, automation level, reversibility.

6. NIST AI RMF FUNCTION ALIGNMENT — Govern, Map, Measure, Manage with
   subcategories and how each is met.

7. GENERATIVE AI PROFILE CROSS-CUTS (if applicable) — e.g., GV-1.1,
   MP-2.2, MS-1.3, MG-1.1.

8. DATA INPUTS AND OUTPUTS — inputs (class, source); outputs (artifact,
   destination, who acts on it).

9. AUTOMATION LEVEL — Advisory | Substantial-assist | Autonomous.

10. PERFORMANCE MEASUREMENT AND REVIEW — metrics, cadence, reviewer.

11. TRAIGA APPLICABILITY AND DISCLOSURE PLAN
    If § 552.051 triggered: disclosure language; method (banner, voice
    prompt, modal); recipient; recordkeeping.
    If not triggered: transparency best-practice plan (AI-assisted
    footer, inventory listing, plain-language description on city site).
    Substantial-compliance posture under § 552.057: cite the NIST AI RMF
    subcategories from § 6.

12. PUBLIC RECORDS AND RETENTION — records, TSLAC schedule item,
    storage, redaction strategy.

13. INCIDENT REPORTING — triggers for routing to
    security-incident-classifier.

14. APPROVAL PATH — Low: AI Governance Lead | Medium: IT Steering
    Committee | High: City Manager and Council | Prohibited: not approved.

15. APPROVAL AND CONDITIONS — approver(s), date, conditions, next
    review date.
```

Length: 4–7 pages. Tone: factual, plain. Cite function alignment honestly; no marketing claims.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [AI Governance Lead]."* This is a policy choice, not a statutory mandate.

**Intake screens for citizen-AI interaction:** unlike other IT skills, this one *intakes* AI use cases that may themselves place citizens in direct AI interaction (chatbots, IVR voice assistants, 311 triage, résumé screening). Section 4 surfaces the § 552.051 question; any "Yes" routes to a disclosure plan in Section 11.

**Substantial-compliance safe harbor — Tex. Bus. & Comm. Code § 552.057:** NIST AI RMF alignment establishes a presumption of substantial compliance, documented in Sections 6–7.

**Prohibited uses — Tex. Bus. & Comm. Code §§ 552.101–552.108:** social scoring, unlawful biometric surveillance, manipulation through vulnerability exploitation. Surfaced in Section 5.

**HB 3512 AI literacy training:** required for users of approved AI tools. Section 14.

**Public records (Tex. Gov't Code Ch. 552):** AI outputs informing City decisions are public records, mapped to TSLAC schedules in Section 12. Structure mirrors the GovAI Coalition Use Case Template.

## References

- See `references/nist-ai-rmf-functions-mapping.md` for NIST AI RMF 1.0 functions, the Generative AI Profile cross-cuts, and the TRAIGA safe harbor.

## Examples

- See `examples/genai-agenda-drafting-intake.md` for a worked example: intake for Cedar Ridge's adoption of a generative AI tool used by the council-ops `agenda-builder` skill for council agenda drafting. Risk classified medium-low; automation advisory; § 552.051 not triggered (drafts pass through staff before posting).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
