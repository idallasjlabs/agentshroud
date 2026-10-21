---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "api.py (2)"
location: "L347"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/apipy_2
---

# Connection failure → {'ok': False, 'error': <exc>} (no exception leaks).

## Connections
- [[dot-test_network_error_returns_synthetic_failure()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/apipy_2
