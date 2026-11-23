---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "test_http_proxy_coverage.py"
location: "L485"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_http_proxy_coveragepy
---

# test_keepalive_set_on_both_tunnel_ends()

## Connections
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_SocketTransportWriter]] - `calls` [EXTRACTED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[_open_conn()_1]] - `contains` [EXTRACTED]
- [[_open_conn()]] - `indirect_call` [INFERRED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_http_proxy_coveragepy
