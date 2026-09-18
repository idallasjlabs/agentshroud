---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "HTTPConnectProxy"
location: "L478"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# Writer exposing a .transport whose socket records setsockopt calls.

## Connections
- [[_SocketTransportWriter]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTPConnectProxy