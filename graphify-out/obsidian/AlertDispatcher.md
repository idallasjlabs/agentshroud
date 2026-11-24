---
source_file: "gateway/security/alert_dispatcher.py"
type: "code"
community: "AlertDispatcher"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertDispatcher
---

# AlertDispatcher

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_169]] - `method` [EXTRACTED]
- [[dot-_format_alert_message()]] - `method` [EXTRACTED]
- [[dot-_is_duplicate()]] - `method` [EXTRACTED]
- [[dot-_is_rate_limited()]] - `method` [EXTRACTED]
- [[dot-_log_alert()]] - `method` [EXTRACTED]
- [[dot-_make_dispatcher()]] - `calls` [EXTRACTED]
- [[dot-_send_notification()]] - `method` [EXTRACTED]
- [[dot-cleanup_seen()]] - `method` [EXTRACTED]
- [[dot-dispatch()]] - `method` [EXTRACTED]
- [[dot-get_digest()]] - `method` [EXTRACTED]
- [[dot-get_stats()_11]] - `method` [EXTRACTED]
- [[dot-test_alert_dedup()]] - `calls` [EXTRACTED]
- [[dot-test_alert_dispatcher_concurrent_dispatch()]] - `calls` [INFERRED]
- [[dot-test_alert_dispatcher_init()]] - `calls` [EXTRACTED]
- [[dot-test_alert_dispatcher_write()]] - `calls` [EXTRACTED]
- [[Dispatches security alerts with dedup and rate limiting.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestAlertDispatcher]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[alert_dispatcher.py]] - `contains` [EXTRACTED]
- [[dispatcher()_1]] - `uses` [INFERRED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[test_alert_dispatcher_retry.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_toolchain.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertDispatcher
