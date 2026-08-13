# Weekly Automation Prompt

Use this prompt with a weekly automation and replace the path:

```text
Use $portable-ai-memory to review and incrementally update the private memory library at /ABSOLUTE/PATH/personal-ai-memory. Read its README, memory index, and current core files; read the change log only when relevant to provenance or conflicts. Use only information actually visible in this task or explicitly provided by the user; do not infer access to other tasks or accounts. Apply only confirmed low-risk durable changes. Do not store secrets, unnecessary sensitive details, routine chat logs, or a rolling conversation inbox. Keep at most 6 representative discussion summaries in archive; when full, merge or propose a replacement instead of adding a seventh. Maintain reusable Skills in tools-and-skills.md only after 2 visible uses in 3 months or when costly to rebuild; demote items unused for 3 months, record only verified public sources, and never invent links or store credentials. Put uncertain or conflicting items into open questions and request confirmation for sensitive core changes. Add a compact change-log entry only when durable memory changed, keep no more than 12 detailed entries, run the included memory checker before and after edits, and report exactly what changed. If there is no durable new information, do not edit the profile or change log.
```

The automation must run in a project that can access both the Skill and the private memory path. A heartbeat attached to one task may see that task's context, but it is not a universal account-wide conversation reader. For information from another account, let the user explicitly provide selected material for one-time extraction rather than building a permanent raw-conversation folder.
