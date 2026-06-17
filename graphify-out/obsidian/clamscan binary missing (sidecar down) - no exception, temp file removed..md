---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "HTTP Proxy Coverage Tests"
location: "L630"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTP_Proxy_Coverage_Tests
---

# clamscan binary missing (sidecar down) -> no exception, temp file removed.

## Connections
- [[test_clamav_scan_unavailable_degrades_silently()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTP_Proxy_Coverage_Tests