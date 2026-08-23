---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "Http Proxy"
location: "L166"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Http_Proxy
---

# test_ssrf_attempt_returns_403()

## Connections
- [[CONNECT to a private IP is blocked by SSRF protection.]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_MockWriter]] - `calls` [EXTRACTED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Http_Proxy