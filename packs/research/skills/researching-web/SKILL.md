---
name: researching-web
description: |
  Researches questions using web search and generates reports with confidence scores and sources.
  Use when: (1) User asks a question requiring current information, (2) User says "find out about X",
  (3) User gives URL to extract data from, (4) Question about code/API/library, (5) Comparing options.
  Triggers: "/research", "find out about", "research this".
invocation: user
---

# Web Research

Orchestrates multiple search tools for hybrid search, parallel extraction, and structured output.

## Pipeline

```
Query -> Classify -> Search (parallel) -> Score -> Extract (parallel) -> Synthesize -> Verify -> Output
```

**Tools:** Uses available web search and extraction tools (Exa, Tabstack, WebSearch, WebFetch, or similar MCP tools).

## Progress Format

Show progress with real data at each step:

```
======================================
   RESEARCHING: "{query}"
======================================
[##----] Search: Source A 8 | Source B 5 -> 10 unique

[###---] Scoring: domain1.com (82), domain2.com (78), ...
         Selected: 5 sources above threshold

[####--] Extracting (parallel)...
         + domain1.com
         + domain2.com
         ...

[#####-] Synthesizing + Verifying...

[######] Confidence: 85%
         |-- Consensus: 4/5 agree
         |-- Top source: 82 (official docs tier)
         |-- Freshness: 5/5 from current year
         |-- Contradictions: none

RESEARCH DEPTH
   Pages analyzed: 12 | Facts extracted: 47
   Sources: 5 (2 official, 2 research, 1 blog)
   Coverage: High, multiple independent confirmations
======================================
```

---

## Step 1: Classify and Plan

| Type | Signals | Sources | Search Strategy |
|------|---------|---------|-----------------|
| Fact | "what is", "when", "how much" | 1-2 | Single search tool |
| How-to | "how to", tutorial | 2-3 | Single search tool |
| Comparison | "vs", "compare", "best" | 5+ | Hybrid (multiple tools) |
| Overview | "explain", "tell me about" | 3-5 | Hybrid |
| Code/API | library, SDK, docs | 1-2 | Code-specific search |

## Step 2: Search

**Has URL**: skip to extraction.

**No URL**: search with query augmentation (synonyms, English version for tech).

For hybrid: call multiple search tools in a single message for parallel execution.

**Fallback:** If a tool is unavailable, note it and continue with remaining tools.

## Step 3: Score and Select

Trust Claude's judgment. Prefer: official docs > research > GitHub > Stack Overflow > blogs > forums.

Skip: SEO spam, paywalls, content older than 2 years (for tech).

## Step 4: Extract (Parallel)

Call ALL extractions in a single message for parallel processing.

If extraction fails: note the failure and continue with others.

## Step 5: Synthesize

1. Merge facts, deduplicate
2. Note contradictions with source attribution
3. Identify consensus vs disputed points

## Step 6: Verify and Detect Contradictions

Before finalizing, actively look for contradictions between sources. When found, display:

```
CONTRADICTION DETECTED:
   Source A (domain.com): "Claim X"
   Source B (other.com): "Claim Y"
   -> Likely cause: {different timeframes / methodology / scope}
```

Also check:
- Single-source claims: mark as "unverified"
- Non-authoritative sources for topic: adjust confidence

## Step 7: Output (Zero Friction)

**Auto-select format, no questions asked:**
- "vs"/"compare": Comparison Table HTML
- Simple question: Answer in chat + sources
- Complex topic: Full HTML Report

Generate immediately. If the user wants a different format, they will ask.

**Include in every output:**
- Confidence score with breakdown
- Contradictions found (if any)
- Research depth stats

---

## Fallback

Tool fails: inform, continue with remaining. Search empty: simplify query. All weak: suggest refining.
