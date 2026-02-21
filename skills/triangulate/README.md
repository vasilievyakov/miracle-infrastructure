# triangulate

Verify claims through 3+ independent sources. Because "I read it somewhere" is not a citation.

## Why

The internet is full of confident, well-written claims that happen to be wrong. Vendor benchmarks that independent tests can't reproduce. Blog posts that cite each other in a circle. Predictions presented as facts. This skill searches for evidence on both sides of a claim, classifies what kind of claim it is, weights sources by authority, and tells you whether you're looking at genuine consensus or an echo chamber.

## How It Works

The skill classifies the claim first, because verifying a fact and evaluating a prediction are fundamentally different tasks.

```
Claim input
  |
  v
Classify (FACT / OPINION / PREDICTION / MIXED)
  |
  v
Search in parallel (3+ independent sources)
  |
  v
Score each source (type, weight, independence, date, bias)
  |
  v
Calculate confidence
  = Quality (40%) + Independence (30%) + Consensus (20%) + Freshness (10%)
  |
  v
Verdict + warnings
```

Each claim type gets its own verification strategy and verdict set:

| Claim type | Goal | Possible verdicts |
|------------|------|-------------------|
| **Fact** | True or false | CONFIRMED, REFUTED, PARTIAL, INCONCLUSIVE |
| **Opinion** | Map positions | CONSENSUS, DIVIDED, MARGINAL |
| **Prediction** | How well-founded | WELL-FOUNDED, SPECULATIVE |

The skill also flags structural problems with the evidence: bias (all sources lean one direction), echo (sources cite each other), outdated info, or insufficient source count for proper triangulation.

## Quick Install

```bash
# As part of Research pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Research pack

# Just this skill:
mkdir -p ~/.claude/skills/triangulate
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/triangulate/SKILL.md \
  -o ~/.claude/skills/triangulate/SKILL.md
```

## Example

```
You: /triangulate "SQLite can handle 100 concurrent writers without issues"

Claim type: FACT
Searching 3+ independent sources...

Sources found:
  [High]   sqlite.org/faq.html (official docs)
  [High]   sqlite.org/lockingv3.html (official docs)
  [Medium]  fly.io/blog/sqlite-internals (tech publication)
  [Medium]  news.ycombinator.com/discussion (community)
  [Low]    medium.com/sqlite-at-scale (blog)

Verdict: PARTIAL (Confidence: 72%)

Breakdown:
  - SQLite supports concurrent READERS without issue
  - SQLite uses a single-writer lock. One writer at a time
  - WAL mode allows concurrent reads during writes
  - 100 concurrent writers would queue, not run in parallel
  - Performance degrades significantly under write contention

Warnings:
  [ECHO] 2 sources reference the same SQLite FAQ section

Key distinction: the claim conflates "handles" with "handles well."
SQLite won't crash with 100 writers. It will serialize them.
```

## Works great with

- [Researching Web](../researching-web/) — do the initial broad research, then triangulate the specific claims that matter

## Part of

[Research Pack](../../packs/research/README.md) — finding, verifying, and never searching for the same thing twice.
