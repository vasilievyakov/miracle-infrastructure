# researching-web

Web research that shows its work. Confidence scores, source rankings, contradiction detection, and a progress bar with actual data instead of a spinner.

## Why

Searching the web is easy. Knowing whether the answer is any good is the hard part. Claude Code can pull results from multiple providers, but without structure, you get a wall of text from whoever ranked highest. This skill adds a pipeline: classify the query, search in parallel, score every source, flag contradictions between them, and output a confidence breakdown so you know exactly how much to trust the answer.

## How It Works

Every query goes through the same 7-step pipeline. Simple questions finish faster, not differently.

```
Query
  |
  v
Classify (fact? comparison? how-to? code?)
  |
  v
Search (parallel across available providers)
  |
  v
Score sources (official docs > research > blogs > forums)
  |
  v
Extract facts + detect contradictions
  |
  v
Synthesize (format auto-selected by query type)
  |
  v
Output with confidence breakdown
```

The output format adapts automatically. "X vs Y" queries produce comparison tables. Simple questions get chat answers with sources. Complex topics get full HTML reports. You never have to ask for a format.

Confidence scores break down into four components: source quality (40%), independence (30%), consensus (20%), and freshness (10%). A 40% confidence answer from diverse sources is often more useful than a 90% answer from a single blog post.

## Quick Install

```bash
# As part of Research pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Research pack

# Just this skill:
mkdir -p ~/.claude/skills/researching-web
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/researching-web/SKILL.md \
  -o ~/.claude/skills/researching-web/SKILL.md
```

## Example

```
You: /research what is the current state of Bun vs Deno for production use?

======================================
   RESEARCHING: "Bun vs Deno production readiness 2026"
======================================
[##----] Search: Exa 8 | WebSearch 5 -> 10 unique

[###---] Scoring: bun.sh (85), deno.com (83), benchmarksgame.org (72)...
         Selected: 6 sources above threshold

[####--] Extracting (parallel)...
         + bun.sh/docs
         + deno.com/blog
         + benchmarksgame.org
         + medium.com/production-review
         ...

[#####-] Synthesizing + Verifying...

[######] Confidence: 78%
         |-- Consensus: 4/6 agree on key claims
         |-- Top source: 85 (official docs tier)
         |-- Freshness: 5/6 from current year
         |-- Contradictions: 1 (benchmark numbers differ)
======================================

CONTRADICTION DETECTED:
   Source: bun.sh: "3x faster HTTP throughput than Node"
   Source: benchmarksgame.org: "1.4x faster in comparable tests"
   -> Likely cause: different benchmark methodology

[Comparison table with features, maturity, ecosystem, performance...]
```

## Part of

[Research Pack](../../packs/research/README.md) — finding, verifying, and never searching for the same thing twice.
