---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "Community 67"
location: "L683"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_67
---

# clamscan runs must never share the default executor with LLM upstream     calls

## Connections
- [[test_clamav_scans_use_dedicated_single_thread_executor()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_67