---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L354"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_system_bypass_without_egress_filter()

## Connections
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[System bypass domains should not error when egress_filter is None.]] - `rationale_for` [EXTRACTED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[_open_conn()_6]] - `contains` [EXTRACTED]
- [[_open_conn()_3]] - `indirect_call` [INFERRED]
- [[asyncio_82]] - `references` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
