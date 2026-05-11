---
name: ordinance-impact-analyzer
description: Analyzes a proposed Texas city ordinance for conflicts with the city charter, existing code, state preemption, federal preemption, and constitutional limits, and identifies enforceability and authority issues before introduction. Use when the city attorney's office, a sponsoring council member's staff, or the city manager's office needs a pre-introduction legal screen on a proposed ordinance.
---

# Ordinance Impact Analyzer

> Produces a structured legal impact analysis on a proposed ordinance, covering authority, conflicts, preemption, enforcement, and constitutional concerns. Built for city attorneys screening drafts before council introduction.

## When to Use

- "Council Member Reyes wants to file a short-term rental ordinance. Run the legal screen."
- "Analyze the draft sign code for preemption and First Amendment issues."
- "We have a proposed pet limits ordinance. Check it against the charter and code."
- "Run an impact analysis on this proposed mobile food vendor ordinance before the meeting."
- "The city manager wants to know whether we can adopt this regulation as a city of our size."
- Any proposed ordinance ahead of council introduction or first reading where the attorney needs a structured pre-screen.

## Inputs Needed

Required:

- Proposed ordinance text or summary, including findings and operative sections
- Sponsoring council member or department
- Form of government: home-rule or general-law (drives authority analysis)
- Existing code sections that may be affected (chapter and section)
- Charter sections that may interact

Optional:

- Specific state law the sponsor believes authorizes the ordinance
- Related federal statutes or regulations (telecom, fair housing, ADA, immigration, etc.)
- Prior versions of the ordinance, if any
- Citizen-initiative or petition status, if applicable
- Public-comment summary if first reading has occurred

If the ordinance text is missing operative provisions or an enforcement mechanism, ask before drafting — the analysis cannot proceed without those.

## Process

1. Identify the city's form of government. Home-rule cities (over 5,000 population with an adopted charter) have all powers not denied by state law (Tex. Loc. Gov't Code § 51.072); general-law cities have only powers expressly granted.
2. Locate authority to adopt. If home-rule, ask whether the ordinance is denied by state law. If general-law, find the specific grant in Title 7 of the Tex. Loc. Gov't Code or elsewhere.
3. Charter conflict screen. Charter prevails over ordinance under Tex. Loc. Gov't Code § 9.005. Look for: powers reserved to the council, supermajority requirements, mandatory referenda, and procurement limits.
4. Existing code conflict screen. Identify code sections that conflict or overlap. Recommend repeal, amendment, or coordination amendments.
5. State preemption analysis. Check each operative provision against: Tex. Loc. Gov't Code § 1.005; HB 2127 (effective 2023 — preemption in Agriculture, Business & Commerce, Finance, Insurance, Labor, Natural Resources, Occupations, and Property Codes) and subsequent expansion; and subject-matter preemption (firearms under Tex. Loc. Gov't Code § 229.001; oil and gas under Tex. Nat. Res. Code § 81.0523; etc.).
6. Federal preemption analysis. Common topics: telecommunications (47 U.S.C. § 253); aviation (49 U.S.C. § 41713); ERISA; immigration; Fair Housing Act; ADA.
7. Enforcement mechanism analysis. Confirm penalties, civil enforcement under Tex. Loc. Gov't Code § 54.001 et seq., criminal penalties capped at $500 or $2,000 for health-and-safety/zoning under § 54.001, administrative penalties, and standing.
8. Constitutional concerns screen. First Amendment for speech, advertising, or assembly regulation; Equal Protection for any classification; Fourth Amendment for inspection or warrant provisions; Takings for property regulation; Due Process for license or permit revocation.
9. Recommendation. Adopt as drafted; adopt with stated amendments; defer; do not adopt.

## Output Format

A legal analysis memo, four to seven pages, addressed to the city attorney and the sponsor, structured as follows:

```
MEMORANDUM — Ordinance Impact Analysis
Privileged work product

To:        [City Attorney]; [Sponsor]
From:      [Author]
Date:      [Date]
Re:        Proposed Ordinance — [Short Title]
           [Sponsoring Council Member or Department]

1. ORDINANCE SUMMARY
   One to two paragraphs describing what the ordinance does.

2. AUTHORITY FOR ADOPTION
   Home-rule or general-law analysis. Specific statutory grants, if any.

3. CHARTER CONFLICTS
   Article and section by article and section. None, if none.

4. EXISTING CODE CONFLICTS
   Code chapter and section. Recommended repeals or amendments.

5. STATE PREEMPTION ANALYSIS
   Provision by provision. Cite the preempting statute.

6. FEDERAL PREEMPTION ANALYSIS
   Where applicable.

7. ENFORCEMENT MECHANISM ANALYSIS
   Penalty, enforcement authority, standing, due process.

8. CONSTITUTIONAL CONCERNS
   First Amendment / Equal Protection / Takings / Due Process /
   Fourth Amendment, as applicable.

9. POLICY OBSERVATIONS
   Drafting issues, enforceability concerns, and operational notes
   that are not strictly legal but affect implementation.

10. RECOMMENDATION
    Adopt | Adopt with stated amendments | Defer | Do not adopt.

11. ATTACHMENTS
    Redline of the draft, if amendments are recommended.
```

Tone: legal-analytic, neutral, no advocacy for or against the policy. The memo screens legality, not wisdom. Distinguish clearly between "this is unlawful" and "this is unwise."

## Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Privilege:** The memo is attorney work product and attorney-client privileged communication when prepared at the attorney's direction. Mark privileged and route to the attorney, the city manager, and the sponsor only. Inclusion of policy observations does not waive privilege but be cautious about disclosure to non-clients.

**Public information:** The memo is excepted under Tex. Gov't Code § 552.107 (attorney communications) and § 552.111 (agency memoranda). The proposed ordinance, once introduced, is a public record. If the memo is later quoted in open session or a public document, privilege may be waived as to the disclosed portions.

**Open meetings:** Council deliberation on the ordinance is in open session unless an executive session exception applies. Legal advice on the ordinance may be discussed in executive session under Tex. Gov't Code § 551.071.

**Retention:** Ordinances retain permanently per Texas State Library Local Government Retention Schedule. Legal opinions and impact analyses retain per the city attorney's records-retention practice, generally 10 years.

## References

- See `references/state-preemption-quick-reference.md` for a categorized list of the major Texas state-law preemption regimes affecting city ordinances, with citations and typical fact patterns.

## Examples

- See `examples/short-term-rental-ordinance-analysis.md` for a worked example: an impact analysis of a Cedar Ridge short-term rental ordinance, addressing HB 2127 and HB 14 preemption, charter authority, and First Amendment advertising concerns.

> **Advisory scaffolding — not legal advice. Review by city attorney required.**

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
