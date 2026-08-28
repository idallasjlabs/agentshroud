---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Community 24"
location: "L347"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_24
---

# Connection failure → {'ok': False, 'error': <exc>} (no exception leaks).

## Connections
- [[.test_network_error_returns_synthetic_failure()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_24