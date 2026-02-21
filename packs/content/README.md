# Content Pack

Nobody reads meeting transcripts twice. This skill reads them once and extracts everything worth doing.

<p align="center">
  <img src="../../docs/gifs/action-items.svg" alt="action-items demo" width="640" />
</p>

## The Idea

You have a wall of text. A meeting transcript, a Telegram chat export, a PDF from a partner, a block of raw notes. Somewhere in there are tasks, commitments, deadlines, and unanswered questions. You could read through the whole thing with a highlighter. Or you could run `/action-items` and get a prioritized checklist in about 30 seconds.

The transcript-to-checklist pipeline saves about 2 hours per meeting. More for the ones with 12 participants who all talk over each other.

## What's Inside

### Skills (1)

| Skill | Command | What it does |
|-------|---------|--------------|
| **action-items** | `/action-items` | Extract tasks, commitments, and deadlines from any text format |

## How It Works

### Input Formats

The skill accepts anything that contains text. It is not picky.

| Format | Examples |
|--------|---------|
| `.txt` | Meeting transcripts, raw notes |
| `.json` | Telegram exports, Slack exports, any structured chat |
| `.html` | WhatsApp exports, web-saved conversations |
| `.pdf` | Partner documents, contracts, briefs |
| Raw text | Paste directly into the prompt |

Large files get processed in blocks. Multiple files get processed by parallel agents. A 90-minute all-hands transcript gets the same treatment as a 3-line Slack message. Just faster.

### Extraction Logic

The skill finds two kinds of tasks:

**Explicit commitments**: Someone said "I will do X by Friday." Clear assignee, clear task, clear deadline.

**Implicit tasks**: A question was asked and nobody answered. A problem was identified and nobody claimed it. An idea was floated and everyone agreed it was great, and then the conversation moved on. These show up in the output too.

### Priority Classification

| Priority | Meaning | Example |
|----------|---------|---------|
| **P0** | Blocker. Nothing else moves until this is done | "Server is down, clients can't log in" |
| **P1** | Urgent. Do this today or tomorrow | "Send the contract before their board meeting Thursday" |
| **P2** | Important. This week | "Update the dashboard with new KPIs" |
| **P3** | Backlog. Eventually | "We should probably automate that report someday" |

### Output Format

```markdown
# Action Items: Q4 Planning Call

## P0: Blockers
- [ ] **Fix authentication on staging** - @alex | by Wednesday
  > "We literally cannot demo anything until staging auth works"

## P1: Urgent
- [ ] **Send updated proposal to Acme Corp** - @maria | by Thursday
  > "Their board meets Friday, we need it in their hands before that"

## P2: Important
- [ ] **Add regional filtering to dashboard** - @dev team | this sprint
  > "They kept asking about per-region breakdown"

## P3: Backlog
- [ ] **Research SSO integration options** - unassigned
  > "Would be nice to have eventually"

## Unanswered Questions
- Who owns the relationship with their CTO? (raised by @maria, no response)
- What's the budget for the pilot phase? (discussed, no conclusion)
```

Every task includes a quote from the source. So when someone says "I never said that," you have the receipt.

## Quick Start

1. Install the pack
2. Have a transcript, chat export, or document ready
3. Run `/action-items` and point it at the file (or paste text directly)
4. Review the prioritized checklist
5. Copy into your task tracker, or use as-is

## Real Usage

Gets used after every meeting that produces a transcript. That's roughly 4-5 times per week. The P0/P1 items go into the task tracker immediately. The P3 items sit in the output file and occasionally turn out to have been important after all.

The "Unanswered Questions" section is unexpectedly valuable. It catches the things that fell through the cracks during the meeting. Questions that were asked, acknowledged, and never actually answered. In a 12-person call, this happens more often than anyone wants to admit.

Accuracy on explicit commitments is close to 100%. Implicit task detection is around 80%. The 20% it misses tends to be very subtle implications that arguably weren't tasks at all.

## Extension Points

- **Custom priority rules**: Adjust the P0-P3 classification criteria for your team's urgency scale
- **Output format**: The markdown structure can be adapted to match your task tracker's import format
- **Participant mapping**: Pre-define participant names and roles so the skill doesn't have to guess from context
- **Multi-file processing**: Feed it an entire week of transcripts. The parallel agents handle the volume
