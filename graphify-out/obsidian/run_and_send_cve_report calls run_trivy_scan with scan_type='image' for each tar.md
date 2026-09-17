---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "TestRunAndSendCveReportImageScans"
location: "L1164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestRunAndSendCveReportImageScans
---

# run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each tar

## Connections
- [[.test_image_scans_run_for_each_target()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestRunAndSendCveReportImageScans