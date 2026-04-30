# Sprint Cadence Decision

**Decision date:** 2026-04-14
**Decision owner:** Isaiah Dallas Jefferson, Jr.
**Status:** Active

## Decision

AgentShroud uses **GSD (Get Shit Done) cadence** — not formal sprint methodology.

Formal sprints (Scrum, SAFe) are optimized for teams of 5–15 humans coordinating
across functions. AgentShroud is a solo developer plus AI agents. Sprint ceremonies
(planning, standup, review, retro) add overhead without proportional value at this
scale.

## What We Do Instead

| Practice | Mechanism | Schedule |
|----------|-----------|----------|
| Weekly retrospective | Weekly Kaizen cron job | Friday 5:00 PM ET |
| Resilience testing | Monthly Chaos Drill cron job | 1st of month 9:00 AM ET |
| Production gating | GSD issues with `approved:isaiah` label | Per production-impacting change |
| Backlog | GitHub Issues with milestone labels | Continuous |
| Prioritization | Isaiah decides, Claude Code executes | As needed |

## GSD Issue Requirements

A GSD issue is required before branching for changes to:
- `gateway/security/**`
- `docker/`, `docker-compose.yml`
- `docker/setup-secrets.sh`
- `docker/config/openclaw/apply-patches.js`
- `.claude/settings.json`
- `.claude/scripts/claude-hooks/`

A GSD issue is NOT required for:
- Pure test additions
- Documentation
- MEMORY.md updates
- Dependency bumps (Dependabot)

## When to Revisit

Revisit this decision when:
- A second full-time engineer joins the project
- External contributors submit more than 3 PRs/week
- A project manager role is introduced

## Skills Available (if needed)

If sprint methodology is ever adopted:
- `/scrum` — Scrum facilitation
- `/agile` — Agile coaching
- `/pm` — Project management
- `/kanban` — Kanban workflow
