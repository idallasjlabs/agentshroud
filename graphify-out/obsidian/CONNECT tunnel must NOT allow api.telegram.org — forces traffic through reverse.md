---
source_file: "gateway/tests/test_http_proxy.py"
type: "rationale"
community: "HTTP CONNECT Proxy & Egress"
location: "L288"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTP_CONNECT_Proxy__Egress
---

# CONNECT tunnel must NOT allow api.telegram.org — forces traffic through reverse

## Connections
- [[test_telegram_api_blocked_in_connect_proxy()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTP_CONNECT_Proxy__Egress
