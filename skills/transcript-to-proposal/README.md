# transcript-to-proposal

From "we had a call" to a commercial proposal, system architecture, and clickable prototype. One command, three deliverables.

## Why

You have a 47-minute recording of a client call. Somewhere in those 47 minutes are pain points, priorities, half-promises, and the one feature they mentioned three separate times while you were busy thinking about the architecture. You could re-listen, take notes, and spend a few hours assembling deliverables. Or you could feed the transcript to `/proposal` and get all three outputs in about 20 minutes. The prototype uses the client's own data: their names, their metrics, their regions. Clients expect a document. They get a working thing with their numbers in it.

## How It Works

The skill runs a 4-step pipeline with two human checkpoints. You review and confirm before it proceeds. No fully autonomous transcript-to-deliverables pipeline. You stay in control.

```
INPUT: product description + call transcript
  |
  v
STEP 1: Pain Analysis
  Extract all pains from transcript
  Classify: Trigger (buying now) / Active (searching) / Latent (aware, passive)
  Identify speaker roles and urgency signals
  |
  v
CHECKPOINT 1 <-- You confirm pains and priorities
  |
  v
STEP 2: Solution Mapping
  Map each pain to product features
  Design system architecture (Mermaid diagrams)
  |
  v
CHECKPOINT 2 <-- You confirm architecture
  |
  v
STEP 3: Generate proposal.md
  Uses the client's own words and phrasing
  |
  v
STEP 4: Generate prototype.html
  Single HTML file, Tailwind CSS, dark theme
  Interactive, realistic data from transcript
  No backend, no build step, just open in browser
```

Output: three files in your project directory.

| File | What's inside |
|------|---------------|
| `proposal.md` | Commercial proposal using the client's own language |
| `architecture.md` | System architecture with Mermaid diagrams |
| `prototype.html` | Clickable HTML prototype with real client data |

## Quick Install

```bash
# As part of Business pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Business pack

# Just this skill:
mkdir -p ~/.claude/skills/transcript-to-proposal
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/transcript-to-proposal/SKILL.md \
  -o ~/.claude/skills/transcript-to-proposal/SKILL.md
```

## Example

```
You: /proposal
     [attaches product-description.md and call-transcript.txt]

Claude: Found 6 pains in the transcript:

TRIGGER (main proposal focus):
  - Manual report assembly - "we spend two days every month just pulling numbers"
  - Client churn visibility - "by the time we notice, they're already gone"

Active problems:
  - No regional breakdown in dashboards
  - Integration with their existing CRM

Latent:
  - SSO for the sales team
  - Mobile access

Priorities correct? Anything missed?

You: Looks right, but move CRM integration to trigger, they mentioned it 3 times

Claude: Updated. Building solution map and architecture...

[Shows architecture diagram]
Key decisions:
1. Real-time sync with CRM - because client said "we can't wait for nightly imports"
2. Automated reports - solves the trigger pain of 2-day manual assembly

Architecture clear? Any constraints?

You: Go ahead

Claude: Done! Created three files:
  proposal.md    - commercial proposal
  architecture.md - solution architecture
  prototype.html  - interactive prototype

  Open the prototype in the browser?
```

## Part of

[Business Pack](../../packs/business/README.md) — from client calls to deliverables, with checkpoints for human judgment.
