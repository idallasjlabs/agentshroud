---
type: community
members: 49
---

# ApprovalHardening

**Members:** 49 nodes

## Members
- [[dot-_check_description_parameter_mismatch()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_misleading_language()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_parameter_obfuscation()]] - code - gateway/security/approval_hardening.py
- [[dot-_check_repeat_request_patterns()]] - code - gateway/security/approval_hardening.py
- [[dot-_cleanup_old_denied_requests()]] - code - gateway/security/approval_hardening.py
- [[dot-_create_parameter_fingerprint()]] - code - gateway/security/approval_hardening.py
- [[dot-_format_parameters_with_highlighting()]] - code - gateway/security/approval_hardening.py
- [[dot-_normalize_description()]] - code - gateway/security/approval_hardening.py
- [[dot-analyze_request()]] - code - gateway/security/approval_hardening.py
- [[dot-format_hardened_message()]] - code - gateway/security/approval_hardening.py
- [[dot-get_stats()_2]] - code - gateway/security/approval_hardening.py
- [[dot-is_request_in_cooldown()]] - code - gateway/security/approval_hardening.py
- [[dot-record_denied_request()]] - code - gateway/security/approval_hardening.py
- [[dot-test_basic_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_custom_config()_1]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_default_config()_3]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_default_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_denied_request_creation()]] - code - gateway/tests/test_approval_hardening.py
- [[Analyze an approval request for potential deception or social engineering.]] - rationale - gateway/security/approval_hardening.py
- [[Any_11]] - code - gateway/security/approval_hardening.py
- [[Check for misleading language patterns in description.]] - rationale - gateway/security/approval_hardening.py
- [[Check for mismatch between description and actual parameters.]] - rationale - gateway/security/approval_hardening.py
- [[Check for obfuscated or encoded parameters.]] - rationale - gateway/security/approval_hardening.py
- [[Check for patterns indicating repeat request attempts.]] - rationale - gateway/security/approval_hardening.py
- [[Check if a similar request is still in cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Clean up old denied requests beyond cooldown period.]] - rationale - gateway/security/approval_hardening.py
- [[Create a fingerprint for request parameters.]] - rationale - gateway/security/approval_hardening.py
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
- [[Test basic detection result creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test custom configuration values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test denied request creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection with default values.]] - rationale - gateway/tests/test_approval_hardening.py
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
- 25 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_ApprovalHardening (2)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]

## Top bridge nodes
- [[test_approval_hardening.py]] - degree 8, connects to 2 communities
- [[approval_hardening.py]] - degree 6, connects to 2 communities
- [[DeceptionDetection]] - degree 18, connects to 1 community
- [[dot-analyze_request()]] - degree 9, connects to 1 community
- [[DeniedRequest]] - degree 9, connects to 1 community
