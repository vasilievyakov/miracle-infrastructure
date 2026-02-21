---
description: Remind to save session context at end of productive sessions
globs: "*"
---

# Save Session Context

If the session was productive (tasks were solved, decisions made, code changed), remind the user to save context:

```
Reminder: you can save this session's context with /session-save
so the next session picks up where you left off.
```

Signs of a productive session:
- Git commits were made
- Files were created or modified
- Architectural decisions were discussed
- Bugs were fixed
- Work lasted more than 10 messages

Do NOT remind if:
- The session was short (quick question-answer)
- The user already ran /session-save
- Work was not tied to a specific project
