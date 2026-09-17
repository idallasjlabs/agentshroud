---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "HTTPConnectProxy"
location: "L241"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# Host-only CONNECT target defaults to port 443; blocked host -> 403.

## Connections
- [[test_target_without_port_defaults_to_443()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTPConnectProxy