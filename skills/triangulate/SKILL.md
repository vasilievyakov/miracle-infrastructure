---
name: triangulate
description: |
  Verifies information through multiple independent sources with transparent confidence scoring.
  Classifies claim type (fact/opinion/prediction), shows where confidence comes from, flags bias.
  Use when: (1) "Verify this", (2) "Triangulate", (3) "Confirm from different sources".
  Triggers: "/triangulate", "verify this", "triangulate", "confirm from multiple sources".
---

# Triangulate

Verification of claims through 3+ independent sources. Transparency: show sources, weights, where confidence comes from.

## Workflow

1. **Classify** the claim type
2. **Search in parallel** using available web search tools
3. **Score sources** (type, weight, independence, date, bias)
4. **Calculate confidence**
5. **Format response** according to claim type

---

## Claim Classification

| Type | Indicators | Verification goal |
|------|-----------|-------------------|
| **FACT** | Dates, numbers, events, tech specs | True or false |
| **OPINION** | "Better", "worse", evaluations, comparisons | Map of positions |
| **PREDICTION** | "Will be", "will become", about the future | How well-founded |
| **MIXED** | Contains multiple types | Decompose |

---

## Strategies by Type

### FACT

**Search:** official sources, documentation, peer-reviewed, primary data.

**Verdicts:**
- CONFIRMED: fact is true
- REFUTED: fact is false
- PARTIAL: partly true
- INCONCLUSIVE: insufficient data

---

### OPINION

**Search:** different viewpoints, arguments from each side, who agrees/disagrees.

**Verdicts:**
- CONSENSUS: most agree
- MAJORITY X: most support X, opponents exist
- DIVIDED: opinions roughly equal
- MARGINAL: this is a minority opinion

**Output:** opinion map (FOR / AGAINST / NEUTRAL) with percentages and arguments.

---

### PREDICTION

**Search:** author's track record, methodology, expert consensus, alternative scenarios.

**Verdicts:**
- WELL-FOUNDED: methodology and track record exist
- PARTIALLY FOUNDED: arguments and counterarguments both present
- SPECULATIVE: weak methodology
- CONTRADICTS CONSENSUS: experts think otherwise

**Output:** assessment of author, methodology, assumptions.

---

### MIXED

1. Split into parts by type
2. Verify each part with its own strategy
3. Synthesize overall conclusion

---

## Source Hierarchy

| Weight | Source types |
|--------|------------|
| **High** | Official docs, peer-reviewed, government sources, primary data |
| **Medium** | Tech publications, experts, educational resources, Wikipedia with sources |
| **Low** | Blogs, forums, social media, anonymous |

---

## Confidence Score

```
Confidence = Quality (40%) + Independence (30%) + Consensus (20%) + Freshness (10%)
```

Show the user what the score is composed of.

---

## Warnings

Flag when detected:

| Signal | When |
|--------|------|
| **BIAS** | All sources lean one way |
| **ECHO** | Sources cite each other (false triangulation) |
| **OUTDATED** | Information may have changed |
| **INSUFFICIENT** | Too few sources for triangulation |

---

## Principles

- Search for refutations, not only confirmations
- Verify source independence
- Official documentation > blogs
- Acknowledge uncertainty honestly
- Note publication dates
