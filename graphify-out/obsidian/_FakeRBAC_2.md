---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "code"
community: "TestProductionCompose"
location: "L141"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestProductionCompose
---

# _FakeRBAC

## Connections
- [[dot-__init__()_191]] - `method` [EXTRACTED]
- [[dot-check_permission()_2]] - `method` [EXTRACTED]
- [[dot-check_tool_permission()_2]] - `method` [EXTRACTED]
- [[dot-get_user_role()_3]] - `method` [EXTRACTED]
- [[dot-test_owner_bypass()_2]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass()_3]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypasses_sandbox()]] - `calls` [EXTRACTED]
- [[dot-test_owner_exempt_when_critical_guard_failed()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_denied()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_exception_fails_closed()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_pass_logs_role_and_allows()]] - `calls` [EXTRACTED]
- [[dot-test_rbac_requires_approval()]] - `calls` [EXTRACTED]
- [[dot-test_tool_permission_denied()]] - `calls` [EXTRACTED]
- [[dot-test_tool_permission_requires_approval()]] - `calls` [EXTRACTED]
- [[dot-test_with_rbac_manager()]] - `calls` [EXTRACTED]
- [[Deterministic stand-in for RBACManager.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_middleware_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestProductionCompose
