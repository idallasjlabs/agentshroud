---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "HTTPConnectProxy"
location: "L68"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# _TimeoutReader

## Connections
- [[.readline()]] - `method` [EXTRACTED]
- [[HTTPConnectProxy_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[readline() always raises TimeoutError — simulates a stalled client.]] - `rationale_for` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]
- [[test_request_line_timeout_returns_408()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy