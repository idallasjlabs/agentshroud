# AgentShroud Session Brief

> Compressed context for fast agent cold-starts. Regenerate this file at session
> start using `/session-prompt` or by running `scripts/gen-session-brief.sh`.
> Max 60 lines — trim ruthlessly.

## Current State

| Field | Value |
|-------|-------|
| Version | <!-- VERSION --> |
| Branch | <!-- BRANCH --> |
| Last commit | <!-- LAST_COMMIT --> |
| CI status | <!-- CI_STATUS --> |

## Recent Commits (last 5)

<!-- RECENT_COMMITS -->

## Active Work

<!-- ACTIVE_ISSUES -->

## Known Broken / Watch Items

<!-- KNOWN_ISSUES -->

## Today's Priorities

<!-- PRIORITIES -->

## Key Paths (do not ask — just read)

| What | Where |
|------|-------|
| Gateway core | `gateway/` |
| Security modules (76) | `gateway/security/` |
| Proxy layer | `gateway/proxy/` |
| Tests (3,700+) | `gateway/tests/` |
| Docker stack | `docker/docker-compose.yml` |
| Bot config patches | `docker/config/openclaw/apply-patches.js` |
| Agent registry | `.claude/agents/` |
| Skills | `.claude/skills/` |
| Cron jobs | `docker/config/openclaw/cron/jobs.json` |
| asb CLI | `scripts/asb` |

## Mandatory Reading

1. `CLAUDE.md` — rules, TDD, security theater definition, coverage floor (94%)
2. `docs/governance/AGENT_ROLES.md` — who owns what
3. `docs/governance/GSD_CADENCE.md` — approval gates
