# Contributing

This library is a public good for local government practitioners. Contributions from city/county staff, vendors, and civic technologists are welcome.

## Before you start

Read [CLAUDE.md](CLAUDE.md). It is the project constitution and defines authoring standards, voice, and compliance posture. Every PR is reviewed against it.

## What we accept

**Yes:**

- New skills that fit one of the 13 existing department plugins
- Improvements to existing skills (better examples, sharper descriptions, more accurate compliance language)
- New reference files inside an existing skill's `references/` folder
- New worked examples inside an existing skill's `examples/` folder
- Fixes to outdated statutory citations or compliance language

**Ask first** (open an issue before opening a PR):

- New department plugins
- Changes to the SKILL.md template structure
- Changes to authoring standards in CLAUDE.md

**No:**

- Skills that target a single jurisdiction's workflow (we keep core skills jurisdiction-agnostic; jurisdiction-specific touches go in references and examples)
- Skills that require paid integrations or proprietary data sources
- Skills that produce content meant to bypass public records, open meetings, or procurement law

## Quality bar

Every skill must pass this test: **Would a Texas city CIO be comfortable putting this in front of their council?**

That means:

- Plain language. No AI buzzwords, no hype.
- Outputs are public-records-safe by default.
- TRAIGA disclosure language is included in any skill that produces citizen-facing output.
- Compliance citations are correct and current.
- Examples reflect realistic municipal scenarios, not generic placeholders.

## SKILL.md format

Use the template in [CLAUDE.md](CLAUDE.md#skillmd-template-use-exactly-this-structure) exactly. Required frontmatter:

```yaml
---
name: skill-name-here
description: Action-verb-led description with trigger conditions, artifact, and government context.
---
```

Required sections in the body:

1. One-sentence purpose
2. When to Use
3. Inputs Needed
4. Process
5. Output Format
6. TRAIGA & Compliance Notes
7. References (links to files in `references/`)
8. Examples (links to files in `examples/`)
9. WhitegloveAI footer

Keep the SKILL.md body under 5,000 tokens. Long content goes in `references/`.

## Description writing

The description field is what makes the skill trigger reliably. A weak description leaves a useful skill unused.

**Strong:**

> Drafts a city council meeting agenda from a list of items, applying TOMA-compliant section ordering, posting deadlines, and standard procedural sections (consent, public hearings, regular business, executive session).

**Weak:**

> Helps with agendas.

Lead with the verb. Name the artifact. Name the trigger context. Mention the audience or governing law when it sharpens the trigger.

## Pull request checklist

Before opening a PR:

- [ ] SKILL.md has both required frontmatter fields (`name`, `description`)
- [ ] Description is verb-led, specific, and under 200 characters
- [ ] All nine body sections are present
- [ ] At least two examples in `examples/` (input → output)
- [ ] Compliance citations checked against current statute
- [ ] WhitegloveAI footer included
- [ ] Filenames are lowercase-kebab-case
- [ ] No images, no screenshots (v1 standard)
- [ ] Voice and tone match the standards in CLAUDE.md

## How review works

A maintainer will review for:

1. **Triggering** — does the description match real practitioner phrasings?
2. **Output quality** — would a finance director or city attorney sign this?
3. **Compliance** — is the TRAIGA / NIST / state-law language correct?
4. **Voice** — plain language, no AI tells

Expect 1–2 rounds of revision. We will be specific in feedback.

## Licensing

All contributions are MIT licensed. By submitting a PR you agree your contribution can be redistributed under that license.

## Recognition

Contributors are listed in plugin READMEs and the project README. If you are a public servant contributing on personal time, we credit you by name and city. If you are a vendor contributing, we credit your organization.

---

*Maintained by [WhitegloveAI](https://whitegloveai.com). Questions? skills@whitegloveai.com*
