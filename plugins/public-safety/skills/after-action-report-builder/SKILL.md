---
name: after-action-report-builder
description: Drafts an after-action report (AAR) for a real-world emergency response or planned exercise using the FEMA HSEEP structure and NIMS/ICS terminology, organized by core capability with strengths, areas for improvement, and assigned recommendations. Use when an emergency management coordinator, incident commander, or training officer needs to produce a formal AAR for the city manager, governing body, TDEM, or a grant report.
---

# After-Action Report Builder

> Drafts a FEMA HSEEP-format after-action report from an incident or exercise summary, organized by core capability with assigned recommendations. Built for emergency managers, incident commanders, and training officers documenting what happened and what should change.

## When to Use

- "We need an AAR on the winter storm response. Due to council in three weeks."
- "Draft the AAR for the EOC tabletop. Send to TDEM with our grant report."
- "The HazMat call had four agencies on scene. We need an AAR that captures all four."
- "Pull the timeline and observations into a draft AAR. We'll workshop it with the IC."
- A real-world incident has closed out and the agency must document lessons learned for internal use, grant compliance, or governing-body briefing.
- A planned exercise (tabletop, functional, full-scale) has concluded under HSEEP and an AAR is required for grant or accreditation purposes.

## Inputs Needed

Required:

- Incident or exercise name, date(s), and location(s).
- Incident commander and command structure (Operations, Planning, Logistics, Finance/Admin chiefs; key unit leaders).
- Participating organizations (city departments, county, state, federal, mutual aid, NGO).
- Timeline of events at decision-relevant resolution (typically hourly for fast incidents, daily for long ones).
- Core capabilities exercised (see `references/nims-ics-aar-structure.md`).
- Observations from participants and observers, ideally grouped by core capability.
- Strengths to recognize and areas for improvement to address.

Optional:

- Exercise objectives and HSEEP evaluation criteria (for exercise AARs).
- Cost and resource utilization data.
- After-action interviews or hot-wash notes.
- Prior AARs for the same hazard, to surface repeat findings.

If the timeline is not yet reconstructed, ask for it. An AAR without a timeline is a memo.

## Process

1. Reconstruct the timeline from CAD, EOC log, and participant interviews. Note who made which decision and when.
2. Identify the core capabilities engaged from the HSEEP list (community resilience, mass care services, mass search and rescue, on-scene security and protection, operational communications, public information and warning, situational assessment, public health, fatality management, others as relevant).
3. For each core capability, draft a Strengths paragraph and an Areas for Improvement paragraph, anchored in specific timeline events.
4. For each Area for Improvement, draft one or more Specific Recommendations with an Owner (named role, not just an agency) and a Target Completion Date.
5. Draft the Executive Summary last. One page maximum. Five to seven sentences. Plain language for the city manager and governing body.
6. Pull repeat findings forward. If a finding appears in this AAR and a prior AAR, mark it as a repeat and escalate the recommendation.
7. Confirm the AAR's distribution list with the IC: internal only, council briefing, TDEM, FEMA, public posting.
8. Add an Acknowledgments section. Named recognition matters in public safety.

## Output Format

Plain markdown. AARs typically run 10 to 30 pages for full incidents; 5 to 10 pages for tabletops. No emoji. Sober, neutral, specific. The reader is a city manager, a council member, or a TDEM reviewer.

```
AFTER-ACTION REPORT
[Incident or Exercise Name]
[Date(s)]
[Issued by: Agency / Date]

EXECUTIVE SUMMARY
[Five to seven sentences. What happened, the response, the
outcome, the top three takeaways.]

INCIDENT / EXERCISE OVERVIEW
- Name:
- Type: [Real-world incident / tabletop / functional / full-scale]
- Date(s) and time(s):
- Location(s):
- Hazard / scenario:
- Objectives (if exercise):

TIMELINE OF EVENTS
[Chronological table. Time | Event | Decision-maker]

PARTICIPATING ORGANIZATIONS
- [City PD, FD, OEM, Public Works, etc.]
- [County, state, federal]
- [Mutual aid, NGO, private sector]

COMMAND STRUCTURE
- Incident Commander: [Name, Title]
- Operations Section Chief:
- Planning Section Chief:
- Logistics Section Chief:
- Finance/Administration Section Chief:
- Public Information Officer:
- Safety Officer:
- Liaison Officer:
- [Branch directors, division supervisors, group supervisors as needed]

CORE CAPABILITIES EXERCISED
- [Capability 1]
- [Capability 2]

OBSERVATIONS

Core Capability: [Name]
Strengths:
- [Strength, anchored to a timeline event]
Areas for Improvement:
- [Issue, anchored to a timeline event]
Recommendations:
- [Recommendation] | Owner: [Role/Name] | Target: [Date]

[Repeat for each capability]

LESSONS LEARNED
- [Cross-cutting lesson 1]
- [Cross-cutting lesson 2]

ACKNOWLEDGMENTS
[Named recognition of personnel, mutual aid partners, and the
community.]

PREPARED BY: [Name, Title]
REVIEWED BY: [Incident Commander]
APPROVED BY: [Chief / Coordinator / City Manager]

AI-assisted draft, reviewed by [Name, Title] and the incident
command staff.
```

Tone: factual, neutral, and respectful of personnel under stress. AARs are read by people who were there; they will catch hedging or blame.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**NIMS/ICS alignment:** Tex. Health & Safety Code Ch. 418 and the TDEM-administered State Emergency Management Plan require NIMS compliance for jurisdictions receiving emergency management performance grants.

**HSEEP:** FEMA's Homeland Security Exercise and Evaluation Program prescribes the AAR structure for exercises. Real-world AARs benefit from its discipline.

**Public records (Tex. Gov't Code Ch. 552):** AARs are public records. Sensitive operational information (tactical positions, vulnerabilities) may be exempt under § 552.108 or § 552.139 (computer security). Coordinate with the City Attorney before public release.

**Open Meetings (Tex. Gov't Code Ch. 551):** AAR presentation to council may occur in open session or, where personnel matters are discussed, executive session under § 551.074. The AAR document itself is generally a public record.

**Retention:** AARs retain per Texas State Library Local Government Retention Schedule PS. Disaster-response records also fall under federal grant retention rules (commonly three years post-grant closeout) when grant funds were used.

## References

- See `references/nims-ics-aar-structure.md` for a working reference on NIMS/ICS positions (Incident Commander, Operations, Planning, Logistics, Finance/Admin), the HSEEP core capabilities list, and the FEMA-expected AAR structure.

## Examples

- See `examples/winter-storm-2026-aar.md` for an AAR on a January 2026 winter storm response, with multi-agency coordination (city PD, FD, Public Works, county, TDEM) and four areas for improvement (warming center activation timing, public communications cadence, mutual aid request process, post-storm debris removal).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
