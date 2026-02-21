# Meta Pack

Your skills library has a doctor. It does not prescribe, it diagnoses.

## What it does

As your skills library grows past a handful of files, things drift. File references break, dependencies change, triggers collide. This pack runs structural audits and reports what needs attention.

## What is included

### Skills (1)

| Skill | Command | What it does |
|-------|---------|-------------|
| **skill-checkup** | `/checkup` | Skills library health audit with 3 validation levels |

## How it works

Three levels of validation:

| Level | What it checks | Speed |
|-------|---------------|-------|
| **Level 0** (binary) | File dependencies exist, cross-references valid, paths valid, naming correct | Fast |
| **Level 1** (structural) | Frontmatter valid, trigger uniqueness, dependency drift detection | Fast |
| **Level 2** (semantic) | Duplicate detection, description clarity, format compliance | `--full` only |

Results are clearly labeled:
- `[x]` Broken (action required)
- `[!]` Needs attention (potential issue)
- `[~]` Suggestion (semantic analysis)

Healthy skills produce no output. Only problems appear.

## When to run

- After installing new skills
- After modifying skill dependencies
- Periodically (the skill reminds you if it has been over 14 days)
- After `/checkup --full` once a month for semantic analysis
