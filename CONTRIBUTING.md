# Contributing

Thanks for your interest in Miracle Infrastructure!

## Reporting Issues

Open a [GitHub issue](https://github.com/vasilievyakov/miracle-infrastructure/issues) with:
- What you expected vs. what happened
- Which skill/pack is affected
- Your OS (macOS / Linux)

## Contributing Skills

1. Fork the repo and create a branch
2. Add your skill under `skills/<skill-name>/SKILL.md`
3. Follow the existing format:
   - YAML frontmatter with `name` and `description`
   - Description starts with "Use when:" and lists triggers
   - English language throughout
   - No hardcoded personal paths (use `~/.claude/` or `$HOME/.claude/`)
4. If your skill has supporting files, place them in the same directory
5. Add the skill to the appropriate pack in `packs/<pack>/README.md`
6. Update `CHANGELOG.md`
7. Open a pull request

## Code Style

- **Language:** English for all code, docs, and skill content
- **Skill format:** See any existing `SKILL.md` for reference
- **Paths:** Use `$HOME` or `~` — never hardcode user-specific paths
- **Dependencies:** Zero external dependencies. Skills rely only on Claude Code built-in tools
- **Testing:** Run `bash install.sh` and verify your skill copies correctly

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.
