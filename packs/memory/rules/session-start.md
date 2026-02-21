---
description: On project start, load project dossier from memory
globs: "*"
---

# Load Project Context

When starting work on any project (user mentions a project name, opens a GitHub URL, or specifies a project path):

1. Identify the project using the keyword mapping from `memory-config.json`:

```
Read ~/.claude/memory/memory-config.json
```

Match user input against the `keywords` array for each project in the config.

2. Read the project dossier:
```
Read ~/.claude/memory/projects/{project-name}.md
```

3. Use dossier information:
   - Do not clone the repo if you already know the architecture
   - Do not ask questions that are answered in the dossier
   - Start with unresolved problems and next steps

4. Tell the user that context is loaded:
```
Loaded {project} dossier. Last session: {date}.
Open problems: {list}.
```
