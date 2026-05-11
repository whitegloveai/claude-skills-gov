---
name: service-request-classifier
description: Classifies a citizen public works service request (311-type) by category, urgency, routing, and follow-up needs, with a duplicate-check note for recurring locations. Use when a call center clerk, 311 coordinator, or public works dispatcher needs to convert a free-form citizen report into a routed work item.
---

# Service Request Classifier

> Turns a free-form citizen report into a classified, routed service request. Built for call center staff and dispatchers who need to triage many requests quickly without losing the recurring-issue pattern.

## When to Use

- "Classify this 311 request and route it. Pothole on Pecan Street with photo, school zone."
- "Triage today's batch of online service requests."
- "This caller is describing a water leak. Where does this go, and how urgent?"
- "Build me a classification record for this dumping complaint behind the warehouse."
- "Quick classification: streetlight out at the intersection of 5th and Magnolia."
- A clerk or dispatcher is converting an unstructured citizen report into a structured ticket that the right work group will see in their queue.

## Inputs Needed

Required:

- Service request text or summary
- Reported location (address, intersection, or geographic descriptor)
- Citizen contact info if available (for callback only; not for classification)

Optional:

- Photos or attachments described
- Reporting channel (online portal, phone, email, walk-in, councilmember referral)
- Citizen's stated urgency (informational; verify against the city's SLA)
- Recent service request history at the same address or block (for duplicate-check)
- Any safety language the citizen used ("water bubbling up," "kids walk this way," "live wire")

Do not include sensitive personal data such as SSNs, driver's license numbers, or financial information in the classification record. Phone and address are sufficient for follow-up.

## Process

1. Read the request text and extract the core issue. Citizens describe symptoms; classification names the asset class and condition.
2. Assign Category from the standard list: pothole, water leak, sewer overflow/back-up, traffic signal, streetlight, sign down/damaged, drainage/standing water, dead animal, illegal dumping, sidewalk hazard, tree in ROW, code complaint (refer), graffiti, pavement marking, manhole, fire hydrant, other.
3. Assign Urgency using the city's SLA matrix. Default tiers and response targets if no local matrix is provided:
   - **Emergency** (life/safety, active release, traffic hazard with no warning): respond same shift, target on-site within 2 hours.
   - **Priority** (degrading condition, safety-adjacent, school zone, ADA): respond next business day, target on-site within 3 business days.
   - **Routine** (cosmetic or non-degrading): respond within 7 business days, schedule within 14.
4. Identify Routing — the work group that owns the task. Streets, Water, Wastewater, Traffic, Facilities, Fleet, Solid Waste, Parks, Code Enforcement (referral).
5. Determine Required Follow-Up. Note whether a callback is expected (yes for safety issues and code referrals; usually yes for water/sewer; routine items may use status-update emails only).
6. Run a Duplicate Check. If the same address or block has three or more requests in 90 days, flag as recurring and add a one-line diagnostic hypothesis.
7. Flag Code Compliance Routing if the request describes a private property condition (overgrown lot, dilapidated structure, junk vehicle), which goes to Code Enforcement under LGC Ch. 54 rather than public works.
8. Flag any cross-jurisdictional handoff (state highway maintained by TxDOT, county road, franchise utility for streetlights, school district sidewalk).

## Output Format

Plain markdown, half a page. Tone: operational, neutral. The reader is a dispatcher or the receiving crew lead.

```
SERVICE REQUEST CLASSIFICATION
Request ID: [SR number]
Date received: [date, time]
Channel: [online / phone / email / walk-in / councilmember]

1. SUMMARY
   [One sentence describing the issue.]

2. LOCATION
   [Address or intersection; council district; mapped asset if known.]

3. CATEGORY
   [From the standard list.]

4. URGENCY
   [Emergency / Priority / Routine — with target response time.]

5. ROUTING
   [Work group; supervisor if the city assigns by name.]

6. REQUIRED FOLLOW-UP
   [Callback yes/no, with rationale. Status update channel.]

7. DUPLICATE-CHECK NOTE
   [Recurrence at this address/block in past 90 days; brief diagnostic if so.]

8. CROSS-JURISDICTIONAL / CODE NOTE
   [If TxDOT, county, franchise utility, or LGC Ch. 54 code routing applies.]

9. CITIZEN-FACING ACKNOWLEDGMENT (DRAFT)
   [Two to three sentences the call center may use verbatim or modify.]
```

## TRAIGA & Compliance Notes

**AI use disclosure — transparency best practice (not a § 552.051 trigger):** Tex. Bus. & Comm. Code § 552.051(b)–(d) requires disclosure when a citizen *interacts directly with an AI system* (e.g., a chatbot, automated voice assistant, or AI-driven service interface). The disclosure trigger is *interaction*, not *output*. This skill produces a static document drafted with AI assistance; it does not put a citizen in direct interaction with AI, so § 552.051 is not engaged.

However, transparency about AI assistance in document drafting is sound practice and should align with the city's adopted AI use policy and the GovAI Coalition's guidance on documenting AI tool use. Consider a brief notation on documents distributed publicly or to the governing body: *"AI-assisted draft, reviewed by [staff title and name]."* This is a policy choice, not a statutory mandate.

**Hybrid deployment caveat:** If the city deploys an automated chatbot or voice assistant that uses this skill to respond to citizens *without* a human in the loop, that deployment is an AI interaction and § 552.051 disclosure attaches at the channel level. This is a deployment choice the city makes outside of this skill.

**Engineering scope:** Triage classifications do not substitute for field assessment by qualified staff. Anything that requires engineering judgment — structural failure of a sidewalk, hydraulic capacity of a drainage system, electrical hazard analysis — must be referred to qualified staff and, where applicable, a licensed P.E. under the Texas Engineering Practice Act.

**Public records (Tex. Gov't Code Ch. 552):** Service requests are public records. Citizen contact information is generally redactable under § 552.117 for current and former government employees, § 552.137 for email addresses provided to a governmental body, and other applicable exceptions on a case-by-case basis.

**Retention:** Service request records retain 2 years under Texas State Library Local Government Retention Schedule PW, Item 5025-02 (Service Requests and Complaints), longer if connected to a claim or litigation hold.

**Verify before close:** Category and routing match the city's actual SLA matrix. Citizen contact data is redacted from any public-facing publication.

## References

- Standard category list and default urgency matrix appear in the Process section.

## Examples

- See `examples/recurring-pothole-classification.md` for a worked example: classification of a Cedar Ridge service request reporting a deteriorating pothole at the 700 block of Pecan Street near Pecan Elementary, marked Priority, routed to Streets, with a duplicate-check note tying this request to two prior reports in the trailing 90 days.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
