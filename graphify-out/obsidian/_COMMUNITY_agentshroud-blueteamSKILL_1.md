---
type: community
cohesion: 0.08
members: 40
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.08 - loosely connected
**Members:** 40 nodes

## Members
- [[dot-__init__()_108]] - code - gateway/security/canary_tripwire.py
- [[dot-_check_encoded()]] - code - gateway/security/canary_tripwire.py
- [[dot-_check_plain()]] - code - gateway/security/canary_tripwire.py
- [[dot-_normalize()]] - code - gateway/security/canary_tripwire.py
- [[dot-_record()]] - code - gateway/security/canary_tripwire.py
- [[dot-detection_count()]] - code - gateway/security/canary_tripwire.py
- [[dot-register_canary()]] - code - gateway/security/canary_tripwire.py
- [[dot-scan()_3]] - code - gateway/security/canary_tripwire.py
- [[dot-scan_response()_2]] - code - gateway/security/canary_tripwire.py
- [[dot-setup_method()_24]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_case_insensitive()_2]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_custom_config()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_empty_input()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_no_canaries()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_normal_content_passes()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_plain_canary_detected()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_reversed_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_rot13_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_blocks_on_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_no_block_when_block_disabled()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_passes_clean_text()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_records_scan_method()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_returns_tripwire_response()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_spaced_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_url_encoded_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_zero_width_bypass()]] - code - gateway/tests/test_canary_tripwire.py
- [[Bridge result returned by scan_response() for pipeline compatibility.]] - rationale - gateway/security/canary_tripwire.py
- [[CanaryConfig_1]] - code - gateway/security/canary_tripwire.py
- [[CanaryResult_1]] - code - gateway/security/canary_tripwire.py
- [[CanaryTripwire]] - code - gateway/security/canary_tripwire.py
- [[Pipeline-compatible bridge scan response text and return TripwireResponse.]] - rationale - gateway/security/canary_tripwire.py
- [[Register a new canary value at runtime for dynamic tripwire testing.]] - rationale - gateway/security/canary_tripwire.py
- [[TestCanaryTripwire]] - code - gateway/tests/test_canary_tripwire.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]

## Top bridge nodes
- [[CanaryTripwire]] - degree 34, connects to 4 communities
- [[canary_tripwire.py]] - degree 6, connects to 1 community
