# action-items

Extract tasks from transcripts, chats, and documents. Every task backed by a direct quote. 30 seconds, not 2 hours.

## Why

Nobody reads meeting transcripts twice. But buried in that wall of text are commitments, deadlines, unanswered questions, and the one thing someone said "I'll handle" and immediately forgot. This skill reads the transcript once and extracts everything worth doing into a prioritized checklist. It catches explicit promises ("I'll send it by Friday") and implicit tasks (questions nobody answered, problems nobody claimed). The "Unanswered Questions" section alone has justified the skill's existence by catching things that fall through the cracks in every meeting with more than 6 people.

## How It Works

```
INPUT: transcript / chat export / PDF / raw text
  |
  v
Identify participants (names, roles)
  |
  v
Extract commitments
  Explicit: "I will do X by Friday"
  Implicit: questions without answers, problems without owners
  |
  v
Classify and prioritize
  P0 Blocker: nothing moves without this
  P1 Urgent:  has a deadline or external pressure
  P2 Important: needs doing, not on fire
  P3 Backlog:  idea, wish, someday
  |
  v
OUTPUT: prioritized checklist with quotes and assignees
```

Accepts any text format: `.txt` transcripts, `.json` chat exports (Telegram, Slack), `.html` exports (WhatsApp), `.pdf` documents, or raw pasted text. Large files get chunked automatically. Multiple files get processed in parallel.

Every task includes a quote from the source text. When someone says "I never said that," you have the receipt.

## Quick Install

```bash
# As part of Content pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Content pack

# Just this skill:
mkdir -p ~/.claude/skills/action-items
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/action-items/SKILL.md \
  -o ~/.claude/skills/action-items/SKILL.md
```

## Example

```
You: /action-items
     [attaches q4-planning-call.txt]

# Action Items: Q4 Planning Call
> Extracted from: q4-planning-call.txt
> Date: 2026-02-21
> Participants: Alex (lead), Maria (sales), Dev team

## P0: Blockers
- [ ] **Fix authentication on staging** - Alex | by Wednesday
  > "We literally cannot demo anything until staging auth works"

## P1: Urgent
- [ ] **Send updated proposal to Acme Corp** - Maria | by Thursday
  > "Their board meets Friday, we need it in their hands before that"

## P2: Important
- [ ] **Add regional filtering to dashboard** - Dev team | this sprint
  > "They kept asking about per-region breakdown"

## P3: Backlog
- [ ] **Research SSO integration options** - unassigned
  > "Would be nice to have eventually"

## Unanswered Questions
- Who owns the relationship with their CTO? (raised by Maria, no response)
- What's the budget for the pilot phase? (discussed, no conclusion)

## Key Decisions
- Go with phased rollout instead of big-bang launch
- Prioritize Acme Corp over other prospects this quarter

---
Extracted 7 tasks from q4-planning-call.txt.

What's next?
1. Save to file (action-items-2026-02-21.md)
2. Link to project via /session-save
3. Clarify/reprioritize
```

## Works great with

- [Transcript to Proposal](../transcript-to-proposal/) — extract tasks from a client call, then generate a full proposal from the same transcript
- [Memory Pack](../../packs/memory/) — after extracting action items, run `/session-save` to record decisions and tasks in your project memory

## Part of

[Content Pack](../../packs/content/README.md) — turning raw text into structured, actionable output.
