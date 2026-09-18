---
type: community
cohesion: 0.16
members: 26
---

# test_forward_stream.py

**Cohesion:** 0.16 - loosely connected
**Members:** 26 nodes

## Members
- [[.__init__()_41]] - code - gateway/tests/test_forward_stream.py
- [[.process_inbound()_5]] - code - gateway/tests/test_forward_stream.py
- [[.process_outbound()_5]] - code - gateway/tests/test_forward_stream.py
- [[.process_outbound()_6]] - code - gateway/tests/test_forward_stream.py
- [[2-sentence sliding window over `sentences` each window (previous +     current,]] - rationale - gateway/ingest_api/routes/forward.py
- [[Buffer streamed text deltas and yield each complete sentence as soon as     its]] - rationale - gateway/ingest_api/routes/forward.py
- [[Mock pipeline that blocks any window containing the word 'secret'.]] - rationale - gateway/tests/test_forward_stream.py
- [[Mock pipeline whose process_outbound returns the window text unchanged     — ver]] - rationale - gateway/tests/test_forward_stream.py
- [[Sliding-window sentinel-joined security filter for streaming voice pipeline]] - concept - gateway/tests/test_forward_stream.py
- [[_BlockingPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_PassthroughPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_aiter()]] - code - gateway/tests/test_forward_stream.py
- [[_filtered_sentence_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[_sentences_from_deltas()]] - code - gateway/ingest_api/routes/forward.py
- [[test_filtered_stream_blocked_final_sentence_yields_nothing()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_blocked_window_releases_nothing_for_that_window()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_redaction_applies_to_released_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_releases_sentences_in_order()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_sentinel_stripped_fails_safe_by_releasing_all()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_single_sentence_flushed_alone()]] - code - gateway/tests/test_forward_stream.py
- [[test_filtered_stream_windows_are_pairs_joined_by_sentinel()]] - code - gateway/tests/test_forward_stream.py
- [[test_forward_stream.py]] - code - gateway/tests/test_forward_stream.py
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
- 13 edges to [[_COMMUNITY__make_stream_app_state()]]
- 9 edges to [[_COMMUNITY_AgentTarget]]
- 8 edges to [[_COMMUNITY__process_inbound()]]
- 3 edges to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[test_forward_stream.py]] - degree 41, connects to 5 communities
- [[_PassthroughPipeline]] - degree 12, connects to 2 communities
- [[_filtered_sentence_stream()]] - degree 11, connects to 1 community
- [[_BlockingPipeline]] - degree 8, connects to 1 community
- [[_sentences_from_deltas()]] - degree 7, connects to 1 community