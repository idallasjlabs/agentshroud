---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Slack Proxy Coverage"
location: "L347"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_Proxy_Coverage
---

# Connection failure → {'ok': False, 'error': <exc>} (no exception leaks).

## Connections
- [[.test_network_error_returns_synthetic_failure()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_Proxy_Coverage