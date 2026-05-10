---
name: policy-analyzer
description: Reviews an HR policy or proposed policy against current federal and Texas employment law and produces a legal-compliance memo identifying risk, recommended edits, and questions for counsel. Use when HR or the city attorney's office is updating a personnel policy, evaluating a draft, or responding to an audit finding.
---

# Policy Analyzer

> Reviews an HR policy and returns a structured risk and recommendation memo. Built for HR directors and city attorneys who need a fast triage of where a policy is exposed and what to change.

## When to Use

- "Review our remote work policy for FLSA and ADA risk."
- "Here's a draft drug and alcohol policy. What's missing?"
- "Audit our PTO policy against Texas law and FMLA."
- "We had a complaint about our social media policy. Walk through the First Amendment risk for public-sector speech."
- "Our political activity policy hasn't been touched since 2015. What needs to change?"
- A pre-litigation demand letter or EEOC charge has surfaced a policy issue and the city attorney needs a working analysis.

## Inputs Needed

Required:

- The policy text, or the policy topic and a description of the current practice
- Jurisdiction scope (Texas, federal, and any local civil-service or collective-bargaining considerations)
- Whether the city has civil service for police and fire (Tex. Loc. Gov't Code Ch. 143) or county civil service (Ch. 158)
- Whether the policy applies to all employees or a subset
- Specific concerns the user wants reviewed (if any)

Optional:

- The triggering event (audit finding, complaint, court decision, statutory change)
- Recent case law or guidance the user wants assessed
- The collective bargaining agreement (CBA) if Tex. Loc. Gov't Code Ch. 174 applies
- A target effective date

If the user has not provided the policy text or topic, ask before drafting. A review without source text is speculation.

## Process

1. Identify the policy area and the federal and state statutes that govern it. Leave policies implicate FMLA, ADA, USERRA, and Texas workers' comp; pay policies implicate FLSA and the Texas Payday Law; speech and political-activity policies implicate the First Amendment, the Hatch Act, and the Texas Election Code.
2. Read the policy against each authority. Classify each issue: **High** (likely violation or significant exposure), **Medium** (defensible but weak), **Low** (best-practice improvement).
3. Distinguish legal risk from operational risk. Flag both, separately.
4. Identify open questions for legal counsel, including federal Circuit splits and recent Texas Supreme Court or Fifth Circuit decisions.
5. Draft specific recommended edits. Provide proposed language tied to each finding.
6. Note implementation considerations: training cascade, supervisor briefing, employee communication, CBA reopeners, and council action requirements.
7. Flag retention and public-records implications.

## Output Format

Plain markdown memo. Length: 800 to 1,500 words depending on policy complexity. Tone: legal-analytical, plain, not editorializing.

```
MEMORANDUM

TO:       [HR Director / City Attorney / City Manager]
FROM:     [Author]
DATE:     [Date]
RE:       Compliance Review — [Policy Name]

I. ISSUE
[1–2 sentences naming the policy under review and the scope of this analysis.]

II. SUMMARY OF FINDINGS
[Bulleted list of the high/medium/low findings with one-line captions.]

III. DETAILED FINDINGS

Finding 1 — [Caption]
Risk Level: [High / Medium / Low]
Controlling Authority: [Citation]
Discussion: [2–4 sentences explaining the issue.]
Recommendation: [Specific edit language.]

Finding 2 — [Caption]
[Same structure.]

IV. OPEN QUESTIONS FOR LEGAL COUNSEL
1. [Question that requires counsel's judgment.]
2. [Question that requires counsel's judgment.]

V. IMPLEMENTATION CONSIDERATIONS
- Approval path (council action / city manager / department)
- Training cascade
- Communication to affected employees
- CBA implications (if any)
- Effective date and grandfathering

VI. RETENTION AND PUBLIC RECORDS
[Notes on Ch. 552 implications and retention schedule.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**EEOC AI guidance:** The EEOC's 2023 technical assistance addresses AI-assisted employment decisions and Title VII disparate impact. Where a policy authorizes AI-assisted screening, selection, or evaluation, the analysis should flag adverse-impact testing, accommodation processes for applicants with disabilities, and notice expectations.

**Federal authorities commonly engaged:** FLSA (29 U.S.C. § 207) — pay and overtime; ADA/ADAAA (42 U.S.C. § 12101 et seq.) — accommodation and medical inquiries; FMLA (29 U.S.C. § 2601 et seq.) — leave; Title VII (42 U.S.C. § 2000e et seq.) — discrimination and harassment; ADEA (29 U.S.C. § 621 et seq.); GINA (42 U.S.C. § 2000ff et seq.); USERRA (38 U.S.C. § 4301 et seq.); PWFA — pregnancy accommodation; § 1983 (42 U.S.C. § 1983) — constitutional claims.

**Texas-specific authorities:** Tex. Lab. Code Ch. 21 (TCHRA); Tex. Lab. Code Ch. 61 (Payday Law); Tex. Lab. Code Title 5 (workers' comp); Tex. Lab. Code Ch. 451 (anti-retaliation); Tex. Gov't Code Ch. 614 (peace officer and firefighter complaint procedures); Tex. Loc. Gov't Code Ch. 143 (civil service for police and fire); Tex. Loc. Gov't Code Ch. 158 (county civil service); Tex. Loc. Gov't Code Ch. 174 (collective bargaining where adopted); Tex. Gov't Code Ch. 411 (TCOLE); Tex. Election Code Ch. 251–254 (political-activity, resign-to-run); Tex. Gov't Code § 617.002.

**First Amendment:** Speech, social media, and political-activity policies for public employees must be analyzed under *Pickering*, *Garcetti*, and progeny.

**Public records:** Adopted policies are public under Tex. Gov't Code Ch. 552. Counsel-reviewed memos may be exempt under § 552.107 (attorney-client) or § 552.103 (litigation); drafts under § 552.111. **Do not conflate** Tex. Gov't Code Ch. 552 (Public Information Act) with Tex. Bus. & Comm. Code Ch. 552 (TRAIGA).

**Retention:** Per Texas State Library Local Government Retention Schedule GR; retain superseded policies for the limitations period for related claims.

## References

This skill does not require a separate reference file; the statutory framework is summarized inline.

## Examples

- See `examples/remote-work-policy-review.md` for a worked example: review of a draft Cedar Ridge remote work policy with high-risk findings on non-exempt timekeeping (FLSA), medium-risk findings on ADA accommodation interplay and workers' comp coverage, and low-risk findings on workplace surveillance limits.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
