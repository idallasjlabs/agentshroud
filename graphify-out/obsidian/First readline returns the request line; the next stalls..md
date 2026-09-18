---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "_DummyTargetWriter"
location: "L76"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_DummyTargetWriter
---

# First readline returns the request line; the next stalls.

## Connections
- [[_HeaderTimeoutReader]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_DummyTargetWriter