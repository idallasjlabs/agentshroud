---
source_file: "gateway/tests/test_soc_realtime_coverage.py"
type: "code"
community: "RBACConfig"
location: "L164"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RBACConfig
---

# _FakeRBAC

## Connections
- [[dot-__init__()_33]] - `method` [EXTRACTED]
- [[dot-check_permission()_2]] - `method` [EXTRACTED]
- [[dot-test_get_caller_passthrough()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_admin_with_teams_config()]] - `calls` [EXTRACTED]
- [[dot-test_is_group_admin_without_teams_config()]] - `calls` [EXTRACTED]
- [[dot-test_is_owner_delegates_to_config()]] - `calls` [EXTRACTED]
- [[dot-test_require_allowed_does_not_raise()]] - `calls` [EXTRACTED]
- [[dot-test_require_denied_raises_403_with_reason()]] - `calls` [EXTRACTED]
- [[dot-test_require_denied_without_reason_uses_forbidden()]] - `calls` [EXTRACTED]
- [[Minimal RBAC stand-in with controllable check_permission results.]] - `rationale_for` [EXTRACTED]
- [[PermissionResult]] - `uses` [INFERRED]
- [[test_soc_realtime_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RBACConfig
