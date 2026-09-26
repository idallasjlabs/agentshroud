---
source_file: "docker/config/openclaw/cron/JOBS-REFERENCE.md"
type: "rationale"
community: "TELEGRAM_ISSUES.md"
location: "L61-L63, L91-L98"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TELEGRAM_ISSUESmd
---

# CVE Triage 3-Job Pipeline

## Connections
- [[Automatic Security Updates (blue-green weekly rebuild)]] - `semantically_similar_to` [INFERRED]
- [[Daily CVE Triage & Remediation Scan Job]] - `implements` [EXTRACTED]
- [[Known Drift from jobs.json Seed File]] - `conceptually_related_to` [EXTRACTED]
- [[cve_prefetch.py (CVE fetch-and-diff)]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TELEGRAM_ISSUESmd