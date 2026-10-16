---
type: community
cohesion: 0.12
members: 39
---

# test_forward_stream.py

**Cohesion:** 0.12 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-__init__()_35]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_inbound()]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()_1]] - code - gateway/tests/test_forward_stream.py
- [[2-sentence sliding window over `sentences` each window (previous +     current,]] - rationale - gateway/ingest_api/routes/forward.py
- [[Buffer streamed text deltas and yield each complete sentence as soon as     its]] - rationale - gateway/ingest_api/routes/forward.py
- [[Build a mock app_state whose router streams `sentences_out` as raw     text delt]] - rationale - gateway/tests/test_forward_stream.py
- [[Mock pipeline that blocks any window containing the word 'secret'.]] - rationale - gateway/tests/test_forward_stream.py
- [[Mock pipeline whose process_outbound returns the window text unchanged     — ver]] - rationale - gateway/tests/test_forward_stream.py
- [[Sliding-window sentinel-joined security filter for streaming voice pipeline]] - concept - gateway/tests/test_forward_stream.py
- [[_BlockingPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_PassthroughPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_aiter()]] - code - gateway/tests/test_forward_stream.py
- [[_filtered_sentence_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[_make_stream_app_state()]] - code - gateway/tests/test_forward_stream.py
- [[_parse_sse_events()]] - code - gateway/tests/test_forward_stream.py
- [[_post_stream()]] - code - gateway/tests/test_forward_stream.py
- [[_sentences_from_deltas()]] - code - gateway/ingest_api/routes/forward.py
- [[test_filtered_stream_blocked_final_sentence_yields_nothing()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_blocked_window_releases_nothing_for_that_window()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_redaction_applies_to_released_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_releases_sentences_in_order()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_sentinel_stripped_fails_safe_by_releasing_all()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_single_sentence_flushed_alone()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_windows_are_pairs_joined_by_sentinel()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream.py]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_503_when_no_pipeline_configured()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_drops_credential_bearing_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_emits_sentence_events_then_done()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_forward_error_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_ledger_failure_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_records_ledger_entry_with_full_assembled_text()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_rejects_non_openai_compat_target()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_returns_early_response_when_queued_for_approval()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream_unexpected_error_still_emits_done_event()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_empty_stream_yields_nothing()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_flushes_trailing_fragment_without_punctuation()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_single_delta_full_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_splits_on_boundaries()]] - code - gateway/tests/test_forward_stream.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_forward_streampy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_AgentTarget_1]]
- 8 edges to [[_COMMUNITY_WebContentScanner_1]]
- 4 edges to [[_COMMUNITY_AsyncMock_1]]
- 3 edges to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]

## Top bridge nodes
- [[test_forward_stream.py]] - degree 41, connects to 4 communities
- [[_make_stream_app_state()]] - degree 14, connects to 2 communities
- [[test_forward_stream_rejects_non_openai_compat_target()]] - degree 5, connects to 2 communities
- [[_PassthroughPipeline]] - degree 12, connects to 1 community
- [[_filtered_sentence_stream()]] - degree 11, connects to 1 community
