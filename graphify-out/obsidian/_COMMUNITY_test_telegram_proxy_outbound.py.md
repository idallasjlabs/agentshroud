---
type: community
cohesion: 0.04
members: 52
---

# test_telegram_proxy_outbound.py

**Cohesion:** 0.04 - loosely connected
**Members:** 52 nodes

## Members
- [[dot-_fake_get_updates_urlopen()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_accepts_uppercase_http_scheme()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_does_not_treat_email_as_domain_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_handles_bare_domain_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_handles_empty_inputs()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_markdown_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_non_http_scheme_and_uses_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_text_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_version_like_tokens()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_prefers_first_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_rejects_ip_literal_bare_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_returns_none_when_no_url_or_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_email_then_finds_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_protocol_relative_host_without_tld()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_strips_markdown_wrapper_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_strips_trailing_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_parenthesized_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_protocol_relative_urls()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_protocol_relative_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_trims_wrapping_quotes()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_body_still_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_resolve_text_field_falls_back_to_first_string_when_all_empty()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_resolve_text_field_prefers_first_non_empty_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_url_encoded_body_calls_mark_delivered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON getUpdates body must still call mark_delivered (existing behaviour preserve]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound filter must redact egress banners but NOT call _send_owner_admin_notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressBannerRedactionNoOwnerNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressTargetExtraction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundTextFieldResolution]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerActivityNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestPendingNoticeIncludesEgressSection]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestReplayBufferOffsetParsing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for TelegramAPIProxy outbound security pipeline integration.  Proves that]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URL-encoded getUpdates body must call mark_delivered with the correct int offset]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound target extraction helper used by egress preflight.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
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
- 17 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 11 edges to [[_COMMUNITY_EgressFilterConfig]]
- 9 edges to [[_COMMUNITY_MCPPermissionManager]]
- 8 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 8 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-bsREADME.md (5)]]
- 1 edge to [[_COMMUNITY__fw_client]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper]]
- 1 edge to [[_COMMUNITY_Blue Team Security Assessment — AgentShroud v0.8.0 Round 2]]
- 1 edge to [[_COMMUNITY_TestLooksLikeSafeCollaboratorInfoQuery]]
- 1 edge to [[_COMMUNITY_Phase 3A3B Implementation Verification Results]]
- 1 edge to [[_COMMUNITY_All Dependencies.md (2)]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (4)]]
- 1 edge to [[_COMMUNITY_TestOutboundScanUnification]]

## Top bridge nodes
- [[test_telegram_proxy_outbound.py]] - degree 30, connects to 15 communities
- [[TestEgressTargetExtraction]] - degree 25, connects to 4 communities
- [[TestReplayBufferOffsetParsing]] - degree 10, connects to 4 communities
- [[TestOutboundTextFieldResolution]] - degree 8, connects to 4 communities
- [[TestOwnerActivityNotice]] - degree 8, connects to 4 communities
