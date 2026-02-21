# search-memory

Query everything your Claude sessions have ever recorded. By type, project, file, date, or just vibes.

## Why

After a few weeks of using the memory system, you accumulate dozens of observations across multiple projects. Finding "that rate limiting issue we hit in March" by manually reading observation files is not realistic. `/search-memory` gives you structured queries with filters, so you get the exact entries you need without loading everything into context. It reads the lightweight index first and only pulls full details for matches, which keeps token costs predictable even with hundreds of observations.

## How It Works

The search uses progressive disclosure across a two-tier structure:

```
Observation files
├── Index table (~40 tokens per row, always scanned)
└── Details section (~150 tokens per row, loaded only for hits)
```

With 100 observations, a filtered search costs around 4,000 tokens instead of 15,000. The savings compound as your observation history grows.

**Filter syntax:**

| Filter | Example | What it searches |
|--------|---------|------------------|
| Free text | `caching` | Summary and details across all observations |
| `type:` | `type:decision` | decision, bugfix, feature, discovery, problem |
| `project:` | `project:my-app` | Scopes to one project |
| `file:` | `file:auth.ts` | Affected files column |
| `date:` | `date:2026-02` | Year-month or year-month-day |
| `status:` | `status:open` | Open problems (no resolution marker) |

Filters combine freely. Results come back sorted newest-first, capped at 20 entries.

## Install

> **Pack-only.** This skill searches observation files that the memory system creates. Without initialized memory, there is nothing to search. Install the full [Memory Pack](../../packs/memory/), not this skill alone.

```bash
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Memory pack
```

After installation, run `/memory-init` to create the directory structure and register your projects.

## Example

You vaguely remember making a decision about caching strategy a few weeks ago, but not which project it was in or what you decided:

```
You: /search-memory type:decision caching

Claude:
## Search results: "type:decision caching"
Found: 2 observations in 2 projects

### ev-radar (1 match)
| # | Date | Type | Summary |
|---|------|------|---------|
| 7 | 2026-01-15 | decision | Redis caching for API responses |

**[7] Details:**
Before: Every request hit the external API directly, 800ms avg
After: Redis cache with 5min TTL, 120ms avg for cached hits
Files: api/cache.py, config/redis.yml
Why: Rate limiting issues forced us to reduce API calls by 80%

### my-app (1 match)
| # | Date | Type | Summary |
|---|------|------|---------|
| 4 | 2026-01-08 | decision | Client-side caching with SWR |

**[4] Details:**
Before: Full page reload on every navigation
After: SWR with stale-while-revalidate, instant navigations
Files: hooks/useData.ts
Why: Server-side caching overkill for read-heavy dashboard
```

Other useful queries:

- `/search-memory type:problem status:open` to see all unresolved issues across every project
- `/search-memory file:dashboard` to find every observation that touched dashboard files
- `/search-memory project:my-app type:decision` for the full decision history of one project

## Part of

[Memory Pack](../../packs/memory/README.md) — A file-based memory system that makes Claude Code remember your projects across sessions.
