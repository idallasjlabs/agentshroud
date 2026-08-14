---
source_file: "gateway/tests/test_http_proxy.py"
type: "rationale"
community: "Gateway Security Module"
location: "L444"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# Second call for same IP uses cache; rDNS is only called once, fDNS never.

## Connections
- [[test_agent_id_for_peer_cached_after_first_lookup()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module