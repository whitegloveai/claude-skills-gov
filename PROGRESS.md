# Progress Tracker

v1 build status. Updated as plugins and skills move through scaffold → authored → reviewed.

## Status legend

- 🟦 scaffolded — directory exists, `.gitkeep` only
- 🟨 authored — SKILL.md complete, references/examples drafted
- 🟩 reviewed — passed maintainer review, ready to ship

## Reconciliation note

CLAUDE.md previously stated "65 skills across 13 plugins." Reconciled to **68 skills across 13 plugins** at wrap.

## Plugins — all 68 skills authored

### council-ops (7/7) — Phase 1

- 🟨 agenda-builder (+ 1 ref: TOMA section taxonomy)
- 🟨 minutes-drafter (+ 1 ref: Robert's Rules quick reference)
- 🟨 public-comment-summarizer
- 🟨 ordinance-tracker
- 🟨 council-packet-prep (+ 1 ref: standard packet attachments)
- 🟨 resolution-drafter
- 🟨 decision-memo-writer

### clerk (6/6) — Phase 2

- 🟨 tpia-response-drafter (+ 1 ref: TPIA exception taxonomy)
- 🟨 records-retention-classifier (+ 1 ref: TSLAC schedule families)
- 🟨 open-meetings-compliance-checker
- 🟨 election-notice-generator
- 🟨 proclamation-writer
- 🟨 public-notice-formatter

### finance (7/7) — Phase 2

- 🟨 budget-narrative-writer (+ 1 ref: GASB framework summary)
- 🟨 variance-analyzer
- 🟨 grant-application-drafter (+ 1 ref: 2 C.F.R. Part 200 summary)
- 🟨 procurement-rfp-builder
- 🟨 transparency-report-generator
- 🟨 audit-response-helper
- 🟨 financial-disclosure-formatter

### communications (5/5) — Phase 2

- 🟨 press-release-drafter
- 🟨 citizen-newsletter-builder (+ 1 ref: section templates)
- 🟨 social-media-municipal-style (+ 1 ref: municipal voice tone guide)
- 🟨 talking-points-writer
- 🟨 crisis-comms-template (+ 1 ref: holding statement patterns)

### hr (6/6) — Phase 3

- 🟨 job-description-writer (+ 1 ref: FLSA exemption test)
- 🟨 policy-analyzer
- 🟨 onboarding-packet-builder
- 🟨 employee-handbook-updater
- 🟨 performance-eval-helper
- 🟨 ada-accommodation-drafter (+ 1 ref: ADA interactive process flow) — signer-ownership reframe applied after spot-check

### planning (6/6) — Phase 3

- 🟨 zoning-narrative-writer (+ 1 ref: TX zoning procedure outline)
- 🟨 permit-application-reviewer
- 🟨 site-plan-summary
- 🟨 public-hearing-notice
- 🟨 variance-request-analyzer
- 🟨 staff-report-writer

### it (5/5) — Phase 3

- 🟨 it-policy-drafter (+ 1 ref: NIST CSF control mapping)
- 🟨 security-incident-classifier (+ 1 ref: severity and notification matrix) — three-way citation routing verified
- 🟨 vendor-risk-questionnaire
- 🟨 ai-governance-checklist (+ 1 ref: NIST AI RMF functions mapping) — TRAIGA framing realigned after spot-check
- 🟨 system-of-record-mapper

### legal (5/5) — Phase 4

- 🟨 contract-redline-summary (+ 1 ref: contract risk categories)
- 🟨 ordinance-impact-analyzer (+ 1 ref: state preemption quick reference)
- 🟨 tpia-legal-review (+ 1 ref: TPIA exception decision tree)
- 🟨 litigation-summary-helper
- 🟨 interlocal-agreement-drafter

**Every legal SKILL.md and every legal example contains the explicit "Advisory scaffolding — not legal advice. Review by city attorney required." disclaimer line above the WhitegloveAI footer.**

### public-safety (5/5) — Phase 4

- 🟨 incident-narrative-cleanup — must-not-alter-facts constraint baked in
- 🟨 training-bulletin-drafter
- 🟨 after-action-report-builder (+ 1 ref: NIMS/ICS AAR structure)
- 🟨 community-engagement-message
- 🟨 emergency-comms-drafter (+ 1 ref: emergency message statutory formats)

### public-works (5/5) — Phase 4

- 🟨 work-order-summarizer
- 🟨 maintenance-log-analyzer (+ 1 ref: end-of-life signals checklist)
- 🟨 capital-improvement-plan-drafter (+ 1 ref: CIP funding source summary)
- 🟨 service-request-classifier
- 🟨 infrastructure-condition-report

### economic-development (4/4) — Phase 5

- 🟨 incentive-proposal-drafter (+ 1 ref: Ch. 380/381/504/505 incentive summary)
- 🟨 site-selection-response (+ 1 ref)
- 🟨 business-retention-survey-analyzer (+ 1 ref)
- 🟨 annual-report-narrative (+ 1 ref)

### parks-recreation (4/4) — Phase 5

- 🟨 program-flyer-drafter
- 🟨 volunteer-recognition-writer
- 🟨 facility-rental-response (+ 1 ref: facility rental policy checklist)
- 🟨 sponsorship-proposal-helper

### library (3/3) — Phase 5

- 🟨 program-description-writer
- 🟨 collection-development-justifier (+ 1 ref: ALA intellectual freedom framework)
- 🟨 community-partnership-proposal

## Totals

- **Plugins:** 13 / 13
- **Skills scaffolded:** 68 / 68
- **Skills authored:** 68 / 68 ✓
- **Skills reviewed:** 0 / 68 (pending maintainer review)

## Final verification (run at wrap)

- **SKILL.md files:** 68 / 68 ✓
- **Worked examples:** 68 (one per skill) ✓
- **Reference files:** 29 (selective per the build plan) ✓
- **Word count lock (800–1,200):** 68 / 68 in range ✓
- **Citation hygiene:** zero bare `Tex. Gov. Code`; zero bare `Tex. Local Gov. Code`. Two intentional `Tex. Gov. Code` references appear inside one example file as the teaching demonstration of the bare-form citation the skill flags as a recommended fix. ✓
- **TPIA-vs-TRAIGA collision:** all `§ 552.051` references correctly paired with `Tex. Bus. & Comm. Code`; all TPIA references correctly use `Tex. Gov't Code` ✓
- **TRAIGA framing:** canonical "transparency best practice (not a § 552.051 trigger)" paragraph present in all 68 SKILL.md files ✓
- **Legal disclaimer:** "Advisory scaffolding — not legal advice. Review by city attorney required." present in all 5 legal SKILL.md and all 5 legal examples ✓
- **WhitegloveAI footer:** present in all 68 SKILL.md files ✓
- **Stray `.gitkeep`:** 0 ✓
- **Jurisdiction-agnostic instructions:** SKILL.md instructions and references files contain no jurisdiction-specific fictional canon (the fictional municipality used in worked examples is contained to `examples/` folders only) ✓

## Cross-skill threads in the worked examples

The example folders are anchored to a single fictional Texas city used consistently across plugins so a reader can follow a coherent civic story end to end. The fictional municipality is contained to the `examples/` folders — the skills themselves are jurisdiction-agnostic.

Notable multi-skill threads in the examples:

- A regular council meeting agenda flows through council-ops (agenda → minutes → packet → resolution).
- A zoning case has a complete file across council-ops + planning (narrative + notice package + staff report).
- The FY2026 street overlay project ties council-ops → finance/procurement-rfp-builder → public-works/work-order-summarizer + infrastructure-condition-report.
- A boil-water incident appears in council-ops/agenda-builder, communications/crisis-comms-template, and public-safety/emergency-comms-drafter.
- A litigation summary handles the executive session matter posted on the council-ops agenda.
- An interlocal cooperation agreement produces the council-ops consent agenda agreement.

## Commits

- `00c32f8` Phases 1-3 complete — 42 skills across 7 plugins
- `50dcee3` Phase 3 refinements: TRAIGA framing + ADA signer-ownership
- `e571032` Phase 4 complete — 15 skills across legal, public-safety, public-works
- `27ca86c` Phase 5 + wrap — 68 of 68 skills authored, library v1 complete
- (next commit, pending review) Example-canon containment cleanup + "About the Examples" documentation

## Next steps (post-v1)

1. **Maintainer review pass** — 2–3 skills per plugin spot-checked against the standards.
2. **Push to GitHub:**
   ```bash
   gh repo create whitegloveai/claude-skills-gov --public --source=. --remote=origin
   git push -u origin main
   ```
3. **GovHub mirror** at whitegloveai.com.
4. **First public release** as v1.0.0 once review completes.
