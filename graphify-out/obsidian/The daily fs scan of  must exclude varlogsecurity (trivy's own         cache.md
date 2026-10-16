---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "TestTrivySkipDirs"
location: "L1124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestTrivySkipDirs
---

# The daily fs scan of / must exclude /var/log/security (trivy's own         cache

## Connections
- [[dot-test_daily_fs_scan_skips_security_log_tree()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestTrivySkipDirs
