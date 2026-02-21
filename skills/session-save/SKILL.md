---
name: session-save
description: |
  Saves session context to project memory. Run at end of work or when switching projects.
  Use when: (1) Ending a work session, (2) Switching projects, (3) Before a long break.
  Triggers: "/session-save", "save session", "remember context".
invocation: user
---

# Session Save

Saves key information from the current session into long-term memory so the next session does not start from zero.

---

## Step 1: Identify the project

Determine which project the work was about:

1. Check the current working directory
2. Check which files were read/modified during the session
3. If the project is unclear, ask the user

Load keyword mappings from config:

```
Read ~/.claude/memory/memory-config.json
```

Match the session context against project keywords. Use `fallback_project` from config if no match.

---

## Step 2: Gather session context

Analyze what happened during the session:

### 2a. What was done
```bash
# If there is a git repository:
git log --oneline -5  # recent commits
git diff --stat       # uncommitted changes
```

If git is unavailable, rely on conversation history: which files were created, modified, which tasks were solved.

### 2b. Decisions made

Extract from the conversation:
- Architectural decisions ("chose X over Y")
- Configuration decisions ("configured Z this way")
- Business decisions ("client wants A, dropped B")

### 2c. Unresolved problems

- Bugs not yet fixed
- Tasks postponed
- Questions without answers

### 2d. What to do next

- Explicitly stated next steps
- Tasks that follow from completed work

---

## Step 3: Read existing dossier

```
Read ~/.claude/memory/projects/{project-name}.md
```

If the file does not exist, create a new dossier using the template from Step 4.

If it exists, **update** it. Do not overwrite completely. Preserve history.

---

## Step 4: Write updated dossier

Project dossier format:

```markdown
# {Project Name}

## Status
{One sentence: active/paused/completed}

## Description
{2-3 sentences: what it is, what it does, who uses it}

## Architecture
{Key components, stack, deployment}

## Current State
- Last session: {date}
- Done: {list}
- Uncommitted: {yes/no, what}

## Unresolved Problems
- {problem 1}
- {problem 2}

## Decisions Made
- [{date}] {decision and rationale}

## Next Steps
1. {task}
2. {task}

## Session History
- [{date}] {brief description of work}
```

**Update rules:**
- **Current State**: overwrite completely (this is a snapshot)
- **Unresolved Problems**: remove solved ones, add new ones
- **Decisions Made**: only append, never delete
- **Next Steps**: overwrite (this is the current plan)
- **Session History**: add new entry at the top, keep the last 10

---

## Step 5: Update Observations

In addition to the dossier, add typed observations to the observations file:

```
Read ~/.claude/memory/projects/{project-name}.observations.md
```

For each significant session event, add an entry:
- To the **Index** table (~40 tokens per row)
- To the **Details** section (Before/After/Files/Why, ~150 tokens)

Types: decision, bugfix, feature, discovery, problem.

If the file does not exist, create it from template:
```markdown
# Observations - {project-name}

## Index
| # | Date | Type | Summary | Files |
|---|------|------|---------|-------|

## Details
```

---

## Step 6: Sync MEMORY.md

After updating the dossier and observations, update MEMORY.md:

```
Read ~/.claude/memory/MEMORY.md
```

Update:
1. **Observation counts** in the project table. Recount Index table rows
2. **Open problems**. Rebuild from all observations:
   - Find all entries of type `problem` without the `[R]` marker in Summary
   - Format: `- {project} #{number}: {summary}`
3. **Warnings**. If there were discoveries signaling risks, add them

---

## Step 7: Save files

```
Edit ~/.claude/memory/projects/{project-name}.md
Edit ~/.claude/memory/projects/{project-name}.observations.md
Edit ~/.claude/memory/MEMORY.md
```

---

## Step 8: Confirmation

Show the user a brief summary:

```
Session saved to {project-name} memory.

Recorded:
- Done: {N items}
- Decisions: {N decisions}
- Problems: {N unresolved}
- Observations: {N new observations}
- Next steps: {N tasks}

Next session will load the dossier and continue from here.
```

---

## Important

- **Do NOT record** sensitive data (passwords, tokens, API keys)
- **Do NOT duplicate** code. Reference files and line numbers
- **Be concise.** The dossier should fit in 200 lines
- **Update, do not overwrite.** Decision history is critical
