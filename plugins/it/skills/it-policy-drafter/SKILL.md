---
name: it-policy-drafter
description: Drafts a municipal IT or acceptable-use policy aligned with NIST CSF 2.0, NIST SP 800-53 Rev. 5, and Texas DIR requirements. Use when a CIO, IT director, or HR partner needs to produce a governing-body-ready policy on topics such as acceptable use, password and authentication, BYOD, remote access, generative AI use, data classification, or incident response.
---

# IT Policy Drafter

> Drafts a council-ready IT policy with the right control framework alignment, the right scope, and the right governance hooks. Built for the CIO who needs a defensible policy on the agenda next month, not a 90-page treatise.

## When to Use

- "Draft an acceptable use policy for staff and contractors."
- "We need a generative AI use policy before TRAIGA takes effect."
- "Council wants a BYOD policy. Align it with NIST 800-53."
- "Draft a password and MFA policy mapped to NIST CSF Protect."
- "We need a data classification policy that handles CJIS, PHI, and ordinary city records."
- "Build us an incident response policy aligned with DIR reporting."
- A renewing cyber insurance policy or TX-RAMP-aligned audit requires a control the city has not yet adopted in writing.

## Inputs Needed

Required:

- Entity name and adopting authority (council, city manager, IT steering committee).
- Policy topic (acceptable use, password and authentication, BYOD, remote access, generative AI use, data classification, incident response, vendor management, change management, vulnerability management, logging and monitoring, physical security, access control, or backup and recovery).
- Primary control framework (NIST CSF 2.0, NIST SP 800-53 Rev. 5, ISO 27001, or CIS Controls). Most Texas cities pick NIST CSF 2.0 as primary with 800-53 Rev. 5 mapping in an appendix.
- Compliance scope: which data classes and regulated workloads are touched (CJIS, HIPAA-covered PHI, FTC Safeguards Rule for utility billing, TX-RAMP-aligned cloud services).
- Adopting body and review cycle (commonly biennial; annual for high-risk topics).

Optional:

- Existing policies the new policy replaces or amends.
- Reference to the city's AI-AMF framework adoption, if any.
- Personnel manual sanctions language so the policy does not contradict it.

If topic, scope, or adopting authority is not specified, ask before drafting. Do not invent a framework alignment.

## Process

1. Confirm topic, scope, adopting authority, and primary framework. For a generative AI use policy, confirm whether the policy must align with HB 3512 AI literacy training and the city's NIST AI RMF posture.
2. Map the policy topic to NIST CSF 2.0 functions and to the most relevant NIST SP 800-53 Rev. 5 control families. See `references/nist-csf-control-mapping.md`.
3. Draft the policy using the nine-section structure below. Keep policy statements at the level of *what* and *who*, not *how*; procedural detail belongs in a separate standard or runbook.
4. For each requirement, note the control family in a comment column so the CIO can verify framework coverage at review.
5. Assign roles to specific titles, not individuals. Include the CIO, the data or business owner, end users, and (where applicable) the privacy officer and records management officer.
6. Reference the personnel manual for sanctions. Do not draft new sanctions; defer to HR.
7. List related documents, the records retention schedule, the AI use policy (if separate), and any DIR or TX-RAMP requirements that drive the policy.
8. Add review cycle, effective date, and adopting authority. Use an ordinance or resolution number placeholder for council-adopted policies.

## Output Format

```
[ENTITY NAME]
[POLICY TITLE]
Policy No. [IT-XXX]
Effective: [DATE]
Adopted by: [COUNCIL/CITY MANAGER/IT STEERING COMMITTEE]
Review cycle: [ANNUAL/BIENNIAL]

1. PURPOSE
[One paragraph stating the policy's objective and what risk it manages.]

2. SCOPE
[Who is covered: employees, contractors, volunteers, vendors with city access.
Which systems and data classes are covered.]

3. DEFINITIONS
[Defined terms used in the policy, listed alphabetically.]

4. POLICY STATEMENT
4.1 [Requirement] — [Control family reference, e.g., NIST 800-53 AC-2]
4.2 [Requirement] — [Control family reference]
...

5. ROLES AND RESPONSIBILITIES
| Role | Responsibility |
|---|---|
| Chief Information Officer | [Owns policy, approves exceptions] |
| Data Owner / Business Owner | [Approves access to their data] |
| End User | [Complies, reports incidents] |
| Privacy Officer | [Reviews PII handling] |
| Records Management Officer | [Ensures retention compliance] |

6. COMPLIANCE AND ENFORCEMENT
[Reference personnel manual. Note that violations may result in
discipline up to and including termination, consistent with the city's
progressive discipline policy.]

7. EXCEPTIONS
[Process for requesting a written exception. Exceptions expire after a
defined period and require CIO sign-off.]

8. RELATED DOCUMENTS
[List of related policies, standards, runbooks, and the records retention
schedule.]

9. REVIEW AND REVISION HISTORY
| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | [Date] | [CIO] | Initial adoption |
```

Length: 4–8 pages. AI use and incident response policies trend toward 7–8; password policies toward 4–5.

Tone: directive, plain. Use "shall" for binding requirements; "may" and "should" for discretionary items.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot or automated voice assistant). The trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

Transparency about AI assistance in drafting is still sound practice and should align with the city's adopted AI use policy and GovAI Coalition guidance. A brief notation on public-distribution documents — *"AI-assisted draft, reviewed by [staff title and name]"* — is a policy choice, not a statutory mandate.

**Texas DIR authority:** Tex. Gov't Code Ch. 2054 vests the Department of Information Resources with statewide information resource management authority. Cities are not state agencies under Ch. 2054 but should align with DIR's information security standards. Tex. Gov't Code § 2054.1125 requires reporting of certain cybersecurity incidents.

**TX-RAMP scope:** Tex. Gov't Code Ch. 2059 establishes TX-RAMP for cloud services consumed by state agencies. Cities are not directly subject to TX-RAMP but many now require TX-RAMP Level 1 or 2 authorization as a procurement floor.

**Personnel-policy interaction:** Acceptable use, BYOD, and AI use policies create employment obligations. Route through HR and the city attorney before adoption. Sanctions belong in the personnel manual.

**Public records:** The adopted policy is a public record under Tex. Gov't Code Ch. 552. Drafts and internal comments may be excepted under § 552.111 (agency memoranda) until adoption.

**Retention:** Adopted IT policies retain permanently per the Texas State Library and Archives Commission (TSLAC) Local Government Retention Schedule GR, Item 1000-21 (Administrative Policies and Procedures).

## References

- See `references/nist-csf-control-mapping.md` for a mapping of common municipal IT policy topics to NIST CSF 2.0 functions and NIST SP 800-53 Rev. 5 control families, with a note on TX-RAMP scope.

## Examples

- See `examples/ai-use-acceptable-use-policy.md` for a worked example: a generative AI acceptable use policy for a Texas city aligned with TRAIGA, NIST AI RMF 1.0, and HB 3512.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
