---
type: community
members: 81
---

# test_telegram_proxy_outbound.py

**Members:** 81 nodes

## Members
- [[dot-_fake_get_updates_urlopen()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_fake_urlopen_factory()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_owner_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy()_5]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_body_still_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_poll_timeout_remains_60s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_non_long_poll_timeout_is_15s()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_search_json_collaborator_safe_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_search_json_owner_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_url_encoded_body_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_web_search_log_called_with_correct_params()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_web_search_no_egress_filter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_web_search_query_truncation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[B1 one-shot 400-retry for unbalanced HTML parse errors.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator chat raw web_search JSON produces a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON getUpdates body must still call mark_delivered (existing behaviour…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound filter must redact egress banners but NOT call…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner chat raw web_search JSON produces 'Switch to tool-capable model' message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback…_1]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction via the pipeline path must not strip parse_mode either (owner,…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Queries longer than 200 chars are truncated in the SOC log reason.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for Telegram HTML parse error caused by PII placeholders. When…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a TelegramAPIProxy configured with a mock owner RBAC.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a urlopen mock that records the timeout kwarg and succeeds.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressBannerRedactionNoOwnerNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestForwardToTelegramTimeouts]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerActivityNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestParseModeStrippedAfterPIIRedaction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestPendingNoticeIncludesEgressSection]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestReplayBufferOffsetParsing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTelegram400Retry]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestWebSearchLog]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for TelegramAPIProxy outbound security pipeline integration. Proves that…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for _trigger_web_search_log and raw web_search JSON outbound handling.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _forward_to_telegram uses correct urlopen timeouts. Regression guard…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URL-encoded getUpdates body must call mark_delivered with the correct int…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Verify URL-encoded and JSON getUpdates bodies both trigger mark_delivered…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()_5]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()_6]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()_7]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_admin_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_admin_notice()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_urlopen()_8]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_fake_urlopen()_9]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_activity_notice must render tracker entries or honest error.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_pending_notice must append Pending Egress Requests when queue non-…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log calls log_external_decision with Brave domain and query.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log returns silently when egress_filter is None.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[log_external_decision()_2]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[log_external_decision()_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode=HTML must be preserved for owner when text contains no PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_22]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[sendMessage and similar calls must use a 15s urlopen timeout.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[test_telegram_proxy_outbound.py]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 42 edges to [[_COMMUNITY__make_sanitizer]]
- 13 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY__make_multipart_body]]
- 3 edges to [[_COMMUNITY_dot-_extract_first_egress_target]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 2 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_dot-_rewrite_known_runtime_errors]]
- 1 edge to [[_COMMUNITY_PIISanitizer]]
- 1 edge to [[_COMMUNITY_dot-_looks_like_safe_collaborator_info_query]]
- 1 edge to [[_COMMUNITY_dot-_is_valid_domain_name]]
- 1 edge to [[_COMMUNITY_TestBuildCollaboratorSafeInfoResponse]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]

## Top bridge nodes
- [[test_telegram_proxy_outbound.py]] - degree 34, connects to 13 communities
- [[dot-_make_proxy()_5]] - degree 5, connects to 2 communities
- [[TestEgressBannerRedactionNoOwnerNotice]] - degree 4, connects to 2 communities
- [[TestParseModeStrippedAfterPIIRedaction]] - degree 8, connects to 1 community
- [[TestWebSearchLog]] - degree 8, connects to 1 community
