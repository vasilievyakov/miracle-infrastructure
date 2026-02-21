---
name: search-memory
description: |
  Search project memory: observations, decisions, problems. Query by type, file, concept, date.
  Use when: (1) "What decisions did we make about auth?", (2) "All bugs in project X",
  (3) "What do we know about caching?", (4) "Open problems across all projects".
  Triggers: "/search-memory", "search memory", "what do we know about".
---

# Search Memory

Searches observations and dossiers across all projects. Like `type:decision file:auth.ts` from structured memory systems, with zero external dependencies.

---

## Query Syntax

Supports filter combinations:

| Filter | Example | Searches |
|--------|---------|----------|
| **Free text** | `caching` | Summary and details across all observations |
| **type:** | `type:decision` | By type: decision, bugfix, feature, discovery, problem |
| **project:** | `project:my-app` | Within a specific project |
| **file:** | `file:auth.ts` | By affected files |
| **date:** | `date:2026-02` | By date (year-month or year-month-day) |
| **status:** | `status:open` | Open problems (problem without resolution) |

### Example queries

```
/search-memory type:decision caching
/search-memory project:my-app type:problem
/search-memory file:dashboard
/search-memory type:problem status:open
/search-memory date:2026-02 type:feature
/search-memory what do we know about websockets
```

---

## Search Algorithm

### Step 1: Determine scope

- If `project:` is specified, search only that project
- If not specified, search **all projects**

### Step 2: Load indexes

For each project in scope:

```
Read ~/.claude/memory/projects/{project}.observations.md
```

Parse **only the Index table** first (progressive disclosure: do not load Details).

### Step 3: Filter by index

Apply filters to index rows:
- `type:` matches the Type column
- `date:` matches the Date column
- `file:` matches the Files column
- Free text matches the Summary column

### Step 4: Load details (on demand)

For matched entries, load the Details section **only for those matches**.

This is **progressive disclosure**: index costs ~40 tokens per entry, details cost ~150 tokens. With 100 observations, savings: 4,000 tokens instead of 15,000.

### Step 5: Also search dossiers

Additionally check `{project}.md` dossier files:
- "Decisions Made" section
- "Unresolved Problems" section
- "Next Steps" section

---

## Output Format

```markdown
## Search results: "{query}"
Found: {N} observations in {M} projects

### project-name ({n} matches)
| # | Date | Type | Summary |
|---|------|------|---------|
| 3 | 2026-01-02 | problem | Scraping too expensive |

**[3] Details:**
Before: High bills
After: Not resolved
Files: scheduler/*, worker/*

### another-project ({n} matches)
...
```

---

## Special Queries

### "All open problems"
```
/search-memory type:problem status:open
```
Finds all entries of type `problem` where Details does not contain "Status: Resolved".

### "What do we know about X?"
```
/search-memory {concept}
```
Searches all fields: summary, details, files. Also checks dossiers.

### "Decision history for project"
```
/search-memory project:my-app type:decision
```
Chronological list of all decisions with before/after context.

### "What changed in file X?"
```
/search-memory file:dashboard_api.py
```
All observations affecting that file.

---

## Important

- **Progressive disclosure**: always start with the index, load details only for matches
- **Sort results by date** (newest first)
- **If nothing found**, say so directly. Do not make things up
- **Maximum 20 results**. If more, show first 20 and state how many remain
