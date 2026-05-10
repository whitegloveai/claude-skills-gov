# Progress Tracker

Working tracker for the v1 build. Updated as plugins and skills move through scaffold → authored → reviewed.

## Status legend

- 🟦 scaffolded — directory exists, `.gitkeep` only
- 🟨 authored — SKILL.md complete, references/examples drafted
- 🟩 reviewed — passed maintainer review, ready to ship

## Reconciliation note

CLAUDE.md states "65 skills across 13 plugins." The actual taxonomy in CLAUDE.md enumerates **68 skills**. Counts below reflect the enumerated taxonomy. Reconcile the headline number in CLAUDE.md once the v1 set is locked.

## Plugins

### council-ops (7/7) — Phase 1 calibration complete

- 🟨 agenda-builder (SKILL + 1 example + 1 reference: TOMA section taxonomy)
- 🟨 minutes-drafter (SKILL + 1 example + 1 reference: Robert's Rules quick reference)
- 🟨 public-comment-summarizer (SKILL + 1 example)
- 🟨 ordinance-tracker (SKILL + 1 example)
- 🟨 council-packet-prep (SKILL + 1 example + 1 reference: standard packet attachments)
- 🟨 resolution-drafter (SKILL + 1 example)
- 🟨 decision-memo-writer (SKILL + 1 example)

All examples cross-reference a single fictional City of Cedar Ridge, TX June 9, 2026 regular meeting for cross-skill consistency.

### clerk (6/6) — Phase 2 complete

- 🟨 tpia-response-drafter (SKILL + 1 example + 1 ref: TPIA exception taxonomy)
- 🟨 records-retention-classifier (SKILL + 1 example + 1 ref: TSLAC schedule families)
- 🟨 open-meetings-compliance-checker (SKILL + 1 example reviewing the council-ops June 9 agenda)
- 🟨 election-notice-generator (SKILL + 1 example: $25M Cedar Ridge bond, English/Spanish)
- 🟨 proclamation-writer (SKILL + 1 example: Public Works Week)
- 🟨 public-notice-formatter (SKILL + 1 example: Cedar Ridge tax rate hearing)

### finance (7/7) — Phase 2 complete

- 🟨 budget-narrative-writer (SKILL + 1 example + 1 ref: GASB framework summary)
- 🟨 variance-analyzer (SKILL + 1 example: Q3 FY2026 General Fund variance)
- 🟨 grant-application-drafter (SKILL + 1 example + 1 ref: 2 C.F.R. Part 200 summary)
- 🟨 procurement-rfp-builder (SKILL + 1 example: street overlay RFP, feeds council-ops Item 6a)
- 🟨 transparency-report-generator (SKILL + 1 example: Cedar Ridge FY2025)
- 🟨 audit-response-helper (SKILL + 1 example: two findings response)
- 🟨 financial-disclosure-formatter (SKILL + 1 example: City Manager Daniel Ahn disclosure)

### hr (0/6)

- 🟦 job-description-writer
- 🟦 policy-analyzer
- 🟦 onboarding-packet-builder
- 🟦 employee-handbook-updater
- 🟦 performance-eval-helper
- 🟦 ada-accommodation-drafter

### planning (0/6)

- 🟦 zoning-narrative-writer
- 🟦 permit-application-reviewer
- 🟦 site-plan-summary
- 🟦 public-hearing-notice
- 🟦 variance-request-analyzer
- 🟦 staff-report-writer

### public-works (0/5)

- 🟦 work-order-summarizer
- 🟦 maintenance-log-analyzer
- 🟦 capital-improvement-plan-drafter
- 🟦 service-request-classifier
- 🟦 infrastructure-condition-report

### it (0/5)

- 🟦 it-policy-drafter
- 🟦 security-incident-classifier
- 🟦 vendor-risk-questionnaire
- 🟦 ai-governance-checklist
- 🟦 system-of-record-mapper

### legal (0/5)

- 🟦 contract-redline-summary
- 🟦 ordinance-impact-analyzer
- 🟦 tpia-legal-review
- 🟦 litigation-summary-helper
- 🟦 interlocal-agreement-drafter

### public-safety (0/5)

- 🟦 incident-narrative-cleanup
- 🟦 training-bulletin-drafter
- 🟦 after-action-report-builder
- 🟦 community-engagement-message
- 🟦 emergency-comms-drafter

### communications (5/5) — Phase 2 complete

- 🟨 press-release-drafter (SKILL + 1 example: Fire Station #3 groundbreaking)
- 🟨 citizen-newsletter-builder (SKILL + 1 example + 1 ref: section templates)
- 🟨 social-media-municipal-style (SKILL + 1 example + 1 ref: municipal voice tone guide)
- 🟨 talking-points-writer (SKILL + 1 example: water rate adjustment, ties to council-ops decision memo)
- 🟨 crisis-comms-template (SKILL + 1 example + 1 ref: holding statement patterns)

### economic-development (0/4)

- 🟦 incentive-proposal-drafter
- 🟦 site-selection-response
- 🟦 business-retention-survey-analyzer
- 🟦 annual-report-narrative

### parks-recreation (0/4)

- 🟦 program-flyer-drafter
- 🟦 volunteer-recognition-writer
- 🟦 facility-rental-response
- 🟦 sponsorship-proposal-helper

### library (0/3)

- 🟦 program-description-writer
- 🟦 collection-development-justifier
- 🟦 community-partnership-proposal

## Totals

- **Plugins:** 13
- **Skills scaffolded:** 68 / 68
- **Skills authored:** 25 / 68 (council-ops, clerk, finance, communications complete)
- **Skills reviewed:** 0 / 68

## Next actions

1. ✅ User spot-check passed with three refinements applied to council-ops:
   - Word count lock 800–1,200 per SKILL.md (overflow goes to references/)
   - TRAIGA reframed as transparency best practice (not § 552.051 compliance) for back-office drafting skills; live-interaction skills get the actual statutory citation
   - Citation hygiene: `Tex. Gov't Code` (apostrophe-t), `Tex. Loc. Gov't Code`, `Tex. Bus. & Comm. Code` (TRAIGA — different code, same chapter number — collision risk)
2. Phase 2 launching: clerk + finance + communications in parallel (18 skills).
3. After Phase 2, re-read CLAUDE.md and verify standards before Phase 3.

## Setup gap to flag

The project directory is not a git repo (`Is a git repository: false`). CLAUDE.md's workflow convention says to commit after each plugin completes, but no commits have happened. When ready, run `git init && git add . && git commit -m "Initial scaffold + council-ops"` and `gh repo create whitegloveai/claude-skills-gov --public --source=. --remote=origin`.
