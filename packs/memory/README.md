# Memory Pack

Your agent remembers what happened yesterday. And last week. And that bug you fixed three months ago.

## What it does

Claude Code forgets everything between sessions. You explain your project architecture on Monday, and by Tuesday it asks what framework you use. Again.

The memory pack fixes this with a file-based memory system that loads automatically, captures events as they happen, and saves context when you are done.

```
Session Start ──> Work ──> Session End
      │              │           │
      v              v           v
  Load dossier   Capture     Save context
  from memory    events      with /session-save
                 (typed)
```

## What is included

### Skills (5)

| Skill | Command | What it does |
|-------|---------|-------------|
| **session-save** | `/session-save` | Saves session context to project memory |
| **search-memory** | `/search-memory` | Queries observations with progressive disclosure |
| **memory-health** | `/memory-health` | Validates memory system integrity |
| **memory-init** | `/memory-init` | First-run setup wizard |
| **project-status** | `/project-status` | Quick status from dossier + git |

### Rules (3)

| Rule | Trigger | What it does |
|------|---------|-------------|
| **session-start** | Every session | Loads project dossier automatically |
| **session-end** | End of session | Reminds to save context |
| **auto-observe** | During work | Captures significant events as typed observations |

### Templates

| File | Purpose |
|------|---------|
| `MEMORY.md` | Empty memory index |
| `memory-config.json` | Project keyword mapping |
| `example-project.md` | Sample project dossier |
| `example-project.observations.md` | Sample observations file |

### Tests

`test_memory_integrity.py` validates consistency across all memory files. Run with `/memory-health` or directly:

```bash
python3 ~/.claude/memory/tests/test_memory_integrity.py
```

## How it works

### Memory hierarchy (progressive disclosure)

```
MEMORY.md (always loaded, ~200 tokens)
    |
    +-- project.md (on project mention, ~800 tokens)
    |
    +-- project.observations.md
        +-- Index (~40 tokens/row)
        +-- Details (~150 tokens/row, loaded only for matches)
```

The key insight: load the minimum needed. MEMORY.md is always in context. Dossiers load only when a project is mentioned. Observation details load only for search matches.

With 100 observations across 10 projects, a search costs ~4,000 tokens instead of ~15,000.

### Observation types

| Type | When | Example |
|------|------|---------|
| `decision` | Architectural/tech/business choice | "Chose JWT over sessions" |
| `bugfix` | Bug found and fixed | "Race condition in token refresh" |
| `feature` | New functionality added | "Added /api/status endpoint" |
| `discovery` | Unexpected fact learned | "API limits 100 req/min" |
| `problem` | Issue found, not yet resolved | "Memory leaks above 1k records" |

Custom types can be added in `memory-config.json`.

### Config-driven project detection

Instead of hardcoded keyword mappings, projects are defined in `memory-config.json`:

```json
{
  "projects": {
    "my-app": {
      "keywords": ["my-app", "dashboard"],
      "github": "user/my-app",
      "path": "~/projects/my-app"
    }
  },
  "fallback_project": "general"
}
```

The `session-start` rule reads this config to match user input to project dossiers.

## Quick start

1. Run `/memory-init` to create the directory structure
2. Add your projects to `~/.claude/memory/memory-config.json`
3. Work normally. At end of session, run `/session-save`
4. Next session, context loads automatically

## Extension points

- **Add observation types**: Edit the `observation_types` array in `memory-config.json`
- **Custom dossier sections**: Add any `## Section` to a dossier file. The system preserves unknown sections during updates
- **Project auto-detection**: The `path` field in config enables matching by working directory, not just keywords
