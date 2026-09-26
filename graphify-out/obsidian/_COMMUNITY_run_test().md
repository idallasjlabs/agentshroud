---
type: community
cohesion: 0.08
members: 37
---

# run_test()

**Cohesion:** 0.08 - loosely connected
**Members:** 37 nodes

## Members
- [[AI Security Standards Watch Cron Prompt]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[AI Security Standards Watch Job (OWASP  NIST AI RMF  MITRE ATLAS)]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[AgentShroud Brand Color Palette]] - concept - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[AgentShroud Branded HTML Report Template]] - document - docker/config/openclaw/cron/templates/report-template.html
- [[AgentShroud Weekly Summary (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/agentshroud-weekly-summary.txt
- [[Agentic AI Threat Intelligence Cron Prompt]] - document - docker/config/openclaw/cron/prompts/agentic-ai-threat-intelligence.txt
- [[Brand colors reference]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Canonical storage]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Collaborator Daily Digest Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-daily-digest.txt
- [[Collaborator Report (Evening) Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-report-evening.txt
- [[Collaborator Report (Morning) Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-report-morning.txt
- [[Collaborator Report - Evening Job]] - document - docker/config/openclaw/cron/prompts/collaborator-report-evening.txt
- [[Collaborator Report Timeout Bump to 1800s]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Contributor Log Read Path (gateway-data primary, memory fallback)]] - concept - docker/config/openclaw/cron/prompts/collaborator-report-morning.txt
- [[CronSessionLifecycleClaimError (stale isolated-session claim leases)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Dual-Surface Report Delivery (Email HTML  Telegram Markdown)]] - rationale - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[HTML version (for email)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[How to build it]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Markdown version (for Telegram + archival)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Multi-User Support with Role-Based Permissions]] - concept - docs/archive/FUTURE-FEATURES.md
- [[OpenClaw Live Cron Job Index (11 jobs)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[OpenClaw Live Cron Store (SQLite on agentshroud-config volume)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Per-CVE Mitigation Assessment (FULLY  PARTIALLY  NOT_MITIGATED)]] - concept - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[Quick checklist]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Report Delivery Format Instructions]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Report Template Placeholder Contract ({{REPORT_TITLE}}{{REPORT_TYPE}}{{REPORT_DATE}}{{REPORT_CONTENT}})]] - concept - docker/config/openclaw/cron/templates/report-template.html
- [[Rules_18]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Scheduled Actions & Automation (in-container cron)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Seed Job AgentShroud Weekly Summary]] - document - docker/config/hermes/cron/jobs.yaml
- [[Sending via email]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Session Cleanup Reaper (30-min openclaw sessions cleanup --fix-missing)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Source Verification Policy]] - rationale - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Source Verification Policy (MANDATORY)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Stdin-Pipe File Deployment Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Telegram delivery rules (from AGENTS.md)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Verification checklist (run before saving any report)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[html-report-instructions]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run_test
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TELEGRAM_ISSUES]]
- 1 edge to [[_COMMUNITY_GroupRegistry]]

## Top bridge nodes
- [[Report Delivery Format Instructions]] - degree 16, connects to 1 community
- [[OpenClaw Live Cron Job Index (11 jobs)]] - degree 10, connects to 1 community
- [[Seed Job AgentShroud Weekly Summary]] - degree 2, connects to 1 community
- [[Per-CVE Mitigation Assessment (FULLY  PARTIALLY  NOT_MITIGATED)]] - degree 2, connects to 1 community