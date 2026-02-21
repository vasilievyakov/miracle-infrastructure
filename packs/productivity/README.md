# Productivity Pack

A weekly review that looks at more than just your commit count.

## What it does

The AQAL (All Quadrants, All Levels) model from integral theory applied to weekly development reviews. Instead of tracking only "what I shipped," it evaluates progress across four dimensions:

| Quadrant | What it measures |
|----------|-----------------|
| **I** (Interior Individual) | Mindfulness, frustration management, self-awareness |
| **WE** (Interior Collective) | Team communication, client interactions, collaboration quality |
| **IT** (Exterior Individual) | Technical skills, new tools mastered, code quality |
| **ITS** (Exterior Collective) | System stability, automation, cost optimization |

Plus 5 development lines scored 0-100%: cognitive, technical, product, emotional, interpersonal.

## What is included

### Skills (1)

| Skill | Command | What it does |
|-------|---------|-------------|
| **aqal-review** | `/aqal-review` | Weekly integral review across 4 quadrants and 5 lines |

## How it works

1. Gathers data: git activity, project progress, session history
2. Evaluates each quadrant: trending up, stable, or declining
3. Scores development lines
4. Records in `~/.claude/aqal-history.json` for tracking over time
5. Produces a summary with highlights, challenges, and next week's focus

Run it every Friday. The history file tracks trends across weeks.

## Assessment criteria

- **Excellent week**: 3+ quadrants trending up, no critical problems
- **Normal week**: Stability, 1-2 quadrants trending up
- **Attention needed**: 2+ quadrants declining, critical problems present
