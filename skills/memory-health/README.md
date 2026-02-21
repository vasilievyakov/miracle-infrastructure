# memory-health

Find out if your memory system is lying to you before it matters.

## Why

The memory system is a collection of interconnected markdown files. MEMORY.md references dossiers, dossiers reference observations, observation indexes should match their detail sections, and problem counts should stay in sync. Over time, things drift. You resolve a problem but forget to update the index. You delete a dossier but leave it in the project table. You add observations but the count in MEMORY.md still says "3 entries" when there are 7. `/memory-health` runs integrity checks across everything and tells you exactly what is broken and how to fix it.

## How It Works

The skill runs in three phases:

**Phase 1: Automated tests.** Executes `test_memory_integrity.py`, which validates:
- Observation counts in MEMORY.md match actual index rows
- Every dossier referenced in the project table exists on disk
- Every observation type is one of the valid types
- Every index entry has a corresponding details section
- Open problems listed in MEMORY.md actually exist as unresolved observations

**Phase 2: Manual checks** that go beyond what the test script covers:
- Freshness: warns about projects with no session in the last 30 days
- Size: flags MEMORY.md over 40 lines or observation files over 20 entries
- Duplicates: spots repeated observations by summary text

**Phase 3: Report.**

```
Memory Health Check: 2 issues found

Tests: 8/10 passed
Dossiers: 5 (ev-radar, my-app, api-service, chatbot, general)
Observations: 47 across all projects
Open problems: 3

Issues:
1. ev-radar observation count: MEMORY.md says 4, actual is 6. Fix: update count.
2. my-app #3 (problem): marked open in MEMORY.md but resolved in observations. Fix: remove from open problems.

Warnings:
- chatbot: last session 45 days ago. Consider archiving or updating.
```

Simple fixes (like count mismatches) get applied automatically. More ambiguous issues get flagged with a suggested fix for you to approve.

## Install

> **Pack-only.** This skill validates the integrity of memory files and runs `test_memory_integrity.py`. Without the memory system installed, there is nothing to validate. Install the full [Memory Pack](../../packs/memory/), not this skill alone.

```bash
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Memory pack
```

After installation, run `/memory-init` to create the directory structure, then `/memory-health` to verify everything is wired correctly.

## Example

After a few weeks of active use across multiple projects, you notice that `/search-memory type:problem status:open` returns a problem you are pretty sure was fixed last week:

```
You: /memory-health

Claude:
Memory Health Check: 3 issues found

Tests: 7/10 passed
Dossiers: 4 (ev-radar, greatlist, my-app, general)
Observations: 31 across all projects
Open problems: 2

Issues:
1. greatlist observation count: MEMORY.md says 6, actual is 8.
   -> Fixed: updated count to 8.
2. ev-radar #4 "Instagram actor blocked": listed as open problem in MEMORY.md,
   but observation has "Status: Resolved" in details.
   -> Fixed: removed from open problems list.
3. my-app #2 has index entry but no Details section.
   -> Added placeholder. Please fill in the Before/After context.

Warnings:
- general: last session 38 days ago.

All other checks passed.
```

Running this once a week (or whenever something feels off) keeps the memory system honest.

## Part of

[Memory Pack](../../packs/memory/README.md) — A file-based memory system that makes Claude Code remember your projects across sessions.
