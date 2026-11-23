---
type: community
members: 66
---

# _make_proxy

**Members:** 66 nodes

## Members
- [[dot-__init__()_14]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_malformed_json_body_forwards_with_empty_payload()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_args_return_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_args_return_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_channel_or_text_skips_tracking()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_name_truncated_to_80_chars()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_network_error_returns_synthetic_failure()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_token_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_token_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_token_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_not_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_other_error_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_other_error_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_slack_error_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_posts_with_bearer_token()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_channel_id_with_sanitized_name()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_unknown_content_type_ignored()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Bodies with an unrecognized Content-Type are not parsed at all.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Cached correlation for the channel → no Slack history call; outbound is…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Channel name is lowercased, spacesunderscores → hyphens, symbols dropped.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Connection failure → {'ok' False, 'error' exc} (no exception leaks).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Coverage tests for SlackAPIProxy — tracker recovery, Slack API call layer,…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Happy path POSTs to slack.comapimethod with injected bot token.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still logged,…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed and…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-thread reply → conversations.history lookup; bot and subtype messages are…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[TestBodyParsing]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestCallSlackApi]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestInviteChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestKickChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOutboundTracking]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestProvisionGroupChannel]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestRedactionCountErrorSwallow]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Thread reply with no cached corr → conversations.replies lookup recovers the…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Tracker errors are non-fatal — Slack response still returned to bot.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Unparseable JSON body → warning logged, empty payload forwarded (no crash).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[_make_proxy()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[asyncio_7]] - code
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_3]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_proxy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[test_slack_proxy_coverage.py]] - degree 12, connects to 2 communities
- [[dot-info_filter_redaction_count()]] - degree 3, connects to 2 communities
- [[_make_proxy()]] - degree 33, connects to 1 community
- [[dot-test_dm_reply_recovers_inbound_via_conversations_history()]] - degree 7, connects to 1 community
- [[dot-test_history_error_records_outbound_without_correlation()]] - degree 7, connects to 1 community
