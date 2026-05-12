# council-ops

Claude skills for city council operations. Built for city secretaries, council aides, executive assistants to elected officials, and city manager's office staff who run the council process.

## Skills in this plugin

| Skill | Purpose |
|---|---|
| [agenda-builder](skills/agenda-builder) | Drafts a TOMA-compliant council meeting agenda from a list of items |
| [minutes-drafter](skills/minutes-drafter) | Turns raw meeting recordings or notes into draft minutes |
| [public-comment-summarizer](skills/public-comment-summarizer) | Condenses a public comment session into a neutral summary for the record |
| [ordinance-tracker](skills/ordinance-tracker) | Tracks an ordinance through first reading, second reading, and adoption |
| [council-packet-prep](skills/council-packet-prep) | Assembles a council packet: agenda, staff reports, attachments, cover memo |
| [resolution-drafter](skills/resolution-drafter) | Drafts a council resolution in standard whereas/now-therefore form |
| [decision-memo-writer](skills/decision-memo-writer) | Drafts an options/recommendation memo from staff to council |

## Install

```
/plugin install council-ops@whitegloveai-gov
```

## Compliance

These skills are designed with the Texas Open Meetings Act (Gov. Code Ch. 551) and TRAIGA (Bus. & Comm. Code Ch. 552) in mind. Outputs intended for public posting include the AI-interaction disclosure language required after Jan 1, 2026.

The skills draft documents. A clerk, attorney, or manager signs them. Don't post anything to a public agenda without human review.

## Notes on Examples

Examples in this plugin reference the fictional City of Cedar Ridge, TX for continuity across skills. The skill logic is jurisdiction-agnostic — adapt example specifics to your city.

## License

[MIT](../../LICENSE).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™.*
