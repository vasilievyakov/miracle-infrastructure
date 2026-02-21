# Meta Pack

Your skills library has a doctor. It does not prescribe. It diagnoses.

<p align="center">
  <img src="../../docs/gifs/checkup.svg" alt="checkup demo" width="640" />
</p>

## The Idea

As your skills library grows past a handful of files, things drift. A skill references a file that was renamed last week. Two triggers collide and produce unpredictable behavior. A dependency chain breaks silently, and you discover it at 2am when the skill you need most returns a cryptic error.

This pack runs structural audits. It reads every skill, rule, and supporting file, validates their relationships, and reports what needs attention. Healthy skills produce no output. Only problems appear.

## What's Inside

### Skills (1)

| Skill | Command | What it does |
|-------|---------|--------------|
| **skill-checkup** | `/checkup` | Skills library health audit with 3 validation levels |

## How It Works

### Three Validation Levels

Each level checks for a different class of problem. Levels 0 and 1 run by default. Level 2 requires the `--full` flag because it involves semantic analysis and takes longer.

| Level | Name | What it checks | Speed |
|-------|------|----------------|-------|
| **Level 0** | Binary | File dependencies exist? Cross-references valid? Paths resolve? Naming conventions followed? | Fast |
| **Level 1** | Structural | Frontmatter valid? Trigger uniqueness? Dependency drift between declared and actual? | Fast |
| **Level 2** | Semantic | Duplicate skill detection? Description clarity? Format compliance across the library? | `--full` only |

### Result Labels

The output uses three labels. No color coding, no severity scores. Three symbols, each with a clear meaning.

| Label | Meaning | Action |
|-------|---------|--------|
| `[x]` | **Broken** | Fix now. Something is actively wrong |
| `[!]` | **Needs attention** | Fix soon. Not broken yet, heading that direction |
| `[~]` | **Suggestion** | Consider fixing. Semantic analysis found something odd |

`[x]` results appear at Level 0 and 1. These are definitive. A file is missing or a reference points nowhere.

`[!]` results appear at Level 1. These are structural concerns. Two skills have overlapping triggers, or a dependency was declared in frontmatter and doesn't match what the skill actually uses.

`[~]` results appear only at Level 2. These are judgment calls. Two skills have suspiciously similar descriptions, or a skill's description doesn't match its actual behavior.

### What "Healthy" Looks Like

```
$ /checkup

Checking 48 skills, 4 rules, 12 supporting files...

All clear. 0 issues found.
```

That's the goal. The best checkup output is no output. If you see results, something needs fixing. If you see nothing, go about your day.

### What "Unhealthy" Looks Like

```
$ /checkup --full

Checking 48 skills, 4 rules, 12 supporting files...

[x] skill/old-research.md → references ./data/sources.json (file not found)
[x] skill/deploy.md → trigger "/deploy" conflicts with skill/devops.md
[!] skill/memory-save.md → declares dependency on memory-config.json,
    actually reads memory-settings.json
[~] skill/research.md and skill/researching-web.md have 78% description overlap
    (possible duplicate?)

4 issues: 2 broken, 1 attention, 1 suggestion
```

## Quick Start

1. Install the pack
2. Run `/checkup` after installation to validate your existing skills
3. Fix any `[x]` results immediately
4. Review `[!]` results and fix if appropriate
5. Run `/checkup --full` once a month for the complete semantic analysis

## Real Usage

The typical cadence: run `/checkup` after installing any new skill or pack. Run `/checkup --full` once a month. The skill also reminds you if more than 14 days have passed since the last run.

The most common issue caught: broken file references. You rename a config file, forget to update the three skills that reference it, and nothing breaks immediately. The skill that needed that config just silently produces worse output. `/checkup` finds it before you do.

The trigger collision detection has caught five conflicts in four months. Two skills responding to the same command produces unpredictable behavior because the one that fires depends on loading order. Not the kind of debugging you want to do at 2am.

The Level 2 duplicate detection found two skills that were functionally identical with different names. One was an early version that never got deleted. Cleanup was trivial once the overlap was visible.

## Extension Points

- **Custom validation rules**: Add Level 1 checks specific to your skill naming conventions or dependency patterns
- **CI integration**: Run the checkup in a pre-commit hook or CI pipeline. The exit code is non-zero when `[x]` results exist
- **Ignore file**: Create a `.checkupignore` to suppress known issues that don't need repeated reporting
- **Report format**: The output is human-readable by default. JSON output is available for programmatic consumption
