---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L166"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_ssrf_attempt_returns_403()

## Connections
- [[CONNECT to a private IP is blocked by SSRF protection.]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[asyncio_82]] - `references` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
