---
source_file: "gateway/tests/test_forward_stream.py"
type: "code"
community: "Community 76"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_76
---

# test_forward_stream.py

## Connections
- [[AgentTarget]] - `imports` [EXTRACTED]
- [[FastAPI app instance]] - `calls` [EXTRACTED]
- [[ForwardError]] - `imports` [EXTRACTED]
- [[ForwardRequest]] - `imports` [EXTRACTED]
- [[_BlockingPipeline]] - `contains` [EXTRACTED]
- [[_PassthroughPipeline]] - `contains` [EXTRACTED]
- [[_aiter()]] - `contains` [EXTRACTED]
- [[_filtered_sentence_stream()]] - `imports` [EXTRACTED]
- [[_make_stream_app_state()]] - `contains` [EXTRACTED]
- [[_parse_sse_events()]] - `contains` [EXTRACTED]
- [[_post_stream()]] - `contains` [EXTRACTED]
- [[_request()]] - `contains` [EXTRACTED]
- [[_resolve_user_trust_level()]] - `imports` [EXTRACTED]
- [[_sentences_from_deltas()]] - `imports` [EXTRACTED]
- [[_target()]] - `contains` [EXTRACTED]
- [[auth_dep()]] - `imports` [EXTRACTED]
- [[auth_dep()_3]] - `imports` [EXTRACTED]
- [[test_filtered_stream_blocked_final_sentence_yields_nothing()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_blocked_window_releases_nothing_for_that_window()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_redaction_applies_to_released_sentence()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_releases_sentences_in_order()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_sentinel_stripped_fails_safe_by_releasing_all()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_single_sentence_flushed_alone()]] - `contains` [EXTRACTED]
- [[test_filtered_stream_windows_are_pairs_joined_by_sentinel()]] - `contains` [EXTRACTED]
- [[test_forward_stream_503_when_no_pipeline_configured()]] - `contains` [EXTRACTED]
- [[test_forward_stream_drops_credential_bearing_sentence()]] - `contains` [EXTRACTED]
- [[test_forward_stream_emits_sentence_events_then_done()]] - `contains` [EXTRACTED]
- [[test_forward_stream_forward_error_still_emits_done_event()]] - `contains` [EXTRACTED]
- [[test_forward_stream_ledger_failure_still_emits_done_event()]] - `contains` [EXTRACTED]
- [[test_forward_stream_records_ledger_entry_with_full_assembled_text()]] - `contains` [EXTRACTED]
- [[test_forward_stream_rejects_non_openai_compat_target()]] - `contains` [EXTRACTED]
- [[test_forward_stream_returns_early_response_when_queued_for_approval()]] - `contains` [EXTRACTED]
- [[test_forward_stream_unexpected_error_still_emits_done_event()]] - `contains` [EXTRACTED]
- [[test_resolve_trust_level_maps_trust_score_to_tier()]] - `contains` [EXTRACTED]
- [[test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted()]] - `contains` [EXTRACTED]
- [[test_resolve_trust_level_no_trust_manager_defaults_untrusted()]] - `contains` [EXTRACTED]
- [[test_resolve_trust_level_non_owner_user_id_does_not_upgrade()]] - `contains` [EXTRACTED]
- [[test_resolve_trust_level_owner_user_id_upgrades_to_full()]] - `contains` [EXTRACTED]
- [[test_sentences_from_deltas_empty_stream_yields_nothing()]] - `contains` [EXTRACTED]
- [[test_sentences_from_deltas_flushes_trailing_fragment_without_punctuation()]] - `contains` [EXTRACTED]
- [[test_sentences_from_deltas_single_delta_full_sentence()]] - `contains` [EXTRACTED]
- [[test_sentences_from_deltas_splits_on_boundaries()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_76