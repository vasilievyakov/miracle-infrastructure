# Research Pack

Your agent checks its homework. Three tools for finding, verifying, and remembering information.

## What it does

Claude Code can search the web. These skills add structure to that capability: confidence scores, source hierarchies, contradiction detection, and a persistent knowledge base so solved problems stay solved.

## What is included

### Skills (3)

| Skill | Command | What it does |
|-------|---------|-------------|
| **researching-web** | `/research` | Web research with parallel search, source scoring, confidence breakdown |
| **triangulate** | `/triangulate` | Claim verification through 3+ independent sources |
| **learned-lessons** | `/til` | Knowledge base that accumulates solutions to solved problems |

## Researching Web

A structured research pipeline:

```
Query -> Classify -> Search (parallel) -> Score -> Extract -> Synthesize -> Verify -> Output
```

Every research output includes:
- Confidence score with component breakdown
- Source quality ratings
- Contradiction detection between sources
- Research depth stats (pages analyzed, facts extracted)

Auto-selects output format: comparison table for "vs" queries, chat answer for simple questions, full HTML report for complex topics.

## Triangulate

Fact verification with transparency. Classifies the claim type first:

| Type | Goal | Example verdict |
|------|------|----------------|
| Fact | True or false | CONFIRMED / REFUTED / PARTIAL |
| Opinion | Map positions | CONSENSUS / DIVIDED / MARGINAL |
| Prediction | How well-founded | WELL-FOUNDED / SPECULATIVE |

Flags potential issues: bias (all sources lean one way), echo (sources cite each other), outdated information, insufficient sources.

## Learned Lessons

A knowledge base that grows from solved problems:

1. After web search solves a technical problem, offers to record the lesson
2. During debugging, checks the knowledge base first
3. Each lesson has: problem, symptoms, solution, tags

The idea: never search for the same thing twice.

## Prerequisites

These skills work with any web search tools available to Claude Code (Exa, Tabstack, WebSearch, WebFetch, or MCP-provided alternatives). If specific tools are unavailable, the skills degrade gracefully.
