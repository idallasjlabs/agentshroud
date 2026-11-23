---
type: community
members: 11
---

# competitive-report-*.md dated reports

**Members:** 11 nodes

## Members
- [[Hermes Competitive Intelligence Email (AMPM)_1]] - document - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[Hermes Competitive Landscape Update (AMPM)_1]] - document - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[OpenClaw cron Competitive Analysis Email (Afternoon)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Competitive Landscape Update (Afternoon)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily Competitive Analysis Email (AM)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily Competitive Landscape Update (zero-hallucination sourcing rules)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[agentshroud-email-send.sh]] - code - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[competitive-analysis.md artifact]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[competitive-report-.md dated reports]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[cron-operations skill]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-intelligence-email-am-pm.txt
- [[trend-log.md artifact]] - concept - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/competitive-report-md_dated_reports
SORT file.name ASC
```
