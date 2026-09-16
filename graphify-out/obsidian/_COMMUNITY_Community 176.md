---
type: community
cohesion: 0.07
members: 39
---

# Community 176

**Cohesion:** 0.07 - loosely connected
**Members:** 39 nodes

## Members
- [[A connection-level error (not a statustimeout) also falls back to the trouble-…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A read-timeout (worst-case latency) is still recorded, then falls back.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn exceeding the soft threshold is flagged as an outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn under the soft threshold is recorded as a non-outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Build the ``metadata`` dict attached to a voice ``forward`` request. Default…]] - rationale - voice_gateway/server.py
- [[DEFAULT OFF forwardstream body carries NO metadata key — byte-for-byte legacy]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[DEFAULT OFF no_memory=False → empty metadata (request unchanged).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Emit a structured per-turn latency record for a voice ``forward`` call.…]] - rationale - voice_gateway/server.py
- [[Exactly at the threshold is NOT an outlier (strict , not =).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Mock httpx.Response usable as the yield value of a mocked     AsyncClient.stream]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Normal (sub-threshold) turns log at INFO, not WARNING.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON forwardstream body carries metadata={no_memory True}.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON no_memory=True → {no_memory True} ephemeral tag.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Outliers log at WARNING; normal turns do not.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Route a voice utterance to a proxied agent via the AgentShroud gateway's POST…]] - rationale - voice_gateway/server.py
- [[The module-level default flag is OFF unless VG_VOICE_NO_MEMORY is set.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[When soft_threshold_s is omitted it is read from the module config at call time.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_call_agent_stream emits a latency record on the success path.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_call_agent_stream()]] - code - voice_gateway/server.py
- [[_mock_stream_resp()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_record_turn_latency()]] - code - voice_gateway/server.py
- [[_sse_body()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_voice_forward_metadata()]] - code - voice_gateway/server.py
- [[mock_stream()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_default_body_has_no_metadata()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_read_timeout()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_success()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_stream_generic_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_record_turn_latency_boundary_is_not_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_default_threshold_from_module()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_normal_logs_info()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_normal_not_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_outlier_logs_warning()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_over_threshold_is_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_default_off_is_empty()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_module_default_is_off()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_on_sets_no_memory_tag()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_latency_guard.py]] - code - gateway/tests/test_voice_latency_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_176
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 47]]
- 5 edges to [[_COMMUNITY_Community 122]]
- 2 edges to [[_COMMUNITY_Voice Gateway Test Fixtures]]
- 1 edge to [[_COMMUNITY_Voice Gateway Routing Tests]]

## Top bridge nodes
- [[_call_agent_stream()]] - degree 18, connects to 3 communities
- [[test_call_agent_stream_generic_http_error_falls_back()]] - degree 7, connects to 3 communities
- [[test_voice_latency_guard.py]] - degree 19, connects to 1 community
- [[_record_turn_latency()]] - degree 10, connects to 1 community
- [[_voice_forward_metadata()]] - degree 7, connects to 1 community