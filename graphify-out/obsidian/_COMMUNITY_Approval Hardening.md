---
type: community
cohesion: 0.03
members: 108
---

# Approval Hardening

**Cohesion:** 0.03 - loosely connected
**Members:** 108 nodes

## Members
- [[.__init__()_43]] - code - gateway/security/approval_hardening.py
- [[._check_description_parameter_mismatch()]] - code - gateway/security/approval_hardening.py
- [[._check_misleading_language()]] - code - gateway/security/approval_hardening.py
- [[._check_parameter_obfuscation()]] - code - gateway/security/approval_hardening.py
- [[._check_repeat_request_patterns()]] - code - gateway/security/approval_hardening.py
- [[._cleanup_old_denied_requests()]] - code - gateway/security/approval_hardening.py
- [[._create_parameter_fingerprint()]] - code - gateway/security/approval_hardening.py
- [[._format_parameters_with_highlighting()]] - code - gateway/security/approval_hardening.py
- [[._normalize_description()]] - code - gateway/security/approval_hardening.py
- [[.analyze_request()]] - code - gateway/security/approval_hardening.py
- [[.config()]] - code - gateway/tests/test_approval_hardening.py
- [[.format_hardened_message()]] - code - gateway/security/approval_hardening.py
- [[.get_stats()_13]] - code - gateway/security/approval_hardening.py
- [[.hardening()]] - code - gateway/tests/test_approval_hardening.py
- [[.is_request_in_cooldown()]] - code - gateway/security/approval_hardening.py
- [[.record_denied_request()]] - code - gateway/security/approval_hardening.py
- [[.test_basic_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_cleanup_old_denied_requests()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_cooldown_disabled_when_feature_disabled()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_cooldown_period_enforcement()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_custom_config()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_authority_claims()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_benign_request()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_destructive_command_not_indicated()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_disabled()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_downplaying_language()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_misleading_description()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_default_config()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_default_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_denied_request_creation()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_different_requests_not_in_cooldown()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_basic()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_with_normalization()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_with_security_concerns()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_parameters_with_highlighting()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_get_stats()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_initialization()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_normalize_description_handles_empty()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_normalize_description_removes_misleading_phrases()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_fingerprinting_consistency()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_fingerprinting_different_params()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_base64()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_hex()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_url()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_repeat_request_pattern_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[Analyze an approval request for potential deception or social engineering.]] - rationale - gateway/security/approval_hardening.py
- [[Anti-social-engineering hardening for approval queue.]] - rationale - gateway/security/approval_hardening.py
- [[Any_28]] - code - gateway/security/approval_hardening.py
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
- [[Test default configuration values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test denied request creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test description normalization removes misleading language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of URL-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of authoritylegitimacy claims.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of base64-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of destructive commands not indicated in description.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of downplaying language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of hex-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
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
TABLE source_file, type FROM #community/Approval_Hardening
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[ApprovalHardening]] - degree 36, connects to 1 community
- [[ApprovalHardeningConfig]] - degree 25, connects to 1 community
