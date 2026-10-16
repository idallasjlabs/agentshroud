---
type: community
cohesion: 0.04
members: 62
---

# Report Delivery Format Instructions

**Cohesion:** 0.04 - loosely connected
**Members:** 62 nodes

## Members
- [[dot-ghsa-ids-cache.json (GHSA registry prefetch artifact)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[dot-new-cves.json (pre-diffed advisory handoff file)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[2026-08-24 incident history (for context, not action items)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[AI Security Standards Watch Cron Prompt]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[AI Security Standards Watch Job (OWASP  NIST AI RMF  MITRE ATLAS)]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[AgentShroud Brand Color Palette]] - concept - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[AgentShroud Branded HTML Report Template]] - document - docker/config/openclaw/cron/templates/report-template.html
- [[AgentShroud Branded Report Template]] - code - docker/config/openclaw/cron/templates/report-template.html
- [[AgentShroud Weekly Summary (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/agentshroud-weekly-summary.txt
- [[Agentic AI Threat Intelligence Cron Prompt]] - document - docker/config/openclaw/cron/prompts/agentic-ai-threat-intelligence.txt
- [[Automatic Security Updates (blue-green weekly rebuild)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Brand colors reference]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[CVE Triage 3-Job Pipeline]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Canonical storage]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Collaborator Daily Digest Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-daily-digest.txt
- [[Collaborator Report (Evening) Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-report-evening.txt
- [[Collaborator Report (Morning) Cron Prompt]] - document - docker/config/openclaw/cron/prompts/collaborator-report-morning.txt
- [[Collaborator Report - Evening Job]] - document - docker/config/openclaw/cron/prompts/collaborator-report-evening.txt
- [[Collaborator Report Timeout Bump to 1800s]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Contributor Log Read Path (gateway-data primary, memory fallback)]] - concept - docker/config/openclaw/cron/prompts/collaborator-report-morning.txt
- [[CronSessionLifecycleClaimError (stale isolated-session claim leases)]] - concept - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Daily CVE Triage & Remediation Scan Job]] - document - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[Daily Memory Journal (Hermes Prompt)]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Daily Memory Journal Job (nightly memory consolidation)]] - document - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[Dual-Surface Report Delivery (Email HTML  Telegram Markdown)]] - rationale - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[HTML version (for email)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Hermes cron Daily Memory Journal (silent, local delivery)]] - code - docker/bots/hermes/init-config.sh
- [[How to build it]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[How to recreate a job_1]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Job index_1]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Known Drift from jobs.json Seed File]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Known drift from `dockerconfigopenclawcronjobs.json`]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Long-Term Memory with Vector Search]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Markdown version (for Telegram + archival)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Monthly Journal File (optdatamemoriesjournal-YYYY-MM.md)]] - concept - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Multi-User Support with Role-Based Permissions]] - concept - docs/archive/FUTURE-FEATURES.md
- [[NO_REPLY Suppression Token]] - concept - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[OpenClaw Live Cron Job Index (11 jobs)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[OpenClaw Live Cron Store (SQLite on agentshroud-config volume)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Per-CVE Mitigation Assessment (FULLY  PARTIALLY  NOT_MITIGATED)]] - concept - docker/config/openclaw/cron/prompts/cve-triage-report.txt
- [[Prompt Daily Memory Journal]] - document - docker/config/hermes/cron/prompts/daily-memory-journal.txt
- [[Quick checklist]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Report Delivery Format Instructions]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Report Template Placeholder Contract ({{REPORT_TITLE}}{{REPORT_TYPE}}{{REPORT_DATE}}{{REPORT_CONTENT}})]] - concept - docker/config/openclaw/cron/templates/report-template.html
- [[Rules_2]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Scheduled Actions & Automation (in-container cron)]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Seed Job AgentShroud Weekly Summary]] - document - docker/config/hermes/cron/jobs.yaml
- [[Seed Job Daily Memory Journal]] - document - docker/config/hermes/cron/jobs.yaml
- [[Sending via email]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Session Cleanup Reaper (30-min openclaw sessions cleanup --fix-missing)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Shared dependencies (must exist before dependent jobs run)]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Source Verification Policy]] - rationale - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Source Verification Policy (MANDATORY)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Stdin-Pipe File Deployment Pattern (never docker cp)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[Telegram delivery rules (from AGENTS.md)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Verification checklist (run before saving any report)]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[Zero Hallucinations On Errors Policy]] - rationale - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[cve_prefetch.py (CVE fetch-and-diff)]] - code - docker/config/openclaw/cron/scripts/cve_prefetch.py
- [[html-report-instructions]] - document - docker/config/openclaw/cron/templates/html-report-instructions.md
- [[memorycontext.md Continuity File (50 lines)]] - concept - docker/config/openclaw/cron/prompts/daily-memory-journal.txt
- [[openclawcronJOBS-REFERENCE]] - document - docker/config/openclaw/cron/JOBS-REFERENCE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Report_Delivery_Format_Instructions
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 1 edge to [[_COMMUNITY__seed_cron]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]

## Top bridge nodes
- [[OpenClaw Cron Jobs Reference & Recreation Guide]] - degree 13, connects to 2 communities
- [[Prompt Daily Memory Journal]] - degree 5, connects to 1 community
- [[Seed Job AgentShroud Weekly Summary]] - degree 2, connects to 1 community
- [[Hermes cron Daily Memory Journal (silent, local delivery)]] - degree 2, connects to 1 community
