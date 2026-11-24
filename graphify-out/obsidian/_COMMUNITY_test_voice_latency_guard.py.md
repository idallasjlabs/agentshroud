---
type: community
members: 41
---

# test_voice_latency_guard.py

**Members:** 41 nodes

## Members
- [[A read-timeout (worst-case latency) is still recorded, then falls back.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn exceeding the soft threshold is flagged as an outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn under the soft threshold is recorded as a non-outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Build the ``metadata`` dict attached to a voice ``forward`` request. Default…]] - rationale - voice_gateway/server.py
- [[DEFAULT OFF forwardstream body carries NO metadata key — byte-for-byte…]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[DEFAULT OFF no_memory=False → empty metadata (request unchanged).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Emit a structured per-turn latency record for a voice ``forward`` call.…]] - rationale - voice_gateway/server.py
- [[Exactly at the threshold is NOT an outlier (strict , not =).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Mock httpx.Response usable as the yield value of a mocked AsyncClient.stream()…]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Normal (sub-threshold) turns log at INFO, not WARNING.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON forwardstream body carries metadata={no_memory True}.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON no_memory=True → {no_memory True} ephemeral tag.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Outliers log at WARNING; normal turns do not.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[SCRUM-56 — Hermes voice-turn latency guard. Covers the two config-gated…]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[The module-level default flag is OFF unless VG_VOICE_NO_MEMORY is set.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[When soft_threshold_s is omitted it is read from the module config at call time.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_aiter_lines()_3]] - code - gateway/tests/test_voice_latency_guard.py
- [[_call_agent_stream emits a latency record on the success path.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_mock_stream_resp()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_record_turn_latency()]] - code - voice_gateway/server.py
- [[_sse_body()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_voice_forward_metadata()]] - code - voice_gateway/server.py
- [[asyncio_77]] - code
- [[mock_stream()_25]] - code - gateway/tests/test_voice_latency_guard.py
- [[mock_stream()_26]] - code - gateway/tests/test_voice_latency_guard.py
- [[mock_stream()_27]] - code - gateway/tests/test_voice_latency_guard.py
- [[mock_stream()_28]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_default_body_has_no_metadata()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_read_timeout()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_success()]] - code - gateway/tests/test_voice_latency_guard.py
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
TABLE source_file, type FROM #community/test_voice_latency_guardpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 3 edges to [[_COMMUNITY_server.py]]

## Top bridge nodes
- [[test_voice_latency_guard.py]] - degree 20, connects to 2 communities
- [[_record_turn_latency()]] - degree 10, connects to 2 communities
- [[_voice_forward_metadata()]] - degree 7, connects to 2 communities
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - degree 6, connects to 1 community
- [[test_call_agent_records_latency_on_read_timeout()]] - degree 6, connects to 1 community
