---
source_file: "gateway/security/approval_hardening.py"
type: "code"
community: "ApprovalHardening"
location: "L111"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalHardening
---

# ApprovalHardening

## Connections
- [[dot-__init__()_152]] - `calls` [EXTRACTED]
- [[dot-__init__()_108]] - `method` [EXTRACTED]
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
- [[dot-get_stats()_11]] - `method` [EXTRACTED]
- [[dot-hardening()]] - `calls` [EXTRACTED]
- [[dot-is_request_in_cooldown()]] - `method` [EXTRACTED]
- [[dot-record_denied_request()]] - `method` [EXTRACTED]
- [[dot-test_cooldown_disabled_when_feature_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_deception_detection_disabled()]] - `calls` [EXTRACTED]
- [[Action_3]] - `uses` [INFERRED]
- [[Anti-social-engineering hardening for approval queue.]] - `rationale_for` [EXTRACTED]
- [[Any_2]] - `uses` [INFERRED]
- [[ContextGuard]] - `semantically_similar_to` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_2]] - `uses` [INFERRED]
- [[Resource_2]] - `uses` [INFERRED]
- [[TestApprovalHardening]] - `uses` [INFERRED]
- [[TestApprovalHardeningConfig]] - `uses` [INFERRED]
- [[TestDeceptionDetection]] - `uses` [INFERRED]
- [[TestDeniedRequest]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[approval_hardening.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py_1]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_approval_hardening.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalHardening
