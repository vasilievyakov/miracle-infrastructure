# session-save

Save your work so tomorrow's Claude actually knows what happened today.

## Why

Claude Code has no memory between sessions. You explain your architecture on Monday, and on Tuesday it asks what framework you use. Again. `/session-save` writes the important parts of your session into a project dossier and observations file, so the next session starts where this one left off instead of from absolute zero.

## How It Works

An 8-step workflow runs when you invoke the command:

1. **Identify the project** from your working directory, modified files, or config keywords
2. **Gather context** from the conversation: git commits, decisions, unresolved problems, next steps
3. **Read the existing dossier** (or create one from scratch)
4. **Update the dossier** with surgical precision: overwrite the snapshot sections, append to history sections, never delete decisions
5. **Record observations** as typed entries (decision, bugfix, feature, discovery, problem) with Before/After context
6. **Sync MEMORY.md** to keep the global index accurate
7. **Write all files** in one batch
8. **Confirm** with a summary of what was recorded

```
Session saved to my-app memory.

Recorded:
- Done: 3 items
- Decisions: 1 decision
- Problems: 1 unresolved
- Observations: 2 new observations
- Next steps: 4 tasks

Next session will load the dossier and continue from here.
```

The dossier uses a specific update policy: Current State gets overwritten (it is a snapshot), Decisions Made only grows (history is sacred), and Session History keeps the last 10 entries. This means you never lose the reasoning behind past choices, but stale status information gets replaced.

## Quick Install

```bash
# As part of Memory pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Memory pack

# Just this skill:
mkdir -p ~/.claude/skills/session-save
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/session-save/SKILL.md \
  -o ~/.claude/skills/session-save/SKILL.md
```

## Example

You spent two hours debugging a race condition in token refresh, decided to switch from polling to websockets, and left three TODO items for tomorrow. Instead of hoping you will remember all of that:

```
You: /session-save

Claude: Session saved to ev-radar memory.

Recorded:
- Done: Fixed race condition in token refresh, refactored auth module
- Decisions: Switched from polling to websockets for real-time updates
- Problems: 1 unresolved (memory leak above 1k records)
- Observations: 3 new observations (bugfix, decision, problem)
- Next steps: Implement websocket handler, add reconnection logic, write tests
```

Tomorrow, when you open the project, `session-start` loads the dossier automatically. Claude knows the architecture, the decision history, and exactly where you left off. No re-explanation needed.

## Part of

[Memory Pack](../../packs/memory/README.md) — A file-based memory system that makes Claude Code remember your projects across sessions.
