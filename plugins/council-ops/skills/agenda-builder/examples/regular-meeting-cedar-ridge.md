# Example: Regular Meeting Agenda — City of Cedar Ridge

This is a worked example for the agenda-builder skill. It uses the fictional City of Cedar Ridge, TX. The same city appears in other council-ops examples (minutes-drafter, council-packet-prep, ordinance-tracker, resolution-drafter) so that a user can read across all six and see one meeting end to end.

## Input

- **Entity:** City of Cedar Ridge, TX (home-rule, council-manager, population 32,000)
- **Meeting type:** Regular
- **Date and time:** Tuesday, June 9, 2026, 6:30 p.m.
- **Location:** Council Chambers, Cedar Ridge City Hall, 200 Live Oak Drive, Cedar Ridge, TX 75000
- **Items submitted:**
  1. Approve minutes of May 26, 2026 regular meeting (consent)
  2. Approve check register for May 2026 (consent)
  3. Approve interlocal agreement with Caddo County for animal control (consent)
  4. Public hearing — proposed FY2026 budget amendment (street maintenance reallocation) — Finance Director Rivera
  5. Public hearing and possible action — rezoning request, 1100 Pecan Street, from Single-Family Residential (R-1) to Neighborhood Commercial (NC-1), Case Z-2026-04 — Planning Director Okafor
  6. Discuss and consider awarding the FY2026 street overlay contract to lowest qualified bidder — Public Works Director Patel
  7. Discuss and consider Resolution 2026-14 honoring retiring City Secretary Helen Marquez — Mayor Castillo
  8. Executive session — § 551.071 consultation with City Attorney regarding pending litigation in *Smith v. City of Cedar Ridge*; § 551.074 annual evaluation of City Manager Daniel Ahn
  9. City Manager and Council comments

## Output

```
CITY OF CEDAR RIDGE, TEXAS
CITY COUNCIL
REGULAR MEETING AGENDA
Tuesday, June 9, 2026 — 6:30 p.m.
Council Chambers, Cedar Ridge City Hall
200 Live Oak Drive, Cedar Ridge, TX 75000

Posted: ____________________________ (to be completed by the City Secretary at posting)

1. CALL TO ORDER, ROLL CALL, AND DETERMINATION OF QUORUM

2. INVOCATION AND PLEDGES OF ALLEGIANCE
   Voluntary invocation. Pledges to the United States flag and the
   State of Texas flag.

3. PUBLIC COMMENT
   The Council will receive public comment on items posted on this
   agenda and on matters of public concern under Tex. Gov't Code
   § 551.007. Each speaker is limited to three (3) minutes. Speakers
   must complete a comment form before the meeting is called to order.
   The Council may not deliberate or take action on items not posted
   under § 551.042; comments on non-posted matters may be referred to
   staff or placed on a future agenda.

4. CONSENT AGENDA
   These items are considered routine and will be approved by a single
   motion unless a member of Council asks that an item be removed for
   separate consideration.

   4a. Approval of the minutes of the May 26, 2026 regular meeting.
   4b. Approval of the check register for the period of May 1–31, 2026,
       in the amount of $1,847,302.14.
   4c. Approval of an interlocal cooperation agreement with Caddo County
       for animal control services for FY2026, with a not-to-exceed
       amount of $84,000, authorized under Tex. Gov't Code Ch. 791.

5. PUBLIC HEARINGS

   5a. Public hearing on a proposed amendment to the FY2026 adopted
       budget reallocating $312,000 from the General Fund contingency
       reserve to the Street Maintenance program. Notice published per
       Tex. Loc. Gov't Code § 102.0065. Presented by Finance Director
       Rivera.

   5b. Public hearing and possible action on Case Z-2026-04, a request
       to rezone the property at 1100 Pecan Street from Single-Family
       Residential (R-1) to Neighborhood Commercial (NC-1). Authorized
       under Tex. Loc. Gov't Code Ch. 211. Notice mailed to property
       owners within 200 feet on May 19, 2026, and published in the
       Cedar Ridge Gazette on May 22, 2026. Presented by Planning
       Director Okafor.

6. REGULAR BUSINESS — INDIVIDUAL CONSIDERATION

   6a. Discussion and possible action awarding the FY2026 street
       overlay contract to the lowest responsible bidder under Tex.
       Local Gov. Code Ch. 252. Bid tabulation and staff recommendation
       included in the packet. Presented by Public Works Director Patel.

   6b. Discussion and possible action on Resolution 2026-14, a
       resolution of the Cedar Ridge City Council recognizing City
       Secretary Helen Marquez upon her retirement after twenty-five
       years of service. Presented by Mayor Castillo.

7. EXECUTIVE SESSION
   The Council may convene in closed executive session pursuant to the
   Texas Open Meetings Act, Tex. Gov't Code Ch. 551, for the following
   purposes:

   7a. § 551.071 — Consultation with the City Attorney regarding pending
       litigation styled *Smith v. City of Cedar Ridge*, Cause No.
       2026-CV-118 in the 235th District Court of Caddo County.

   7b. § 551.074 — Personnel matter: annual performance evaluation of
       City Manager Daniel Ahn.

8. RECONVENE IN OPEN SESSION AND ACTION ON EXECUTIVE SESSION ITEMS
   The Council will reconvene in open session and may take any action
   deemed necessary on the matters discussed in executive session.

9. CITY MANAGER AND COUNCIL COMMENTS
   Reports on items of community interest. No deliberation or action.

10. ADJOURNMENT

CERTIFICATION OF POSTING

I, Helen Marquez, City Secretary of the City of Cedar Ridge, Texas,
certify that the foregoing agenda was posted on the public bulletin
board at Cedar Ridge City Hall, 200 Live Oak Drive, Cedar Ridge, TX,
and on the City's internet website at www.cedarridgetx.gov, on
__________________ at ___________ a.m./p.m., not less than seventy-two
(72) hours before the scheduled meeting time, in accordance with Tex.
Gov. Code §§ 551.043 and 551.056.

____________________________________
Helen Marquez, City Secretary

Persons with disabilities who plan to attend this meeting and who may
need auxiliary aids or services are requested to contact the City
Secretary's office at (555) 555-0100 at least 48 hours in advance so
reasonable accommodations can be made.

This agenda was drafted with the assistance of artificial intelligence
tools and reviewed by the City Secretary before posting.
```

## Notes for the User

- Mailed notice for the zoning hearing must be sent at least 10 days before the hearing under § 211.007 — verify the May 19 mailing satisfies this.
- The budget amendment hearing notice publication date should be at least 10 days before the hearing under § 102.0065(b).
- For the lowest-responsible-bidder language under Ch. 252, confirm the bid was advertised once a week for two consecutive weeks.
- The City Manager evaluation under § 551.074 entitles Mr. Ahn to request an open hearing; confirm with him before the meeting.
- The litigation citation should be confirmed by the City Attorney before posting.
