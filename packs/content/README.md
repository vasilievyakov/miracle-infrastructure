# Content Pack

Extracts actionable tasks from walls of text. Because nobody reads meeting transcripts twice.

## What it does

Give it a transcript, chat export, PDF, or just a block of text. It extracts every task, commitment, and deadline, classifies by priority, identifies assignees, and produces a structured checklist.

## What is included

### Skills (1)

| Skill | Command | What it does |
|-------|---------|-------------|
| **action-items** | `/action-items` | Extract tasks from transcripts, chats, and documents |

## How it works

1. Accepts any text format: .txt transcripts, JSON/HTML chat exports, PDFs, raw text
2. Identifies participants by name and role
3. Extracts explicit commitments ("I will do X by Friday") and implicit tasks (unanswered questions, unresolved problems)
4. Classifies each task: P0 (blocker) through P3 (backlog)
5. Outputs a structured checklist with quotes from the source

Handles large files by processing in blocks. Handles multiple files by running parallel agents.

## Output format

```markdown
# Action Items: {source}

## P0: Blockers
- [ ] **Task** - Assignee | Deadline
  > Context: "quote from text"

## P1: Urgent
...

## Unanswered Questions
- Question that was raised and not resolved
```
