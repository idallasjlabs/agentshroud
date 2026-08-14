---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "Gateway Security Module"
location: "L166"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# test_ssrf_attempt_returns_403()

## Connections
- [[CONNECT to a private IP is blocked by SSRF protection.]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_MockWriter]] - `calls` [EXTRACTED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module