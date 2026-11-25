---
type: community
members: 72
---

# test_forward_stream.py

**Members:** 72 nodes

## Members
- [[dot-__init__()_39]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_inbound()_1]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()_1]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()_2]] - code - gateway/tests/test_forward_stream.py
- [[2-sentence sliding window over `sentences` each window (previous + current,…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Buffer streamed text deltas and yield each complete sentence as soon as its…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Build a mock app_state whose router streams `sentences_out` as raw text deltas…]] - rationale - gateway/tests/test_forward_stream.py
- [[Exception_1]] - code
- [[ForwardError]] - code - gateway/ingest_api/router.py
- [[Live regression 2026-08-07 Hermes's own internal LLM failover (Anthropic…]] - rationale - gateway/tests/test_router_streaming.py
- [[Mock pipeline that blocks any window containing the word 'secret'.]] - rationale - gateway/tests/test_forward_stream.py
- [[Mock pipeline whose process_outbound returns the window text unchanged —…]] - rationale - gateway/tests/test_forward_stream.py
- [[Raised when forwarding to agent fails]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[Tests for POST forwardstream — the streaming voice pipeline. Covers the…]] - rationale - gateway/tests/test_forward_stream.py
- [[_BlockingPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_PassthroughPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_aiter()]] - code - gateway/tests/test_forward_stream.py
- [[_aiter_lines()]] - code - gateway/tests/test_router_streaming.py
- [[_event_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[_filtered_sentence_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[_make_stream_app_state()]] - code - gateway/tests/test_forward_stream.py
- [[_mock_stream_response()]] - code - gateway/tests/test_router_streaming.py
- [[_parse_sse_events()]] - code - gateway/tests/test_forward_stream.py
- [[_post_stream()]] - code - gateway/tests/test_forward_stream.py
- [[_queued()]] - code - gateway/tests/test_forward_stream.py
- [[_raise_forward_error()]] - code - gateway/tests/test_forward_stream.py
- [[_raise_unexpected()]] - code - gateway/tests/test_forward_stream.py
- [[_sentences_from_deltas()]] - code - gateway/ingest_api/routes/forward.py
- [[_sse_lines()]] - code - gateway/tests/test_router_streaming.py
- [[_stream()]] - code - gateway/tests/test_forward_stream.py
- [[asyncio_26]] - code
- [[asyncio_27]] - code
- [[mock_stream()]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_1]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_2]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_3]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_4]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_5]] - code - gateway/tests/test_router_streaming.py
- [[mock_stream()_6]] - code - gateway/tests/test_router_streaming.py
- [[process_outbound()]] - code - gateway/tests/test_forward_stream.py
- [[process_outbound()_1]] - code - gateway/tests/test_forward_stream.py
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
- [[test_stream_ignores_lines_without_data_prefix()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_payload_sets_stream_true()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_connect_failure()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_http_status_error()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_raises_forward_error_on_malformed_json()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_rejects_non_openai_compat_target()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_skips_chunk_missing_choices_key_and_continues()]] - code - gateway/tests/test_router_streaming.py
- [[test_stream_yields_content_deltas_in_order()]] - code - gateway/tests/test_router_streaming.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_forward_streampy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_AgentTarget]]
- 15 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_asyncio_9]]
- 2 edges to [[_COMMUNITY__mock_response]]
- 2 edges to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[ForwardError]] - degree 24, connects to 4 communities
- [[test_forward_stream.py]] - degree 44, connects to 2 communities
- [[_make_stream_app_state()]] - degree 15, connects to 2 communities
- [[test_stream_raises_forward_error_on_connect_failure()]] - degree 6, connects to 2 communities
- [[test_stream_raises_forward_error_on_http_status_error()]] - degree 6, connects to 2 communities
