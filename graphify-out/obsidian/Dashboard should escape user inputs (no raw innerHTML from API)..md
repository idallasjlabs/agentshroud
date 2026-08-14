---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "ESP32 Firmware"
location: "L747"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# Dashboard should escape user inputs (no raw innerHTML from API).

## Connections
- [[.test_xss_in_dashboard_inputs()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ESP32_Firmware