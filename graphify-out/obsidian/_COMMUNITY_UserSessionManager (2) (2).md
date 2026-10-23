---
type: community
cohesion: 0.05
members: 92
---

# UserSessionManager (2) (2)

**Cohesion:** 0.05 - loosely connected
**Members:** 92 nodes

## Members
- [[dot-__init__()_154]] - code - gateway/tests/test_forward_stream.py
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-process_inbound()_8]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()_5]] - code - gateway/tests/test_forward_stream.py
- [[dot-process_outbound()_6]] - code - gateway/tests/test_forward_stream.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[2-sentence sliding window over `sentences` each window (previous +     current,]] - rationale - gateway/ingest_api/routes/forward.py
- [[AgentTarget_2]] - code - gateway/ingest_api/routes/forward.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/forward.py
- [[Buffer streamed text deltas and yield each complete sentence as soon as     its]] - rationale - gateway/ingest_api/routes/forward.py
- [[Build a mock app_state whose router streams `sentences_out` as raw     text delt]] - rationale - gateway/tests/test_forward_stream.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/models.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[ForwardError]] - code - gateway/ingest_api/router.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Mock pipeline that blocks any window containing the word 'secret'.]] - rationale - gateway/tests/test_forward_stream.py
- [[Mock pipeline whose process_outbound returns the window text unchanged     — ver]] - rationale - gateway/tests/test_forward_stream.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Raised when forwarding to agent fails]] - rationale - gateway/ingest_api/router.py
- [[Request_5]] - code - gateway/ingest_api/routes/forward.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Resolve the outbound trust level for `request`, shared by the blocking     and s]] - rationale - gateway/ingest_api/routes/forward.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Sliding-window sentinel-joined security filter for streaming voice pipeline]] - concept - gateway/tests/test_forward_stream.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_BlockingPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_PassthroughPipeline]] - code - gateway/tests/test_forward_stream.py
- [[_aiter()]] - code - gateway/tests/test_forward_stream.py
- [[_filtered_sentence_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_make_stream_app_state()]] - code - gateway/tests/test_forward_stream.py
- [[_parse_sse_events()]] - code - gateway/tests/test_forward_stream.py
- [[_post_stream()]] - code - gateway/tests/test_forward_stream.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[_request()]] - code - gateway/tests/test_forward_stream.py
- [[_resolve_user_trust_level()]] - code - gateway/ingest_api/routes/forward.py
- [[_sentences_from_deltas()]] - code - gateway/ingest_api/routes/forward.py
- [[_target()]] - code - gateway/tests/test_forward_stream.py
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_15]] - code - gateway/tests/test_channel_ownership.py
- [[client()_16]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
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
- [[test_resolve_trust_level_maps_trust_score_to_tier()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_no_trust_manager_defaults_untrusted()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_non_owner_user_id_does_not_upgrade()]] - code - gateway/tests/test_forward_stream.py
- [[test_resolve_trust_level_owner_user_id_upgrades_to_full()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_empty_stream_yields_nothing()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_flushes_trailing_fragment_without_punctuation()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_single_delta_full_sentence()]] - code - gateway/tests/test_forward_stream.py
- [[test_sentences_from_deltas_splits_on_boundaries()]] - code - gateway/tests/test_forward_stream.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_2_2
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY__make_proxy()]]
- 10 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 7 edges to [[_COMMUNITY_ForwardRequest]]
- 4 edges to [[_COMMUNITY_api.py (2)]]
- 4 edges to [[_COMMUNITY_ServiceManager]]
- 3 edges to [[_COMMUNITY_WebContentScanner]]
- 3 edges to [[_COMMUNITY_WebhookReceiver]]
- 3 edges to [[_COMMUNITY_AgentShroud Access Control Matrix]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_create_auth_dependency()]]
- 3 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)]]
- 3 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (3)]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 2 edges to [[_COMMUNITY_ApprovalHardening]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TestOwnerEmailBypassesPii]]
- 1 edge to [[_COMMUNITY_TestEmailSend]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_Remediation]]
- 1 edge to [[_COMMUNITY_TestPatternDetection]]
- 1 edge to [[_COMMUNITY_TestTelegramWebhook]]

## Top bridge nodes
- [[forward.py]] - degree 37, connects to 12 communities
- [[ForwardError]] - degree 16, connects to 5 communities
- [[_process_inbound()]] - degree 12, connects to 4 communities
- [[test_forward_stream.py]] - degree 41, connects to 3 communities
- [[email_send()]] - degree 13, connects to 3 communities
