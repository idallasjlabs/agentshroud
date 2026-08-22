---
source_file: "gateway/tests/test_http_proxy.py"
type: "rationale"
community: "Http Proxy"
location: "L167"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Http_Proxy
---

# CONNECT to a private IP is blocked by SSRF protection.

## Connections
- [[test_ssrf_attempt_returns_403()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Http_Proxy