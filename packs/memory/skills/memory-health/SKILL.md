---
name: memory-health
description: |
  Validates memory system integrity: file consistency, observation counts, format correctness.
  Use when: (1) Suspecting data desync, (2) After bulk edits, (3) Periodic health check.
  Triggers: "/memory-health", "check memory", "memory health check".
invocation: user
---

# Memory Health Check

Runs validation across all memory files and produces a health report.

---

## Step 1: Run integrity tests

```bash
python3 ~/.claude/memory/tests/test_memory_integrity.py 2>&1
```

If all tests pass, report "All green" with the test count.

---

## Step 2: On failures, show and offer fixes

For each failed test:
1. Explain **what is wrong** (plain language)
2. Suggest a **specific fix**
3. If the fix is simple, do it immediately

Common errors:
- **Counts mismatch**: recount observations and update MEMORY.md
- **Missing in table**: add project to the MEMORY.md table
- **Invalid type**: check for typos in observations
- **No details for index**: add the missing Details section
- **Stale problem**: check if the problem has been resolved, update accordingly

---

## Step 3: Additional checks (beyond automated tests)

Manually check:
1. **Freshness**: Any projects with "Last session" more than 30 days ago? Warn.
2. **Size**: MEMORY.md over 40 lines? Observations over 20 entries? Suggest cleanup.
3. **Duplicates**: Any repeating observations by summary?

---

## Step 4: Report

```
Memory Health Check: {OK / N issues found}

Tests: {passed}/{total}
Dossiers: {count} ({list})
Observations: {total across all projects}
Open problems: {count}
{warnings if any}
```
