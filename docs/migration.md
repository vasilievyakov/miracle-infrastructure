# Migration Guide

## From version 0.x to 1.0

Version 1.0 is the first public release. If you are upgrading from a personal setup:

### Memory path change

Old path: `~/.claude/projects/-Users-{username}/memory/`
New path: `~/.claude/memory/`

To migrate:
```bash
cp -r ~/.claude/projects/-Users-*/memory/* ~/.claude/memory/
```

### Hardcoded mappings to config

Old: keyword mappings hardcoded in `session-start.md`
New: keyword mappings in `~/.claude/memory/memory-config.json`

Create `memory-config.json` from the template and add your projects:

```json
{
  "memory_path": "~/.claude/memory",
  "projects": {
    "project-name": {
      "keywords": ["keyword1", "keyword2"],
      "github": "user/repo"
    }
  },
  "fallback_project": "general"
}
```

### Dossier section headers

Old: Russian headers (`## Статус`, `## Описание`, etc.)
New: English headers (`## Status`, `## Description`, etc.)

The integrity tests validate English headers. Update your dossiers:

| Old | New |
|-----|-----|
| `## Статус` | `## Status` |
| `## Описание` | `## Description` |
| `## Текущее состояние` | `## Current State` |
| `## Нерешённые проблемы` | `## Unresolved Problems` |
| `## Принятые решения` | `## Decisions Made` |
| `## Следующие шаги` | `## Next Steps` |
| `## История сессий` | `## Session History` |

### Observation format

The observation format is unchanged. No migration needed for observation files.

## Future versions

Re-run `bash install.sh` to upgrade. The installer backs up existing files before overwriting. Your memory data (dossiers, observations) is never overwritten.

If `memory-config.json` already exists, the installer keeps your version. New config fields added in future versions will use sensible defaults.
