# WhitegloveAI Claude Skills for Local Government

A free, open-source library of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) and Claude Code plugins built specifically for the day-to-day work of city, county, and special-district staff.

Distributed as a Claude Code Plugin Marketplace. Maintained by [WhitegloveAI](https://whitegloveai.com), the Managed AI Service Provider™ for state and local government.

## What's in here

13 plugins, organized by department, with 68 skills covering the artifacts that local government staff actually produce — council agendas, TPIA responses, budget narratives, zoning staff reports, RFPs, ADA accommodation memos, after-action reports, and more.

| Plugin | Skills | Audience |
|---|---|---|
| [council-ops](plugins/council-ops) | 7 | City secretary, council aides |
| [clerk](plugins/clerk) | 6 | City clerk's office |
| [finance](plugins/finance) | 7 | Finance directors, budget analysts |
| [hr](plugins/hr) | 6 | Human resources |
| [planning](plugins/planning) | 6 | Planning & development services |
| [public-works](plugins/public-works) | 5 | Public works, engineering |
| [it](plugins/it) | 5 | IT, AI governance leads |
| [legal](plugins/legal) | 5 | City attorney's office |
| [public-safety](plugins/public-safety) | 5 | Police, fire, EMS, emergency mgmt |
| [communications](plugins/communications) | 5 | PIO, public information |
| [economic-development](plugins/economic-development) | 4 | ED corporations, BR&E staff |
| [parks-recreation](plugins/parks-recreation) | 4 | Parks & recreation |
| [library](plugins/library) | 3 | Public library staff |

## About the Examples

Every skill ships with one worked example anchored in the fictional City of Cedar Ridge, TX — a deliberately neutral, jurisdiction-agnostic municipality designed to demonstrate the skill in realistic civic context without referencing any real city, county, school district, or named public servant. Cedar Ridge does not exist.

The skill logic itself is universally applicable to any local government in Texas, and with minor adaptation (citation swaps, statutory references) to any U.S. jurisdiction. Cedar Ridge exists only in the examples — the skills work for your city.

If you want to adapt an example to your jurisdiction, replace the fictional names, addresses, and dates with your own. The structure, statutory citations, and procedural patterns are designed to translate.

## Install

In Claude Code, add this marketplace:

```
/plugin marketplace add whitegloveai/claude-skills-gov
```

Then install the plugins you want:

```
/plugin install council-ops@whitegloveai-gov
/plugin install clerk@whitegloveai-gov
```

You can also clone this repo and add the marketplace from a local path:

```
/plugin marketplace add /path/to/whitegloveai-claude-skills-gov
```

## Compliance posture

These skills are built with public-sector compliance in mind:

- **TRAIGA-aware.** Skills that produce citizen-facing output include the AI-interaction disclosure language required under Tex. Bus. & Comm. Code § 552.051 (effective Jan 1, 2026).
- **NIST AI RMF aligned.** Authoring follows the Govern–Map–Measure–Manage functions to support the substantial-compliance safe harbor under TRAIGA § 552.057.
- **GovAI Coalition-compatible.** Skills use the Coalition's use-case template fields where applicable, so a city already using Coalition templates can drop these in.
- **Public-records-safe.** Outputs are written assuming they may be subject to disclosure under state public records law.

These skills do not replace legal review or human judgment. They produce drafts. A person signs the document.

## How to use a skill

Skills load automatically when their description matches your request. For example, after installing the `council-ops` plugin:

> Draft an agenda for the next regular council meeting. Items: budget amendment public hearing, two zoning consent items, an interlocal agreement with the county, and an executive session on litigation.

Claude will recognize the request and apply the `agenda-builder` skill. You don't invoke skills by name — you describe what you need, and the matching skill activates.

## Contributing

Contributions are welcome from local government staff, vendors, and civic technologists. See [CONTRIBUTING.md](CONTRIBUTING.md) for the authoring standards and PR process. Every skill is reviewed against the constitution in [CLAUDE.md](CLAUDE.md).

## License

[MIT](LICENSE). Free for any government, vendor, or contributor to use, modify, and redistribute.

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™. Need this operationalized across your city? [Talk to us.](https://whitegloveai.com/contact)*
