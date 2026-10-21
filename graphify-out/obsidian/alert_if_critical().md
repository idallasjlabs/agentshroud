---
source_file: "docker/scripts/security-scan.sh"
type: "code"
community: "Regression guard (2026-08-30): the report scanned :latest tags while deploys…"
location: "L22"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Regression_guard_2026-08-30_the_report_scanned_latest_tags_while_deploys
---

# alert_if_critical()

## Connections
- [[dockerscriptssecurity-scan.sh]] - `defines` [EXTRACTED]
- [[log()_11]] - `calls` [EXTRACTED]
- [[run_clamav()]] - `calls` [EXTRACTED]
- [[run_trivy()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Regression_guard_2026-08-30_the_report_scanned_latest_tags_while_deploys
