---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "Http Proxy Coverage"
location: "L457"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Http_Proxy_Coverage
---

# target_writer.close() raising after relay completes must not propagate.

## Connections
- [[test_tunnel_target_writer_close_failure_swallowed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Http_Proxy_Coverage