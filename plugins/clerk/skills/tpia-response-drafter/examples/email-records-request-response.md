# Example: Council Email Records Response — City of Cedar Ridge

This is a worked example for the tpia-response-drafter skill. The fictional City of Cedar Ridge, TX anchors examples across the clerk and council-ops plugins. This example continues the Z-2026-04 rezoning thread introduced in the agenda-builder example.

## Input

- **Entity:** City of Cedar Ridge, TX
- **Requester:** Joanne Reyes, Cedar Ridge Gazette
  - 412 Magnolia Avenue, Cedar Ridge, TX 75000
  - jreyes@cedarridgegazette.com
- **Date received:** Monday, May 26, 2026
- **Reference number:** PIR-2026-118
- **Request text:** *"All emails sent or received by Mayor Castillo and any member of the Cedar Ridge City Council between April 1, 2026 and May 22, 2026 that reference the property at 1100 Pecan Street or Case Z-2026-04."*
- **Response posture:** Partial production with redactions and one AG referral
- **Records identified:** 47 emails across five council mailboxes
- **Withholding posture:**
  - 12 emails between council and the City Attorney containing legal advice — § 552.107(1)
  - 2 emails containing a constituent's home address — § 552.117 (employee election does not apply; treated under § 552.101 reading-in of common-law privacy as a backstop)
  - 1 email chain involving negotiation with the property owner regarding a possible city acquisition adjacent to the parcel — referring to the Attorney General under § 552.301 with § 552.105 asserted
- **Cost:** Under $40 threshold — no charge

## Output

```
CITY OF CEDAR RIDGE, TEXAS
OFFICE OF THE CITY SECRETARY
200 Live Oak Drive
Cedar Ridge, TX 75000
(555) 555-0100

June 6, 2026

Ms. Joanne Reyes
Cedar Ridge Gazette
412 Magnolia Avenue
Cedar Ridge, TX 75000

Re: Public Information Request received May 26, 2026
    Reference No. PIR-2026-118

Dear Ms. Reyes:

This letter responds to the public information request that the City of
Cedar Ridge received on May 26, 2026, in which you requested:

"All emails sent or received by Mayor Castillo and any member of the
Cedar Ridge City Council between April 1, 2026 and May 22, 2026 that
reference the property at 1100 Pecan Street or Case Z-2026-04."

The City conducted a search of the official mailboxes of Mayor Castillo,
Mayor Pro Tem Whitfield, and Council Members Aragon, Bell, Diaz, Han,
and Park. The search identified 47 responsive emails.

Production. The City is producing 34 of the responsive emails today by
secure file transfer to the email address above. A delivery link will
follow this letter.

Redactions. The City is withholding portions of 14 emails under the
following exceptions to disclosure:

  - Tex. Gov't Code § 552.107(1) — Attorney-client privilege.
    Twelve emails contain communications between members of the Council
    and the City Attorney, exchanged for the purpose of obtaining legal
    advice regarding Case Z-2026-04 and related land-use matters.

  - Tex. Gov't Code § 552.117 and § 552.101 — Personal information.
    Two emails contain the home address of a private constituent
    provided in the course of correspondence with the Council and not
    intended for public release.

Attorney General referral. The City is withholding one additional email
chain pending a ruling from the Office of the Attorney General. The
chain concerns the possible acquisition of a parcel adjacent to 1100
Pecan Street and contains information that may be excepted under Tex.
Gov't Code § 552.105 (information relating to location or price of
property). Under Tex. Gov't Code § 552.301, the City has requested a
ruling and a copy of the referral letter is enclosed for your records.
The Attorney General will issue a decision, and the City will release
any portion of the chain consistent with that decision.

Appeal rights. You may submit a written objection to any portion of
this response to the Office of the Attorney General, Open Records
Division, P.O. Box 12548, Austin, TX 78711-2548. Questions regarding
this response may be directed to the City's Public Information Officer
at the address above or at pir@cedarridgetx.gov.

Sincerely,

Marisol Tovar
City Secretary
City of Cedar Ridge, Texas

Enclosure: § 552.301 Referral Letter (Office of the Attorney General)

This response was drafted with the assistance of artificial intelligence
tools and reviewed by the City Secretary and the City Attorney before
issuance.
```

## Notes for the User

- The May 26 receipt date and the June 6 letter date land within the 10-business-day window under § 552.221 (counting forward across the Memorial Day weekend, excluding Monday May 25 as a state holiday).
- The § 552.301 referral letter to the AG must be sent the same day as this response so the 10-business-day clock for referral is met. Verify postmark.
- The legal-arguments brief to the AG follows within 15 business days under § 552.302. The City Attorney has the brief on calendar for June 16, 2026.
- The retiring City Secretary, Helen Marquez, has been succeeded by Marisol Tovar effective June 1, 2026. Signatures on TPIA correspondence after that date should reflect the successor.
- Continuity with the agenda-builder example: Case Z-2026-04 is the same rezoning case scheduled for public hearing on the June 9, 2026 Cedar Ridge council agenda.
- The City Attorney should review the redacted set against the privilege log before delivery to confirm no inadvertent waiver occurred through routing to non-council recipients.
