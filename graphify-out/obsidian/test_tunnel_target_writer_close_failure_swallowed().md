---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "test_http_proxy_coverage.py"
location: "L456"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_http_proxy_coveragepy
---

# test_tunnel_target_writer_close_failure_swallowed()

## Connections
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_MockWriter]] - `calls` [EXTRACTED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[_open_conn()_2]] - `contains` [EXTRACTED]
- [[_open_conn()]] - `indirect_call` [INFERRED]
- [[target_writer.close() raising after relay completes must not propagate.]] - `rationale_for` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_http_proxy_coveragepy
