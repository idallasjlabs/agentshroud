---
type: community
members: 5
---

# GSDL-715 (silent regression incident)

**Members:** 5 nodes

## Members
- [[dot-test_store_nonzero_returncode_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_rejects_malformed_reference()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_success()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_timeout_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStoreIn1Password]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GSDL-715_silent_regression_incident
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_A2AMethod]]
- 2 edges to [[_COMMUNITY_AgentShroud Documentation]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]

## Top bridge nodes
- [[TestStoreIn1Password]] - degree 10, connects to 3 communities
