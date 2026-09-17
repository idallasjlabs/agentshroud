---
source_file: "gateway/tests/test_soc_realtime_coverage.py"
type: "code"
community: "TestFromAuditChainEntry"
location: "L503"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TestFromAuditChainEntry
---

# TestCollectRecentEvents

## Connections
- [[.test_collects_and_converts()]] - `method` [EXTRACTED]
- [[.test_none_store_returns_empty()]] - `method` [EXTRACTED]
- [[.test_severity_filter_drops_lower()]] - `method` [EXTRACTED]
- [[.test_store_error_returns_empty()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[PermissionResult]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler_1]] - `uses` [INFERRED]
- [[collect_recent_events()]] - `calls` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/TestFromAuditChainEntry