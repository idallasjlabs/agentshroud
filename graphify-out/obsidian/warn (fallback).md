---
source_file: "scripts/lib/sunday-scan.sh"
type: "code"
community: "sunday_run_scan_gate"
location: "53"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sunday_run_scan_gate
---

# warn (fallback)

## Connections
- [[sunday-scan.sh]] - `defines` [EXTRACTED]
- [[sunday_ensure_trivy]] - `calls` [EXTRACTED]
- [[sunday_resolve_scan_image]] - `calls` [EXTRACTED]
- [[sunday_run_scan_gate]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sunday_run_scan_gate