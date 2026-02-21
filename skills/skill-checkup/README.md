# skill-checkup

Health audit for your skills library. Finds broken references, trigger collisions, and dependency drift before they find you at 2am.

## Why

As your skills library grows past a handful of files, things drift silently. A skill references a config file you renamed last week. Two triggers collide and produce unpredictable behavior depending on loading order. A dependency gets updated but the skill that relies on it was never retested. Nothing crashes immediately. Output just gets quietly worse. This skill reads every file, validates every reference, checks every trigger for uniqueness, and reports what needs attention. If everything is healthy, it says so and shuts up.

## How It Works

Three validation levels. Levels 0 and 1 run by default. Level 2 requires the `--full` flag because semantic analysis takes longer.

```
LEVEL 0: Binary Checks (fast)
  - Do referenced files exist?
  - Do cross-references to other skills resolve?
  - Are absolute paths valid?
  - Is the file named SKILL.md (not skill.md)?

LEVEL 1: Structural Checks (fast)
  - Is YAML frontmatter valid (name, description)?
  - Are triggers unique across all skills?
  - Has a dependency been modified after the skill that uses it?

LEVEL 2: Semantic Analysis (--full only)
  - Do two skills do the same thing? (>70% overlap flagged)
  - Can a user tell when to invoke it from the description alone?
  - Does the description follow the "Use when..." pattern?
```

Three result labels, each with a clear meaning:

| Label | Meaning | Action |
|-------|---------|--------|
| `[x]` | Broken | Fix now. A file is missing or a reference points nowhere |
| `[!]` | Needs attention | Fix soon. Trigger collision, dependency drift |
| `[~]` | Suggestion | Consider fixing. Semantic overlap, vague description |

Healthy skills produce no output. Only problems appear. The best checkup result is no result.

## Quick Install

```bash
# As part of Meta pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Meta pack

# Just this skill:
mkdir -p ~/.claude/skills/skill-checkup
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/skill-checkup/SKILL.md \
  -o ~/.claude/skills/skill-checkup/SKILL.md
```

## Example

```
You: /checkup

48 skills. Library is healthy.

Checked in 4 seconds. No issues found.
```

And when things go wrong:

```
You: /checkup --full

48 skills. 4 issues found.
46 healthy. 2 need attention. 1 broken.

[x] /old-research: references ./data/sources.json (file not found)
    -> Restore the file or update the path (line 34 in SKILL.md)

[!] /deploy: trigger "/deploy" conflicts with /devops
    -> Rename one trigger to avoid unpredictable behavior

[!] /memory-save: dependency memory-config.json modified 12 days
    after skill was last updated
    -> Review whether the config change affects skill logic

---
Suggestions:

[~] /research and /researching-web: 78% description overlap
    -> Consider merging or clarifying boundaries

Checked in 8 seconds.
```

Results are stored in `~/.claude/checkup-history.json` (last 20 runs), so you can track whether your library health is improving or drifting over time.

## Part of

[Meta Pack](../../packs/meta/README.md) — structural audits for your skills infrastructure.
