---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "test_agent_cve_registry.py (2)"
location: "L151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_agent_cve_registrypy_2
---

# A nested base64(base64(injection)) payload is peeled and blocked.

## Connections
- [[test_inbound_nested_base64_injection_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_agent_cve_registrypy_2
