# Productivity Pack

A weekly review that looks at more than just your commit count.

<p align="center">
  <img src="../../docs/gifs/aqal-review.svg" alt="aqal-review demo" width="640" />
</p>

## The Idea

Most developer productivity reviews track one thing: output. Commits, PRs merged, tickets closed. That's one quadrant out of four. You could be shipping code every day while your team communication deteriorates, your technical debt compounds, and your stress levels quietly climb toward burnout.

The AQAL (All Quadrants, All Levels) model from integral theory measures development across four dimensions simultaneously. It takes 5 minutes every Friday. The history file tracks trends over months. This is structure for self-reflection, not just output measurement.

## What's Inside

### Skills (1)

| Skill | Command | What it does |
|-------|---------|--------------|
| [**aqal-review**](../../skills/aqal-review/) | `/aqal-review` | Weekly integral review across 4 quadrants and 5 development lines |

## How It Works

### The Four Quadrants

| Quadrant | Dimension | What it measures |
|----------|-----------|-----------------|
| **I** | Interior Individual | Mindfulness, frustration management, focus quality, self-awareness |
| **WE** | Interior Collective | Team communication, client interactions, collaboration quality, feedback given |
| **IT** | Exterior Individual | Technical skills, new tools mastered, code quality, learning velocity |
| **ITS** | Exterior Collective | System stability, automation coverage, cost optimization, infrastructure health |

The "I" quadrant is the one most reviews ignore. Shipping code while running on fumes is not sustainable. The review notices when that pattern starts forming.

### The Five Development Lines

Each line gets scored 0-100%. These track long-term growth, not weekly output.

| Line | What it tracks |
|------|---------------|
| **Cognitive** | Problem-solving complexity, systems thinking, abstraction ability |
| **Technical** | Language mastery, tool proficiency, architecture skills |
| **Product** | User empathy, business sense, prioritization quality |
| **Emotional** | Stress management, resilience, self-regulation |
| **Interpersonal** | Communication clarity, conflict resolution, mentoring |

### Assessment Criteria

The review evaluates each quadrant's trend direction, then synthesizes an overall assessment:

| Assessment | Criteria |
|------------|----------|
| **Excellent week** | 3+ quadrants trending up, no critical problems |
| **Normal week** | Stability, 1-2 quadrants trending up |
| **Attention needed** | 2+ quadrants declining, critical problems present |

"Attention needed" is not a failure. It's a signal. Two declining quadrants usually means one root cause, and finding it early beats finding it in a month when the damage is real.

### Field Notes (4 months of weekly reviews)

The "attention needed" assessment fired 3 times in 4 months. Each time, it identified the root cause correctly:

1. **Overwork.** I quadrant declining + IT quadrant declining. Shipping more code, enjoying it less, quality dropping. The fix was not "work harder." The fix was rest.
2. **Isolation.** WE quadrant declining + emotional line dropping. Building solo for too long without any human feedback loop. The fix was scheduling calls.
3. **Technical debt.** ITS quadrant declining across two consecutive weeks. Infrastructure warnings that got ignored until they couldn't be. The fix was a dedicated cleanup sprint.

The most common pattern in the first month: IT quadrant climbing steadily, WE quadrant flat or declining. This is the classic solo developer trajectory. You get technically sharper every week while your communication skills, client relationships, and collaboration instincts quietly atrophy. The review caught it. Adjustments were made. Without the structured check, this pattern would have continued invisibly for months.

### Data Collection

The review gathers data from:

```
Git activity (commits, branches, repos)
    +
Project progress (dossiers, open issues)
    +
Session history (topics discussed, problems solved)
    +
Your answers to 4-5 reflective questions
    ↓
Quadrant assessment + Development line scores
    ↓
Stored in ~/.claude/aqal-history.json
```

The reflective questions change based on what the data suggests. If git activity spiked this week, you might get asked about code review quality. If session history shows debugging-heavy work, you might get asked about frustration levels. The skill adapts.

### History Tracking

Results accumulate in `~/.claude/aqal-history.json`. Each entry records:

- Date and week number
- Quadrant trends (up, stable, down)
- Development line scores
- Highlights and challenges
- Next week's focus areas

After 4+ weeks, the skill starts identifying patterns. "IT quadrant has been trending up for 3 weeks, WE quadrant has been flat for 5 weeks" tells a clear story about where to invest attention next.

## Quick Start

1. Install the pack
2. Run `/aqal-review` on a Friday
3. Answer the reflective questions honestly (nobody sees this file except you)
4. Review the output. Note the "next week's focus" section
5. Repeat next Friday. Trends emerge after about a month

## Real Usage

Every Friday, 5 minutes, no exceptions. The value is not in any single review. The value is in the trend lines over 12+ weeks. One data point is a number. Twelve data points is a story.

The history file has become its own kind of journal. Not a diary. A structured record of growth patterns that's actually useful to re-read. The development line scores over 12 weeks paint a picture that no commit graph could show.

The structured format is what makes self-reflection work. Without structure, "how was your week?" gets a vague answer and a shrug. With four specific quadrants and five scored lines, the same question gets a precise answer that can be compared to last week's.

## Extension Points

- **Custom quadrant questions**: Add domain-specific reflective questions for your work context
- **Integration with project data**: The skill already reads git and session history. Additional data sources (time tracking, calendar) can be added
- **Team mode**: The AQAL model works for teams too. Adapt the WE and ITS quadrants for group assessment
- **Export format**: The JSON history can be visualized with any charting library. The structure is intentionally simple
