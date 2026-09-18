---
type: community
cohesion: 1.00
members: 2
---

# Cron: AgentShroud Daily Check-in

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Cron AgentShroud Daily Check-in]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[daily-checkin.sh (marvinpi status check)]] - code - docker/config/openclaw/cron/scripts/daily-checkin.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Cron_AgentShroud_Daily_Check-in
SORT file.name ASC
```
