---
name: checkup
description: "Use when you need to validate the health of your Claude Code skills library. Checks for broken file references, missing dependencies, frontmatter issues, duplicate triggers, and dependency drift. Runs structural and semantic audits across all installed skills. Invoke via '/checkup', '/review-skills', or 'check my skills'."
argument-hint: "[--quick | --full | skill-name]"
---

# /checkup: Skills Library Health Check

Validates the structural health of your Claude Code skills. Reports problems, does not auto-fix.

## Triggers

- `/checkup`: standard check (Level 0 + Level 1)
- `/checkup --quick`: binary checks only (Level 0)
- `/checkup --full`: all levels including semantic analysis (Level 2)
- `/checkup <skill-name>`: check a single skill
- `/review-skills`: alias for `/checkup`

## When NOT to Use

- Checking a single skill file you just wrote: use manual review instead
- Investigating runtime behavior: this is structural, not functional
- Fewer than 5 skills installed: overhead exceeds value

## Workflow

### Phase 0: Canary + Discovery

**Canary test**: verify a known truth before proceeding:

Determine the skills directory. Use `$HOME` to expand the path:
```
Bash: ls "$HOME/.claude/skills/"
```
If the directory does not exist or is empty, STOP. Report: "Skills directory not found at ~/.claude/skills/. Cannot proceed." The rest of the report is unreliable.

**Discovery**: build the full catalog:

1. Find all skill files:
```
Bash: find "$HOME/.claude/skills" -maxdepth 2 -name "SKILL.md" | sort
```
Also check for lowercase variants (`skill.md`) which indicate a naming issue.

2. For each skill, collect metadata:
   - File path
   - Last modified date
   - File size
   - `name` from frontmatter
   - `description` from frontmatter

3. Store the catalog in memory for subsequent phases.

### Phase 1: Validation (Level 0 + Level 1)

All results are marked as **FACT**.

#### Level 0: Binary Checks

For each skill:

**1. File dependencies exist.**
Extract all file paths from the skill text. For each path, expand `~` to `$HOME` and check existence. If missing: `[x]`.

**2. Cross-references to other skills are valid.**
Extract all skill mentions. Verify each referenced skill exists in the catalog. If not: `[x]`.

**3. Absolute paths are valid.**
Find all absolute paths. Verify existence. If missing: `[x]`.

**4. File naming is correct.**
Verify the main file is named exactly `SKILL.md`. If wrong: `[!]`.

#### Level 1: Structural Checks

**5. Frontmatter is valid.**
Verify required elements:
- YAML frontmatter block (between `---` markers)
- `name` field present and non-empty
- `description` field present and non-empty
- At least one `##` section heading in the body
If anything is missing — `[!]`.

Verify no invalid fields. The only valid frontmatter fields are:
`name`, `description`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `context`, `agent`, `hooks`.
Any other field (e.g. `invocation`, `license`, `version`) — `[!]` with message: "unknown frontmatter field '{field}' — will be ignored by Claude Code".

**6. Trigger uniqueness.**
Collect all triggers from all skills. If two skills share the same trigger: `[!]` for both.

**7. Drift detection.**
Compare skill last-modified date with each dependency's last-modified date. If dependency was modified AFTER the skill: `[!]` with drift in days.

### Phase 2: Semantic Analysis (Level 2, only with --full)

Results are marked as **SUGGESTION**.

The auditor SKIPS ITSELF in semantic checks.

**8. Duplicate detection.**
Compare skills pairwise: do two skills do the same thing? If overlap >70%: `[~]`.

**9. Description clarity.**
Can a user tell when to invoke it from the description alone? If vague: `[~]`.

**10. Description format.**
Does it follow the "Use when..." pattern? If not: `[~]`.

---

## Output Format

```
Last checkup: {date}. Since then: {+N skills, -N issues resolved, +N new issues}.

{N} skills. Library is healthy.
{healthy} healthy. {attention} need attention. {broken} broken.

[x] /{skill}: {what is wrong, plain language}
    -> {what to do} (line {N} in {file path})

[!] /{skill}: drift, dependency {file} modified {N} days after skill
    -> Review whether the change affects skill logic

---
Suggestions (--full only):

[~] /{skill-a} and /{skill-b}: possible functional overlap
    -> Consider merging or clarifying boundaries

Checked in {N} seconds.
```

**Format rules:**
- Healthy skills are NOT listed
- `[x]`: broken (FACT, action required)
- `[!]`: needs attention (FACT, drift or potential issue)
- `[~]`: suggestion (SUGGESTION, from Level 2)
- Verdict first, then numbers, then issues
- Each issue: what is wrong + what to do + where (file:line)
- SUGGESTIONS block is visually separated from FACTS
- If everything is healthy, say so. Do not list N lines of "OK"
- No emoji

**If the library is fully healthy:**
```
{N} skills. Library is healthy.

Checked in {N} seconds. No issues found.
```

---

## History

After each run, persist the result to `~/.claude/checkup-history.json`:

```json
{
  "date": "YYYY-MM-DD",
  "mode": "default|quick|full",
  "summary": {
    "total": 48,
    "healthy": 46,
    "attention": 2,
    "broken": 0
  },
  "issues": [],
  "duration_seconds": 8
}
```

Keep the last 20 runs. Drop older entries when writing a new one.

---

## Principles

1. **Navigator, not autopilot.** Reports problems, does not fix them.
2. **FACT vs SUGGESTION.** The user always knows what is deterministic and what is a recommendation.
3. **Healthy skills are silence.** Only problems appear in the report.
4. **Tone is care, not control.** No shouting, no aggression. A calm doctor.
5. **Specificity.** Not "problem in skill X". Rather "file Y not found, line Z, action: restore or update path".
