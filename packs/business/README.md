# Business Pack

From "we had a call" to "here is the proposal, architecture, and clickable prototype." In one command.

## What it does

You have a transcript from a client call. The skill extracts every pain point, classifies urgency, maps pains to your product features, generates a commercial proposal, creates system architecture, and builds an interactive HTML prototype focused on the client's trigger pain.

## What is included

### Skills (1)

| Skill | Command | What it does |
|-------|---------|-------------|
| **transcript-to-proposal** | `/proposal` | Call transcript to proposal + architecture + HTML prototype |

## How it works

The workflow has checkpoints where you review and confirm before proceeding:

1. **Input**: product description + call transcript
2. **Pain analysis**: extracts all pains, classifies by urgency (trigger/active/latent)
3. **Checkpoint 1**: you confirm the pains and priorities
4. **Solution mapping**: maps pains to product features
5. **Checkpoint 2**: you confirm the architecture
6. **Output generation**: proposal.md + architecture.md + prototype.html

The prototype uses Tailwind CSS, dark theme, responsive layout, and includes realistic data from the transcript (client names, metrics, regions).

## Output files

| File | What it contains |
|------|-----------------|
| `proposal.md` | Commercial proposal using client's own words |
| `architecture.md` | System diagram with Mermaid, component descriptions |
| `prototype.html` | Single-file interactive prototype, no backend needed |
