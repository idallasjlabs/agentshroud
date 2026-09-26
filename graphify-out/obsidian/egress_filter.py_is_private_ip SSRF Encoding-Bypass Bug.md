---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "hermes/skills/i-icloud/scripts/calendar.js"
location: "lines 459-480"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/hermes/skills/i-icloud/scripts/calendarjs
---

# egress_filter.py::_is_private_ip SSRF Encoding-Bypass Bug

## Connections
- [[EgressFilter.check()]] - `shares_data_with` [INFERRED]
- [[a2a_policy.py]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/hermes/skills/i-icloud/scripts/calendarjs