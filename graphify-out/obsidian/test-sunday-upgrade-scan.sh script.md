---
source_file: "scripts/smoke.d/test-sunday-upgrade-scan.sh"
type: "code"
community: "sunday_run_scan_gate"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sunday_run_scan_gate
---

# test-sunday-upgrade-scan.sh script

## Connections
- [[check]] - `calls` [EXTRACTED]
- [[make_apply_bin]] - `calls` [EXTRACTED]
- [[make_fake_repo]] - `calls` [EXTRACTED]
- [[run_apply]] - `calls` [EXTRACTED]
- [[run_gate]] - `calls` [EXTRACTED]
- [[test-sunday-upgrade-scan.sh]] - `contains` [EXTRACTED]
- [[write_fake]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sunday_run_scan_gate