---
source_file: "gateway/security/alert_dispatcher.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L35"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# AlertDispatcher

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_163]] - `method` [EXTRACTED]
- [[dot-_format_alert_message()]] - `method` [EXTRACTED]
- [[dot-_is_duplicate()]] - `method` [EXTRACTED]
- [[dot-_is_rate_limited()]] - `method` [EXTRACTED]
- [[dot-_log_alert()]] - `method` [EXTRACTED]
- [[dot-_send_notification()]] - `method` [EXTRACTED]
- [[dot-cleanup_seen()]] - `method` [EXTRACTED]
- [[dot-dispatch()]] - `method` [EXTRACTED]
- [[dot-get_digest()]] - `method` [EXTRACTED]
- [[dot-get_stats()_1]] - `method` [EXTRACTED]
- [[dot-test_alert_dedup()]] - `calls` [EXTRACTED]
- [[dot-test_alert_dispatcher_concurrent_dispatch()]] - `calls` [INFERRED]
- [[dot-test_alert_dispatcher_init()]] - `calls` [EXTRACTED]
- [[dot-test_alert_dispatcher_write()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[CronStateMonitor]] - `calls` [INFERRED]
- [[Dispatches security alerts with dedup and rate limiting.]] - `rationale_for` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[Kaizen Fix AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14week) at ERROR level]] - `rationale_for` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Path]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[alert_dispatcher.py_2]] - `contains` [EXTRACTED]
- [[dispatcher()]] - `calls` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run_canary()_1]] - `conceptually_related_to` [INFERRED]
- [[test_alert_dispatcher_retry.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Alert_Dispatcher__RBAC_Reliability