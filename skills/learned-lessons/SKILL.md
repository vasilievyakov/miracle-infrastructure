---
name: learned-lessons
description: |
  Accumulates knowledge from solved problems. Activates automatically after web search or MCP tools
  are used to solve technical problems. Also activates during debugging to check the knowledge base first.
  Invoke explicitly via "/til" to record a lesson manually.
  Triggers: "/til", "record a lesson", "what lessons do we have".
---

# Learned Lessons: Knowledge Base

## Purpose

This skill accumulates knowledge from solved problems so you never search for the same thing twice.

## When it activates

1. **After web search for problem solving**: offer to record the lesson
2. **After using MCP tools**: if a technical problem was solved
3. **During debugging**: check the knowledge base first
4. **Explicit invocation**: user says "/til" or "record a lesson"

## Workflow after search/MCP

After successfully using web search or MCP tools to solve a technical problem:

1. Ask the user briefly:
   ```
   Record this lesson to the knowledge base? (yes/no)
   ```

2. If yes, add an entry to the knowledge base file (default: `~/.claude/projects/-Users-vasiliev/memory/knowledge-base.md`):
   ```markdown
   ## [YYYY-MM-DD] Brief title

   **Problem**: What was not working

   **Symptoms**: How it manifested (errors, behavior)

   **Solution**: What helped

   **Tags**: #python #asyncio #networking
   ```

3. Add entries at the TOP of the file (newest lessons first)

## Workflow during debugging

When systematic-debugging activates or during explicit debugging:

1. Read `~/.claude/projects/-Users-vasiliev/memory/knowledge-base.md` first
2. Search for similar problems by keywords and tags
3. If relevant match found, show the user
4. If nothing found, continue normal debugging

## Entry Format

Each entry contains:

| Field | Description |
|-------|-------------|
| Date | When it was learned |
| Title | Gist in 5-7 words |
| Problem | What you were trying to do |
| Symptoms | Errors, traceback, behavior |
| Solution | Specific steps or code |
| Tags | For search (#python, #docker, #api) |

## Commands

- `/til`: record a lesson manually (asks for details)
- `/lessons`: show last 5 lessons
- `/search-lessons <query>`: search the knowledge base

## Important

- Do NOT record trivial things (typos, forgotten imports)
- Record what was NON-OBVIOUS and required research
- Record SPECIFIC solutions, not general advice
- Tags help search. Use technologies and concepts

## Example

```
User: why does requests hang in asyncio?

Claude: [uses web search]
Claude: Found it! requests blocks the event loop. Use
        aiohttp or run_in_executor instead.

        Record this lesson to the knowledge base? (yes/no)

User: yes

Claude: Recorded with tags #python #asyncio #requests
```

## Knowledge Base

The file `~/.claude/projects/-Users-vasiliev/memory/knowledge-base.md` contains all accumulated lessons.
Read this file during debugging to check for known solutions.
Create it on first use if it does not exist.
