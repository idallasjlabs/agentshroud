---
type: community
cohesion: 0.16
members: 20
---

# _process_inbound()

**Cohesion:** 0.16 - loosely connected
**Members:** 20 nodes

## Members
- [[AgentTarget_2]] - code - gateway/ingest_api/routes/forward.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Resolve the outbound trust level for `request`, shared by the blocking     and s]] - rationale - gateway/ingest_api/routes/forward.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[_request()]] - code - gateway/tests/test_forward_stream.py
- [[_resolve_user_trust_level()]] - code - gateway/ingest_api/routes/forward.py
- [[_target()]] - code - gateway/tests/test_forward_stream.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[test_resolve_trust_level_maps_trust_score_to_tier()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_manager_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_non_owner_user_id_does_not_upgrade()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_owner_user_id_upgrades_to_full()]] - code - gateway/tests/test_forward_stream.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_process_inbound
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_forward.py]]
- 8 edges to [[_COMMUNITY_test_forward_stream.py]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 3 edges to [[_COMMUNITY_AgentTarget]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_make_event()]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[_process_inbound()]] - degree 12, connects to 5 communities
- [[forward_content()]] - degree 9, connects to 3 communities
- [[_resolve_user_trust_level()]] - degree 12, connects to 2 communities
- [[forward_content_stream()]] - degree 8, connects to 2 communities
- [[_request()]] - degree 7, connects to 2 communities