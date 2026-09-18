---
type: community
cohesion: 0.50
members: 5
---

# Hermes Service

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Members
- [[Hermes Service]] - code - docker/docker-compose.yml
- [[Multi-Agent Orchestration (specialized agents, per-agent isolation)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw cron backup 2026-08-31]] - document - docs/dev-notes/cron-backup-20260831-161542/jobs.json
- [[hermes-cron-dedup.sh]] - code - docker/scripts/hermes-cron-dedup.sh
- [[hermes-cron-dedup.sh script]] - code - docker/scripts/hermes-cron-dedup.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Hermes_Service
SORT file.name ASC
```
