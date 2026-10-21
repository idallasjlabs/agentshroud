---
type: community
members: 1
---

# Audit-log-every-fetch design rationale

**Members:** 1 nodes

## Members
- [[CVE Triage Report Cron Prompt]] - document - docker/config/openclaw/cron/prompts/cve-triage-report.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit-log-every-fetch_design_rationale
SORT file.name ASC
```
