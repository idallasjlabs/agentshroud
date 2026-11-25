---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L254"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_connect_unknown_domain_can_be_allowed_by_interactive_egress()

## Connections
- [[EgressAction]] - `uses` [INFERRED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[_open_conn()_4]] - `contains` [EXTRACTED]
- [[_open_conn()_3]] - `indirect_call` [INFERRED]
- [[asyncio_83]] - `references` [EXTRACTED]
- [[check_async()_65]] - `contains` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
