---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "code"
community: "Security Module Middleware"
location: "L141"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# _FakeRBAC

## Connections
- [[.__init__()_162]] - `method` [EXTRACTED]
- [[.check_permission()_1]] - `method` [EXTRACTED]
- [[.check_tool_permission()_2]] - `method` [EXTRACTED]
- [[.get_user_role()_2]] - `method` [EXTRACTED]
- [[.test_owner_bypass()_1]] - `calls` [EXTRACTED]
- [[.test_owner_bypass()_2]] - `calls` [EXTRACTED]
- [[.test_owner_bypasses_sandbox()]] - `calls` [EXTRACTED]
- [[.test_owner_exempt_when_critical_guard_failed()]] - `calls` [EXTRACTED]
- [[.test_rbac_denied()]] - `calls` [EXTRACTED]
- [[.test_rbac_exception_fails_closed()]] - `calls` [EXTRACTED]
- [[.test_rbac_pass_logs_role_and_allows()]] - `calls` [EXTRACTED]
- [[.test_rbac_requires_approval()]] - `calls` [EXTRACTED]
- [[.test_second_message_after_window_sends_again()]] - `calls` [INFERRED]
- [[.test_tool_permission_denied()]] - `calls` [EXTRACTED]
- [[.test_tool_permission_requires_approval()]] - `calls` [EXTRACTED]
- [[.test_two_messages_within_window_send_only_one_mirror()]] - `calls` [INFERRED]
- [[.test_with_rbac_manager()]] - `calls` [EXTRACTED]
- [[Deterministic stand-in for RBACManager.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_middleware_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Module_Middleware