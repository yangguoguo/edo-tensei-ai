---
name: portable-ai-memory
description: Build, restore, review, and incrementally update a portable Markdown-based personal AI memory library. Use when a user wants an AI continuity or "digital resurrection" system, needs to carry identity, preferences, interests, projects, decisions, and collaboration style across AI agents or accounts, wants to import conversation exports or notes into durable memory, or asks for a weekly memory review. Keep reusable skill files separate from private user memory.
---

# Portable AI Memory

Maintain a user-owned Markdown memory library that any capable AI agent can read. Treat it as a curated personal context layer, not a transcript archive and not an unquestionable profile.

## Choose the operation

- **Initialize**: Create a new library from the template in `assets/memory-template/`.
- **Restore**: Read an existing library in the order defined by its `README.md`, then summarize current understanding and uncertainty.
- **Update**: Review context or material explicitly available in the current run, compare it with current memory, and make evidence-backed incremental changes.
- **Migrate**: Convert existing memory notes or conversation archives into the library schema without losing originals.
- **Share**: Package this Skill separately from all private memory content.

## Core rules

1. Keep the Skill and private memory library in different directories.
2. Never infer access to conversations from another account or agent. Only use files, task context, or exports actually available in the current run.
3. Treat new evidence as potentially temporary. Promote it to durable memory only when the user states it explicitly, it recurs, or it materially affects future collaboration.
4. Distinguish facts, preferences, interpretations, and open questions. Do not rewrite interpretations as facts.
5. Do not store passwords, tokens, cookies, private keys, recovery codes, precise financial account numbers, identity-document numbers, or unnecessary third-party personal data.
6. Require user confirmation before changing core identity, relationships, health, finances, political beliefs, or other high-impact sensitive claims unless the user explicitly requested that exact update.
7. Preserve important disagreement and evolution. Use `history/change-log.md` as a compact audit trail, not as conversation history or a weekly diary.
8. Prefer small edits. Do not rewrite the whole profile during a weekly update.
9. Do not maintain a rolling conversation inbox. Store distilled memory, not chat logs.
10. Keep at most 6 representative discussion summaries in `archive/`. Add one only when it captures a durable idea, important decision, or meaningful change that loses essential context when reduced to a profile bullet. When 6 already exist, merge with an existing theme or replace a lower-value theme with user confirmation; never create a seventh.
11. Do not copy full conversations into the memory library by default. When the user supplies a conversation for review, extract durable information and leave the source outside the library.
12. Treat frequently used Skills and their public installation sources as portable capability assets. Keep them in `tools-and-skills.md`, not in identity or interests.
13. Add a Skill after at least 2 real uses in 3 months, or when it is low-frequency but costly to rediscover or rebuild. Remove or demote items unused for 3 months during review. Do not impose a fixed item limit; control growth through evidence-based promotion and regular demotion.
14. Store only public or official source URLs, portable installation instructions, non-secret dependencies, and last-used dates. Never store credentials or present a machine-specific path as the portable source.

## Initialize

1. Ask for or infer a writable destination. Default to a clearly named user-owned folder, not the Skill folder.
2. Run:

```bash
python3 scripts/init_memory.py --destination /absolute/path/to/personal-ai-memory
```

3. Import user-provided background material into the appropriate files.
4. Run `python3 scripts/check_memory.py /absolute/path/to/personal-ai-memory`.
5. Tell the user what was created, what remains uncertain, and how to invoke the restore workflow.

## Restore

1. Read `README.md` and `memory-index.md` first.
2. Read all core files listed in the index. Read archives only when the active question needs them.
3. Read `tools-and-skills.md` when restoring the user's working environment or choosing an established capability for a task.
4. State a short working model of the user, including stable preferences, active projects, and open questions.
5. Explicitly say that newer user statements override stored memory.
6. Do not edit files unless the user also requested an update.

## Weekly update

Read `references/update-policy.md` before changing memory.

1. Run `check_memory.py` and stop on structural errors.
2. Read current core memory. Read `history/change-log.md` only to understand prior edits, conflicts, or provenance relevant to the update.
3. Review relevant information actually visible in the current task or material explicitly provided by the user. Do not assume access to other conversations. Update a Skill's usage count or last-used date only when its real use is visible.
4. Prepare candidate changes grouped as confirmed, plausible but unconfirmed, contradictory, sensitive, and ephemeral.
5. Apply confirmed low-risk changes. Put uncertain items into `open-questions.md`; do not silently promote them.
6. For sensitive or contradictory changes, write a proposed change summary and request confirmation instead of editing the core claim.
7. Add a compact dated entry to `history/change-log.md` only when durable memory actually changed. Include the change and evidence source; do not list unchanged files.
8. Run the checker again and report a concise diff summary.
9. If there is no durable new information, make no profile edits and do not add a change-log entry.
10. Keep no more than 12 detailed change-log entries. When adding the thirteenth, compress older entries into a short `Historical summary` section without losing important reversals or provenance.

## Migrate existing material

1. Inventory source files and preserve them unchanged.
2. Initialize a fresh destination library.
3. Map stable facts and preferences into core files; summarize only representative high-value discussions into `archive/`.
4. Add provenance notes to the first change-log entry.
5. Flag conflicts and stale claims rather than choosing silently.
6. Validate the result.

## Automation boundary

A scheduled agent can review only data available in its configured project and task context. It cannot act as an account-wide conversation reader. Prefer a weekly run that uses visible context, applies confirmed low-risk updates, and creates no change when there is no durable new information. Users may explicitly provide a conversation or note for one-time extraction, but the source should remain outside the memory library. Never claim cross-account synchronization unless an external export or connector actually provides it.

For a suggested automation prompt, read `references/automation-prompt.md`.
