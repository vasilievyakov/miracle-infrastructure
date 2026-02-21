---
name: aqal-review
description: "Weekly development review through the AQAL integral model. Evaluates progress across 4 quadrants (I/WE/IT/ITS) and 5 development lines. Run on Fridays via '/aqal-review'."
invocation: user
---

# AQAL Weekly Review

Weekly development review through the AQAL integral model. Evaluates progress holistically across interior/exterior and individual/collective dimensions.

## When to use
- Every Friday for weekly review
- When you need to assess progress for the week
- To update the AQAL dashboard

## Process

### Step 1: Gather data for the week

Review recent activity:
- Git commits across active projects
- Files created/modified
- Sessions completed
- Key decisions made

### Step 2: Analyze project activity

For each active project in memory:

```
Read ~/.claude/memory/MEMORY.md
```

For each project listed:
- New commits?
- Resolved issues?
- Production stability?
- Progress on planned work?

### Step 3: Evaluate across 4 quadrants

For each quadrant, evaluate progress: up (growth), stable (steady), down (declining)

**I (Interior Individual):**
- Mindfulness during work
- Frustration management
- Reflection and self-awareness

**WE (Interior Collective):**
- Team communication quality
- GitHub Issues quality
- Client interactions

**IT (Exterior Individual):**
- Technical skills
- New tools mastered
- Code quality

**ITS (Exterior Collective):**
- System stability
- Automation improvements
- Cost optimization

### Step 4: Evaluate development lines

Update scores (0-100%) for:
- Cognitive (systems thinking)
- Technical (tooling)
- Product (vision)
- Emotional (self-regulation)
- Interpersonal (delegation)

### Step 5: Record in history

Add a new entry to `~/.claude/aqal-history.json`:

```json
{
  "date": "YYYY-MM-DD",
  "week": N,
  "quadrants": {
    "I": { "score": 75, "trend": "up", "notes": "..." },
    "WE": { "score": 70, "trend": "stable", "notes": "..." },
    "IT": { "score": 80, "trend": "up", "notes": "..." },
    "ITS": { "score": 72, "trend": "up", "notes": "..." }
  },
  "lines": {
    "cognitive": 85,
    "technical": 78,
    "product": 82,
    "emotional": 65,
    "interpersonal": 70
  },
  "projects": {
    "project-a": { "status": "active", "progress": "stable" }
  },
  "highlights": ["..."],
  "challenges": ["..."],
  "nextWeekFocus": ["..."]
}
```

### Step 6: Generate summary

Show the user:
1. **Overall progress**: indicator (green: excellent / yellow: normal / red: attention needed)
2. **Key achievements** for the week
3. **Growth zones**: what needs attention
4. **Focus for next week**

## Assessment Criteria

### Overall week status
- **Excellent**: 3+ quadrants trending up, no critical problems
- **Normal**: Stability, 1-2 quadrants trending up
- **Attention**: 2+ quadrants trending down, critical problems

### Project status
- **thriving**: Active development, everything stable
- **stable**: Working, minimal changes
- **struggling**: Problems need attention
- **dormant**: No activity

## Reminder

Run every Friday:
```
/aqal-review
```
