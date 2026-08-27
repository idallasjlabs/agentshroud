---
source_file: "gateway/tests/test_soc_realtime_coverage.py"
type: "code"
community: "Community 15"
location: "L164"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_15
---

# _FakeRBAC

## Connections
- [[.__init__()_182]] - `method` [EXTRACTED]
- [[.check_permission()_2]] - `method` [EXTRACTED]
- [[.test_get_caller_passthrough()]] - `calls` [EXTRACTED]
- [[.test_is_group_admin_with_teams_config()]] - `calls` [EXTRACTED]
- [[.test_is_group_admin_without_teams_config()]] - `calls` [EXTRACTED]
- [[.test_is_owner_delegates_to_config()]] - `calls` [EXTRACTED]
- [[.test_require_allowed_does_not_raise()]] - `calls` [EXTRACTED]
- [[.test_require_denied_raises_403_with_reason()]] - `calls` [EXTRACTED]
- [[.test_require_denied_without_reason_uses_forbidden()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Minimal RBAC stand-in with controllable check_permission results.]] - `rationale_for` [EXTRACTED]
- [[PermissionResult]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler]] - `uses` [INFERRED]
- [[test_soc_realtime_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_15