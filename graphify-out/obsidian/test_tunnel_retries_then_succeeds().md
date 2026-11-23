---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "test_http_proxy_coverage.py"
location: "L307"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_http_proxy_coveragepy
---

# test_tunnel_retries_then_succeeds()

## Connections
- [[First open_connection attempt fails; retry (with patched sleep) succeeds.]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_MockWriter]] - `calls` [EXTRACTED]
- [[_fake_sleep()_1]] - `indirect_call` [INFERRED]
- [[_flaky_open()]] - `indirect_call` [INFERRED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_http_proxy_coveragepy
