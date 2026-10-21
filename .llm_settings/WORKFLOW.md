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
| Development | `/i-unit-tdd` (was `/i-tdd`), `/i-apollo`, `/i-atlas`, `/i-hdev`, `/i-odev` |
| Testing | `/i-test-architect`, `/i-integration-qa`, `/i-system-nfr`, `/i-bdd`, `/i-code-reviewer` (see Testing Agent Workflow) |
| Security | `/i-sec`, `/i-sec-defense`, `i-security-reviewer` (subagent) |
| Build | `/i-ci`, `/i-cd`, `/i-cicd` |
| Deploy | `/i-production`, `/i-gitops` |
| Operate | `/i-sre`, `/i-aws`, `/i-observability` |
| Improve | `/i-kaizen`, `/i-eightd`, `/i-socrates` |

## Testing Agent Workflow

| Stage | Agent(s) (skill `/i-…` and subagent of the same name) | Gate script |
|---|---|---|
| Plan | `i-test-architect` | — |
| Implement | `i-unit-tdd` | `scripts/testing/run-unit.sh` |
| Pre-commit | `i-code-reviewer` + `i-security-scanner` | `impact-map.sh`, `sec-scan.sh` |
| PR / CI | `i-integration-qa` | `run-integration.sh`, `smoke.sh` |
| Pre-release | `i-system-nfr` | — (staging runs) |
| Release / post-deploy | `i-release-gate` | `release-check.sh`, `sbom-verify.sh`, `smoke.sh` |
| SQL, pipeline, prompt, agent or OT/telemetry paths (any stage) | `i-data-ai-ot` | `sql-fixtures.sh`, `eval-run.sh`, `telemetry-check.sh` |

Canonical source: `agents-src/i-<name>/`; `scripts/render-agents.sh` renders it into `.llm_settings/agents/` and
`.llm_settings/skills/` (never hand-edit generated files); `llm-init` deploys them to every tool. Gate scripts honour
`I_GATE=report|block` (default `report`: findings are printed, nothing is blocked). `i-code-reviewer` impact analysis is
mandatory on every change; the push hook (`require_impact_analysis.sh`) checks for its section. Deprecated aliases:
`i-tdd`→`i-unit-tdd`, `i-cr`→`i-code-reviewer`, `i-qa`→`i-integration-qa`+`i-system-nfr`, `i-prod-safety`→`i-release-gate`
(`i-gg` GIT-GUARD is unchanged). Full mapping: `docs/testing/TAXONOMY.md`.

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
