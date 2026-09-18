---
source_file: "scripts/lib/sunday-scan.sh"
type: "code"
community: "sunday_run_scan_gate"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sunday_run_scan_gate
---

# sunday-scan.sh

## Connections
- [[die (fallback)]] - `defines` [EXTRACTED]
- [[log (fallback)]] - `defines` [EXTRACTED]
- [[sunday-scan.sh script]] - `contains` [EXTRACTED]
- [[sunday-upgrade-apply.sh]] - `imports_from` [INFERRED]
- [[sunday_ensure_trivy]] - `defines` [EXTRACTED]
- [[sunday_resolve_scan_image]] - `defines` [EXTRACTED]
- [[sunday_run_scan_gate]] - `defines` [EXTRACTED]
- [[warn (fallback)]] - `defines` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sunday_run_scan_gate