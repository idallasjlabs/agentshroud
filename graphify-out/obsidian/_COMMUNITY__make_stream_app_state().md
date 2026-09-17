---
type: community
cohesion: 0.31
members: 13
---

# _make_stream_app_state()

**Cohesion:** 0.31 - loosely connected
**Members:** 13 nodes

## Members
- [[Build a mock app_state whose router streams `sentences_out` as raw     text delt]] - rationale - gateway/tests/test_forward_stream.py
- [[_make_stream_app_state()]] - code - gateway/tests/test_forward_stream.py
- [[_parse_sse_events()]] - code - gateway/tests/test_forward_stream.py
- [[_post_stream()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_503_when_no_pipeline_configured()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_drops_credential_bearing_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_emits_sentence_events_then_done()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_forward_error_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_ledger_failure_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_records_ledger_entry_with_full_assembled_text()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_rejects_non_openai_compat_target()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_returns_early_response_when_queued_for_approval()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_unexpected_error_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_stream_app_state
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_test_forward_stream.py]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[_make_stream_app_state()]] - degree 14, connects to 3 communities
- [[test_forward_stream_rejects_non_openai_compat_target()]] - degree 5, connects to 3 communities
- [[test_forward_stream_drops_credential_bearing_sentence()]] - degree 5, connects to 2 communities
- [[test_forward_stream_forward_error_still_emits_done_event()]] - degree 5, connects to 2 communities
- [[test_forward_stream_ledger_failure_still_emits_done_event()]] - degree 5, connects to 2 communities