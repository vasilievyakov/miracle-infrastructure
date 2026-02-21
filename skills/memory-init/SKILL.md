---
name: memory-init
description: |
  First-run setup wizard for the memory system. Creates directory structure, config, and starter files.
  Use when: (1) First time using Miracle Infrastructure, (2) "Initialize memory", (3) Setting up on new machine.
  Triggers: "/memory-init", "initialize memory", "setup memory".
---

# Memory Init - Setup Wizard

Creates the full memory directory structure, configuration, and starter files. Safe to re-run (idempotent).

---

## Step 1: Check existing setup

```bash
ls ~/.claude/memory/ 2>/dev/null
```

If the directory exists and has content, warn:
```
Memory system already exists at ~/.claude/memory/
Found: {N} dossiers, {N} observation files, MEMORY.md

Re-running will not overwrite existing files. Only missing pieces will be created.
Continue? (yes/no)
```

Wait for confirmation before proceeding.

---

## Step 2: Create directory structure

```bash
mkdir -p ~/.claude/memory/projects
mkdir -p ~/.claude/memory/tests
```

---

## Step 3: Create memory-config.json

```
Write ~/.claude/memory/memory-config.json
```

Content:
```json
{
  "memory_path": "~/.claude/memory",
  "projects": {},
  "fallback_project": "general",
  "max_dossier_lines": 200,
  "observation_types": ["decision", "bugfix", "feature", "discovery", "problem"]
}
```

---

## Step 4: Auto-detect projects

Scan for git repositories to pre-populate the config:

```bash
find ~ -maxdepth 3 -name ".git" -type d 2>/dev/null | head -20
```

For each found repo:
1. Extract the directory name as project slug
2. Check for GitHub remote: `git -C {path} remote get-url origin 2>/dev/null`
3. Generate keyword suggestions from the directory name

Present findings to user:
```
Found {N} git repositories. Want to add any to memory?

1. ~/projects/my-app (github.com/user/my-app)
2. ~/work/dashboard (no remote)
3. ~/experiments/chatbot (github.com/user/chatbot)

Enter numbers to add (e.g., 1 3), or skip:
```

For selected projects, update `memory-config.json` with entries:
```json
{
  "project-slug": {
    "keywords": ["project", "slug"],
    "github": "user/repo",
    "path": "~/projects/my-app"
  }
}
```

---

## Step 5: Create starter MEMORY.md

```
Write ~/.claude/memory/MEMORY.md
```

Content:
```markdown
# Memory Index

## Active Projects
| Project | Dossier | Observations | GitHub |
|---------|---------|-------------|--------|
| General | `projects/general.md` | `*.observations.md` (0 entries) | - |

## Open Problems
(none yet)

## Workflow
- On project mention: load dossier + observations from memory/projects/
- During work: record significant observations (auto-observe rule)
- End of session: run /session-save

## Infrastructure
- Config: ~/.claude/memory/memory-config.json
- Skills: session-save, search-memory, memory-health, project-status
- Rules: session-start, session-end, auto-observe
```

---

## Step 6: Create general dossier and observations

Create the fallback "general" project:

```
Write ~/.claude/memory/projects/general.md
```

```markdown
# General

## Status
Permanent. Catch-all for sessions not tied to a specific project.

## Description
Default dossier for miscellaneous work: infrastructure setup, research, experiments, one-off tasks.

## Current State
- Last session: {today}
- Done: Memory system initialized
- Uncommitted: no

## Unresolved Problems
(none)

## Decisions Made
- [{today}] Initialized Miracle Infrastructure memory system

## Next Steps
1. Add projects to memory-config.json
2. Start using /session-save at end of work sessions

## Session History
- [{today}] Memory system initialized
```

```
Write ~/.claude/memory/projects/general.observations.md
```

```markdown
# Observations - general

## Index
| # | Date | Type | Summary | Files |
|---|------|------|---------|-------|

## Details
```

---

## Step 7: Copy integrity tests

If the test file exists in the Miracle Infrastructure installation:

```bash
cp {miracle_infra_path}/packs/memory/tests/test_memory_integrity.py ~/.claude/memory/tests/
```

If not available, inform the user where to find it.

---

## Step 8: Verify

Run a quick health check:

```bash
python3 ~/.claude/memory/tests/test_memory_integrity.py 2>&1
```

---

## Step 9: Confirmation

```
Memory system initialized!

Created:
- ~/.claude/memory/MEMORY.md
- ~/.claude/memory/memory-config.json
- ~/.claude/memory/projects/general.md
- ~/.claude/memory/projects/general.observations.md
- ~/.claude/memory/tests/test_memory_integrity.py

{N} projects detected and added to config.

Quick start:
- Work on a project, then run /session-save
- Search past work with /search-memory
- Check integrity with /memory-health
```
