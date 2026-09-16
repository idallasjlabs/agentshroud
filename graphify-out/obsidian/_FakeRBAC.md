---
source_file: "gateway/tests/test_soc_realtime_coverage.py"
type: "code"
community: "Ingest API & RBAC Core"
location: "L164"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Ingest_API__RBAC_Core
---

# _FakeRBAC

## Connections
- [[dot-__init__()_11]] - `method` [EXTRACTED]
- [[dot-check_permission()_1]] - `method` [EXTRACTED]
- [[dot-test_get_caller_passthrough()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_admin_with_teams_config()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_admin_without_teams_config()]] - `calls` [EXTRACTED]
- [[dot-test_is_owner_delegates_to_config()]] - `calls` [EXTRACTED]
- [[dot-test_require_allowed_does_not_raise()]] - `calls` [EXTRACTED]
- [[dot-test_require_denied_raises_403_with_reason()]] - `calls` [EXTRACTED]
- [[dot-test_require_denied_without_reason_uses_forbidden()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Minimal RBAC stand-in with controllable check_permission results.]] - `rationale_for` [EXTRACTED]
- [[PermissionResult]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler_1]] - `uses` [INFERRED]
- [[test_soc_realtime_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Ingest_API__RBAC_Core