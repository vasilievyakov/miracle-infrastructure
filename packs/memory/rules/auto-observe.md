---
description: Automatically capture observations during project work
globs: "*"
---

# Auto-Capture Observations (Live Observer)

During project work, **after each significant event**, record an observation in the observations file.

## What counts as a significant event

| Type | Trigger | Example |
|------|---------|---------|
| **decision** | Architectural/technical/business decision made | "Chose JWT over sessions" |
| **bugfix** | Bug found and fixed | "Race condition in token refresh" |
| **feature** | New functionality created | "Added /api/status endpoint" |
| **discovery** | Unexpected fact uncovered | "API limits to 100 req/min" |
| **problem** | Issue found, not resolved now | "Memory leaks above 1000 records" |

## How to record

### 1. Identify the project

Match against `memory-config.json` keyword mappings (same as session-start.md).

### 2. Add entry to the Index table

```
Read ~/.claude/memory/projects/{project}.observations.md
```

Add a row to the Index table:
```
| {next_number} | {today} | {type} | {summary_30_chars} | {files} |
```

### 3. Add Details (at end of file)

```
### [{number}] {date} | {type} | {summary}
**Before:** {state before the change}
**After:** {state after the change}
**Files:** {affected files}
**Why:** {rationale / context for the decision}
```

### 4. Write the file

```
Edit ~/.claude/memory/projects/{project}.observations.md
```

## Rules

- **Do NOT interrupt** work for recording. Add observations alongside your response
- **Do NOT record trivia** like typos, formatting, trivial edits
- **Record causality.** Before/After are mandatory for decision and bugfix types
- **1-3 observations per session** at most, only significant ones
- **Summary under 50 characters.** This is what goes into the lightweight index
- If the observations file does not exist for a project, create it from the template:

```markdown
# Observations - {project-name}

## Index
| # | Date | Type | Summary | Files |
|---|------|------|---------|-------|

## Details
```

## Resolving observations

If a previously recorded problem is **solved** during work:

1. Find the entry in observations (type `problem`)
2. Add a `**Resolved:**` field in Details:

```
### [N] date | problem | summary
**Symptoms:** ...
**Impact:** ...
**Status:** Resolved
**Resolved:** {today} - {what was done}
```

3. Update the Index table. Add the `[R]` marker to Summary:

```
| N | date | problem | [R] summary | files |
```

4. If the problem was listed in MEMORY.md, remove it from "Open problems"

**Types that can be resolved:** problem, bugfix (recurring).
**Do not resolve:** decision, feature, discovery. They are not closable by nature.

---

## Do NOT record if

- Session is short (quick question-answer)
- Work is not tied to a specific project
- Nothing significant happened
- User is clearly experimenting/exploring
