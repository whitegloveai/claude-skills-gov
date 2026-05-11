---
name: tpia-legal-review
description: Reviews a clerk-drafted Texas Public Information Act response under Tex. Gov't Code Ch. 552 for legal sufficiency, required Attorney General referral, exception assertions, redaction adequacy, and business-day clock compliance before the response leaves the city. Use when the city attorney's office must sign off on a TPIA response prepared by the city secretary or records officer.
---

# TPIA Legal Review

> Produces a legal-review memo on a clerk-drafted TPIA response, confirming clock compliance, exception adequacy, redaction completeness, and AG referral sufficiency. Built for the city attorney's office as the final legal check before release.

## When to Use

- "The clerk drafted a TPIA response. Run the legal review before it goes out."
- "We're about to file an AG referral. Confirm the exception assertions and the brief."
- "Review the redactions on this email production for legal sufficiency."
- "The 10-business-day clock closes tomorrow. Sign off or kick it back."
- Any clerk-drafted response under Tex. Gov't Code Ch. 552 awaiting attorney sign-off.

## Inputs Needed

Required:

- The clerk's draft response letter
- Original request text (verbatim)
- Records identified as responsive
- Exceptions being asserted, by section number, with the basis for each
- Redactions proposed (or a redacted set with markings)
- Date the request was received and the 10-business-day clock status
- AG referral status if applicable (referral letter and brief, if drafted)

Optional:

- Third-party notice status under Tex. Gov't Code § 552.305
- Prior AG decisions on similar records (cite OR letter numbers)
- The requester's clarification correspondence, if any
- Cost-estimate calculation if § 552.2615 applies
- The records themselves, in unredacted form, for sampling review

If exceptions are being asserted but the underlying records are not made available for sampling, ask before drafting — the legal review cannot confirm redaction adequacy without seeing the records.

## Process

1. Compute the deadline. Confirm the 10-business-day acknowledgment under Tex. Gov't Code § 552.221. For exceptions requiring AG referral, the city has 10 business days from receipt to ask for an AG decision under § 552.301(b), and 15 business days to submit a brief and the records.
2. Verify the response posture matches the records. If "producing in full," is anything redacted? If "producing with redactions," are the exceptions listed? If "AG referral," is the referral letter drafted?
3. Walk every exception. Confirm: the citation is correct; the factual basis is stated; if the exception requires AG referral (any compelled withholding lacking a prior OR ruling), the referral is in train; if the exception involves third-party information (§ 552.110, § 552.104, etc.), the § 552.305 notice has been sent.
4. Distinguish three categories: (a) records required to be public under § 552.022 — cannot be withheld; (b) records confidential by other law under § 552.101 — must be withheld; (c) discretionary exceptions. Confirm the response is on the right side.
5. Sample-review the redactions. Confirm each redaction matches the cited exception. Watch for over-redaction (e.g., redacting names in attorney emails when only the advice is privileged) and under-redaction (e.g., releasing personal email addresses without § 552.117 or § 552.137).
6. AG referral package review. Confirm timeliness, the brief argument for each exception, identifiable records, and that copies (with records redacted) have been sent to the requester.
7. Required disclosures. Appeal rights, PIO contact, § 552.2615 deposit window if costs over $40, and § 552.305 third-party notice if applicable.
8. Sign-off or kick-back. Return with sign-off if clean; otherwise return markup with required edits and a deadline tied to the clock.

## Output Format

A legal-review memo to the records officer, two to four pages:

```
MEMORANDUM — TPIA Response Legal Review
Privileged — attorney-client communication

To:        [Records Officer / City Secretary]
From:      [Attorney]
Date:      [Date]
Re:        TPIA Request No. [PIR-####] — [Brief description]
           Requester: [Name]
           Date received: [Date]
           Day-10 deadline: [Date]

1. CLOCK CHECK
   Acknowledgment deadline under Tex. Gov't Code § 552.221.
   AG referral deadline under § 552.301(b), if applicable.
   Brief and records to AG under § 552.302, if applicable.
   Status: ON TRACK | AT RISK | MISSED.

2. EXCEPTION ADEQUACY REVIEW
   For each exception asserted:
   - § 552.xxx — [name]
   - Records covered
   - Factual basis stated in letter
   - AG referral required: yes | no | already obtained (OR ####)
   - Status: ADEQUATE | REVISE | INSUFFICIENT

3. REDACTION COMPLETENESS REVIEW
   Sampling notes. Over-redaction | Under-redaction | Adequate.

4. THIRD-PARTY NOTICE STATUS (§ 552.305)
   Records implicating third-party proprietary or privacy interests.
   Notice sent | Not required.

5. REQUIRED DISCLOSURES IN RESPONSE LETTER
   Checklist with status:
   - Verbatim request restated
   - Response posture clear
   - Exception list with citations
   - Cost estimate if applicable
   - Appeal rights notice
   - PIO contact

6. RECOMMENDED EDITS
   Numbered, with markup line if needed.

7. SIGN-OFF
   APPROVED FOR RELEASE | RETURN FOR REVISION | HOLD FOR AG.

[Attorney signature block]
```

Tone: legal-analytic, attorney-to-staff, instructional on close calls. Cite OR letter numbers and AG ruling categories where they support the conclusion.

## Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**TPIA controlling sections (Tex. Gov't Code Ch. 552):** § 552.021 (disclosure rule); § 552.022 (records that cannot be withheld); § 552.101 (confidential by other law); § 552.107 (attorney communications); § 552.108 (law-enforcement); § 552.111 (agency memoranda); § 552.117 (officer/employee personal information); § 552.137 (personal email addresses); § 552.221 (10-business-day response); § 552.222 (clarification pauses the clock); § 552.261 / § 552.2615 (cost rules); § 552.301 (AG referral within 10 business days); § 552.302 (brief and records within 15 business days; non-compliance presumes records public); § 552.305 (third-party notice).

**Privilege:** This memo is attorney-client communication under § 552.107. Mark privileged and do not include in the released file.

**Retention:** TPIA correspondence retains three years after the request closes per Texas State Library Local Government Retention Schedule GR Item 1025-01. Legal review memos retain with the city attorney's file.

## References

- See `references/tpia-exception-decision-tree.md` for whether each major TPIA exception requires AG referral and the standard arguments on the most contested exceptions.

## Examples

- See `examples/council-emails-review.md` for a worked example: legal review of the Cedar Ridge clerk's draft response on the Z-2026-04 zoning emails request, refining the § 552.107 privilege assertion and the § 552.301 AG referral.

> **Advisory scaffolding — not legal advice. Review by city attorney required.**

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
