---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Community 809"
location: "L995"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_809
---

# run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each tar

## Connections
- [[.test_image_scans_run_for_each_target()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_809