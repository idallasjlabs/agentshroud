---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "test_daily_cve_report.py"
location: "L182"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# Silently appending a new key could create a pin nothing consumes.

## Connections
- [[dot-test_write_pin_refuses_an_absent_key()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy
