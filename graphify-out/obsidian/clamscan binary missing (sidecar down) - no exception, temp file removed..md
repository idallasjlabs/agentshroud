---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "Http Proxy Coverage"
location: "L768"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Http_Proxy_Coverage
---

# clamscan binary missing (sidecar down) -> no exception, temp file removed.

## Connections
- [[test_clamav_scan_unavailable_degrades_silently()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Http_Proxy_Coverage