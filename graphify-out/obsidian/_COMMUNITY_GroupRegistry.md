---
type: community
cohesion: 0.12
members: 20
---

# GroupRegistry

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[.start-history Epoch Restart Ledger]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[Cron AgentShroud Weekly Summary]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Hermes Failure Scenario Catalog (gateway crash, volume corruption, bot disconnect, dependency outage)]] - concept - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Hermes cron Monthly Chaos Engineering Drill (gemma-4-26b-a4b-it)]] - code - docker/bots/hermes/init-config.sh
- [[Mandatory Daily Delivery (never SILENT)]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Monthly Chaos Engineering Drill (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Prompt Daily Component Health Digest]] - document - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Prompt Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Prompt Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[Prompt Weekly Kaizen Review]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Restart Backoff Pause (5-minute sleep)]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[SHIPPED  FRICTION  IMPROVE Retrospective Format]] - concept - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Script-Output-Only Constraint (no tools, no recomputation)]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Seed Job Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/jobs.yaml
- [[Silence-Over-Hallucination Principle]] - rationale - docker/config/hermes/cron/prompts/hermes-competitive-landscape-update-am-pm.txt
- [[Stale Trivy Scan Disclosure Requirement]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Telegram Formatting Rule (bold only, no headers or tables)]] - rationale - docker/config/hermes/cron/prompts/agentshroud-daily-check-in.txt
- [[Zero-Hallucination Primary-Source Rule (30-day recency)]] - rationale - docker/config/hermes/cron/prompts/newsletter-coding-agent-clis.txt
- [[gateway-exit-diag.log RestartExit Telemetry]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupRegistry
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_telegram_replay.py]]
- 2 edges to [[_COMMUNITY_ssh-configuration]]
- 2 edges to [[_COMMUNITY_mcp-proxy-wrapper.js]]
- 1 edge to [[_COMMUNITY_TELEGRAM_ISSUES]]
- 1 edge to [[_COMMUNITY_run_test()]]
- 1 edge to [[_COMMUNITY_TestSplitForSpeech]]

## Top bridge nodes
- [[Cron AgentShroud Weekly Summary]] - degree 5, connects to 3 communities
- [[Prompt Daily Component Health Digest]] - degree 7, connects to 2 communities
- [[Prompt Weekly Kaizen Review]] - degree 4, connects to 2 communities
- [[Telegram Formatting Rule (bold only, no headers or tables)]] - degree 6, connects to 1 community
- [[Prompt Weekly Hermes Stability Report]] - degree 6, connects to 1 community