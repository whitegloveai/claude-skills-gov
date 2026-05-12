# public-safety

Claude skills for police, fire, EMS, and emergency management. Built for command staff, training officers, PIOs in uniformed services, and emergency management coordinators.

## Skills in this plugin

| Skill | Purpose |
|---|---|
| [incident-narrative-cleanup](skills/incident-narrative-cleanup) | Cleans up grammar, completeness, and report-writing structure of an incident narrative without altering the facts |
| [training-bulletin-drafter](skills/training-bulletin-drafter) | Drafts a training bulletin or roll-call training note |
| [after-action-report-builder](skills/after-action-report-builder) | Drafts an after-action report (AAR) using the standard incident timeline / observations / recommendations format |
| [community-engagement-message](skills/community-engagement-message) | Drafts a community-facing post or message about a public safety topic |
| [emergency-comms-drafter](skills/emergency-comms-drafter) | Drafts emergency communications: shelter-in-place notices, evacuation orders, all-clear messages |

## Install

```
/plugin install public-safety@whitegloveai-gov
```

## Compliance and operational notes

The `incident-narrative-cleanup` skill **does not change facts**. It only restructures and copy-edits. Officers, EMTs, and firefighters retain full authority over the substance of their report.

Emergency comms output is a draft. In an active emergency, the incident commander or designated PIO releases the actual message after agency clearance.

These skills are designed to be compatible with NIMS/ICS terminology and standard AAR formats used by FEMA and the Texas Division of Emergency Management.

## Notes on Examples

Examples in this plugin reference the fictional City of Cedar Ridge, TX for continuity across skills. The skill logic is jurisdiction-agnostic — adapt example specifics to your city.

## License

[MIT](../../LICENSE).

---

*Built by [WhitegloveAI](https://whitegloveai.com) — your Managed AI Service Provider™.*
