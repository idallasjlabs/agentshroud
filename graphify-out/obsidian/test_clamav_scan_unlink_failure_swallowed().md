---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "test_clamav_scan_unavailable_degrades_silently"
location: "L783"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_clamav_scan_unavailable_degrades_silently
---

# test_clamav_scan_unlink_failure_swallowed()

## Connections
- [[HTTPConnectProxy]] - `calls` [EXTRACTED]
- [[_fake_clamscan()_3]] - `contains` [EXTRACTED]
- [[_fake_clamscan()_1]] - `indirect_call` [INFERRED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_clamav_scan_unavailable_degrades_silently
