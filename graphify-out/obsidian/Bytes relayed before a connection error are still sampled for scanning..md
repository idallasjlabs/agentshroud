---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "Http Proxy Coverage"
location: "L692"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Http_Proxy_Coverage
---

# Bytes relayed before a connection error are still sampled for scanning.

## Connections
- [[test_relay_and_scan_read_error_scans_partial_buffer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Http_Proxy_Coverage