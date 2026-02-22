# Meta Pack

Audits for your infrastructure and code. Skills health and security posture in one pack.

<p align="center">
  <img src="../../docs/gifs/checkup.svg" alt="checkup demo" width="640" />
</p>

## The Idea

Two kinds of audits that you would never do manually.

**Skills health** (`/checkup`): as your library grows past a handful of files, things drift. References break, triggers collide, dependencies go stale. The checkup reads every file, validates relationships, and reports what needs attention.

**Security review** (`/security review`, `/security assess`): you ask Claude to "check security" and get inconsistent results. This skill runs 5 parallel agents for code review or 4 for enterprise assessment, each scanning through a specialized lens. Threat model calibration ensures findings match your actual deployment context.

The philosophy: apply, reflect, audit. The meta pack is the "reflect" step.

## What's Inside

### Skills (2)

| Skill | Command | What it does |
|-------|---------|--------------|
| [**skill-checkup**](../../skills/skill-checkup/) | `/checkup` | Skills library health audit with 3 validation levels |
| [**miracle-security**](../../skills/miracle-security/) | `/security review`, `/security assess` | Code security review (5 agents) and enterprise assessment (4 agents) with threat model calibration |

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

Checking 17 skills, 3 rules, 8 supporting files...

All clear. 0 issues found.
```

That's the goal. The best checkup output is no output. If you see results, something needs fixing. If you see nothing, go about your day.

### What "Unhealthy" Looks Like

```
$ /checkup --full

Checking 17 skills, 3 rules, 8 supporting files...

[x] skill/old-research.md → references ./data/sources.json (file not found)
[x] skill/deploy.md → trigger "/deploy" conflicts with skill/devops.md
[!] skill/memory-save.md → declares dependency on memory-config.json,
    actually reads memory-settings.json
[~] skill/research.md and skill/researching-web.md have 78% description overlap
    (possible duplicate?)

4 issues: 2 broken, 1 attention, 1 suggestion
```

### Field Notes (4 months of regular audits)

Trigger collision detection caught **5 conflicts in 4 months**. Two skills responding to the same command produces unpredictable behavior because the one that fires depends on loading order. Not the kind of debugging you want to do at 2am. Not the kind of debugging you want to do at any hour, really.

The Level 2 duplicate detection found **2 functionally identical skills with different names**. One was an early version that never got deleted. Cleanup was trivial once the overlap was visible. Without the semantic scan, these duplicates would have lived forever, silently consuming tokens and causing confusion about which version was "real."

The most common issue caught across all runs: broken file references. You rename a config file, forget to update the three skills that reference it, and nothing breaks immediately. The skill that needed that config just silently produces worse output. `/checkup` finds it before you notice the degradation.

## Quick Start

1. Install the pack
2. Run `/checkup` after installation to validate your existing skills
3. Fix any `[x]` results immediately
4. Review `[!]` results and fix if appropriate
5. Run `/checkup --full` once a month for the complete semantic analysis

## Real Usage

The typical cadence: run `/checkup` after installing any new skill or pack. Run `/checkup --full` once a month. The skill also reminds you if more than 14 days have passed since the last run.

The value proposition is maintenance you would never do manually. Nobody sits down on a Sunday morning and thinks "I should cross-reference all my skill triggers for collisions." Nobody opens dozens of skill files and compares their descriptions for semantic overlap. Nobody traces every file path reference to verify it still resolves. The checkup does all of this in seconds.

As the skills library grew from 10 to 48 skills (author's personal library including custom skills) over 6 months, the checkup went from "nice to have" to "necessary." At 10 skills, you can keep the whole system in your head. At 48 skills across 7 packs with shared dependencies, you cannot. The checkup is what lets you trust your infrastructure instead of worrying about it.

## Extension Points

- **Custom validation rules**: Add Level 1 checks specific to your skill naming conventions or dependency patterns
- **CI integration**: Use exit codes in CI: non-zero when `[x]` results exist
- **Ignore file**: Plan: `.checkupignore` to suppress known issues that don't need repeated reporting
- **Report format**: Plan: JSON output for programmatic consumption
