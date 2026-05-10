# Example: FY2026 Tax Rate Hearing Notice — City of Cedar Ridge

This is a worked example for the public-notice-formatter skill. The fictional City of Cedar Ridge, TX is proposing a property tax rate for FY2026 that exceeds the no-new-revenue tax rate, in part because of incremental debt service capacity built into the FY2026 rate to support the $25 million street improvement bond issuance noticed in the election-notice-generator example.

## Input

- **Entity:** City of Cedar Ridge, TX
- **Notice type:** Tax rate hearing under Tex. Tax Code § 26.06
- **Hearing date and place:** Tuesday, September 8, 2026, 6:30 p.m., Council Chambers, Cedar Ridge City Hall, 200 Live Oak Drive
- **FY2026 tax rate inputs (assumed for the example, all values per $100 of taxable value):**
  - No-new-revenue tax rate: $0.4612
  - Voter-approval tax rate: $0.5108
  - Proposed total tax rate: $0.5025
  - Proposed M&O (maintenance and operations) rate: $0.3825
  - Proposed I&S (debt service) rate: $0.1200
- **Average homestead taxable value FY2025:** $278,400
- **Average homestead taxable value FY2026:** $292,150
- **Tax on average homestead at adopted FY2025 rate ($0.4950):** $1,378.08
- **Tax on average homestead at proposed FY2026 rate:** $1,467.55
- **Difference per average homestead:** an increase of $89.47 per year
- **Newspaper:** Cedar Ridge Gazette
- **City Secretary:** Marisol Tovar
- **Posting:** Publish at least 7 days before the hearing under § 26.06(b), and post on the city's website beginning the date of the first publication

## Output

```
NOTICE OF PUBLIC HEARING ON TAX INCREASE
CITY OF CEDAR RIDGE, TEXAS
PROPOSED FY2026 TAX RATE

Controlling statute: Tex. Tax Code § 26.06
Posting deadline: At least 7 days before the hearing date of
Tuesday, September 8, 2026

PROPOSED TAX RATE                            $0.5025 per $100
NO-NEW-REVENUE TAX RATE                      $0.4612 per $100
VOTER-APPROVAL TAX RATE                      $0.5108 per $100

The no-new-revenue tax rate is the tax rate for the 2026 tax year that
will raise the same amount of property tax revenue for the City of
Cedar Ridge from the same properties in both the 2025 tax year and
the 2026 tax year.

The voter-approval rate is the highest tax rate that the City of
Cedar Ridge may adopt without holding an election to seek voter
approval of the rate.

The proposed tax rate is greater than the no-new-revenue tax rate.
This means that the City of Cedar Ridge is proposing to increase
property taxes for the 2026 tax year.

A PUBLIC HEARING ON THE PROPOSED TAX RATE WILL BE HELD ON:

  Tuesday, September 8, 2026, at 6:30 p.m.
  Council Chambers, Cedar Ridge City Hall
  200 Live Oak Drive, Cedar Ridge, TX 75000

The proposed tax rate is not greater than the voter-approval tax rate.
As a result, the City of Cedar Ridge is not required to hold an
election at which voters may accept or reject the proposed tax rate.
However, you may express your support for or opposition to the
proposed tax rate by contacting the members of the City Council of
the City of Cedar Ridge at their offices or by attending the public
hearing mentioned above.

YOUR TAXES OWED UNDER ANY OF THE TAX RATES MENTIONED ABOVE CAN BE
CALCULATED AS FOLLOWS:

  Property tax amount = (tax rate) × (taxable value of your property)
                        ÷ 100

FOR THE AVERAGE TAXABLE VALUE HOMESTEAD:

  FY2025 average homestead taxable value:   $278,400
  FY2026 average homestead taxable value:   $292,150

  Tax on the FY2025 average homestead at the adopted FY2025 rate
  of $0.4950 per $100:                       $1,378.08

  Tax on the FY2026 average homestead at the proposed FY2026 rate
  of $0.5025 per $100:                       $1,467.55

  Year-over-year change for the average homestead:
                                             + $89.47

The members of the governing body voted on the proposed tax rate as
follows:

  FOR:     [to be inserted after the August 25, 2026 council vote]
  AGAINST: [to be inserted after the August 25, 2026 council vote]
  PRESENT AND NOT VOTING: [as applicable]
  ABSENT: [as applicable]

The 86th Texas Legislature modified the manner in which the
voter-approval tax rate is calculated to limit the rate of growth of
property taxes in the state.

You are urged to attend and express your views at the scheduled public
hearing on the tax rate. The City Council of the City of Cedar Ridge
will meet to vote on the proposed tax rate following the public
hearing.

____________________________________
Marisol Tovar
City Secretary, City of Cedar Ridge, Texas

POSTING VERIFICATION

This notice was posted on the city's official bulletin board at
Cedar Ridge City Hall, 200 Live Oak Drive, Cedar Ridge, TX, and on
the city's internet website at www.cedarridgetx.gov on
__________________ at ___________ a.m./p.m., and was published in the
Cedar Ridge Gazette on __________________, in accordance with Tex.
Tax Code § 26.06 and § 26.18.

This notice was drafted with the assistance of artificial intelligence
tools and reviewed by the City Secretary and the Finance Director
before publication.
```

## Notes for the User

- This notice is drafted for the case in which the proposed rate exceeds the no-new-revenue rate but does not exceed the voter-approval rate. The "you may express your support" paragraph under § 26.06 is the correct version. If the council were to propose a rate above the voter-approval rate, the notice would also need the protest petition and election language under § 26.07.
- The homestead impact calculation must reflect actual values certified by the appraisal district. The numbers in this example are illustrative.
- The publication deadline under § 26.06(b) is at least seven days before the hearing. For a September 8, 2026 hearing, the notice must be published in the Cedar Ridge Gazette no later than September 1, 2026. Recommended target: September 1 to allow for a Labor Day weekend buffer; verify the Gazette's submission schedule.
- The Truth-in-Taxation worksheet from the Texas Comptroller's office (comptroller.texas.gov) is the source of record for the rate calculations and should be filed with the notice in the FY2026 budget record.
- The "members voted on the proposed tax rate" paragraph should be completed after the council's August 25, 2026 vote on the proposed rate and before publication.
- Continuity: the I&S component of $0.1200 reflects an incremental debt service capacity sized to support the $25 million bond issuance noticed in the election-notice-generator example. The Finance Director, Rivera, is the staff point of contact for the rate calculations.
