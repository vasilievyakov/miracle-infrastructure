# memory-init

Set up the entire memory system in one command. Zero to functional in about 30 seconds.

## Why

The memory system needs a specific directory structure, a config file, a root index, a fallback dossier, observation templates, and integrity tests. Creating all of that by hand is tedious and error-prone. `/memory-init` is a setup wizard that builds everything, auto-detects your git repositories, and verifies the result with a health check. It is idempotent, so running it twice will not destroy anything. It only creates what is missing.

## How It Works

A 9-step wizard:

1. **Check for existing setup.** If `~/.claude/memory/` already has content, warn and confirm before proceeding. Existing files are never overwritten.
2. **Create directories.** `~/.claude/memory/projects/` and `~/.claude/memory/tests/`.
3. **Write config.** `memory-config.json` with defaults: observation types, fallback project, max dossier size.
4. **Auto-detect projects.** Scans your home directory (3 levels deep) for git repos, extracts names and GitHub remotes, and lets you pick which ones to register.
5. **Create MEMORY.md.** The root index with the project table, open problems section, and workflow notes.
6. **Create the "general" project.** A catch-all dossier and empty observations file for sessions that do not belong to any specific project.
7. **Copy integrity tests.** Places `test_memory_integrity.py` in the tests directory.
8. **Verify.** Runs the integrity tests to confirm everything is wired correctly.
9. **Confirm** with a summary of what was created.

```
~/.claude/memory/
├── MEMORY.md                          # Root index
├── memory-config.json                 # Project keywords, settings
├── projects/
│   ├── general.md                     # Fallback dossier
│   └── general.observations.md        # Fallback observations
└── tests/
    └── test_memory_integrity.py       # Integrity checks
```

## Install

> **Pack-only.** This is the setup wizard for the memory system. It copies templates and integrity tests from the pack into your `~/.claude/memory/` directory. Without the pack files available, it has nothing to install. Install the full [Memory Pack](../../packs/memory/), not this skill alone.

```bash
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Memory pack
```

After installation, `/memory-init` is the first command you run.

## Example

Fresh machine, nothing set up yet:

```
You: /memory-init

Claude: No existing memory system found. Creating from scratch.

Created directory structure:
- ~/.claude/memory/
- ~/.claude/memory/projects/
- ~/.claude/memory/tests/

Scanning for git repositories...
Found 6 git repositories:

1. ~/projects/ev-radar (github.com/vasilievyakov/ev-radar)
2. ~/projects/my-app (github.com/vasilievyakov/my-app)
3. ~/projects/chatbot (no remote)
4. ~/work/api-service (github.com/vasilievyakov/api-service)
5. ~/experiments/ml-playground (no remote)
6. ~/dotfiles (github.com/vasilievyakov/dotfiles)

Enter numbers to add (e.g., 1 2 4), or skip: 1 2 4

Added 3 projects to memory-config.json.

Memory system initialized!

Created:
- ~/.claude/memory/MEMORY.md
- ~/.claude/memory/memory-config.json
- ~/.claude/memory/projects/general.md
- ~/.claude/memory/projects/general.observations.md
- ~/.claude/memory/tests/test_memory_integrity.py

Health check: 10/10 tests passed.

Quick start:
- Work on a project, then run /session-save
- Search past work with /search-memory
- Check integrity with /memory-health
```

If you run it again later (say, on the same machine after adding more repos), it fills in the gaps without touching existing files.

## Part of

[Memory Pack](../../packs/memory/README.md) — A file-based memory system that makes Claude Code remember your projects across sessions.
