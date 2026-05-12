---
name: election-notice-generator
description: Drafts a Texas municipal election notice in English and Spanish under the Texas Election Code, including notice of election (Ch. 4), bond election language under § 1251.052 of the Government Code, and bilingual notice required for covered jurisdictions. Use when a city secretary or elections administrator needs a posting-ready notice.
---

# Election Notice Generator

> Drafts a Texas municipal election notice in English and Spanish for general municipal, bond, charter amendment, or special elections. Built for city secretaries and elections administrators posting under deadline.

## When to Use

- "Draft the notice of election for the May 2026 general municipal election."
- "We have a bond election on the November ballot. Build the notice in English and Spanish."
- "The charter amendment vote needs a posted notice. Draft it."
- "Special election for the District 3 council vacancy — generate the notice."
- "Translate the election notice into Spanish and verify the statutory citations."
- Any election where the notice must comply with Tex. Election Code Ch. 4 and, in covered jurisdictions, with the federal Voting Rights Act and Tex. Election Code Ch. 272 bilingual materials requirements.

## Inputs Needed

Required:

- Entity holding the election (city, school district, special district)
- Election type: general municipal, bond, charter amendment, special, runoff
- Election date
- Offices on the ballot and any propositions (proposition number, full proposition text)
- Polling place locations on election day with addresses and hours
- Early voting period (start and end date, hours, locations)
- Name and contact of the early voting clerk
- Bilingual languages required (Spanish is the most common; some jurisdictions also require Vietnamese, Chinese, or other languages under the Voting Rights Act)

Optional:

- Bond election specifics: principal amount, purpose, tax impact statement, maturity schedule
- Charter amendment ballot language as adopted by the council ordering the election
- Mobile or extended early voting locations
- The publication and posting calendar already adopted by the elections administrator
- Identity of the local newspaper of general circulation for publication

If proposition text or bilingual language requirements are missing, ask before drafting. Bond and charter amendment language is statutorily prescribed and must not be paraphrased.

## Process

1. Identify the election type and the controlling Election Code chapters. General municipal elections run under Ch. 4 (notice) and Chs. 41 and 42. Bond elections add Tex. Gov't Code Ch. 1251. Charter amendments add Tex. Loc. Gov't Code Ch. 9.
2. Compute publication and posting deadlines. Notice must publish once in a newspaper of general circulation not earlier than 30 days and not later than 10 days before election day under § 4.003(a)(2). Bulletin board and (if available) website posting begins the 21st day before election day under § 4.003(c).
3. Draft the English notice with the statutorily required content: entity, date, offices or propositions, election-day polling places and hours, early voting period and locations, early voting clerk name and contact, and an accessibility contact.
4. For bond propositions, use the prescribed ballot language under Tex. Gov't Code § 1251.052 (and § 3501.001 et seq. for school districts). The question must include the phrase "The issuance of bonds for [purpose] and the levying of a tax in payment thereof" with a clear principal amount.
5. For charter amendments, recite the ballot language adopted by the ordering ordinance. Do not paraphrase.
6. Translate the notice into Spanish using official Texas Secretary of State phrasing where it exists; otherwise use the city's prepared translation. Do not back-translate ballot language word-for-word.
7. Add polling-location and early-voting tables in both languages.
8. Add the accessibility contact under HAVA and Tex. Election Code § 61.012.
9. Add the signature block for the election ordering authority and a footer citing Tex. Election Code § 4.003.

## Output Format

A two-language notice (English then Spanish) in a single document. Each language block stands alone for the newspaper submission and the bulletin board posting. Structure for each block:

- Header: "NOTICE OF [TYPE] ELECTION / CITY OF [NAME], TEXAS / [ELECTION DATE]"
- Opening paragraph addressing registered voters and stating the election date and purpose
- "PROPOSITIONS" section reproducing each ballot question verbatim
- "ELECTION DAY POLLING LOCATIONS" table (name, address, hours)
- "EARLY VOTING" section with dates, locations table, early voting clerk contact, and the § 84.007 ballot-by-mail deadline
- "ACCESSIBILITY" paragraph citing Tex. Election Code § 61.012
- Signature block and a footer citing Tex. Election Code § 4.003 (and § 1251.003 for bond elections)

See `examples/bond-election-notice.md` for the complete bilingual form.

Tone: formal, statutory, exact. Do not paraphrase ballot language. Do not editorialize about propositions, candidates, or tax impact beyond what statute requires.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Texas Election Code:** Ch. 4 (notice; § 4.003 deadlines, § 4.004 content); Ch. 41 (uniform dates); Ch. 42 (precincts); § 61.012 (accessibility); Ch. 84 (ballot by mail); Ch. 272 (bilingual materials in covered jurisdictions).

**Bond elections (Tex. Gov't Code Ch. 1251):** § 1251.052 prescribes ballot language including principal amount and tax-levy phrase. § 1251.003 requires posting at three public places and on the city website at least 21 days before. Special-purpose bond language under other code provisions (e.g., Ch. 3501 for school districts) controls when applicable.

**Bilingual materials:** The federal Voting Rights Act and Tex. Election Code Ch. 272 require bilingual materials in covered jurisdictions. Most Texas cities are covered for Spanish; additional languages apply in specific counties. Verify coverage with the Texas Secretary of State or the DOJ list before posting.

**Retention:** Election records, including the notice and the posting certification, retain permanently under TSLAC Schedule EL and under Tex. Election Code § 66.058 (election records preservation period).

**Verify before posting:** All proposition language against the ordering ordinance, the bilingual coverage determination, the publication deadline against the newspaper's submission schedule, and the early voting clerk contact.

## References

- Statutory citations are drawn from the Texas Election Code, Tex. Gov't Code Ch. 1251, and Tex. Loc. Gov't Code Ch. 9. The Texas Secretary of State publishes official Spanish translations of standard ballot phrases at sos.state.tx.us.

## Examples

- See `examples/bond-election-notice.md` for a worked example: a $25 million general obligation street improvement bond election notice in English and Spanish.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
