---
type: community
cohesion: 0.14
members: 16
---

# Telegram Formatting Rule (bold only, no headers 

**Cohesion:** 0.14 - loosely connected
**Members:** 16 nodes

## Members
- [[.start-history Epoch Restart Ledger]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[Hermes Failure Scenario Catalog (gateway crash, volume corruption, bot disconnect, dependency outage)]] - concept - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Hermes cron Monthly Chaos Engineering Drill (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Hermes cron Weekly Kaizen Review (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Monthly Chaos Engineering Drill (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Prompt Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Prompt Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[Prompt Weekly Kaizen Review]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Restart Backoff Pause (5-minute sleep)]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[SHIPPED  FRICTION  IMPROVE Retrospective Format]] - concept - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Seed Job Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Weekly Kaizen Review]] - document - docker/config/hermes/cron/jobs.yaml
- [[Telegram Formatting Rule (bold only, no headers or tables)]] - rationale - docker/config/hermes/cron/prompts/agentshroud-daily-check-in.txt
- [[Weekly Kaizen Review (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[gateway-exit-diag.log RestartExit Telemetry]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Formatting_Rule_bold_only_no_headers_
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 2 edges to [[_COMMUNITY_OpenClaw Live Cron Job Index (11 jobs)]]
- 2 edges to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_AgentShroud Changelog]]

## Top bridge nodes
- [[Telegram Formatting Rule (bold only, no headers or tables)]] - degree 6, connects to 3 communities
- [[Prompt Weekly Hermes Stability Report]] - degree 6, connects to 1 community
- [[Prompt Monthly Chaos Engineering Drill]] - degree 4, connects to 1 community
- [[Prompt Weekly Kaizen Review]] - degree 4, connects to 1 community
- [[SHIPPED  FRICTION  IMPROVE Retrospective Format]] - degree 2, connects to 1 community