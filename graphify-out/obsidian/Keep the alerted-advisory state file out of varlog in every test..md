---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "_build_image_targets()"
location: "L23"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_build_image_targets
---

# Keep the alerted-advisory state file out of /var/log in every test.

## Connections
- [[_isolated_alert_state()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_build_image_targets
