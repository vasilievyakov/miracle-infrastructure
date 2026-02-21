# learned-lessons

A knowledge base that grows from solved problems. Search the web once, remember forever.

## Why

You solve a tricky CORS issue on Tuesday. Six months later, the same CORS issue shows up in a different project. You search the web again, read the same Stack Overflow thread again, and spend 30 minutes re-discovering a solution you already found. This skill records solutions as they happen and checks the knowledge base before searching the web. The agent stops googling the same error twice.

## How It Works

The skill operates in two directions: recording and retrieval.

```
RECORDING (after solving a problem):

Web search finds solution -> Problem solved ->
  "Record this lesson?" -> yes ->
    Entry added to ~/.claude/knowledge-base.md

RETRIEVAL (during debugging):

Bug encountered -> Check knowledge-base.md first ->
  Match found? -> Show solution, skip web search
  No match?    -> Continue normal debugging
```

Each entry stores the problem, symptoms, solution, and tags:

```markdown
## [2026-02-15] requests blocks asyncio event loop

**Problem**: HTTP calls with requests library hang inside async code

**Symptoms**: Program freezes on requests.get(), no error, no timeout

**Solution**: Use aiohttp for async HTTP, or wrap with
asyncio.run_in_executor(None, requests.get, url)

**Tags**: #python #asyncio #requests #networking
```

Entries go at the top of the file (newest first). Tags enable filtered retrieval. The knowledge base persists across sessions in your home directory.

## Quick Install

```bash
# As part of Research pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Research pack

# Just this skill:
mkdir -p ~/.claude/skills/learned-lessons
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/learned-lessons/SKILL.md \
  -o ~/.claude/skills/learned-lessons/SKILL.md
```

## Example

```
You: why does requests hang in asyncio?

Claude: [searches the web]
Claude: Found it! requests blocks the event loop because it uses
        synchronous I/O. Use aiohttp or wrap the call with
        asyncio.run_in_executor.

        Record this lesson to the knowledge base? (yes/no)

You: yes

Claude: Recorded with tags #python #asyncio #requests

--- 3 months later ---

You: my async scraper keeps freezing on HTTP calls

Claude: [checks knowledge base first]
Claude: Found a match in the knowledge base (recorded 2026-02-15):
        "requests blocks asyncio event loop"
        Solution: use aiohttp or run_in_executor.

        No web search needed.
```

Three commands for manual use:
- `/til` to record a lesson on the spot
- `/lessons` to see the last 5 entries
- `/search-lessons <query>` to search by keyword or tag

## Part of

[Research Pack](../../packs/research/README.md) — finding, verifying, and never searching for the same thing twice.
