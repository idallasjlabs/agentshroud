---
type: community
cohesion: 0.03
members: 61
---

# test_telegram_proxy_outbound.py

**Cohesion:** 0.03 - loosely connected
**Members:** 61 nodes

## Members
- [[._make_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_accepts_hyphenated_inner_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_accepts_mixed_case_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_accepts_numeric_inner_labels()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_accepts_standard_host()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_accepts_uppercase_input_via_normalization()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_enforces_tld_rules()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_handles_none_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_empty_or_whitespace()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_leading_or_trailing_dot()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_malformed_hosts()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_overlong_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_overlong_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_punycode_and_non_ascii_labels()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_single_label_host()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_underscore_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_rejects_whitespace_inside_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_valid_domain_name_strips_surrounding_whitespace()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_resolve_text_field_falls_back_to_first_string_when_all_empty()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_resolve_text_field_prefers_first_non_empty_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_accepts_hyphen_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_accepts_underscore_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_handles_non_string_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_matches_cannot_to_access_variant()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_matches_healthcheck_skill_sandbox_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_matches_http_status_without_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_matches_memory_embedding_provider_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_matches_no_response_generated_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_requires_skill_marker_for_healthcheck_branch()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_rewrite_known_runtime_errors_returns_none_for_unrelated_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[B1 one-shot 400-retry for unbalanced HTML parse errors.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDomainValidationHelper]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressBannerRedactionNoOwnerNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundTextFieldResolution]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerActivityNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestPendingNoticeIncludesEgressSection]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestRuntimeRewriteHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTelegram400Retry]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for TelegramAPIProxy outbound security pipeline integration.  Proves that]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for deterministic runtime error rewrite helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for domain validator used by egress approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound text field resolution helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
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
- 18 edges to [[_COMMUNITY_TrustManager]]
- 17 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 10 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 9 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_TestBuildCollaboratorSafeInfoResponse]]
- 1 edge to [[_COMMUNITY_TestEgressTargetExtraction]]
- 1 edge to [[_COMMUNITY_TestForwardToTelegramTimeouts]]
- 1 edge to [[_COMMUNITY_TestInternalBannerMatcher]]
- 1 edge to [[_COMMUNITY_TestLooksLikeSafeCollaboratorInfoQuery]]
- 1 edge to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 1 edge to [[_COMMUNITY_TestOutboundScanUnification]]
- 1 edge to [[_COMMUNITY_TestParseModeStrippedAfterPIIRedaction]]
- 1 edge to [[_COMMUNITY_TestReplayBufferOffsetParsing]]
- 1 edge to [[_COMMUNITY_TestWebSearchLog]]

## Top bridge nodes
- [[test_telegram_proxy_outbound.py]] - degree 30, connects to 16 communities
- [[TestDomainValidationHelper]] - degree 23, connects to 3 communities
- [[TestRuntimeRewriteHelpers]] - degree 16, connects to 3 communities
- [[TestTelegram400Retry]] - degree 9, connects to 3 communities
- [[TestOutboundTextFieldResolution]] - degree 8, connects to 3 communities