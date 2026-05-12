---
name: vendor-risk-questionnaire
description: Drafts or fills a vendor risk questionnaire for IT, cloud, or SaaS procurement, modeled on the CSA CAIQ but adapted for Texas municipal scope. Use when an IT director, procurement officer, or city attorney needs a structured questionnaire response (or a blank template) to assess a vendor's security and compliance posture for new procurement or contract renewal.
---

# Vendor Risk Questionnaire

> Produces a defensible vendor risk questionnaire — either a blank template tuned to the data class involved, or a structured response with gap flags — sized for municipal procurement. Built for the IT director who has 24 hours to brief procurement on whether a SaaS vendor passes the smell test.

## When to Use

- "Draft a vendor risk questionnaire for the new permit-tracking SaaS."
- "Fill in this CAIQ for the vendor and flag what's missing."
- "Renewing the police RMS contract — build the questionnaire for CJIS scope."
- "Procurement asked for a security review of this HR payroll vendor; PHI in scope."
- "Cyber pool wants a third-party risk assessment on our utility billing vendor."
- Council has asked staff for a vendor risk assessment as a condition of award.

## Inputs Needed

Required:

- Vendor name and the service or product under consideration.
- Service model: SaaS, IaaS, PaaS, on-premises licensed, managed service, professional services.
- Data flow: what City data the vendor will see, store, transmit, or process.
- Data class in scope: Public, Internal, Confidential, Restricted. Note regulated overlays (CJIS, PHI, financial-account data, election data).
- Vendor's posted certification posture (SOC 2 Type II, ISO 27001, FedRAMP, TX-RAMP, HITRUST, PCI DSS, CJIS compliance attestation).
- Contract status: new procurement vs. renewal; estimated contract value.

Optional:

- Specific procurement statute path (competitive sealed proposal, cooperative purchasing, sole source).
- Insurance pool or cyber insurance requirements.
- Whether a Business Associate Agreement (BAA) or Data Processing Addendum (DPA) is already in place from a prior engagement.
- Vendor sales contact or assigned security contact.

If data class or service model is not specified, ask. Those two inputs drive everything else.

## Process

1. Confirm service model and data class. These two inputs select the relevant question banks.
2. Build the questionnaire in sections (see Output Format), using the CSA CAIQ family as the structural backbone adapted for municipal scope.
3. For renewals, pre-populate with prior-cycle responses and mark items requiring re-attestation.
4. For new procurement, leave responses blank and ship to the vendor with a response deadline.
5. When the city fills sections from vendor evidence (SOC 2, FedRAMP package, security FAQ), record the source document and specific section.
6. Flag gaps at the end of each section. Categorize as Critical (cannot proceed), High (remediate or accept risk), Medium (request plan), Low (note for next renewal).
7. List required contractual provisions: BAA, DPA, breach notification clause, audit rights, indemnification floors, insurance minimums.
8. Produce a one-page executive summary at the top for procurement and the city attorney.

## Output Format

```
VENDOR RISK QUESTIONNAIRE
City of [ENTITY] — [Vendor Name]
Service: [Description] | Data class: [Class + regulated overlays]
Reviewed by: [Name, title] | Date: [Date]
Disposition: Approve | Approve with conditions | Do not proceed

EXECUTIVE SUMMARY
- Service overview, top three risks, required contractual provisions,
  disposition rationale (limit to one page).

1. COMPANY AND SERVICE OVERVIEW
   Legal entity, jurisdiction, years in business, service architecture
   (multi-tenant, single-tenant, on-prem).

2. DATA HANDLING AND CLASSIFICATION
   Data collected, residency at rest, vendor classification, retention
   and deletion timelines, data return at contract end.

3. SECURITY CERTIFICATIONS
   SOC 2 Type II (date, auditor, exceptions); ISO 27001; FedRAMP;
   TX-RAMP Level 1 or 2; HITRUST, PCI DSS, CJIS attestation as applicable.

4. ACCESS CONTROLS AND AUTHENTICATION
   MFA for admins and end users; SSO/SAML/OIDC; RBAC and audit; PAM for
   vendor personnel; background checks for personnel with City data access.

5. ENCRYPTION
   In transit (protocol/cipher); at rest (algorithm/keys); customer-
   managed keys / BYOK; database, backup, log encryption.

6. VULNERABILITY MANAGEMENT
   Pen test cadence and latest summary; scanning and remediation SLAs;
   secure SDLC; third-party library and SBOM posture.

7. INCIDENT RESPONSE AND NOTIFICATION
   IR plan summary; contractual customer notification SLA; forensics
   support; past 24-month incident history.

8. BUSINESS CONTINUITY AND DR
   RPO and RTO; backup frequency, retention, geographic separation; DR
   exercise cadence and latest test result; multi-region failover.

9. SUBPROCESSORS
   Subprocessor list with geographic detail; flow-down of obligations;
   notification of changes; right of objection.

10. DATA RESIDENCY
    Primary and DR data center locations; cross-border transfers;
    support center geography and remote access geography.

11. CONTRACTUAL PROVISIONS REQUIRED
    BAA (if PHI), DPA, breach notification clause (24–72 hours), audit
    rights, indemnification floor, insurance minimums, termination for
    material security failure, data return and deletion at termination.

12. DECISION
    Recommendation with conditions or remediation timeline.

For each section: include a response column, an evidence-source column,
and a gap-and-follow-up row categorized Critical / High / Medium / Low.
```

Length: 8–14 pages full; the one-page executive summary is the deliverable for the city manager and council.

Tone: factual, neutral. Flag concerns specifically.

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system*. This skill produces a static internal procurement document; § 552.051 is not engaged. Annotate *"AI-assisted draft, reviewed by [staff title]"* per city AI use policy.

**TX-RAMP context:** Tex. Gov't Code Ch. 2059 applies directly to state agencies. Cities are not directly subject but increasingly require TX-RAMP Level 1 or 2 as a procurement floor. Note in the questionnaire whether TX-RAMP authorization is required, preferred, or considered alongside SOC 2 and FedRAMP.

**CJIS Security Policy:** Any vendor that touches criminal justice information must meet the FBI CJIS Security Policy and sign the CJIS Addendum. Do not approve without it.

**HIPAA:** If PHI flows to the vendor and the City operates a covered component, a Business Associate Agreement under 45 C.F.R. § 164.504(e) is mandatory.

**FTC Safeguards Rule:** Under 16 C.F.R. Part 314, cities meeting the "financial institution" definition through utility-billing credit operations must impose Safeguards-aligned obligations on service providers under § 314.4(f).

**Texas breach obligations flow through:** Vendor contracts must obligate the vendor to support the City's notification obligations under Tex. Bus. & Comm. Code § 521.053, with a notification timeline that protects the City's 60-day statutory window.

**Public records:** The completed questionnaire is a public record under Tex. Gov't Code Ch. 552, subject to § 552.139 (computer network security) and § 552.110 (proprietary commercial information) exceptions.

**Retention:** Procurement and vendor management files retain per TSLAC Schedule GR, Items 1050-21 (Bid and Proposal Files) and 1000-01 (Contracts).

## References

- The skill uses the CSA CAIQ structure as a backbone. Vendors that have completed a CAIQ may submit it in lieu of the city's questionnaire, subject to review for municipal gaps.

## Examples

- See `examples/saas-permit-tracking-vendor.md` — a completed questionnaire for a fictional SaaS permit-tracking vendor under evaluation by a Texas city, with flagged gaps (no FedRAMP, no geographic subprocessor detail, no DPA template).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
