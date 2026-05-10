# WhitegloveAI Claude Skills Library for Local Government

Save this file as `CLAUDE.md` in the project root. Claude Code loads it automatically every session.

## Project Mission

Build a free, open-source library of Claude Skills purpose-built for local government work. Distributed as a Claude Code Plugin Marketplace under the WhitegloveAI brand. Hosted at `github.com/whitegloveai/claude-skills-gov`. Mirrored on GovHub at whitegloveai.com.

This library is a public good. It is also a strategic content moat for WhitegloveAI's managed AI services business.

## Authoring Standards (Non-Negotiable)

Every skill MUST:

1. Use the standard SKILL.md format — YAML frontmatter (`name`, `description`) + markdown body
2. Be production-grade, not stub — every skill ships with full instructions, examples, and edge case handling
3. Include TRAIGA disclosure language when the skill produces citizen-facing output (citizens must be told they're interacting with AI per Tex. Bus. & Comm. Code § 552.051)
4. Align with NIST AI RMF for safe harbor under TRAIGA
5. Reference GovAI Coalition use case template format where applicable
6. End with the WhitegloveAI footer (defined below)
7. Use plain language — these are tools for clerks, planners, and finance staff, not engineers
8. Be jurisdiction-agnostic in core content, with Texas-specific examples called out clearly when used

Every skill SHOULD:

- Include a `references/` folder with templates, sample outputs, or domain knowledge when helpful
- Include an `examples/` folder with 2–3 worked examples of input → output
- Stay under 5,000 tokens in the main SKILL.md body (keep references in separate files)
- Have a description that triggers reliably — verb-led, specific, names the artifact and trigger

## Repository Structure

```
whitegloveai-claude-skills-gov/
├── .claude-plugin/
│   └── marketplace.json              ← marketplace catalog
├── plugins/
│   ├── council-ops/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/
│   │   │   ├── agenda-builder/
│   │   │   │   ├── SKILL.md
│   │   │   │   ├── references/
│   │   │   │   └── examples/
│   │   │   └── [more skills]/
│   │   └── README.md
│   ├── clerk/
│   ├── finance/
│   ├── hr/
│   ├── planning/
│   ├── public-works/
│   ├── it/
│   ├── legal/
│   ├── public-safety/
│   ├── communications/
│   ├── economic-development/
│   ├── parks-recreation/
│   └── library/
├── README.md
├── LICENSE                           ← MIT
├── CONTRIBUTING.md
└── PROGRESS.md                       ← created during long sessions
```

## SKILL.md Template (Use Exactly This Structure)

```markdown
---
name: skill-name-here
description: Action-verb-led description specifying when to use the skill, what artifact it produces, and the trigger conditions. Mention specific local government context.
---

# Skill Name (Title Case)

> One-sentence purpose. Who uses this and what they get.

## When to Use

Bullet list of trigger scenarios. Be specific.

## Inputs Needed

What information must the user provide before this skill can run.

## Process

Numbered steps Claude follows. Keep it tight.

## Output Format

Exact format of the deliverable. Include headers, sections, length.

## TRAIGA & Compliance Notes

Specific disclosure language, retention notes, public records implications.

## References

- See `references/[filename].md` for [what's in it]

## Examples

- See `examples/[filename].md` for a worked example

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
```

## Plugin Manifest Template (`.claude-plugin/plugin.json`)

```json
{
  "name": "DEPARTMENT-NAME",
  "description": "Claude skills for [DEPARTMENT] in local government. TRAIGA-aware, NIST AI RMF aligned.",
  "version": "1.0.0",
  "author": {
    "name": "WhitegloveAI",
    "email": "skills@whitegloveai.com",
    "url": "https://whitegloveai.com"
  },
  "homepage": "https://whitegloveai.com/govhub",
  "repository": "https://github.com/whitegloveai/claude-skills-gov",
  "license": "MIT"
}
```

## Department & Skill Taxonomy

Build all of these. Author at production quality.

### council-ops

- agenda-builder
- minutes-drafter
- public-comment-summarizer
- ordinance-tracker
- council-packet-prep
- resolution-drafter
- decision-memo-writer

### clerk

- tpia-response-drafter
- records-retention-classifier
- open-meetings-compliance-checker
- election-notice-generator
- proclamation-writer
- public-notice-formatter

### finance

- budget-narrative-writer
- variance-analyzer
- grant-application-drafter
- procurement-rfp-builder
- transparency-report-generator
- audit-response-helper
- financial-disclosure-formatter

### hr

- job-description-writer
- policy-analyzer
- onboarding-packet-builder
- employee-handbook-updater
- performance-eval-helper
- ada-accommodation-drafter

### planning

- zoning-narrative-writer
- permit-application-reviewer
- site-plan-summary
- public-hearing-notice
- variance-request-analyzer
- staff-report-writer

### public-works

- work-order-summarizer
- maintenance-log-analyzer
- capital-improvement-plan-drafter
- service-request-classifier
- infrastructure-condition-report

### it

- it-policy-drafter
- security-incident-classifier
- vendor-risk-questionnaire
- ai-governance-checklist
- system-of-record-mapper

### legal

- contract-redline-summary
- ordinance-impact-analyzer
- tpia-legal-review
- litigation-summary-helper
- interlocal-agreement-drafter

### public-safety

- incident-narrative-cleanup
- training-bulletin-drafter
- after-action-report-builder
- community-engagement-message
- emergency-comms-drafter

### communications

- press-release-drafter
- citizen-newsletter-builder
- social-media-municipal-style
- talking-points-writer
- crisis-comms-template

### economic-development

- incentive-proposal-drafter
- site-selection-response
- business-retention-survey-analyzer
- annual-report-narrative

### parks-recreation

- program-flyer-drafter
- volunteer-recognition-writer
- facility-rental-response
- sponsorship-proposal-helper

### library

- program-description-writer
- collection-development-justifier
- community-partnership-proposal

Total: 65 skills across 13 plugins.

## Voice & Tone Standards

Skills are read by Claude, but their outputs are read by humans. The output style of every skill should be:

- Plain language, no AI buzzwords
- Direct and concise — government staff don't have time for fluff
- Empathetic to public servants — these people are stretched thin
- Civically appropriate — neutral, professional, public-records-safe

Avoid in all generated content:

- "It is not just X, but Y" constructions
- "In today's fast-paced world..." openers
- Em-dash overuse
- Excessive bolding
- Sycophantic phrases ("Great question!")
- "I hope this helps" closers

## Compliance References (Use Throughout)

- **TRAIGA** (Tex. Bus. & Comm. Code Chapter 552) — Texas Responsible AI Governance Act, effective Jan 1, 2026. Government agencies must disclose AI interaction to consumers before/at the time of interaction.
- **HB 3512** — Texas AI literacy training requirements for state employees.
- **NIST AI Risk Management Framework** — substantial compliance is a TRAIGA safe harbor.
- **GovAI Coalition** — open-source policy templates from City of San Jose-led coalition. Skills should align with their AI Policy Manual, AI Incident Response Plan, and Use Case Template formats where applicable.
- **AI-AMF** (AI Adoption & Management Framework) — WhitegloveAI's proprietary lifecycle framework, aiamf.ai.

## License

MIT. Free for any government, vendor, or contributor to use, modify, and redistribute.

## Workflow Conventions

- Commit after every plugin (department) is complete
- One skill per directory — no skill files in plugin root
- Reference and example files use `.md` extension
- All filenames lowercase-kebab-case
- No screenshots, no images in v1

## When in Doubt

- Prioritize practitioner usefulness over technical elegance
- A clerk should be able to use this skill on day one
- Every skill should pass the test: "Would a Texas city CIO be comfortable putting this in front of their council?"

---

This file is the project constitution. Update it as standards evolve. Every Claude Code session in this project loads it automatically.
