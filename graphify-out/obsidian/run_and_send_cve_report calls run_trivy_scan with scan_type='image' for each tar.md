---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L988"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each tar

## Connections
- [[.test_image_scans_run_for_each_target()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite