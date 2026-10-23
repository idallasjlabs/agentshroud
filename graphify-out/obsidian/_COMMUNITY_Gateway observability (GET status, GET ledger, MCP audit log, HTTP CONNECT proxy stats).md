---
type: community
cohesion: 0.67
members: 3
---

# Gateway observability (GET /status, GET /ledger, MCP audit log, HTTP CONNECT proxy stats)

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[75 Active Security Modules — no stubs, fully wired]] - rationale - CLAUDE.md
- [[OpenClaw cron AI Security Standards Watch (OWASPNISTISOMAESTROATLAS)]] - code - docker/bots/openclaw/config/cron/jobs.json
- [[OpenClaw cron Daily CVE Triage & Remediation Scan (cites agent_cve_registry.py)]] - code - docker/bots/openclaw/config/cron/jobs.json

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_observability_GET_/status_GET_/ledger_MCP_audit_log_HTTP_CONNECT_proxy_stats
SORT file.name ASC
```
