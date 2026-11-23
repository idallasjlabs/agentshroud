---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L443"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_agent_id_for_peer_cached_after_first_lookup()

## Connections
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[Second call for same IP uses cache; rDNS is only called once, fDNS never.]] - `rationale_for` [EXTRACTED]
- [[_fdns()]] - `indirect_call` [INFERRED]
- [[_rdns()]] - `indirect_call` [INFERRED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
