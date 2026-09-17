---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "_DummyTargetWriter"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_DummyTargetWriter
---

# _HeaderTimeoutReader

## Connections
- [[.__init__()_182]] - `method` [EXTRACTED]
- [[.readline()_1]] - `method` [EXTRACTED]
- [[First readline returns the request line; the next stalls.]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy_1]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[test_header_read_timeout_returns_408()]] - `calls` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_DummyTargetWriter