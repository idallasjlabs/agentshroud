---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L218"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_connect_system_bypass_domain_skips_policy_checks()

## Connections
- [[EgressAction]] - `uses` [INFERRED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[_open_conn()_3]] - `indirect_call` [INFERRED]
- [[asyncio_82]] - `references` [EXTRACTED]
- [[check_async()_64]] - `contains` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
