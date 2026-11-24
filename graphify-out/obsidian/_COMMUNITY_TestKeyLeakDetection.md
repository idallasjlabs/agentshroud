---
type: community
members: 9
---

# TestKeyLeakDetection

**Members:** 9 nodes

## Members
- [[dot-_make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestKeyLeakDetection
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_KeyVault]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_KeyLeakDetector]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TrustManager]]

## Top bridge nodes
- [[TestKeyLeakDetection_1]] - degree 13, connects to 5 communities
- [[dot-_make_vault_pipeline()]] - degree 10, connects to 4 communities
- [[dot-test_detector_failure_fails_closed_for_non_owner()]] - degree 4, connects to 1 community
- [[dot-test_clean_response_passes_unchanged()_1]] - degree 3, connects to 1 community
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - degree 3, connects to 1 community
