---
type: community
cohesion: 0.09
members: 24
---

# Report Delivery Format Instructions (2)

**Cohesion:** 0.09 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-ghsa-ids-cache.json (GHSA registry prefetch artifact)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[dot-new-cves.json (pre-diffed advisory handoff file)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[2026-08-24 incident history (for context, not action items)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[AgentShroud Branded Report Template]] - code - docker/config/openclaw/cron/templates/report-template.html
- [[Automatic Security Updates (blue-green weekly rebuild)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[CVE Triage 3-Job Pipeline]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Daily CVE Triage & Remediation Scan Job]] - document - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[Daily Memory Journal (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Daily Memory Journal Job (nightly memory consolidation)]] - document - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[How to recreate a job_1]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Job index_1]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Known Drift from jobs.json Seed File]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Known drift from `dockerconfigopenclawcronjobs.json`]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Long-Term Memory with Vector Search]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Monthly Journal File (optdatamemoriesjournal-YYYY-MM.md)]] - concept - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[NO_REPLY Suppression Token]] - concept - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Prompt Daily Memory Journal]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Seed Job Daily Memory Journal]] - document - docker/config/hermes/cron/jobs.yaml
- [[Shared dependencies (must exist before dependent jobs run)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Zero Hallucinations On Errors Policy]] - rationale - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[cve_prefetch.py (CVE fetch-and-diff)]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[memorycontext.md Continuity File (50 lines)]] - concept - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[openclawcronJOBS-REFERENCE]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Report_Delivery_Format_Instructions_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AgentTarget (5)]]
- 2 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 1 edge to [[_COMMUNITY_run-standalone.sh]]

## Top bridge nodes
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - degree 13, connects to 3 communities
- [[Daily CVE Triage & Remediation Scan Job]] - degree 7, connects to 1 community
- [[Prompt Daily Memory Journal]] - degree 5, connects to 1 community
- [[Daily Memory Journal Job (nightly memory consolidation)]] - degree 4, connects to 1 community
- [[AgentShroud Branded Report Template]] - degree 2, connects to 1 community
