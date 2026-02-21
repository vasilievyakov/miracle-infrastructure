# project-status

Get the full picture of any project in 30 seconds. No cloning, no exploring, no re-reading the codebase.

## Why

You have 10 projects. You worked on this one two weeks ago. What was the last thing you did? Are there open issues? Any uncommitted changes sitting on the laptop? Finding all of this manually means opening the repo, checking git log, checking GitHub, and trying to recall what you were thinking at the time. `/project-status` pulls from two sources at once: your memory dossier (the "what we know" layer) and live data from git and GitHub (the "what is happening now" layer). The result is a single status report you can read in 10 seconds.

## How It Works

The skill accepts a project name, GitHub URL, directory path, or even a vague description like "that project with the landing page." It matches your input against the keyword mappings in `memory-config.json`.

Then it gathers data from two sources in parallel:

```
Memory dossier                    Live data
├── Last session date             ├── git log (last 10 commits)
├── What was done                 ├── git status (uncommitted files)
├── Unresolved problems           ├── Time since last commit
├── Decisions made                ├── GitHub issues (last 5)
├── Next steps                    ├── GitHub PRs (last 5)
└── Session history               └── Last push date
```

These get merged into a compact report. The dossier provides context (why things were done, what is planned). Live data provides facts (what actually happened since you last looked).

**Speed is the design constraint.** The skill never clones a repository. If there is no local copy, it uses the GitHub API via `gh`. It never reads project files unless the question specifically requires it. Dossier + git log + issues covers 90% of status questions.

## Install

> **Pack-only.** This skill reads project dossiers and `memory-config.json` for keyword matching. Without the memory system, it can only show raw git/GitHub data, losing most of its value. Install the full [Memory Pack](../../packs/memory/), not this skill alone.

```bash
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Memory pack
```

After installation, run `/memory-init` to create the directory structure and register your projects.

## Example

You want to check in on a project you have not touched in a week:

```
You: /project-status ev-radar

Claude:
# EV Radar - Status

## Pulse
- Last commit: 6 days ago (Feb 15)
- Last push: 6 days ago
- Uncommitted: yes, 2 files (src/scraper.py, config.yml)

## Recent Changes
a3f1b2c Add retry logic for rate-limited requests
8d4e9f1 Fix Instagram actor timeout handling
2c7a3d0 Bump API client to v2.3
f1e6b8a Add caching layer for search results
9a2c4e7 Refactor data pipeline

## Open Issues
### From dossier (unresolved problems):
- Instagram actor blocked for rate limiting
- Memory usage spikes above 1k records

### GitHub Issues:
- #12 Add support for TikTok listings
- #9  Export to CSV broken for large datasets

### Pull Requests:
- #14 feat: add websocket notifications (open)

## Next Steps (from dossier)
1. Resolve Instagram rate limiting with proxy rotation
2. Profile memory usage in data pipeline
3. Implement websocket handler for real-time updates

## Since Last Session
Last session: 2026-02-15
What was done: Fixed race condition in token refresh, added retry logic for API calls
```

You can also ask specific follow-up questions like "when was the last scrape?" or "what broke recently?" and the skill searches git history for relevant commits.

## Part of

[Memory Pack](../../packs/memory/README.md) — A file-based memory system that makes Claude Code remember your projects across sessions.
