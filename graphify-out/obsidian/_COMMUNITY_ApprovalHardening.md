---
type: community
members: 107
---

# ApprovalHardening

**Members:** 107 nodes

## Members
- [[dot-__init__()_108]] - code - gateway/security/approval_hardening.py
- [[dot-_check_description_parameter_mismatch()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_misleading_language()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_parameter_obfuscation()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_repeat_request_patterns()]] - code - gateway/security/approval_hardening.py
- [[dot-_cleanup_old_denied_requests()]] - code - gateway/security/approval_hardening.py
- [[dot-_create_parameter_fingerprint()]] - code - gateway/security/approval_hardening.py
- [[dot-_format_parameters_with_highlighting()]] - code - gateway/security/approval_hardening.py
- [[dot-_normalize_description()]] - code - gateway/security/approval_hardening.py
- [[dot-analyze_request()]] - code - gateway/security/approval_hardening.py
- [[dot-config()_3]] - code - gateway/tests/test_approval_hardening.py
- [[dot-format_hardened_message()]] - code - gateway/security/approval_hardening.py
- [[dot-get_stats()_11]] - code - gateway/security/approval_hardening.py
- [[dot-hardening()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-is_request_in_cooldown()]] - code - gateway/security/approval_hardening.py
- [[dot-record_denied_request()]] - code - gateway/security/approval_hardening.py
- [[dot-test_basic_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_cleanup_old_denied_requests()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_cooldown_disabled_when_feature_disabled()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_cooldown_period_enforcement()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_custom_config()_1]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_authority_claims()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_benign_request()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_destructive_command_not_indicated()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_disabled()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_downplaying_language()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_deception_detection_misleading_description()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_default_config()_4]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_default_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_denied_request_creation()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_different_requests_not_in_cooldown()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_basic()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_with_normalization()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_with_security_concerns()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_parameters_with_highlighting()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_get_stats()_1]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_initialization()_4]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_normalize_description_handles_empty()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_normalize_description_removes_misleading_phrases()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_parameter_fingerprinting_consistency()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_parameter_fingerprinting_different_params()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_parameter_obfuscation_detection_base64()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_parameter_obfuscation_detection_hex()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_parameter_obfuscation_detection_url()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_repeat_request_pattern_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[Analyze an approval request for potential deception or social engineering.]] - rationale - gateway/security/approval_hardening.py
- [[Anti-social-engineering hardening for approval queue.]] - rationale - gateway/security/approval_hardening.py
- [[Any_37]] - code - gateway/security/approval_hardening.py
- [[ApprovalHardening]] - code - gateway/security/approval_hardening.py
- [[ApprovalHardeningConfig]] - code - gateway/security/approval_hardening.py
- [[Check for misleading language patterns in description.]] - rationale - gateway/security/approval_hardening.py
- [[Check for mismatch between description and actual parameters.]] - rationale - gateway/security/approval_hardening.py
- [[Check for obfuscated or encoded parameters.]] - rationale - gateway/security/approval_hardening.py
- [[Check for patterns indicating repeat request attempts.]] - rationale - gateway/security/approval_hardening.py
- [[Check if a similar request is still in cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Clean up old denied requests beyond cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Configuration for approval queue hardening.]] - rationale - gateway/security/approval_hardening.py
- [[Create a fingerprint for request parameters.]] - rationale - gateway/security/approval_hardening.py
- [[Create approval hardening instance for testing.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Create test configuration.]] - rationale - gateway/tests/test_approval_hardening.py
- [[DeceptionDetection]] - code - gateway/security/approval_hardening.py
- [[DeniedRequest]] - code - gateway/security/approval_hardening.py
- [[Format an approval message with hardening measures applied.]] - rationale - gateway/security/approval_hardening.py
- [[Format parameters with risk highlighting.]] - rationale - gateway/security/approval_hardening.py
- [[Get statistics about approval hardening.]] - rationale - gateway/security/approval_hardening.py
- [[Normalize description by removing misleading language.]] - rationale - gateway/security/approval_hardening.py
- [[Record a denied request for cooldown tracking.]] - rationale - gateway/security/approval_hardening.py
- [[Record of a denied approval request.]] - rationale - gateway/security/approval_hardening.py
- [[Result of deception detection analysis.]] - rationale - gateway/security/approval_hardening.py
- [[Test DeceptionDetection dataclass.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test DeniedRequest dataclass.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test approval hardening configuration.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test approval hardening functionality.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test basic detection result creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test basic hardened message formatting.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test cleanup of old denied requests.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test cooldown is disabled when feature is disabled.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test cooldown period enforcement for denied requests.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test custom configuration values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test deception detection with legitimate request.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test denied request creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test description normalization removes misleading language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of URL-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of authoritylegitimacy claims.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of base64-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of destructive commands not indicated in description.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of downplaying language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of misleading descriptions.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of repeat request patterns.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection with default values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test getting hardening statistics.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting when description is normalized.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting with security concerns.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardening initialization.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test normalization handles empty descriptions.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test parameter formatting with risk highlighting.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that deception detection can be disabled.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that different parameters create different fingerprints.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that different requests are not affected by cooldown.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that parameter fingerprinting is consistent.]] - rationale - gateway/tests/test_approval_hardening.py
- [[TestApprovalHardening]] - code - gateway/tests/test_approval_hardening.py
- [[TestApprovalHardeningConfig]] - code - gateway/tests/test_approval_hardening.py
- [[TestDeceptionDetection]] - code - gateway/tests/test_approval_hardening.py
- [[TestDeniedRequest]] - code - gateway/tests/test_approval_hardening.py
- [[approval_hardening.py]] - code - gateway/security/approval_hardening.py
- [[test_approval_hardening.py]] - code - gateway/tests/test_approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalHardening
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]

## Top bridge nodes
- [[ApprovalHardening]] - degree 38, connects to 2 communities
- [[ApprovalHardeningConfig]] - degree 26, connects to 2 communities
- [[approval_hardening.py]] - degree 6, connects to 1 community
