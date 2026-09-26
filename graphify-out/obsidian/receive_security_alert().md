---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "InjectionSeverity"
location: "L1707"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# receive_security_alert()

## Connections
- [[.test_alerts_accepted_from_localhost()]] - `calls` [EXTRACTED]
- [[Receive structured security alerts from gateway-internal scripts.      Called by]] - `rationale_for` [EXTRACTED]
- [[Request_1]] - `references` [EXTRACTED]
- [[Request_10]] - `references` [EXTRACTED]
- [[main.py_2]] - `contains` [EXTRACTED]
- [[make_event()]] - `calls` [EXTRACTED]
- [[test_main_endpoints.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/InjectionSeverity