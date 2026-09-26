---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "OutboundInfoFilter"
location: "L347"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/OutboundInfoFilter
---

# Connection failure → {'ok': False, 'error': <exc>} (no exception leaks).

## Connections
- [[.test_network_error_returns_synthetic_failure()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/OutboundInfoFilter