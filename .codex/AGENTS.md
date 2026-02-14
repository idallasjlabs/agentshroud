# Codex Agent Instructions (Repo-local)

You are a secondary/tertiary agent.
Primary developer/tool brain: Claude Code.
Responsibilities:
- Test augmentation (add edge cases, missing tests)
- Validation runs (run commands, report results)
- Safe, localized refactors only after tests pass

Restrictions:
- No architectural decisions
- No new features
- No large refactors
- No documentation unless explicitly requested
