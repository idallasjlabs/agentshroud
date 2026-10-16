---
type: community
cohesion: 0.38
members: 10
---

# WebContentScanner

**Cohesion:** 0.38 - loosely connected
**Members:** 10 nodes

## Members
- [[AgentTarget]] - code - gateway/ingest_api/routes/forward.py
- [[Resolve the outbound trust level for `request`, shared by the blocking     and s]] - rationale - gateway/ingest_api/routes/forward.py
- [[_request()]] - code - gateway/tests/test_forward_stream.py
- [[_resolve_user_trust_level()]] - code - gateway/ingest_api/routes/forward.py
- [[_target()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_maps_trust_score_to_tier()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_manager_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_non_owner_user_id_does_not_upgrade()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_owner_user_id_upgrades_to_full()]] - code - gateway/tests/test_forward_stream.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebContentScanner
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_forward_stream.py_1]]
- 4 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_AgentTarget_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[_resolve_user_trust_level()]] - degree 12, connects to 2 communities
- [[_request()]] - degree 7, connects to 2 communities
- [[_target()]] - degree 7, connects to 2 communities
- [[test_resolve_trust_level_maps_trust_score_to_tier()]] - degree 4, connects to 1 community
- [[test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted()]] - degree 4, connects to 1 community
