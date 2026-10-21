---
type: community
members: 38
---

# Hermes Cron Jobs Reference & Recreation Guide

**Members:** 38 nodes

## Members
- [[dot-start-history Epoch Restart Ledger]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[AgentShroud Daily Check-in (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/agentshroud-daily-check-in.txt
- [[Cron Job Recreation Procedure (create + model pin edit)]] - concept - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Cron Daily Competitive Landscape Update]] - document - docker/bots/openclaw/config/cron/jobs.json
- [[Hermes Cron Jobs Reference & Recreation Guide]] - document - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Hermes Failure Scenario Catalog (gateway crash, volume corruption, bot disconnect, dependency outage)]] - concept - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Hermes Live Cron Store (optdatacronjobs.json)]] - concept - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[How to recreate a job]] - document - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Job index]] - document - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Monthly Chaos Engineering Drill (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Never docker cp Prompt Files (pipe via stdin instead)]] - rationale - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[OpenClaw cron AgentShroud Weekly Summary]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[PrepSend Job Split (agent prep job + no-agent email job)]] - rationale - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Prompt AgentShroud Daily Check-in]] - document - docker/config/hermes/cron/prompts/agentshroud-daily-check-in.txt
- [[Prompt Daily Component Health Digest]] - document - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Prompt Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/prompts/monthly-chaos-engineering-drill.txt
- [[Prompt Newsletter — Model Version Tracker]] - document - docker/config/hermes/cron/prompts/newsletter-model-version-tracker.txt
- [[Prompt OMLX MoE Streaming Health Check]] - document - docker/config/hermes/cron/prompts/omlx-moe-streaming-health-check.txt
- [[Prompt Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[Prompt Weekly Kaizen Review]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Provider Must Be `custom` (not ollama  openai-local)]] - rationale - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Provider-Must-Be-Custom Rule]] - rationale - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[Restart Backoff Pause (5-minute sleep)]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[SHIPPED  FRICTION  IMPROVE Retrospective Format]] - concept - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[Script-Output-Only Constraint (no tools, no recomputation)]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Seed Job AgentShroud Daily Check-in]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Monthly Chaos Engineering Drill]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Weekly Hermes Stability Report]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Weekly Kaizen Review]] - document - docker/config/hermes/cron/jobs.yaml
- [[Stale Trivy Scan Disclosure Requirement]] - rationale - docker/config/hermes/cron/prompts/daily-component-health-digest.txt
- [[Stale `model_provider ollama` in Seed YAML]] - rationale - docker/config/hermes/cron/jobs.yaml
- [[Telegram Formatting Rule (bold only, no headers or tables)]] - rationale - docker/config/hermes/cron/prompts/agentshroud-daily-check-in.txt
- [[Tracked Open-Weight Model Families (Qwen, DeepSeek, Gemma, gpt-oss, GLM)]] - concept - docker/config/hermes/cron/prompts/newsletter-model-version-tracker.txt
- [[Weekly Kaizen Review (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/weekly-kaizen-review.txt
- [[gateway-exit-diag.log RestartExit Telemetry]] - concept - docker/config/hermes/cron/prompts/weekly-hermes-stability-report.txt
- [[gemma-4-26b-a4b-it Model Pin]] - concept - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[hermescronJOBS-REFERENCE]] - document - docker/config/hermes/cron/JOBS-REFERENCE.md
- [[oMLX Chat Completions Endpoint (host.docker.internal8000v1)]] - concept - docker/config/hermes/cron/prompts/omlx-moe-streaming-health-check.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Hermes_Cron_Jobs_Reference__Recreation_Guide
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_DockerEngine]]
- 5 edges to [[_COMMUNITY_Atlas — Curriculum Architect (3)]]
- 4 edges to [[_COMMUNITY_hermesskillsi-icloudscriptscalendar.js]]
- 2 edges to [[_COMMUNITY_Report Delivery Format Instructions (2)]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py (4)]]
- 1 edge to [[_COMMUNITY_AgentTarget (5)]]
- 1 edge to [[_COMMUNITY_Browser — Secure Browser Automation]]

## Top bridge nodes
- [[Hermes Cron Jobs Reference & Recreation Guide]] - degree 31, connects to 5 communities
- [[Prompt Daily Component Health Digest]] - degree 7, connects to 2 communities
- [[OpenClaw cron AgentShroud Weekly Summary]] - degree 5, connects to 2 communities
- [[gemma-4-26b-a4b-it Model Pin]] - degree 5, connects to 1 community
- [[Prompt OMLX MoE Streaming Health Check]] - degree 5, connects to 1 community
