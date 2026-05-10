# Example: FY2025 Management Responses to Two Audit Findings — City of Cedar Ridge

This is a worked example for the audit-response-helper skill. It uses the fictional City of Cedar Ridge, TX. The FY2025 audit was completed in February 2026 (referenced in the transparency-report-generator example). The audit produced one significant deficiency in internal controls and one Single Audit compliance finding.

## Input

### Finding 2025-001

- **Type:** Significant Deficiency in Internal Control over Financial Reporting (GAAS)
- **Subject:** Travel reimbursement supporting documentation
- **Auditor finding text (verbatim):**

  > **Condition.** During testing of 40 travel reimbursements drawn from the general fund, the auditor noted 9 reimbursements (22.5%) lacked itemized receipts for meal expenditures totaling $1,847.32. Three reimbursements were paid in advance of the travel and not subsequently reconciled to actual incurred costs. The aggregate amount of non-reconciled advances was $612.50.
  >
  > **Criteria.** City of Cedar Ridge Travel Policy 4.2.3 requires itemized receipts for any meal expenditure to be reimbursed; Policy 4.2.5 requires travel advances to be reconciled to actual incurred costs within 10 business days of the trip's conclusion.
  >
  > **Cause.** Department-level review of reimbursement packets is inconsistent. The Finance Department's payment process does not block payment when receipts are missing.
  >
  > **Effect.** $1,847.32 of meal reimbursements and $612.50 of unreconciled advances were paid without supporting documentation, creating a control deficiency. While the dollar amount is not material, the rate of exception (22.5%) indicates a control deficiency that could compound across additional volume.
  >
  > **Recommendation.** Implement a checklist-based reimbursement review at the department level; configure the financial system to block payment until required documentation is uploaded; train department reimbursement preparers on Travel Policy 4.2.

- **Department:** All departments; Finance Department for system control
- **Proposed corrective action:** new checklist; system block; mandatory training
- **Responsible person:** M. Rivera, Finance Director; with K. Patel, Public Works Director (highest-volume travel user) for departmental training cascade

### Finding 2025-002

- **Type:** Compliance Finding (Single Audit, 2 C.F.R. § 200.512(b))
- **Federal program:** Highway Planning and Construction; Assistance Listing 20.205; pass-through Texas Department of Transportation; award TASA-2022-04
- **Questioned cost:** None (records existed but were not located within reasonable time)
- **Repeat finding:** No
- **Auditor finding text (verbatim):**

  > **Condition.** During testing of certified payroll documentation under the Davis-Bacon Act for the FY2022 TASA-funded Sycamore Lane sidewalk project, the auditor requested weekly certified payrolls from the prime contractor and one subcontractor. The prime contractor's certified payrolls for the period of May 16 through June 27, 2024 (7 weeks) were not located within the City's project file at the time of fieldwork (August 4–8, 2025). The records were ultimately produced from the contractor's records on August 15, 2025 and verified to be in compliance with Davis-Bacon wage decisions.
  >
  > **Criteria.** 29 C.F.R. § 5.5(a)(3)(ii) and 2 C.F.R. § 200.334 require the City as the contracting agency to retain certified payroll records for federally-funded construction for three years from project closeout. 2 C.F.R. § 200.303(a) requires the non-federal entity to establish and maintain effective internal control over the federal award.
  >
  > **Cause.** Certified payrolls were maintained in the contractor's project files rather than transferred to the City's project closeout file. The City's checklist for federal-funded project closeout did not include a step to confirm transfer of certified payrolls.
  >
  > **Effect.** Records were not available within a reasonable time, creating a compliance finding. The records were subsequently located and verified compliant with wage decisions; no monetary impact.
  >
  > **Recommendation.** Update the federal-funded project closeout checklist to require transfer of all certified payrolls and Davis-Bacon documentation to the City's project file at substantial completion; train Public Works engineering staff on the updated checklist.

- **Department:** Public Works Engineering; Finance for grant administration
- **Proposed corrective action:** revised closeout checklist; training; retroactive sweep of two other active federal-funded projects
- **Responsible person:** K. Patel, Public Works Director; with M. Rivera, Finance Director for grant compliance oversight

## Output

```
MANAGEMENT RESPONSE — FINDING 2025-001

Finding Reference: 2025-001
Type: Significant Deficiency in Internal Control over Financial
      Reporting (GAAS)
Repeat Finding: No

Response Position: Concur

RESPONSE

Management concurs with the finding. The 22.5 percent exception rate
identified by the auditor is consistent with our own quality
spot-checks during the year and reflects inconsistent department-
level review of travel reimbursement packets, compounded by a
financial system process that does not block payment when required
documentation is missing. The corrective action plan below addresses
both the control gap and the underlying training gap.

CORRECTIVE ACTION PLAN

1. The Finance Department will configure the Tyler Munis travel
   reimbursement workflow to require upload of itemized receipts and
   an advance reconciliation form before a reimbursement can advance
   from "Submitted" to "Approved for Payment." The configuration is
   in test in the development environment and will be promoted to
   production no later than April 30, 2026.

2. The Finance Department will publish a one-page Travel Reimbursement
   Checklist (Finance Form 4.2-CK) by March 31, 2026. Department
   preparers will be required to attach the completed checklist to
   each reimbursement.

3. The Finance Department will deliver a 30-minute training on
   Travel Policy 4.2 to all department reimbursement preparers (an
   estimated 22 staff across 11 departments) in two sessions held
   April 15 and April 17, 2026. Attendance will be tracked through
   the City's LMS.

4. The Finance Department will perform a follow-up sample of 30
   reimbursements drawn from the period May 1 – August 31, 2026
   and report results to the Audit Committee in September 2026.

IMPLEMENTATION TIMELINE

| Action                                  | Target Date    | Responsible |
|-----------------------------------------|----------------|-------------|
| Travel Reimbursement Checklist published| March 31, 2026 | Finance Dir |
| Training delivered (2 sessions)         | April 17, 2026 | Finance Dir |
| Tyler Munis workflow change in prod     | April 30, 2026 | Finance Dir |
| Follow-up sample reported to Audit Cmte | Sept 22, 2026  | Finance Dir |

PREVENTIVE CONTROLS

The Tyler Munis workflow change is the preventive control. The
system will mechanically block reimbursement payment when itemized
receipts or an advance reconciliation form are missing, removing
reliance on manual review consistency across 11 departments.

RESPONSIBLE PERSON

Primary:   M. Rivera, Finance Director
Alternate: J. Ortega, Controller


MANAGEMENT RESPONSE — FINDING 2025-002

Finding Reference: 2025-002
Type: Compliance — Single Audit, 2 C.F.R. § 200.512(b)
Federal Program: Highway Planning and Construction; Assistance
                 Listing 20.205; Texas Department of Transportation
                 (pass-through); award TASA-2022-04 (Sycamore Lane
                 Sidewalk Project)
Questioned Cost: None
Repeat Finding: No

Response Position: Concur

RESPONSE

Management concurs with the finding. The certified payroll records
were ultimately produced and confirmed compliant with the applicable
Davis-Bacon wage decision, but the City was unable to produce them
within a reasonable time during fieldwork because the records had
not been transferred from the contractor's project files to the
City's project closeout file. The City's federal-funded project
closeout checklist did not include this step, and the City accepts
responsibility for the documentation gap. The corrective action
plan addresses both the closeout checklist and a retroactive sweep
of two other active federal-funded projects to confirm certified
payroll records are on file.

CORRECTIVE ACTION PLAN

1. The Public Works Engineering Division, in consultation with the
   Finance Department's Grants Administrator, will revise the
   Federal-Funded Project Closeout Checklist (Engineering Procedure
   ENG-7.4) to require transfer of all certified payrolls, Davis-
   Bacon compliance documentation, Form WH-347 weekly statements,
   and apprenticeship documentation from the contractor's records
   to the City's project file at substantial completion. Revised
   checklist effective May 1, 2026.

2. The Public Works Engineering Division will conduct a documentation
   sweep of the two currently active federal-funded construction
   projects (a CDBG sidewalk project and an FAA airport access
   project) to confirm certified payrolls are on file through the
   most recent pay application. Sweep complete by May 31, 2026.

3. Public Works Engineering staff and the Finance Grants Administrator
   will complete a 60-minute training on Davis-Bacon recordkeeping
   under 29 C.F.R. § 5.5 and Uniform Guidance recordkeeping under
   2 C.F.R. § 200.334. Training delivered by May 15, 2026.

4. For new federal-funded construction contracts let on or after
   June 1, 2026, the construction contract will include a clause
   requiring certified payrolls to be transmitted to the City within
   7 days of the contractor's submission, separate from the contractor's
   own retention obligation.

IMPLEMENTATION TIMELINE

| Action                                       | Target Date  | Responsible |
|----------------------------------------------|--------------|-------------|
| Revised closeout checklist (ENG-7.4) effective| May 1, 2026 | PW Director |
| Davis-Bacon recordkeeping training           | May 15, 2026 | PW Director |
| Active-project sweep complete                | May 31, 2026 | PW Director |
| Contract clause inserted in new contracts    | June 1, 2026 | PW Director |

PREVENTIVE CONTROLS

The combination of the revised closeout checklist (process control)
and the new contract clause requiring 7-day transmittal of certified
payrolls (contractual control) is the preventive control. Records
will be transferred to the City's project file routinely during
construction rather than at closeout, eliminating the gap.

RESPONSIBLE PERSON

Primary:   K. Patel, Public Works Director
Alternate: L. Kim, Grants Administrator (Finance Department)
```

## Notes for the User

- These responses are drafted for the auditor's preliminary review.
  Final responses are reviewed by the City Manager and the Audit
  Committee before submission.
- Finding 2025-002 will require a corrective action plan submitted
  to the FAC under 2 C.F.R. § 200.511(c) when the audit reporting
  package is filed; this management response language carries over
  to the CAP form.
- TxDOT (the pass-through entity) may issue a management decision
  under 2 C.F.R. § 200.521 within six months of FAC acceptance.
- This draft was prepared with AI assistance and reviewed by Finance
  Director Rivera before submission to the auditor.
```
