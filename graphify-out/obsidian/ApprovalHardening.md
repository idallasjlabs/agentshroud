---
source_file: "gateway/security/approval_hardening.py"
type: "code"
community: "Memory Lifecycle & Egress Filtering"
location: "L111"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Memory_Lifecycle__Egress_Filtering
---

# ApprovalHardening

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[.__init__()_54]] - `method` [EXTRACTED]
- [[._check_description_parameter_mismatch()]] - `method` [EXTRACTED]
- [[._check_misleading_language()]] - `method` [EXTRACTED]
- [[._check_parameter_obfuscation()]] - `method` [EXTRACTED]
- [[._check_repeat_request_patterns()]] - `method` [EXTRACTED]
- [[._cleanup_old_denied_requests()]] - `method` [EXTRACTED]
- [[._create_parameter_fingerprint()]] - `method` [EXTRACTED]
- [[._format_parameters_with_highlighting()]] - `method` [EXTRACTED]
- [[._normalize_description()]] - `method` [EXTRACTED]
- [[.analyze_request()]] - `method` [EXTRACTED]
- [[.format_hardened_message()]] - `method` [EXTRACTED]
- [[.get_stats()_13]] - `method` [EXTRACTED]
- [[.hardening()]] - `calls` [EXTRACTED]
- [[.is_request_in_cooldown()]] - `method` [EXTRACTED]
- [[.record_denied_request()]] - `method` [EXTRACTED]
- [[.test_cooldown_disabled_when_feature_disabled()]] - `calls` [EXTRACTED]
- [[.test_deception_detection_disabled()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Anti-social-engineering hardening for approval queue.]] - `rationale_for` [EXTRACTED]
- [[Any_8]] - `uses` [INFERRED]
- [[ContextGuard]] - `semantically_similar_to` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestApprovalHardening]] - `uses` [INFERRED]
- [[TestApprovalHardeningConfig]] - `uses` [INFERRED]
- [[TestDeceptionDetection]] - `uses` [INFERRED]
- [[TestDeniedRequest]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[approval_hardening.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[test_approval_hardening.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Memory_Lifecycle__Egress_Filtering