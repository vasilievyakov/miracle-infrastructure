---
name: action-items
description: |
  Extracts tasks, commitments, and deadlines from transcripts, chats, and documents.
  Use when: (1) Audio transcript + "what needs to be done", (2) Chat export + "tasks for the meeting",
  (3) Multiple files for batch processing, (4) Any text that needs action items extracted.
  Triggers: "/action-items", "what needs to be done", "action items", "extract tasks".
---

# Action Items: Extract Tasks from Any Text

Quickly turns call transcripts, chats, documents into a structured task list with assignees, deadlines, and priorities.

---

## Step 1: Accept input

The user can provide:

| Format | How to process |
|--------|---------------|
| `.txt` file | Audio transcript (Whisper). Read entirely |
| `.json` (Chat export) | Extract `messages[].text`, `messages[].from` |
| `.html` (Chat export) | Extract message text from HTML |
| `.pdf` | Extract text |
| Multiple files | Process each, merge results |
| Text in message | Process directly |

**If no file provided, ask:**
```
Attach a file (transcript, chat, document) or paste text
from which to extract tasks.
```

### Handling large files

If file > 25000 tokens:
1. Read first 500 lines for context and participants
2. Process in blocks of 500 lines
3. Merge results, remove duplicates

### Handling multiple files

If the user provides multiple files:
1. Process each in parallel via Task tool (subagent_type: "general-purpose")
2. Give each agent this same prompt for extraction
3. Merge and deduplicate results

---

## Step 2: Identify participants

Extract all mentioned people/roles from the text:

- By name: "Alex said...", "Maria suggested..."
- By role: "client", "designer", "developer"
- User = "I", "me", "we"

Result: list of `{name/role}` for task assignment.

---

## Step 3: Extract all commitments and tasks

Search the text for:

### Explicit commitments
- "I will do...", "We will prepare...", "I will send by..."
- "Need to...", "Must...", "Should..."
- "Let's...", "Agreed that..."

### Implicit tasks
- Questions without answers -> task "find out/answer"
- Problems without solutions -> task "resolve/investigate"
- Ideas/suggestions -> task "consider/evaluate"

### Deadlines
- Explicit: "by Friday", "by February 15", "next week"
- Implicit: "urgently", "ASAP", "when there's time"
- Contextual: "before the meeting", "before launch"

---

## Step 4: Classify and prioritize

For each task determine:

**Priority:**
- **P0, Blocker**: cannot move forward without this
- **P1, Urgent**: has a deadline or external pressure
- **P2, Important**: needs to be done, not on fire
- **P3, Someday**: idea, wish, backlog

**Type:**
- Decision (approve/decide)
- Action (do/create/send)
- Communication (write/call/discuss)
- Research (find out/verify/investigate)

---

## Step 5: Generate report

Output format:

```markdown
# Action Items: {source}
> Extracted from: {filename or description}
> Date: {today}
> Participants: {list}

## P0: Blockers
- [ ] **{task}** - {assignee} | {deadline}
  > Context: "{quote from text}"

## P1: Urgent
- [ ] **{task}** - {assignee} | {deadline}
  > Context: "{quote}"

## P2: Important
- [ ] **{task}** - {assignee}
  > Context: "{quote}"

## P3: Backlog
- [ ] {task}

---

## Unanswered Questions
- {question that was raised and not resolved}

## Key Decisions
- {what was decided during the conversation, for context}
```

---

## Step 6: Suggest next step

After the report:

```
Extracted {N} tasks from {source}.

What's next?
1. Save to file (action-items-{date}.md)
2. Link to project via /session-save
3. Clarify/reprioritize
```

---

## Rules

### Accuracy over completeness
- Better to miss a questionable task than to invent a nonexistent one
- Every task must be backed by a quote from the source text
- If assignee unclear, write "unassigned"

### Do not over-interpret
- Extract only what is **said** or **clearly implied**
- Do not invent tasks that are not in the text
- If context is ambiguous, note it

### Audio transcript specifics
- Whisper may confuse names. Flag if a name seems uncertain
- "I guess we kinda should..." = weak task (P3)
- "Make sure you do this by..." = strong task (P1)
- Transcripts often contain false starts and repetitions. Filter them
