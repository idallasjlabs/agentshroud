---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "test_http_proxy_coverage.py"
location: "L432"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_http_proxy_coveragepy
---

# test_tunnel_all_attempts_fail_returns_502()

## Connections
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_MockWriter]] - `calls` [EXTRACTED]
- [[_always_fail()]] - `indirect_call` [INFERRED]
- [[_fake_sleep()]] - `contains` [EXTRACTED]
- [[_fake_sleep()_1]] - `indirect_call` [INFERRED]
- [[_make_stream()]] - `calls` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_http_proxy_coveragepy
