---
source_file: "docker/scripts/security-scheduler.sh"
type: "code"
community: "format_upstream_cve_alert()"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/format_upstream_cve_alert
---

# security-scheduler.sh

## Connections
- [[_stamp_read()]] - `defines` [EXTRACTED]
- [[_stamp_write()]] - `defines` [EXTRACTED]
- [[gateway-seccomp.json (Docker seccomp profile)]] - `conceptually_related_to` [AMBIGUOUS]
- [[log()_5]] - `defines` [EXTRACTED]
- [[security-report-retention.sh]] - `calls` [EXTRACTED]
- [[security-report.sh]] - `calls` [EXTRACTED]
- [[security-scan.sh (unified scan dispatcher)]] - `calls` [EXTRACTED]
- [[security-scheduler.sh script]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/format_upstream_cve_alert