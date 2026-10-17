---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "code"
community: "_req"
location: "L141"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_req
---

# _FakeRBAC

## Connections
- [[dot-__init__()_76]] - `method` [EXTRACTED]
- [[dot-check_permission()]] - `method` [EXTRACTED]
- [[dot-check_tool_permission()]] - `method` [EXTRACTED]
- [[dot-get_user_role()]] - `method` [EXTRACTED]
- [[dot-test_owner_bypass()_1]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass()_2]] - `calls` [EXTRACTED]
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
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_middleware_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_req
