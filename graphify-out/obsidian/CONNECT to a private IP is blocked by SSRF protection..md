---
source_file: "gateway/tests/test_http_proxy.py"
type: "rationale"
community: "Gateway Security Module"
location: "L167"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# CONNECT to a private IP is blocked by SSRF protection.

## Connections
- [[test_ssrf_attempt_returns_403()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module