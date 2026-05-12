# clerk

Claude skills for the city clerk's office. Built for clerks, deputy clerks, and records management staff who handle public information requests, retention scheduling, election notices, and the procedural backbone of municipal recordkeeping.

## Skills in this plugin

| Skill | Purpose |
|---|---|
| [tpia-response-drafter](skills/tpia-response-drafter) | Drafts a Texas Public Information Act response letter, including the 10-business-day clock and AG referral language |
| [records-retention-classifier](skills/records-retention-classifier) | Classifies a document against the state local-government retention schedule |
| [open-meetings-compliance-checker](skills/open-meetings-compliance-checker) | Reviews a posted agenda against TOMA notice and content requirements |
| [election-notice-generator](skills/election-notice-generator) | Drafts election notices in English and Spanish per Election Code requirements |
| [proclamation-writer](skills/proclamation-writer) | Drafts a mayoral or council proclamation in standard whereas form |
| [public-notice-formatter](skills/public-notice-formatter) | Formats a public notice for newspaper publication or website posting |

## Install

```
/plugin install clerk@whitegloveai-gov
```

## Compliance

These skills target Texas Public Information Act (Gov. Code Ch. 552), Texas Open Meetings Act (Gov. Code Ch. 551), Texas Election Code, and the State Library and Archives Commission Local Government Records Retention Schedules. Statutory citations should be verified against current law before relying on output.

## Notes on Examples

Examples in this plugin reference the fictional City of Cedar Ridge, TX for continuity across skills. The skill logic is jurisdiction-agnostic — adapt example specifics to your city.

## License

[MIT](../../LICENSE).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™.*
