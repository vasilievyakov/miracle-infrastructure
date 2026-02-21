---
name: project-status
description: |
  Quick project status in 30 seconds: dossier from memory + live data from git/GitHub.
  Use when: (1) "Give me project status", (2) GitHub URL + "status/commits/what's left",
  (3) "When was the last deploy", (4) "What broke", (5) "What's left to do".
  Triggers: "/project-status", "project status", "what's left", "latest commits".
invocation: user
---

# Project Status

Assembles a complete picture from two sources: the memory dossier (what we know) + live data (what is happening now).

---

## Step 1: Identify the project

Extract the project from the user's message. Input types:

| Input | How to identify |
|-------|----------------|
| GitHub URL | Extract repo name from URL |
| Project name | Direct match against memory-config.json keywords |
| Directory path | Last path component |
| Context ("that project with the landing page") | Search dossiers by description |

Load keyword mappings:
```
Read ~/.claude/memory/memory-config.json
```

If the project cannot be identified, ask the user.

---

## Step 2: Load dossier

```
Read ~/.claude/memory/projects/{project-name}.md
```

If dossier not found, warn and work with live data only.

---

## Step 3: Gather live data

Run in parallel (whatever is available for the project):

### 3a. Git (if local repository exists)

```bash
git -C {project_path} log --oneline -10
git -C {project_path} status --short
git -C {project_path} log -1 --format="%cr" # time since last commit
```

### 3b. GitHub (if remote repo exists)

```bash
gh repo view {owner/repo} --json updatedAt,pushedAt --jq '.pushedAt'
gh issue list -R {owner/repo} --limit 5 --json number,title,labels
gh pr list -R {owner/repo} --limit 5 --json number,title,state
```

### 3c. Deploy status (if applicable)

Check last deploy if the dossier mentions a deployment platform.

---

## Step 4: Generate report

Output format, compact and structured:

```markdown
# {Project Name} - Status

## Pulse
- Last commit: {when}
- Last push: {when}
- Uncommitted: {yes/no, N files}

## Recent Changes (git log -10)
{commit list}

## Open Issues
### From dossier (unresolved problems):
- {problem}

### GitHub Issues:
- #{N} {title}

### Pull Requests:
- #{N} {title} ({state})

## Next Steps (from dossier)
1. {task}
2. {task}

## Since Last Session
Last session: {date}
What was done: {from dossier}
```

---

## Rules

### Speed over completeness
- Do NOT clone the repository. If no local copy exists, use GitHub API via `gh`
- Do NOT read project files unless the question requires it
- Dossier + git log + issues = enough for 90% of queries

### Specific questions
The user may ask specifics:
- "when was the last scrape?" - search git log for commits with scrape/parse/crawl
- "what broke?" - search issues with bug label, or git log for fix commits

### Update dossier if new data found
If live data reveals something not in the dossier (new commits, closed issues), suggest updating via `/session-save`.
