# Update Policy

## Evidence levels

| Level | Meaning | Action |
|---|---|---|
| Confirmed | Explicit user statement or repeated stable signal | Update low-risk memory |
| Plausible | One contextual signal or AI interpretation | Add to open questions |
| Contradictory | Conflicts with existing memory | Preserve both and ask |
| Sensitive | Health, intimate relationships, exact finances, politics, identity changes | Ask before core update |
| Ephemeral | Mood, one-off task detail, passing preference | Do not promote |

## Promotion tests

Before adding an item to durable memory, ask:

1. Will this likely improve future collaboration?
2. Is it supported by visible evidence?
3. Is it expected to remain relevant for months rather than hours?
4. Can it be stored at a less sensitive level of detail?
5. Would the user reasonably expect this to be remembered?

If any answer is unclear, record a question instead of a fact.

## Merge behavior

- Add dates only when time matters.
- Keep exact wording for strong preferences when practical.
- Use neutral language and avoid diagnosis or personality typing.
- Deduplicate before adding new bullets.
- Keep each core file concise; move long narratives to `archive/`.
- Keep `archive/` selective: preserve only representative discussion summaries, not raw or routine conversation history.
- Prefer updating an existing archive summary over creating another file about the same theme.
- Enforce a hard limit of 6 archive topics. Before creating a topic, try in order: update an existing theme, merge two overlapping themes, or propose replacing the least useful theme.
- Log the source filename or task date, never hidden chain-of-thought.

## Representative topic test

An archive topic must affect how a future AI understands the user's values, important decisions, or recurring questions. It must also satisfy at least one of these:

- Preserve reasoning that cannot be reduced to one core-profile bullet.
- Record a meaningful change or tension in the user's view.
- Explain why a durable preference matters.

Do not archive a discussion merely because it was interesting, detailed, emotional, or well written.

## Change-log limits

- Treat `history/change-log.md` as an audit trail of memory edits, not a user biography or conversation archive.
- Log only durable changes to core memory, archive topics, open questions, or memory policy.
- Keep each entry to the date, the change, and its evidence source; normally no more than 3 bullets.
- Do not log no-change weekly reviews.
- Keep at most 12 detailed entries. Compress older entries into one historical summary while preserving important reversals and source provenance.

## Skill asset limits

- Record active reusable capabilities in `tools-and-skills.md`; do not inventory every installed Skill.
- Promote a Skill after at least 2 visible uses in 3 months, or when a single use proves it is costly to rediscover, configure, or rebuild.
- Do not impose a fixed active-Skill limit. Control growth through visible usage evidence, deduplication, and demoting items unused for 3 months.
- Record name, purpose, public or official source URL, portable installation method, non-secret prerequisites, usage evidence, and last-used date.
- Never store tokens, cookies, webhooks, private repository URLs, or machine-specific credentials.
- Mark an unknown source as `待确认`; never invent a download link.
- During review, demote items unused for 3 months unless the user explicitly considers them high-value recovery assets.

## Weekly report

Report:

- Files reviewed
- Durable changes applied
- Changes awaiting confirmation
- Contradictions or stale items
- Sensitive material intentionally excluded
- Validation result
