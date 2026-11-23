---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L196"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_connect_denied_by_egress_filter_returns_403()

## Connections
- [[EgressAction]] - `uses` [INFERRED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[asyncio_82]] - `references` [EXTRACTED]
- [[check_async()_63]] - `contains` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
