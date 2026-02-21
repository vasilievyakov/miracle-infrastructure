# Business Pack

From "we had a call" to "here's the proposal, architecture, and clickable prototype." One command.

<p align="center">
  <img src="../../docs/gifs/proposal.svg" alt="proposal demo" width="640" />
</p>

## The Idea

You have a 47-minute recording of a client call. Somewhere in those 47 minutes are pain points, priorities, feature requests, and half-promises. You could re-listen, take notes, and spend a few hours assembling deliverables. Or you could feed the transcript to `/proposal` and get a commercial proposal, system architecture, and interactive HTML prototype in about 20 minutes. The prototype uses the client's own data. Their names, their metrics, their regions.

A clickable prototype with the client's actual data leaves an unforgettable impression. Clients expect a document. They get a working thing with their numbers in it. That changes the conversation from "what would this look like" to "when can we start."

### Field Notes (dozens of real client engagements)

The key insight from extended use: we often look through our own focus and miss what the client is really trying to say. LLMs understand language patterns well enough to catch what you missed. A client says "it would be nice if..." three separate times about the same feature while you're busy thinking about the architecture. The skill catches that repetition and surfaces it as a trigger pain. You might have filed it under "nice to have."

If you understand your client, you know what to sell. This creates mutual value, not just a closed deal. The skill is built around that principle: listen first, classify accurately, propose honestly.

## What's Inside

### Skills (1)

| Skill | Command | What it does |
|-------|---------|--------------|
| [**transcript-to-proposal**](../../skills/transcript-to-proposal/) | `/proposal` | Call transcript to proposal + architecture + interactive HTML prototype |

## How It Works

The workflow has checkpoints. You review and confirm before the skill proceeds. No fully autonomous 47-minute-transcript-to-deliverables pipeline. You stay in control of the narrative.

```
INPUT
  │
  ├── Product description (what you sell)
  └── Call transcript (what the client said)
       │
       ▼
PAIN ANALYSIS
  Extract all pains → classify by urgency
  ┌─────────────────────────────────────┐
  │ Trigger: "we're losing clients NOW" │
  │ Active:  "this is annoying daily"   │
  │ Latent:  "haven't thought about it" │
  └─────────────────────────────────────┘
       │
       ▼
CHECKPOINT 1 ← You confirm pains and priorities
       │
       ▼
SOLUTION MAPPING
  Map each pain to your product features
  Design system architecture
       │
       ▼
CHECKPOINT 2 ← You confirm the architecture
       │
       ▼
OUTPUT GENERATION
  proposal.md + architecture.md + prototype.html
```

The checkpoints exist because pain classification is subjective. What sounds like a trigger pain to the AI might be a latent concern the client mentioned once in passing. You know the client. The skill doesn't. This is a deliberate design choice, not a limitation.

### Output Files

| File | What's inside | Key details |
|------|---------------|-------------|
| `proposal.md` | Commercial proposal | Uses the client's own words and phrasing. Addresses pains in their language |
| `architecture.md` | System architecture | Mermaid diagrams, component descriptions, integration points |
| `prototype.html` | Interactive prototype | Single HTML file, no backend, no build step, just open in browser |

### The Prototype

The prototype deserves its own section because it's not a wireframe. It's a functional, styled, interactive HTML page:

- **Tailwind CSS** for styling (loaded via CDN, no build tools)
- **Dark theme** as default
- **Responsive layout** (works on mobile)
- **Realistic data** pulled from the transcript (client names, actual metrics, real regions)
- **Single file** delivery. One HTML file. No dependencies. Email it to the client, they double-click it, it works

The prototype focuses on the trigger pain. Whatever hurts most gets the best-looking demo.

## Quick Start

1. Install the pack
2. Prepare two things: a description of your product, and a call transcript (any format)
3. Run `/proposal`
4. Review pains at Checkpoint 1. Adjust if needed
5. Review architecture at Checkpoint 2. Adjust if needed
6. Receive three files in your project directory

## Real Usage

Used dozens of times on real clients over 6 months.

The typical flow: 47-minute client call recorded on Monday. Transcript uploaded Tuesday morning. `/proposal` run at 10am. By 10:20, three deliverables ready for review. Some light editing of the proposal language (the AI tends to be more formal than necessary). Prototype sent to client by noon.

The prototype consistently gets the strongest reaction. Not the proposal document, not the architecture diagram. The clickable thing with their data in it. Every time.

Pain classification accuracy sits around 85%. The remaining 15% is caught at Checkpoint 1. This is exactly why the checkpoints exist. Pain classification is subjective, and "subjective" means the person who was on the call should have final say, not the algorithm.

The language pattern detection has become the quiet superpower of this skill. Clients repeat themselves when something matters. They circle back to the same topic from different angles. The skill picks up on these patterns better than a human taking notes in real-time, because the human is busy formulating responses while the client is still talking.

## Extension Points

- **Custom pain categories**: The trigger/active/latent classification can be extended with domain-specific urgency levels
- **Proposal templates**: Replace the default markdown structure with your company's proposal format
- **Prototype themes**: The Tailwind config in the prototype can be customized. Light theme, brand colors, whatever the client expects
- **Multi-language**: The proposal generates in the same language as the transcript. Feed it Russian, get Russian back
