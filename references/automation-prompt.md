# Weekly Automation Prompt

## Setup contract

Installing the Skill does not schedule it. After initializing and validating a private memory library:

1. Ask the user whether to create weekly automatic maintenance.
2. If yes, ask for weekday and local time; suggest Sunday 20:00 only when a default is useful.
3. Confirm the project can access the Skill and private memory paths.
4. Create the weekly Automation with the prompt below and the user's chosen schedule.
5. Verify that its saved status is `ACTIVE`; report the exact schedule and paths.

Do not create, enable, or modify a recurring task without explicit consent.

Use this prompt with a weekly automation and replace the path:

```text
Use $portable-ai-memory to review and incrementally update the private memory library at /ABSOLUTE/PATH/personal-ai-memory. Read its README, memory index, and current core files; read the change log only when relevant to provenance or conflicts. Use only information actually visible in this task or explicitly provided by the user; do not infer access to other tasks or accounts. Apply only confirmed low-risk durable changes. Do not store secrets, unnecessary sensitive details, routine chat logs, or a rolling conversation inbox. Keep at most 6 representative discussion summaries in archive; when full, merge or propose a replacement instead of adding a seventh. Maintain reusable Skills in tools-and-skills.md only after 2 visible uses in 3 months or when costly to rebuild; demote items unused for 3 months, record only verified public sources, and never invent links or store credentials. Put uncertain or conflicting items into open questions and request confirmation for sensitive core changes. Add a compact change-log entry only when durable memory changed, keep no more than 12 detailed entries, run the included memory checker before and after edits, and report exactly what changed. If there is no durable new information, do not edit the profile or change log.
```

The Automation must run in a project that can access both the Skill and the private memory path. A task attached to one context is not a universal account-wide conversation reader. For information from another account, let the user explicitly provide selected material for one-time extraction rather than building a permanent raw-conversation folder.
