---
name: onboarding-packet-builder
description: Assembles a new-hire onboarding packet checklist tailored to position type with required forms, training assignments, retirement system enrollment, and 30/60/90 milestones. Use when HR or a hiring manager is preparing for a new employee's first day in a Texas city, county, or special district.
---

# Onboarding Packet Builder

> Assembles a position-specific new-hire onboarding checklist covering paperwork, IT setup, retirement enrollment, training, and the first 90 days. Built for HR generalists who onboard ten different positions and cannot afford to miss anything.

## When to Use

- "Build an onboarding packet for a Senior Accountant starting June 2."
- "We're hiring a police officer. Generate the packet with TCOLE verification and the oath."
- "Draft a 30/60/90 schedule for a new Code Enforcement Officer."
- "What forms does a Building Inspector sign on day one?"
- A new hire's start date is set and the supervisor needs a working checklist.

## Inputs Needed

Required: position title, department, and supervisor; start date; FLSA status; whether the position is sworn or civilian; retirement system (TMRS, TCDRS, or other); whether the position requires a sworn oath, civil service certification, or specific licensure (TCOLE, TCFP, ICC).

Optional: bilingual designation and pay differential; background, drug test, and physical status; special clearances (CJIS, IRS Pub. 1075); accommodations arranged from interview; mentoring or training assignments.

If the user has not provided FLSA status or whether the role is sworn, ask before drafting — the paths diverge.

## Process

1. Identify the position type: civilian non-exempt, civilian exempt, sworn peace officer, sworn firefighter, or contract/grant-funded.
2. Build the Day 1 Checklist. Include I-9 (8 U.S.C. § 1324a, complete within three business days of start), W-4, direct deposit, retirement and life insurance beneficiary designations, ethics acknowledgment, drug-free workplace acknowledgment, IT acceptable use, and confidentiality acknowledgment if applicable.
3. Add IT and facilities setup tasks: badge, system credentials, MDM enrollment, parking, key access. Coordinate with IT so accounts are provisioned before Day 1.
4. Add retirement system enrollment. TMRS and TCDRS each have specific enrollment and beneficiary forms; vesting and contribution rates are set by the city's adopted plan.
5. For sworn personnel, add TCOLE or TCFP credential verification, oath of office, civil service forms under Tex. Loc. Gov't Code Ch. 143 where applicable, Garrity-warning training, body-worn camera training, and use-of-force policy acknowledgment.
6. Build Week 1 Milestones: payroll cycle orientation, supervisor 1:1, department orientation, safety briefing, EAP introduction, benefits enrollment.
7. Build 30/60/90-day reviews. At 30, role clarity and basic competency. At 60, workflow integration and gaps. At 90, formal probationary review.
8. Cross-check AI literacy training if the city has adopted standards mirroring HB 3512.

## Output Format

Plain markdown checklist. Length: 700 to 1,300 words. Tone: operational and plain, formatted as a working document with checkboxes.

```
[CITY OF X] — NEW HIRE ONBOARDING PACKET

Employee: [Name]
Position: [Title], [Department]
Supervisor: [Name and Title]
Start Date: [Date]
FLSA Status: [Exempt / Non-Exempt]
Retirement System: [TMRS / TCDRS / Other]

PRE-START
[ ] Background, drug, physical cleared
[ ] System accounts provisioned
[ ] Badge and access prepared
[ ] Workspace and equipment ready
[ ] Day 1 supervisor 1:1 scheduled

DAY 1 — PAPERWORK
[ ] Form I-9 (Sections 1 and 2 within 3 business days)
[ ] W-4 federal withholding
[ ] Direct deposit
[ ] Retirement enrollment ([TMRS / TCDRS])
[ ] Beneficiary designations (retirement, life, deferred comp)
[ ] Ethics acknowledgment
[ ] Drug-free workplace acknowledgment
[ ] IT acceptable use
[ ] Confidentiality acknowledgment (if applicable)
[ ] Emergency contact form

DAY 1 — ORIENTATION
[ ] Welcome and tour
[ ] Badge photo
[ ] Payroll cycle and timekeeping briefing
[ ] Benefits overview (enrollment window: [X] days)
[ ] EAP introduction
[ ] Safety briefing

[FOR SWORN POSITIONS — DAY 1 ADDENDUM]
[ ] Oath of office administered
[ ] TCOLE / TCFP license verification
[ ] Civil service forms (Ch. 143)
[ ] BWC training scheduled
[ ] Use-of-force policy acknowledgment
[ ] Garrity-warning training scheduled

WEEK 1 MILESTONES
[ ] Supervisor 1:1 (priorities, FLSA timekeeping)
[ ] Department orientation
[ ] Required training assigned
[ ] Mentor introduction (if applicable)

TRAINING MATRIX
- [Required training 1] — Due by [date]
- [Required training 2] — Due by [date]

30/60/90-DAY CHECK-INS
- 30: Role clarity, basic competency, equipment functional
- 60: Workflow integration, identified gaps, mid-probation feedback
- 90: Formal probationary review, retention decision, goal-setting; for civil service positions, documentation per Ch. 143

SIGN-OFF MATRIX
[ ] Employee: ____________________ Date: ________
[ ] Supervisor: __________________ Date: ________
[ ] HR: __________________________ Date: ________
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**EEOC AI guidance:** If the city uses AI in benefits enrollment or any tool that interacts directly with the new employee, evaluate that interaction under the EEOC's 2023 technical assistance and TRAIGA § 552.051.

**Form I-9:** 8 U.S.C. § 1324a requires the I-9 within three business days of start. Texas does not generally require E-Verify for cities, but verify grant or contract conditions.

**Tax forms:** Federal W-4 required. Texas has no state income tax withholding.

**HB 3512:** AI literacy training applies to state employees; cities may adopt similar standards.

**Retirement:** TMRS and TCDRS enrollment, beneficiary, and contribution rate confirmation must be completed in the first pay period.

**Sworn positions:** Peace officer onboarding implicates Tex. Gov't Code Ch. 411 (TCOLE), Tex. Gov't Code Ch. 614 (complaint and Garrity-style protections), Tex. Loc. Gov't Code Ch. 143, and the city's use-of-force and BWC policies. Firefighter onboarding implicates TCFP and Ch. 143.

**Public records:** Onboarding records are personnel records. Some are exempt under Tex. Gov't Code § 552.117; others are open under § 552.022. Tex. Gov't Code Ch. 552 (Public Information Act) is separate from Tex. Bus. & Comm. Code Ch. 552 (TRAIGA).

**Retention:** Per Texas State Library Local Government Retention Schedule GR; sworn files have additional rules under Ch. 614 and Ch. 143.

## References

This skill does not require a separate reference file; the onboarding sequence is structured inline.

## Examples

- See `examples/police-officer-onboarding.md` for a worked example: full onboarding packet for a police officer (sworn, civil service, TCOLE-licensed), including the oath of office, TCOLE verification, Garrity warning training, and the civil service probationary period.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
