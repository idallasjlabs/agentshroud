---
type: community
members: 14
---

# OpenClaw Cron Jobs Reference & Recreation Guide

**Members:** 14 nodes

## Members
- [[2026-08-24 incident history (for context, not action items)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[CVE Triage 3-Job Pipeline]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[How to recreate a job]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Job index]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Known drift from `dockerconfigopenclawcronjobs.json`]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Monthly Journal File (optdatamemoriesjournal-YYYY-MM.md)]] - concept - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[NO_REPLY Suppression Token]] - concept - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[OpenClaw Cron Jobs — Reference & Recreation Guide]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Prompt Daily Memory Journal]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Shared dependencies (must exist before dependent jobs run)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[cve_prefetch.py (CVE fetch-and-diff)]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[openclawcronJOBS-REFERENCE]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenClaw_Cron_Jobs_Reference__Recreation_Guide
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Report Delivery Format Instructions]]
- 1 edge to [[_COMMUNITY_Telegram Formatting Rule (bold only, no headers or tables)]]
- 1 edge to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]

## Top bridge nodes
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - degree 12, connects to 2 communities
- [[Prompt Daily Memory Journal]] - degree 4, connects to 1 community
