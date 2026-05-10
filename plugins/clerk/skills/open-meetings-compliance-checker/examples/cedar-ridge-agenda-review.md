# Example: Pre-Posting TOMA Review — City of Cedar Ridge June 9, 2026 Agenda

This is a worked example for the open-meetings-compliance-checker skill. It reviews the City of Cedar Ridge, TX regular council meeting agenda for June 9, 2026, drafted by the agenda-builder skill. The two skills are designed to be used as a pair: the agenda-builder produces the agenda, and this skill clears it for posting.

## Input

- **Entity:** City of Cedar Ridge, TX (home-rule, council-manager, population approximately 32,000)
- **Governing body:** City Council
- **Meeting type:** Regular
- **Meeting time:** Tuesday, June 9, 2026, 6:30 p.m.
- **Intended posting:** Friday, June 5, 2026, 4:30 p.m.
- **Agenda items:** Ten items as drafted by the agenda-builder example (consent agenda, two public hearings on budget amendment and rezoning Case Z-2026-04, two regular business items including a Ch. 252 contract award and Resolution 2026-14 recognizing retiring City Secretary Helen Marquez, executive session under §§ 551.071 and 551.074, reconvene and action, council comments, adjournment)
- **Reviewer:** Marisol Tovar, incoming City Secretary
- **Notes from staff:** All ancillary notices for the rezoning and the budget amendment hearing have been run. The City Attorney has cleared the litigation citation in the executive session item.

## Output

```
TOMA COMPLIANCE REVIEW — CITY OF CEDAR RIDGE, REGULAR MEETING JUNE 9, 2026

Reviewed by: Marisol Tovar, City Secretary
Review date: June 4, 2026
Intended posting: Friday, June 5, 2026 at 4:30 p.m.
Meeting time: Tuesday, June 9, 2026 at 6:30 p.m.

1. POSTING TIMELINE CHECK
   Gap from posting to meeting: 4 days 2 hours. Exceeds the 72-hour
   minimum under Tex. Gov't Code § 551.043. PASS.

   Internet posting under § 551.056: Cedar Ridge has a population of
   approximately 32,000 and falls below the 48,000 statutory threshold
   for required internet posting. The city's adopted practice is to
   post on the website as a matter of policy. Recommend continuing
   that practice and posting the agenda to www.cedarridgetx.gov
   concurrently with the bulletin board.

   No state or local holiday falls between June 5 and June 9 that
   would affect posting.

2. SUBJECT SPECIFICITY CHECK
   Item 1 (Call to order, roll call, and determination of quorum):
     Standard procedural item. PASS.

   Item 2 (Invocation and pledges):
     Standard procedural item. PASS.

   Item 3 (Public comment):
     Comment language tracks § 551.007 and § 551.042. PASS.

   Item 4 (Consent agenda):
     4a (May 26 minutes): PASS.
     4b (Check register, May 2026, $1,847,302.14): PASS. Stating the
        amount is good practice.
     4c (Interlocal with Caddo County, animal control, NTE $84,000,
        Ch. 791): PASS.

   Item 5a (Budget amendment hearing — $312,000 reallocation from
   contingency to Street Maintenance): PASS. Caption identifies the
   amount, the funds involved, the program affected, and the controlling
   statute under Tex. Loc. Gov't Code § 102.0065.

   Item 5b (Rezoning Z-2026-04, 1100 Pecan Street, R-1 to NC-1): PASS.
   Caption identifies the case number, the address, the requested
   change, and the controlling statute under Tex. Loc. Gov't Code
   Ch. 211.

   Item 6a (FY2026 street overlay contract award, lowest responsible
   bidder, Ch. 252): RECOMMEND TIGHTENING. The caption identifies the
   project and statutory authority but does not state the dollar range
   or term. Recommend appending the not-to-exceed amount or the bid
   range from the packet so the public has notice of the financial
   stake.

   Item 6b (Resolution 2026-14, recognition of retiring City Secretary
   Helen Marquez): PASS.

   Item 7a (§ 551.071 consultation — Smith v. City of Cedar Ridge,
   Cause No. 2026-CV-118, 235th District Court of Caddo County): PASS.
   Specific cause and court. City Attorney has cleared the caption.

   Item 7b (§ 551.074 — annual evaluation of City Manager Daniel Ahn):
   PASS. The statute affords Mr. Ahn the right to request an open
   hearing under § 551.074(b); confirm this has been offered.

   Item 8 (Reconvene and action on executive session items): PASS.

   Item 9 (City Manager and Council comments): PASS. Caption notes
   no deliberation or action, tracking § 551.0415.

   Item 10 (Adjournment): PASS.

3. EXECUTIVE SESSION CITATION CHECK
   Items 7a and 7b each cite the specific § 551.07x exception and
   identify the subject with sufficient detail. PASS.

4. PUBLIC COMMENT COMPLIANCE
   Three-minute speaker limit and pre-meeting comment form are
   stated. The agenda recites the § 551.007 hearing right and the
   § 551.042 limitation on deliberating non-posted items. PASS.

5. SPECIAL-NOTICE ITEMS
   Item 5a (budget amendment hearing): Tex. Loc. Gov't Code § 102.0065
   requires newspaper publication at least 10 days before the hearing.
   Staff has confirmed publication in the Cedar Ridge Gazette on
   May 29, 2026, which clears the 10-day window. PASS.

   Item 5b (rezoning hearing Z-2026-04): Tex. Loc. Gov't Code § 211.007
   requires mailed notice to property owners within 200 feet at least
   10 days before the hearing, and newspaper publication at least 15
   days before. The agenda-builder example reflects May 19 mailing
   and May 22 publication, both of which clear the windows. PASS.

   No tax rate, budget adoption, bond election, or charter amendment
   notice is implicated on this agenda.

6. MEMBER-REQUESTED ITEMS
   Resolution 2026-14 (Item 6b) was requested by Mayor Castillo under
   § 551.0411 and is reflected on the posted agenda. PASS.

7. RECONVENE AND ACTION LANGUAGE
   Item 8 provides for reconvening in open session and acting on
   matters discussed in executive session. PASS.

8. POSTING CERTIFICATION BLOCK
   Block present with placeholders for date and time. The certification
   in the agenda-builder example cites "Tex. Gov. Code §§ 551.043 and
   551.056." RECOMMEND CITATION CORRECTION to "Tex. Gov't Code"
   (apostrophe-t) to match Bluebook and Attorney General format. The
   substance of the citation is correct; this is a style fix.

OVERALL FINDING: PASS WITH RECOMMENDED FIXES

Recommended fixes (paste-ready language):

  - Item 6a: replace caption with:
    "6a. Discussion and possible action awarding the FY2026 street
    overlay contract in an estimated amount of $[NTE] to the lowest
    responsible bidder under Tex. Loc. Gov't Code Ch. 252. Bid
    tabulation and staff recommendation included in the packet.
    Presented by Public Works Director Patel."

  - Posting certification block: replace "Tex. Gov. Code" with
    "Tex. Gov't Code" in both citations.

Next steps before posting:
  1. Confirm City Manager Ahn's response on the § 551.074(b) open
     hearing election.
  2. Apply the two recommended fixes above.
  3. Post on the bulletin board and the city website Friday, June 5
     at 4:30 p.m.
  4. Sign and date the posting certification at the moment of posting.

This compliance review was drafted with the assistance of artificial
intelligence tools and reviewed by the City Secretary.
```

## Notes for the User

- The Cedar Ridge population is under the § 551.056 internet posting threshold, but the city's adopted practice exceeds the statutory minimum. Maintaining that practice and documenting it in the records management policy provides a defensible posture if the city's population crosses the threshold in the future or if a citizen challenges website availability of the agenda.
- The citation correction in the posting certification block is stylistic but worth catching: the Government Code abbreviation in Texas Bluebook and AG style is "Gov't" with an apostrophe. The Business and Commerce Code uses "Bus. & Comm." — different code, different abbreviation.
- This review intentionally stops at compliance. It does not opine on the substance of the items, the merits of the rezoning, the bidder selection, or the executive session matters. Those judgments belong to council and staff.
- Continuity: the same Z-2026-04 rezoning case appears in the tpia-response-drafter example (request for council emails about the case).
