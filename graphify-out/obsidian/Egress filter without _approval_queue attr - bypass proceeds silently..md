---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "rationale"
community: "HTTP Proxy Coverage Tests"
location: "L275"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/HTTP_Proxy_Coverage_Tests
---

# Egress filter without _approval_queue attr -> bypass proceeds silently.

## Connections
- [[test_bypass_with_egress_filter_lacking_approval_queue()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/HTTP_Proxy_Coverage_Tests