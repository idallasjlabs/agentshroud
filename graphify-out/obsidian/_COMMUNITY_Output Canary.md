---
type: community
cohesion: 0.05
members: 45
---

# Output Canary

**Cohesion:** 0.05 - loosely connected
**Members:** 45 nodes

## Members
- [[.__init__()_104]] - code - gateway/security/output_canary.py
- [[._scan_for_canary()]] - code - gateway/security/output_canary.py
- [[.check_response()]] - code - gateway/security/output_canary.py
- [[.get_status()_1]] - code - gateway/security/output_canary.py
- [[.setup_method()_19]] - code - gateway/tests/test_output_canary.py
- [[.test_canary_cleanup()]] - code - gateway/tests/test_output_canary.py
- [[.test_canary_generation_per_session()]] - code - gateway/tests/test_output_canary.py
- [[.test_clean_response_passes()]] - code - gateway/tests/test_output_canary.py
- [[.test_detection_patterns_creation()]] - code - gateway/tests/test_output_canary.py
- [[.test_different_sessions_get_different_canaries()]] - code - gateway/tests/test_output_canary.py
- [[.test_incident_logging()]] - code - gateway/tests/test_output_canary.py
- [[.test_invisible_canary_creation()]] - code - gateway/tests/test_output_canary.py
- [[.test_leaked_canary_detected_in_response()]] - code - gateway/tests/test_output_canary.py
- [[.test_partial_canary_match_handling()]] - code - gateway/tests/test_output_canary.py
- [[.test_session_without_canary_returns_safe_result()]] - code - gateway/tests/test_output_canary.py
- [[.test_status_reporting()_1]] - code - gateway/tests/test_output_canary.py
- [[.test_unicode_normalization_resistance()]] - code - gateway/tests/test_output_canary.py
- [[.test_zero_width_character_detection()]] - code - gateway/tests/test_output_canary.py
- [[Any_53]] - code - gateway/security/output_canary.py
- [[CanaryConfig_1]] - code - gateway/security/output_canary.py
- [[CanaryResult_2]] - code - gateway/security/output_canary.py
- [[Check if response contains the session's canary (prompt leakage detected).]] - rationale - gateway/security/output_canary.py
- [[Configuration for the Output Canary System.]] - rationale - gateway/security/output_canary.py
- [[Initialize the Output Canary System.          Args             config Optional]] - rationale - gateway/security/output_canary.py
- [[Result of checking a response for canary presence.]] - rationale - gateway/security/output_canary.py
- [[Return canary status for dashboard.          Args             session_id Sessi]] - rationale - gateway/security/output_canary.py
- [[Scan response text for a specific canary.          Args             session_id]] - rationale - gateway/security/output_canary.py
- [[Set up test fixtures._1]] - rationale - gateway/tests/test_output_canary.py
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
- [[output_canary.py]] - code - gateway/security/output_canary.py
- [[test_output_canary.py]] - code - gateway/tests/test_output_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Output_Canary
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]

## Top bridge nodes
- [[TestOutputCanary]] - degree 18, connects to 1 community
- [[._scan_for_canary()]] - degree 5, connects to 1 community
- [[.check_response()]] - degree 4, connects to 1 community
- [[.setup_method()_19]] - degree 4, connects to 1 community
- [[.test_incident_logging()]] - degree 4, connects to 1 community