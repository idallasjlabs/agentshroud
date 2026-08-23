---
type: community
cohesion: 0.09
members: 28
---

# Canary Tripwire

**Cohesion:** 0.09 - loosely connected
**Members:** 28 nodes

## Members
- [[.__init__()_60]] - code - gateway/security/canary_tripwire.py
- [[.setup_method()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_case_insensitive()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_custom_config()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_empty_input()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_no_canaries()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_normal_content_passes()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_plain_canary_detected()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_reversed_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_rot13_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_blocks_on_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_no_block_when_block_disabled()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_passes_clean_text()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_records_scan_method()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_returns_tripwire_response()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_spaced_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_url_encoded_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_zero_width_bypass()]] - code - gateway/tests/test_canary_tripwire.py
- [[Bridge result returned by scan_response() for pipeline compatibility.]] - rationale - gateway/security/canary_tripwire.py
- [[CanaryConfig]] - code - gateway/security/canary_tripwire.py
- [[TestCanaryTripwire]] - code - gateway/tests/test_canary_tripwire.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Canary_Tripwire
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]

## Top bridge nodes
- [[canary_tripwire.py]] - degree 6, connects to 2 communities
- [[TestCanaryTripwire]] - degree 25, connects to 1 community
- [[TripwireResponse]] - degree 5, connects to 1 community
- [[test_canary_tripwire.py]] - degree 4, connects to 1 community
- [[.test_custom_config()_1]] - degree 3, connects to 1 community