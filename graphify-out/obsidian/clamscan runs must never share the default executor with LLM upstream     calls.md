---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L683"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# clamscan runs must never share the default executor with LLM upstream     calls

## Connections
- [[test_clamav_scans_use_dedicated_single_thread_executor()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite