---
type: community
members: 60
---

# OutputCanary

**Members:** 60 nodes

## Members
- [[dot-__init__()_93]] - code - gateway/security/output_canary.py
- [[dot-_create_detection_patterns()]] - code - gateway/security/output_canary.py
- [[dot-_create_invisible_canary()]] - code - gateway/security/output_canary.py
- [[dot-_scan_for_canary()]] - code - gateway/security/output_canary.py
- [[dot-check_response()_1]] - code - gateway/security/output_canary.py
- [[dot-cleanup_expired_canaries()]] - code - gateway/security/output_canary.py
- [[dot-generate_canary()]] - code - gateway/security/output_canary.py
- [[dot-get_status()]] - code - gateway/security/output_canary.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_output_canary.py
- [[dot-test_canary_cleanup()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_canary_generation_per_session()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_clean_response_passes()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_detection_patterns_creation()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_different_sessions_get_different_canaries()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_incident_logging()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_invisible_canary_creation()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_leaked_canary_detected_in_response()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_output_canary_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_partial_canary_match_handling()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_session_without_canary_returns_safe_result()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_status_reporting()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_unicode_normalization_resistance()]] - code - gateway/tests/test_output_canary.py
- [[dot-test_zero_width_character_detection()]] - code - gateway/tests/test_output_canary.py
- [[Any_32]] - code
- [[CanaryConfig]] - code - gateway/security/output_canary.py
- [[CanaryResult_1]] - code - gateway/security/output_canary.py
- [[Check if response contains the session's canary (prompt leakage detected).…]] - rationale - gateway/security/output_canary.py
- [[Clean up old canaries to prevent memory leaks. Args max_age_seconds Maximum…]] - rationale - gateway/security/output_canary.py
- [[Configuration for the Output Canary System.]] - rationale - gateway/security/output_canary.py
- [[Create an invisible version of the canary using various techniques. Args…]] - rationale - gateway/security/output_canary.py
- [[Create regex patterns to detect the canary in responses. Args base_canary…]] - rationale - gateway/security/output_canary.py
- [[Generate and store a canary for this session. Args session_id Unique session…]] - rationale - gateway/security/output_canary.py
- [[Initialize the Output Canary System. Args config Optional configuration. Uses…]] - rationale - gateway/security/output_canary.py
- [[Main Output Canary System for detecting prompt leakage. This system generates…]] - rationale - gateway/security/output_canary.py
- [[Output Canary System for AgentShroud Gateway Detects prompt leakage by…]] - rationale - gateway/security/output_canary.py
- [[OutputCanary]] - code - gateway/security/output_canary.py
- [[Pattern_3]] - code
- [[Result of checking a response for canary presence.]] - rationale - gateway/security/output_canary.py
- [[Return canary status for dashboard. Args session_id Session identifier…]] - rationale - gateway/security/output_canary.py
- [[Scan response text for a specific canary. Args session_id Session identifier…]] - rationale - gateway/security/output_canary.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_output_canary.py
- [[Test canary status reporting for dashboard.]] - rationale - gateway/tests/test_output_canary.py
- [[Test cases for the Output Canary System.]] - rationale - gateway/tests/test_output_canary.py
- [[Test cleanup of expired canaries.]] - rationale - gateway/tests/test_output_canary.py
- [[Test detection of canaries with zero-width characters.]] - rationale - gateway/tests/test_output_canary.py
- [[Test handling of partial canary matches.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that canaries work with different Unicode representations.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that clean responses pass without detection.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that detection patterns are created correctly.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that different sessions get different canaries.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that incidents are logged when enabled.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that invisible canaries are created properly.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that leaked canaries are detected in responses.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that sessions without canaries return safe results.]] - rationale - gateway/tests/test_output_canary.py
- [[Test that unique canaries are generated per session.]] - rationale - gateway/tests/test_output_canary.py
- [[TestOutputCanary]] - code - gateway/tests/test_output_canary.py
- [[Tests for the Output Canary System.]] - rationale - gateway/tests/test_output_canary.py
- [[output_canary.py]] - code - gateway/security/output_canary.py
- [[patch_3]] - code
- [[test_output_canary.py]] - code - gateway/tests/test_output_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutputCanary
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_PathIsolationManager]]

## Top bridge nodes
- [[OutputCanary]] - degree 21, connects to 4 communities
- [[output_canary.py]] - degree 7, connects to 2 communities
- [[dot-test_output_canary_instantiates()]] - degree 2, connects to 1 community
