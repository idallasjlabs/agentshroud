---
type: community
cohesion: 0.09
members: 27
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.09 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-__init__()_120]] - code - gateway/security/canary_tripwire.py
- [[dot-setup_method()_22]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_case_insensitive()_3]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_custom_config()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_canary_tripwire.py
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
- [[TestCanaryTripwire]] - code - gateway/tests/test_canary_tripwire.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_InjectionAction]]

## Top bridge nodes
- [[TripwireResponse]] - degree 5, connects to 2 communities
- [[TestCanaryTripwire]] - degree 25, connects to 1 community
- [[CanaryConfig_1]] - degree 7, connects to 1 community
- [[test_canary_tripwire.py]] - degree 4, connects to 1 community
- [[dot-test_custom_config()_1]] - degree 3, connects to 1 community
