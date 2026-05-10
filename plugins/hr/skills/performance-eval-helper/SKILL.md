---
name: performance-eval-helper
description: Drafts a public-sector performance evaluation narrative from raw supervisor notes, goal status, and competency observations, with strengths, development areas, and goals for the next period. Use when a supervisor or HR generalist is preparing an annual or probationary evaluation in a Texas city, county, or special district.
---

# Performance Evaluation Helper

> Drafts the narrative for a public-sector performance evaluation from supervisor notes and goal data. Built for supervisors who do good work all year and then have one bad weekend writing evals.

## When to Use

- "Help me draft the annual eval for our Streets Supervisor. Here are my notes."
- "Turn these performance notes into competency narratives."
- "I have goal status for the year. Draft the goal achievement section."
- "Write the development-area narrative for someone who needs to improve at documentation."
- "Draft a 90-day probationary eval for the Code Enforcement Officer we hired in February."
- The annual evaluation cycle is open and the supervisor has 11 evaluations due in two weeks.

## Inputs Needed

Required:

- Employee name and position
- Supervisor name and position
- Review period (start and end dates) and review type (annual, probationary, mid-year, special)
- Goals set at the start of the period, with current status (achieved, partial, not achieved, deferred)
- Supervisor notes for the period — observations, project outcomes, incidents, recognition
- The competency model the city uses (job knowledge, work quality, productivity, dependability, communication, judgment, teamwork, supervisory if applicable, customer service, safety)
- Any quantitative KPIs the position is measured on

Optional:

- Documented coachings or disciplinary actions during the period
- Commendations, awards, or external recognition
- Training completed during the period
- Self-evaluation submitted by the employee
- Civil service requirements that apply (Tex. Loc. Gov't Code Ch. 143 specific evaluation procedures)

If the user has not provided supervisor notes for the period or the goals set at the start, ask before drafting. An eval drafted without observations is fiction and exposes the supervisor in any future personnel action.

## Process

1. Confirm review type and the city's evaluation form. Probationary evaluations under Ch. 143 affect the retention decision.
2. Draft the Goal Achievement Summary. For each goal, restate the goal, status, and supporting evidence. Quantify where possible.
3. Draft Competency Ratings with specific narrative for each competency. Ratings without narrative are unsupportable in a grievance or appeal. Tie observations to behaviors, not personality.
4. Identify three to five Strengths supported by observations during the period.
5. Identify one to three Areas for Development, phrased developmentally with a planned action — training, mentoring, project assignment.
6. Draft three to five SMART goals for the next period tied to department priorities.
7. Draft the Overall Rating with rationale anchored to competency ratings and goal achievement.
8. Add the Employee Acknowledgment, supervisor, and HR signature blocks. Note the right to attach a written response.

## Output Format

Plain markdown. Length: 600 to 1,200 words depending on position and period. Tone: factual, specific, professional. Never personal. Never sarcastic. Never speculative about the employee's life outside work.

```
[CITY OF X] PERFORMANCE EVALUATION

Employee: [Name]
Position: [Title], [Department]
Supervisor: [Name and Title]
Review Period: [Start] to [End]
Review Type: [Annual / Probationary / Mid-Year / Special]
Date Prepared: [Date]

GOAL ACHIEVEMENT
Goal 1: [Original goal]
Status: [Achieved / Partial / Not Achieved / Deferred]
Evidence: [2–3 sentences with specifics, quantified where possible.]

Goal 2: [Original goal]
Status: [Status]
Evidence: [2–3 sentences.]

[Additional goals as needed.]

COMPETENCY RATINGS

Job Knowledge — [Rating]
[2–3 sentence narrative tied to observations during the period.]

Work Quality — [Rating]
[2–3 sentence narrative.]

Productivity — [Rating]
[2–3 sentence narrative.]

Dependability — [Rating]
[2–3 sentence narrative.]

Communication — [Rating]
[2–3 sentence narrative.]

Judgment and Decision-Making — [Rating]
[2–3 sentence narrative.]

Teamwork — [Rating]
[2–3 sentence narrative.]

Customer Service — [Rating]
[2–3 sentence narrative.]

Safety — [Rating]
[2–3 sentence narrative.]

[Supervisory competencies if applicable.]

STRENGTHS
- [Strength 1, with evidence.]
- [Strength 2, with evidence.]
- [Strength 3, with evidence.]

AREAS FOR DEVELOPMENT
- [Area 1.]
  Plan: [Training, mentoring, project assignment, timeline.]
- [Area 2.]
  Plan: [Action with timeline.]

GOALS FOR NEXT PERIOD
1. [SMART goal.]
2. [SMART goal.]
3. [SMART goal.]

OVERALL RATING: [Rating]
Rationale: [3–5 sentence summary tying competency ratings, goal
achievement, and the overall.]

EMPLOYEE ACKNOWLEDGMENT
My signature indicates that this evaluation has been discussed with me.
It does not necessarily indicate agreement. I have the right to attach
a written response within [X] days.

Employee Signature: ___________________ Date: ________
Supervisor Signature: _________________ Date: ________
Department Head Review: _______________ Date: ________
HR Review: ____________________________ Date: ________
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**EEOC AI guidance:** The EEOC's 2023 technical assistance addresses AI in employment decisions. AI-assisted drafting must include human review; the supervisor — not the AI — is the rater of record. Keep narrative tied to observed behavior.

**Title VII and ADA:** Evaluations are frequent points of disparate treatment and failure-to-accommodate exposure. Tie ratings to specific behaviors. Avoid language referencing protected characteristics. Do not penalize accommodated limitations.

**Public records:** Performance evaluations are personnel records. Tex. Gov't Code § 552.022(a)(2) makes some personnel information presumptively public; § 552.117 and § 552.1175 exempt specific categories such as home addresses. Do not include information in an evaluation the city would not want produced in a public records request or in discovery. Tex. Gov't Code Ch. 552 (Public Information Act) is separate from Tex. Bus. & Comm. Code Ch. 552 (TRAIGA).

**Civil service:** Tex. Loc. Gov't Code Ch. 143 (police and fire) or Ch. 158 (county) systems have specific evaluation procedures and may carry appeal rights.

**Tex. Gov't Code Ch. 614:** Peace officer and firefighter misconduct allegations must be reduced to writing, signed, and provided to the officer before discipline. A supervisor should not use the evaluation to introduce previously unwritten misconduct allegations.

**Retention:** Per Texas State Library Local Government Retention Schedule GR.

**At-will:** Evaluations should not include language suggesting an implied contract.

## References

This skill does not require a separate reference file; the structure is captured inline.

## Examples

- See `examples/streets-supervisor-annual-eval.md` for a worked example: annual evaluation for a Cedar Ridge Streets Supervisor with goal achievement on the overlay project ramp-up and one development area on documentation completeness.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
