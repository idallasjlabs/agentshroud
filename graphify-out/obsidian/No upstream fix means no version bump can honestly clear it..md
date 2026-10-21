---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "test_daily_cve_report.py (2)"
location: "L96"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy_2
---

# No upstream fix means no version bump can honestly clear it.

## Connections
- [[dot-test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_daily_cve_reportpy_2
