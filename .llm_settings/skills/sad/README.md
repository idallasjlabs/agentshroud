# System Audit Documentation

**Command:** `/sad` (Claude Code) | paste `.gemini/agents/sad.md` (Gemini/Codex)
**Platforms:** Claude Code (native `/skill`) | Gemini CLI, Codex CLI (paste agent file)

## Purpose
Produces exhaustive technical documentation for any codebase across 13 sections: system overview, file map, environment variables, dependencies, step-by-step setup, startup sequence, every module and function reference, data flow, error catalog, shutdown/recovery, troubleshooting matrix, complete Mermaid flowchart, and a quick-reference card. Assumes the reader has never seen the code before.

## Usage
Invoke `/sad`, then paste your codebase (source files, config files, docker-compose, .env examples, logs, etc.) below the prompt.

## Related Skills
- [[sav]] — Obsidian vault version of the same analysis
- See [SKILLS_GUIDE.md](../reference/SKILLS_GUIDE.md) for the complete skill catalog.
