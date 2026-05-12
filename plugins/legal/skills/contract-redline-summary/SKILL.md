---
name: contract-redline-summary
description: Summarizes a vendor's redlines on a city contract draft with categorized risk flags, negotiation recommendations, and routing notes for the city attorney's review. Use when a contract negotiator, assistant city attorney, or department contract liaison receives a vendor's revised contract and needs a structured pre-review memo before the city attorney reads the redline in full.
---

# Contract Redline Summary

> Produces a redline summary memo categorizing every vendor edit on a city contract, flagging risks, and recommending negotiation positions. Built for attorneys who need a fast, structured read of a vendor's changes before line-by-line review.

## When to Use

- "Vendor returned redlines on our SaaS agreement. Summarize what changed and flag the risk."
- "Draft a redline memo for the city attorney on the construction contract changes."
- "Compare the vendor's revisions to our original. Categorize each change and recommend a response."
- "We have a 40-page interlocal back from the other party. Build me a redline summary."
- Any vendor or counterparty return of a city-drafted contract where the city attorney needs a categorized pre-review.

## Inputs Needed

Required:

- Original contract text or section being negotiated (city's starting draft)
- Vendor's redlined version or list of changes (tracked changes, markup, or change inventory)
- Contract type: purchase of goods, professional services, IT/SaaS, construction, interlocal, real estate, or other
- Contract value and term (drives Tex. Loc. Gov't Code Ch. 252 procurement and council-approval thresholds)

Optional:

- Specific risk concerns the attorney wants emphasized (insurance, data, IP, indemnity, etc.)
- Council approval threshold under the city charter or Tex. Loc. Gov't Code § 252.021
- Prior negotiation history or vendor's positions in similar deals
- Whether the vendor is a sole-source or competitively procured
- Any third-party flow-down obligations from grants or other funding sources

If contract type or value is missing, ask before drafting — the analysis depth and risk priorities differ substantially between, e.g., a $25,000 software subscription and a $4 million construction contract.

## Process

1. Build a change inventory. For each redline, capture: section number, original language summary, revised language summary, and a one-line characterization.
2. Categorize each change into one of four categories: substantive (changes a right, duty, or risk allocation), clarifying (improves precision without shifting risk), risk-shift (moves risk from vendor to city or vice versa), or cleanup (typo, cross-reference, formatting).
3. For each substantive and risk-shift change, score risk as high, medium, or low. Use `references/common-contract-risk-categories.md` for the taxonomy and typical red-flag triggers.
4. Cross-check four critical clusters: indemnification scope and any floor on vendor's obligation; liability caps relative to project value; insurance limits and additional-insured status; and data ownership and breach notification (for IT/SaaS).
5. Identify any provision that may be void or unenforceable under Texas law: arbitration provisions in public contracts under Tex. Civ. Prac. & Rem. Code § 154.001 et seq. and Tex. Loc. Gov't Code § 271.154; choice of law away from Texas; venue away from the contracting county; waivers of sovereign immunity beyond what is statutorily authorized.
6. Flag items requiring council approval based on contract value against the city's purchasing thresholds under Tex. Loc. Gov't Code § 252.021 (currently $50,000) or the city's adopted ordinance threshold if lower.
7. Identify items requiring routing to other departments: Finance (payment terms, audit rights), IT (data and security terms), Risk Management (insurance, indemnification), HR (any background check or labor terms).
8. Draft negotiation recommendations: accept, push back with specific counter-language, reject, or escalate to the attorney for a judgment call.

## Output Format

A redline summary memo, three to six pages, structured as follows:

```
MEMORANDUM — Contract Redline Summary
Privileged work product — for city attorney review

To:        [City Attorney]
From:      [Author]
Date:      [Date]
Re:        [Vendor / Contract Title / Project]
Original draft date: [Date]
Vendor return date:  [Date]

1. CONTRACT OVERVIEW
   Type, value, term, sponsoring department, council approval status.

2. SUMMARY OF VENDOR POSITION
   One paragraph characterizing the overall thrust of the vendor's changes.

3. CHANGE INVENTORY
   Table with: Section | Vendor Change | Category | Risk

4. RISK FLAGS — HIGH
   Each flag: section, what changed, why it's high risk, recommended response.

5. RISK FLAGS — MEDIUM
   Same structure, abbreviated.

6. RISK FLAGS — LOW / CLEANUP
   Bullet list.

7. PROVISIONS POTENTIALLY VOID OR UNENFORCEABLE UNDER TEXAS LAW
   Any item flagged under Process Step 5.

8. NEGOTIATION RECOMMENDATIONS
   By section, with specific counter-language where appropriate.

9. COUNCIL APPROVAL REQUIRED
   Under Tex. Loc. Gov't Code § 252.021 and city ordinance.

10. ROUTING — OTHER DEPARTMENT REVIEW
    Finance | IT | Risk Management | HR | Other.

11. OPEN QUESTIONS FOR THE CITY ATTORNEY
    Items the author could not resolve.
```

Tone: factual, attorney-to-attorney, no editorializing about the vendor. Cite contract sections precisely. Quote vendor language only when the exact wording matters. Do not characterize a redline as "bad faith" or similar — the memo is a working document that may be discoverable.

## Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Privilege:** The memo is attorney work product when prepared at the attorney's direction in anticipation of contract negotiation. Mark it "Privileged work product — for city attorney review" and route only to the attorney and necessary internal reviewers. Privilege is waived by external disclosure.

**Public information:** The final executed contract is public under Tex. Gov't Code Ch. 552. Drafts and the redline memo are exempt while in deliberation under § 552.111 (agency memoranda), and the legal-advice portions are excepted under § 552.107. Mark privileged portions clearly.

**Procurement:** Council approval thresholds under Tex. Loc. Gov't Code § 252.021. Construction performance and payment bonds under Tex. Gov't Code Ch. 2253 (over $50,000 payment bond; over $100,000 performance bond).

**Retention:** Contract files retain 10 years after contract expiration per Texas State Library Local Government Retention Schedule GR Item 1050-26. The legal review memo retains as part of the contract file.

## References

- See `references/common-contract-risk-categories.md` for the taxonomy of typical municipal contract risk areas and the standard red-flag triggers in each.

## Examples

- See `examples/saas-permit-tracking-redline-summary.md` for a worked example: a redline summary memo on a SaaS permit-tracking contract showing 14 vendor edits with three high-risk flags on data ownership, indemnification, and breach notification timing.

> **Advisory scaffolding — not legal advice. Review by city attorney required.**

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
