---
type: community
cohesion: 0.06
members: 37
---

# TestApprovalHardening

**Cohesion:** 0.06 - loosely connected
**Members:** 37 nodes

## Members
- [[.config()_3]] - code - gateway/tests/test_approval_hardening.py
- [[.hardening()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_cleanup_old_denied_requests()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_authority_claims()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_benign_request()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_destructive_command_not_indicated()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_deception_detection_downplaying_language()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_parameters_with_highlighting()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_get_stats()_1]] - code - gateway/tests/test_approval_hardening.py
- [[.test_initialization()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_normalize_description_handles_empty()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_normalize_description_removes_misleading_phrases()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_fingerprinting_consistency()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_fingerprinting_different_params()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_base64()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_hex()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_parameter_obfuscation_detection_url()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_repeat_request_pattern_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[Create approval hardening instance for testing.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Create test configuration.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test approval hardening functionality.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test cleanup of old denied requests.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test deception detection with legitimate request.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test description normalization removes misleading language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of URL-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of authoritylegitimacy claims.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of base64-encoded parameters.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of destructive commands not indicated in description.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of downplaying language.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection of repeat request patterns.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test getting hardening statistics.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardening initialization.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test normalization handles empty descriptions.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test parameter formatting with risk highlighting.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that different parameters create different fingerprints.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test that parameter fingerprinting is consistent.]] - rationale - gateway/tests/test_approval_hardening.py
- [[TestApprovalHardening]] - code - gateway/tests/test_approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestApprovalHardening
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_DeceptionDetection]]
- 2 edges to [[_COMMUNITY_DeniedRequest]]
- 1 edge to [[_COMMUNITY_.test_cooldown_period_enforcement()]]
- 1 edge to [[_COMMUNITY_.test_deception_detection_misleading_description]]
- 1 edge to [[_COMMUNITY_.test_different_requests_not_in_cooldown()]]

## Top bridge nodes
- [[TestApprovalHardening]] - degree 32, connects to 6 communities
- [[.config()_3]] - degree 3, connects to 1 community
- [[.hardening()]] - degree 3, connects to 1 community