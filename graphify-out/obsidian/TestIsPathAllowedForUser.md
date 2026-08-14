---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "code"
community: "Approval Queue Tests"
location: "L770"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Queue_Tests
---

# TestIsPathAllowedForUser

## Connections
- [[.test_default_deny()]] - `method` [EXTRACTED]
- [[.test_exception_fails_secure()]] - `method` [EXTRACTED]
- [[.test_no_session_manager_denied()]] - `method` [EXTRACTED]
- [[.test_other_user_under_users_base_denied()]] - `method` [EXTRACTED]
- [[.test_own_workspace_allowed()]] - `method` [EXTRACTED]
- [[.test_owner_bypass()_3]] - `method` [EXTRACTED]
- [[.test_users_heuristic_denied()]] - `method` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_middleware_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Queue_Tests