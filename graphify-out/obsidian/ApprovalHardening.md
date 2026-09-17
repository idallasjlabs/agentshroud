---
source_file: "gateway/security/approval_hardening.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L111"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# ApprovalHardening

## Connections
- [[dot-__init__()_12]] - `calls` [EXTRACTED]
- [[dot-__init__()_13]] - `method` [EXTRACTED]
- [[dot-_check_description_parameter_mismatch()]] - `method` [EXTRACTED]
- [[dot-_check_misleading_language()]] - `method` [EXTRACTED]
- [[dot-_check_parameter_obfuscation()]] - `method` [EXTRACTED]
- [[dot-_check_repeat_request_patterns()]] - `method` [EXTRACTED]
- [[dot-_cleanup_old_denied_requests()]] - `method` [EXTRACTED]
- [[dot-_create_parameter_fingerprint()]] - `method` [EXTRACTED]
- [[dot-_format_parameters_with_highlighting()]] - `method` [EXTRACTED]
- [[dot-_normalize_description()]] - `method` [EXTRACTED]
- [[dot-analyze_request()]] - `method` [EXTRACTED]
- [[dot-format_hardened_message()]] - `method` [EXTRACTED]
- [[dot-get_stats()_2]] - `method` [EXTRACTED]
- [[dot-hardening()]] - `calls` [EXTRACTED]
- [[dot-is_request_in_cooldown()]] - `method` [EXTRACTED]
- [[dot-record_denied_request()]] - `method` [EXTRACTED]
- [[dot-test_cooldown_disabled_when_feature_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_deception_detection_disabled()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Anti-social-engineering hardening for approval queue.]] - `rationale_for` [EXTRACTED]
- [[Any_2]] - `uses` [INFERRED]
- [[ContextGuard]] - `semantically_similar_to` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestApprovalHardening]] - `uses` [INFERRED]
- [[TestApprovalHardeningConfig]] - `uses` [INFERRED]
- [[TestDeceptionDetection]] - `uses` [INFERRED]
- [[TestDeniedRequest]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[approval_hardening.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_approval_hardening.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Alert_Dispatcher__RBAC_Reliability