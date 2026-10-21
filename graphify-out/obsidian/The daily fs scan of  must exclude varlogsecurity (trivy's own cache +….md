---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "format_cve_report() (2)"
location: "L1273"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/format_cve_report_2
---

# The daily fs scan of / must exclude /var/log/security (trivy's own cache +…

## Connections
- [[dot-test_daily_fs_scan_skips_security_log_tree()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/format_cve_report_2
