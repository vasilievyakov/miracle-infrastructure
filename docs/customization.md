# Customization

How to extend Miracle Infrastructure without forking.

## Add observation types

Edit `~/.claude/memory/memory-config.json`:

```json
{
  "observation_types": ["decision", "bugfix", "feature", "discovery", "problem", "experiment", "milestone"]
}
```

The `auto-observe` rule and `session-save` skill will pick up new types automatically. The integrity tests validate against this list.

## Add custom dossier sections

Dossier files (`projects/{name}.md`) support any `## Section` heading. The `session-save` skill preserves unknown sections during updates.

Example: adding a "Team" section to track who works on the project:

```markdown
## Team
- Alice: frontend
- Bob: backend, API design
- Carol: DevOps, monitoring
```

## Add directors

In `~/.claude/skills/directors/SKILL.md`, add a new entry to the director table and create a system prompt following the existing pattern:

1. Background and credentials
2. Philosophy (5-7 bullet points)
3. Key questions for any project (6-8 questions)
4. Response format template

## Add frameworks

In `~/.claude/skills/frameworks/SKILL.md`:

1. Add the framework to the appropriate category table
2. Assign it to one or more stages in the stage-to-framework mapping
3. If it conflicts with existing frameworks, add a resolution rule to the Conflict Points table

## Add agents to the orchestrator

Edit `~/.claude/skills/orchestrate/agents-library.json`:

```json
{
  "id": "security-auditor",
  "name": "Security Auditor",
  "priority": 3,
  "system_prompt": "You are a security auditor...",
  "typical_tasks": ["security review", "vulnerability assessment"],
  "tools": ["Read", "Grep", "Bash"],
  "output_format": "security_report"
}
```

Then add keyword mappings in the `orchestration_rules.task_to_agents_mapping` section.

## Change the memory path

Edit `memory-config.json`:

```json
{
  "memory_path": "~/my-custom-memory-path"
}
```

All skills and rules read the path from this config. The integrity tests also read from config.

## Create pack-specific rules

Rules in `~/.claude/rules/` apply globally. To create rules that only apply to specific projects, use the `globs` frontmatter:

```yaml
---
description: Auto-run tests after code changes
globs: "projects/my-app/**"
---
```

## Disable a rule

Delete or rename the file in `~/.claude/rules/`. The installer creates backups, so you can restore later.

## Disable a skill

Delete or rename the directory in `~/.claude/skills/`. Skills are independent. Removing one does not break others, with one exception: `memory-health` depends on the memory directory structure created by `memory-init`.
