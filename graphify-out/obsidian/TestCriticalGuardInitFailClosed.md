---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "code"
community: "Community 1003"
location: "L1026"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_1003
---

# TestCriticalGuardInitFailClosed

## Connections
- [[.test_context_guard_init_raise_recorded_and_logged()]] - `method` [EXTRACTED]
- [[.test_mm_fixture_without_failed_guards_attr_is_safe()]] - `method` [EXTRACTED]
- [[.test_non_critical_guard_failure_not_recorded()]] - `method` [EXTRACTED]
- [[.test_non_owner_blocked_when_critical_guard_failed()]] - `method` [EXTRACTED]
- [[.test_not_configured_guard_does_not_fail_closed()]] - `method` [EXTRACTED]
- [[.test_owner_exempt_when_critical_guard_failed()]] - `method` [EXTRACTED]
- [[A security-critical guard whose constructor RAISES during __init__ must     NOT]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_middleware_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_1003