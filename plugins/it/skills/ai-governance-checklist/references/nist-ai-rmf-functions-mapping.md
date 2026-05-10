# NIST AI RMF 1.0 Functions and Subcategories for Municipal Deployments

This reference summarizes the four functions of the NIST AI Risk Management Framework 1.0 and identifies the subcategories most relevant to municipal AI deployments. It cross-references the NIST Generative AI Profile (NIST AI 600-1) cross-cuts that apply when the use case involves generative AI, and it explains how this alignment supports the substantial-compliance safe harbor under Tex. Bus. & Comm. Code § 552.057.

## The four functions

### Govern (GV)

Establishes organizational context, policies, accountability, and culture for AI risk management. Govern is foundational; without it, the other functions lack authority.

Most relevant municipal subcategories:

- **GV-1.1** — Legal and regulatory requirements involving AI are understood, managed, and documented. (Pairs with TRAIGA, HB 3512, sectoral statutes.)
- **GV-1.4** — Risk management process is established to identify, assess, prioritize, and respond to AI risks.
- **GV-2.1** — Roles and responsibilities for AI risk management are clear within the City and with third parties.
- **GV-3.2** — Procedures for AI risks are documented and applied.
- **GV-4.1** — Organizational policies provide for accountability of AI development and deployment.
- **GV-5.1** — Policies and procedures address engagement with affected communities.
- **GV-6.1** — Policies and procedures address third-party AI risks (vendors, models, data).

### Map (MP)

Establishes the context to frame AI risks for a specific use case: purpose, users, data, intended impact, and the assumptions behind deployment.

Most relevant subcategories:

- **MP-1.1** — Intended purposes, prospective settings, and the categories of users and people affected are understood.
- **MP-1.2** — Inter-disciplinary AI actors and others are consulted.
- **MP-2.1** — The specific tasks and methods to implement the AI system are defined.
- **MP-2.2** — Information about the system is documented (model cards, datasheets). *Generative AI Profile cross-cut.*
- **MP-3.4** — Potential impacts (benefits and harms) to individuals, groups, communities, and the environment are identified.
- **MP-5.1** — Risks and benefits are characterized for affected individuals and the community.

### Measure (MS)

Establishes how the AI system will be evaluated, monitored, and assessed. Measurement is what makes AI risk visible.

Most relevant subcategories:

- **MS-1.1** — Approaches and metrics for measurement of AI risks are identified.
- **MS-1.3** — Tested and trustworthy metrics are used for AI risks, with attention to fairness, accuracy, and reliability. *Generative AI Profile cross-cut.*
- **MS-2.1** — Test sets and methods are documented; outcomes are interpretable.
- **MS-2.5** — System validity is regularly evaluated and documented.
- **MS-2.7** — System security and resilience are evaluated and documented.
- **MS-2.9** — Bias and discrimination indicators are evaluated.
- **MS-2.11** — Fairness and bias metrics are documented for the deployment context.
- **MS-3.1** — Risk responses are tracked and re-evaluated as the AI evolves.

### Manage (MG)

Allocates resources and acts on identified risks: mitigation, transfer, acceptance, or avoidance, with monitoring and improvement.

Most relevant subcategories:

- **MG-1.1** — A determination is made whether the AI system achieves its intended purpose and whether benefits outweigh negative impacts. *Generative AI Profile cross-cut.*
- **MG-1.2** — Treatment of identified AI risks is prioritized based on impact, likelihood, and resources.
- **MG-2.2** — Mechanisms for sustaining the AI system are in place.
- **MG-3.1** — AI risks and benefits from third parties are regularly monitored.
- **MG-4.1** — Post-deployment monitoring is in place.
- **MG-4.2** — Incident response, recovery, and continuous improvement processes are in place.

## NIST Generative AI Profile (NIST AI 600-1) cross-cuts

Where the use case involves generative AI, layer these in addition to the Map/Measure/Manage subcategories:

- **GV-1.1** — Confidential information disclosure risks are addressed.
- **MP-2.2** — System documentation includes generative AI specifics (model lineage, training data summary, known limitations).
- **MS-1.3** — Metrics include generative AI risk categories (confabulation, harmful content, data leakage, intellectual property, environmental impact, value alignment).
- **MG-1.1** — Determinations include generative-AI-specific risk acceptance, including a hallucination tolerance assessment.

## TRAIGA substantial-compliance safe harbor

Tex. Bus. & Comm. Code § 552.057 establishes that substantial compliance with the NIST AI Risk Management Framework is a defense to certain TRAIGA enforcement actions. The intake form should therefore *document* the function alignment specifically — not just assert it. Specific citations to GV, MP, MS, and MG subcategories in the intake record allow the City to demonstrate, on review, that the use case was developed and is operated within an AI RMF posture.

The safe harbor is not a substitute for the § 552.051 disclosure obligation when a citizen interacts directly with AI. Disclosure and substantial compliance are independent.

## Tier-to-function emphasis

| Risk Tier | Govern | Map | Measure | Manage |
|---|---|---|---|---|
| Low | Light | Light | Light | Light |
| Medium | Standard | Standard | Standard | Standard |
| High | Strong | Strong | Strong; quarterly review | Strong; pre-deployment red team |
| Prohibited | — | — | — | — (do not approve) |

## How to use this mapping

1. Identify the function the use case primarily exercises.
2. Pull the relevant subcategory IDs into Section 6 of the intake form.
3. Where generative AI is involved, layer the Generative AI Profile cross-cuts.
4. Use the documented subcategory mapping as the substantial-compliance record.
