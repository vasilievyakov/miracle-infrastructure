# aqal-review

Weekly development review that looks at more than your commit count. Four quadrants, five growth lines, one honest assessment every Friday.

## Why

Most productivity reviews track output: commits, PRs merged, tickets closed. That is one quadrant out of four. You could be shipping code every day while your team communication deteriorates, your technical debt compounds, and your stress levels quietly climb toward burnout. The AQAL model from integral theory measures development across four dimensions simultaneously. It takes 5 minutes every Friday. The history file tracks trends over months. After 12 weeks, you have a growth story no commit graph could tell.

## How It Works

The review evaluates progress across four quadrants and five development lines, then stores the results in a JSON history file for trend tracking.

```
DATA COLLECTION
  Git commits + project dossiers + session history
  + your answers to 4-5 reflective questions
       |
       v
QUADRANT ASSESSMENT
  I   (Interior Individual)  - mindfulness, focus, stress levels
  WE  (Interior Collective)  - communication, collaboration, client work
  IT  (Exterior Individual)  - technical skills, tools, code quality
  ITS (Exterior Collective)  - system stability, automation, infrastructure
       |
       v
DEVELOPMENT LINES (scored 0-100%)
  Cognitive     - systems thinking, abstraction
  Technical     - tool mastery, architecture
  Product       - user empathy, business sense
  Emotional     - stress management, resilience
  Interpersonal - communication, mentoring
       |
       v
STORED IN ~/.claude/aqal-history.json
  Trends visible after 4+ weeks
```

The overall assessment is simple:

| Assessment | Criteria |
|------------|----------|
| **Excellent** | 3+ quadrants trending up, no critical problems |
| **Normal** | Stability, 1-2 quadrants trending up |
| **Attention needed** | 2+ quadrants declining, critical problems present |

"Attention needed" is not a failure. It is a signal. Two declining quadrants usually point to one root cause, and catching it early beats discovering it a month later when the damage is real.

## Quick Install

```bash
# As part of Productivity pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Productivity pack

# Just this skill:
mkdir -p ~/.claude/skills/aqal-review
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/aqal-review/SKILL.md \
  -o ~/.claude/skills/aqal-review/SKILL.md
```

## Example

```
You: /aqal-review

Claude: Gathering data for the week...
  - 47 commits across 3 projects
  - 2 issues resolved (ev-radar, miracleops)
  - 8 sessions completed

Reflective questions:
1. How was your focus quality this week? Any distractions?
2. Did you communicate with anyone outside your own head?
3. What was the most frustrating moment?
4. Any infrastructure fires?

You: Focus was good, heads-down all week. No calls with anyone.
     Frustrating: spent 3 hours on a Docker networking issue.
     No fires, but I've been ignoring the monitoring alerts.

Claude:
  WEEKLY REVIEW — Week 8, 2026

  Overall: Normal (yellow)

  QUADRANTS
    I   (Individual Interior)  ↑ Up    — Good focus, managed frustration well
    WE  (Collective Interior)  ↓ Down  — Zero collaboration, no external feedback
    IT  (Individual Exterior)  ↑ Up    — 47 commits, 2 issues resolved
    ITS (Collective Exterior)  → Stable — No fires, but ignored monitoring alerts

  DEVELOPMENT LINES
    Cognitive:     82% (stable)
    Technical:     80% (+2, Docker issue resolved)
    Product:       75% (stable)
    Emotional:     70% (stable)
    Interpersonal: 62% (-3, isolation pattern forming)

  HIGHLIGHTS
    - Resolved long-standing ev-radar blocking issue
    - Clean debugging process on Docker networking

  GROWTH ZONES
    - WE quadrant declining for 2nd consecutive week
    - Schedule at least one external conversation next week
    - Address monitoring alerts before they become fires

  Saved to ~/.claude/aqal-history.json
```

## Part of

[Productivity Pack](../../packs/productivity/README.md) — structured self-reflection, not just output measurement.
