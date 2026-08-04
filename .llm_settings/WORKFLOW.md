# AI Engineering Workflow

This repository implements a full lifecycle AI-augmented development system.

## Lifecycle

1. Product Discovery
2. Architecture Design
3. Development
4. Testing
5. Security
6. Continuous Integration/Continuous Delivery (CI/CD)
7. Deployment
8. Operations
9. Continuous Improvement

## Core Flow

| Stage | Skills |
|-------|--------|
| Idea | `/i-pm`, `/i-agile`, `/i-scrum` |
| Design | `/i-sad`, `/i-architecture-review` |
| Development | `/i-tdd`, `/i-apollo`, `/i-atlas` |
| Testing | `/i-qa`, `/i-bdd`, `/i-cr` |
| Security | `/i-sec`, `/i-sec-defense`, `i-security-reviewer` (subagent) |
| Build | `/i-ci`, `/i-cd`, `/i-cicd` |
| Deploy | `/i-production`, `/i-gitops` |
| Operate | `/i-sre`, `/i-aws`, `/i-observability` |
| Improve | `/i-kaizen`, `/i-eightd`, `/i-socrates` |

## Agent Layer

- **Skills** (`/i-*`) — User-invocable slash commands in Claude Code; converted to `@i-*` agents for Gemini and Codex
- **Subagents** (`.llm_settings/agents/`) — Claude subagents referenced by skills for specialized tasks (e.g. `i-security-reviewer`)
- **Orchestration** — Skills chain together via `.claude/ORCHESTRATOR.md`

## Multi-Agent Roles

| Role | Tool | Responsibilities |
|------|------|-----------------|
| PRIMARY | Claude Code | Architecture, features, refactoring, Pull Requests (PRs) |
| SECONDARY | Gemini Command-Line Interface (CLI) | Document analysis, cross-referencing, research |
| TERTIARY | Codex CLI | Test augmentation, validation runs, safe refactors |
