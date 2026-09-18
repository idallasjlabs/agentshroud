---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "asyncio"
location: "L1164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/asyncio
---

# run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each…

## Connections
- [[.test_image_scans_run_for_each_target()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/asyncio