# System Audit Vault

**Command:** `/sav` (Claude Code) | paste `.gemini/agents/sav.md` (Gemini/Codex)
**Platforms:** Claude Code (native `/skill`) | Gemini CLI, Codex CLI (paste agent file)

## Purpose
Analyzes a codebase and produces a complete Obsidian vault — interconnected markdown notes with wikilinks, tags, YAML frontmatter, and Mermaid diagrams. Generates 30+ notes organized into: Start Here, Architecture, Modules (one per source file), Configuration, Environment Variables (one per var), Dependencies, Containers, Errors & Troubleshooting, Runbooks, and Diagrams.

## Usage
Invoke `/sav`, then paste your codebase (source files, config files, docker-compose, .env examples, logs, etc.) below the prompt.

## Related Skills
- [[sad]] — Linear documentation version (13 sections, no Obsidian structure)
- See [SKILLS_GUIDE.md](../reference/SKILLS_GUIDE.md) for the complete skill catalog.
