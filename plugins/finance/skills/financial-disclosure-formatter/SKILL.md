---
name: financial-disclosure-formatter
description: Formats required financial disclosure statements for elected officials and key non-elected employees under Tex. Loc. Gov't Code Ch. 176 and city charter or code requirements. Use when a city secretary, city manager, or filer needs to prepare an annual or transactional financial disclosure for filing with the local filing authority.
---

# Financial Disclosure Formatter

> Formats the financial disclosure statement filed by an elected official or covered employee. Built for city secretaries and disclosure filers who need a clean, complete, defensible statement on file.

## When to Use

- "Format the annual financial disclosure for the City Manager."
- "Draft the conflict-of-interest disclosure for Council Member Garcia."
- "We have a vendor contract going to council — generate the Form CIS for the Mayor's relationship."
- "Build the disclosure statement for the new department head's onboarding packet."
- A city officer is preparing the annual statement required by city ordinance or a Ch. 176 disclosure.

## Inputs Needed

Required:

- Officer or employee name, title, and the filing entity (city, board, special district)
- Filing type: annual disclosure under city ordinance, Form CIQ vendor questionnaire (Ch. 176, vendor-side), Form CIS officer disclosure (Ch. 176, officer-side), or a transactional disclosure for a specific contract
- Period covered (calendar year for annual filings; specific transaction for transactional)
- Business and substantial interests of the filer and family members in the filing period
- Real property holdings in the city or adjacent jurisdictions
- Gifts received over the city's reportable threshold

Optional:

- Sources of income above a city-defined reporting threshold
- Boards or governing bodies of nonprofits or businesses on which the filer serves
- Litigation or pending administrative actions involving the filer in their official capacity
- Honorarium considerations under Tex. Penal Code § 36.07
- A prior-year disclosure to mirror in voice and structure

If the user has not provided the filing type or the period covered, ask before drafting. The statutory forms (CIQ, CIS) have specific lines that cannot be substituted.

## Process

1. Confirm the filing type. Tex. Loc. Gov't Code Ch. 176 distinguishes *Form CIQ* (vendor-side) and *Form CIS* (officer-side). Many cities also adopt an annual statement of financial interest by ordinance that goes beyond Ch. 176.
2. Confirm the trigger. Form CIS must be filed before the 7th business day after the officer becomes aware of a covered relationship with a vendor that has or seeks a contract.
3. Identify covered relationships under Ch. 176: family within the first degree of consanguinity or affinity; income sources exceeding $2,500 in the prior 12 months; ownership of 10 percent or $15,000+ in a business entity; gifts of more than $100 from a vendor in the prior 12 months.
4. Draft Officer Identification: name, title, mailing address, filing authority.
5. Draft Business Relationships: each entity with a covered relationship, with relationship type and period.
6. Draft Family Member Holdings within the first degree.
7. Draft Gifts Above Threshold: gifts of more than $100 aggregate from a vendor in the prior 12 months.
8. Draft Real Property Holdings: property in the city and adjacent jurisdictions, especially where city actions may affect value.
9. Draft Conflict-of-Interest Statement and Certification: accuracy confirmation, signature block, notarization where required.

## Output Format

Plain markdown. Tone: precise, complete, declarative. The reader is the city secretary and any subsequent records requestor.

Length: 1 to 3 pages depending on the volume of holdings. Structure:

```
[FILING ENTITY] FINANCIAL DISCLOSURE STATEMENT

Filing Type: [Annual / Form CIQ / Form CIS / Transactional]
Filer Name:  [Name]
Title:       [Title]
Filing Authority: [City Secretary, Address]
Period Covered:   [Date range / Transaction reference]
Filed:       [Date]

1. OFFICER IDENTIFICATION
[Name, title, mailing address.]

2. BUSINESS RELATIONSHIPS
[Each entity with a covered relationship, with relationship type
and period.]

3. FAMILY MEMBER HOLDINGS
[Holdings of family members within the first degree of consanguinity
or affinity, where reportable.]

4. GIFTS ABOVE THRESHOLD
[Gifts of more than the reportable threshold received from a vendor
or any source the city's policy requires to be disclosed.]

5. REAL PROPERTY HOLDINGS
[Property held in the city or adjacent jurisdictions.]

6. CONFLICT-OF-INTEREST STATEMENT
[Identification of any matter pending before the city in which the
filer has a substantial interest, with the abstention or recusal
plan.]

7. CERTIFICATION
[Signature block and notarization line if required.]
```

For Form CIQ and Form CIS, follow the Texas Ethics Commission's published form exactly; this skill produces narrative content for the form lines, not a substitute for the form.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas conflict-of-interest framework:**

- Tex. Loc. Gov't Code Ch. 176 — Form CIQ (vendor) and Form CIS (officer) filed with the records administrator. Failure to file is a Class C misdemeanor (§ 176.013).
- Tex. Loc. Gov't Code § 176.003 — gift threshold (gifts exceeding $100 aggregate from a vendor in the prior 12 months).
- Tex. Loc. Gov't Code Ch. 171 — substantial interest in business or real property; abstention from voting required; affidavit of substantial interest filed with the official records custodian.
- Tex. Penal Code § 36.07 — acceptance of honorarium restrictions.
- Tex. Penal Code § 36.08 — gifts to public servants restrictions.
- City charter and code — many home-rule cities adopt a broader annual statement of financial interest by ordinance; consult the local code.

**Public records:** Filed disclosures are public records under Tex. Gov't Code Ch. 552. Form CIQ and Form CIS must be posted on the city's website if one is maintained.

**Retention:** Form CIQ and Form CIS retain at least the period of the relationship or contract plus 4 years (Texas State Library Local Government Retention Schedule GR, Item 1135). Annual statements retain as the local ordinance directs.

**Verify before filing:** Filer has personally reviewed and signed; covered relationships confirmed with family members; gifts and real property reflect the full period; filing is timely (Form CIS within 7 business days of the trigger).

## References

- Texas Ethics Commission, Form CIQ and Form CIS templates at ethics.state.tx.us — the controlling forms.

## Examples

- See `examples/city-manager-annual-disclosure.md` for a worked example: City Manager Daniel Ahn's annual financial disclosure for calendar year 2025, filed with the Cedar Ridge City Secretary.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
