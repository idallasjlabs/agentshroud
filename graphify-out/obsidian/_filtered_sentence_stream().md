---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "Forward Stream"
location: "L797"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Forward_Stream
---

# _filtered_sentence_stream()

## Connections
- [[2-sentence sliding window over `sentences` each window (previous +     current,]] - `rationale_for` [EXTRACTED]
- [[Sliding-window sentinel-joined security filter for streaming voice pipeline]] - `rationale_for` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[test_filtered_stream_blocked_final_sentence_yields_nothing()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_blocked_window_releases_nothing_for_that_window()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_redaction_applies_to_released_sentence()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_releases_sentences_in_order()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_sentinel_stripped_fails_safe_by_releasing_all()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_single_sentence_flushed_alone()]] - `calls` [EXTRACTED]
- [[test_filtered_stream_windows_are_pairs_joined_by_sentinel()]] - `calls` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Forward_Stream