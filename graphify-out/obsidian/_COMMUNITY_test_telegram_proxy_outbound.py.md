---
type: community
cohesion: 0.04
members: 50
---

# test_telegram_proxy_outbound.py

**Cohesion:** 0.04 - loosely connected
**Members:** 50 nodes

## Members
- [[dot-_fake_get_updates_urlopen()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_body_still_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_resolve_text_field_falls_back_to_first_string_when_all_empty()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_resolve_text_field_prefers_first_non_empty_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_accepts_hyphen_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_accepts_underscore_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_handles_non_string_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_cannot_to_access_variant()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_healthcheck_skill_sandbox_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_http_status_without_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_memory_embedding_provider_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_no_response_generated_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_requires_skill_marker_for_healthcheck_branch()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_returns_none_for_unrelated_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_url_encoded_body_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[B1 one-shot 400-retry for unbalanced HTML parse errors.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON getUpdates body must still call mark_delivered (existing behaviour preserve]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressBannerRedactionNoOwnerNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundTextFieldResolution]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerActivityNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestPendingNoticeIncludesEgressSection]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestReplayBufferOffsetParsing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestRuntimeRewriteHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTelegram400Retry]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for TelegramAPIProxy outbound security pipeline integration.  Proves that]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URL-encoded getUpdates body must call mark_delivered with the correct int offset]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for deterministic runtime error rewrite helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound text field resolution helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Verify URL-encoded and JSON getUpdates bodies both trigger mark_delivered correc]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_activity_notice must render tracker entries or honest error.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_pending_notice must append Pending Egress Requests when queue non-em]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[test_telegram_proxy_outbound.py]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 18 edges to [[_COMMUNITY_PIIConfig]]
- 10 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 9 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 3 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_TestForwardToTelegramTimeouts]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_TestWebSearchLog]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper]]
- 1 edge to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 1 edge to [[_COMMUNITY_TestLooksLikeSafeCollaboratorInfoQuery]]
- 1 edge to [[_COMMUNITY_TestBuildCollaboratorSafeInfoResponse]]
- 1 edge to [[_COMMUNITY_TestParseModeStrippedAfterPIIRedaction]]
- 1 edge to [[_COMMUNITY_TestInternalBannerMatcher]]

## Top bridge nodes
- [[test_telegram_proxy_outbound.py]] - degree 30, connects to 15 communities
- [[TestRuntimeRewriteHelpers]] - degree 16, connects to 3 communities
- [[TestReplayBufferOffsetParsing]] - degree 10, connects to 3 communities
- [[TestTelegram400Retry]] - degree 9, connects to 3 communities
- [[TestOutboundTextFieldResolution]] - degree 8, connects to 3 communities
