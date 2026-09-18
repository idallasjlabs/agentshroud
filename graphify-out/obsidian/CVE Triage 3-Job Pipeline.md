---
source_file: "docker/config/openclaw/cron/JOBS-REFERENCE.md"
type: "rationale"
community: "OpenClaw Live Cron Job Index (11 jobs)"
location: "L61-L63, L91-L98"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/OpenClaw_Live_Cron_Job_Index_11_jobs
---

# CVE Triage 3-Job Pipeline

## Connections
- [[Automatic Security Updates (blue-green weekly rebuild)]] - `semantically_similar_to` [INFERRED]
- [[Daily CVE Triage & Remediation Scan Job]] - `implements` [EXTRACTED]
- [[Known Drift from jobs.json Seed File]] - `conceptually_related_to` [EXTRACTED]
- [[cve_prefetch.py (CVE fetch-and-diff)]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/OpenClaw_Live_Cron_Job_Index_11_jobs