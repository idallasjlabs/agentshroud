---
type: community
members: 3
---

# gifgrep/SKILL.md

**Members:** 3 nodes

## Members
- [[OpenClaw cron Collaborator Daily Digest]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Collaborator Report - Evening]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Collaborator Report - Morning (Telegram HTML, PII filter rules)]] - code - docker/bots/openclaw/config/cron/jobs.json

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gifgrep/SKILLmd
SORT file.name ASC
```
