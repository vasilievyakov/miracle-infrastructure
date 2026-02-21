# Token Budget

How the memory system manages token costs through progressive disclosure.

## The problem

A naive memory system loads everything into context every session. With 10 projects and 100 observations, that is ~15,000 tokens per session just for memory. Your actual work competes with memory for context window space.

## The solution: progressive disclosure

Load the minimum needed. Expand on demand.

### Cost per component

| Component | When loaded | Tokens |
|-----------|-----------|--------|
| MEMORY.md | Every session | ~200 |
| memory-config.json | Every session | ~100 |
| project.md (dossier) | On project mention | ~800 |
| observations Index (per row) | On search | ~40 |
| observations Details (per row) | On match only | ~150 |

### Scenario analysis

**Daily session, 1 project, no search:**
- MEMORY.md: 200
- Config: 100
- Dossier: 800
- **Total: ~1,100 tokens**

**Search across all projects (10 projects, 100 observations, 5 matches):**
- MEMORY.md: 200
- Config: 100
- 100 Index rows: 4,000
- 5 Detail blocks: 750
- **Total: ~5,050 tokens**

**Same search without progressive disclosure:**
- Everything: 15,000+ tokens
- **Savings: 3x**

### Keeping costs low

- MEMORY.md: capped at 200 lines
- Dossiers: capped at 200 lines
- Observation summaries: capped at 50 characters
- Details: loaded only for search matches
- Session history: capped at 10 entries per dossier

### When to clean up

Run `/memory-health` to check sizes. The skill warns when:
- MEMORY.md exceeds 40 lines
- Any observations file exceeds 20 entries
- Duplicate observations detected
