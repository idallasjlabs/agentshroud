---
type: community
cohesion: 0.67
members: 3
---

# 3. Code Quality

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[OpenClaw cron Collaborator Daily Digest]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Collaborator Report - Evening]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Collaborator Report - Morning (Telegram HTML, PII filter rules)]] - code - docker/bots/openclaw/config/cron/jobs.json

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/3_Code_Quality
SORT file.name ASC
```
