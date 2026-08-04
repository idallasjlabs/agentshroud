---
type: community
cohesion: 0.04
members: 83
---

# Slack Proxy

**Cohesion:** 0.04 - loosely connected
**Members:** 83 nodes

## Members
- [[.__init__()_27]] - code - gateway/proxy/slack_proxy.py
- [[.__init__()_132]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[._call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[._intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[._is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[.get_stats()_8]] - code - gateway/proxy/slack_proxy.py
- [[.handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[.info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[.test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_malformed_json_body_forwards_with_empty_payload()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_args_return_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_args_return_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_channel_or_text_skips_tracking()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_name_truncated_to_80_chars()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_network_error_returns_synthetic_failure()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_token_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_token_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_token_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_not_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_other_error_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_other_error_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_slack_error_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_posts_with_bearer_token()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_channel_id_with_sanitized_name()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_true()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_unknown_content_type_ignored()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Bodies with an unrecognized Content-Type are not parsed at all.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Cached correlation for the channel → no Slack history call; outbound         is]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Channel name is lowercased, spacesunderscores → hyphens, symbols dropped.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Connection failure → {'ok' False, 'error' exc} (no exception leaks).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a Slack channel for a group. Returns channel_id or None on failure.]] - rationale - gateway/proxy/slack_proxy.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Handle an inbound Slack event payload received via Socket Mode.          Called]] - rationale - gateway/proxy/slack_proxy.py
- [[Happy path POSTs to slack.comapimethod with injected bot token.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still         logg]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route         t]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-thread reply → conversations.history lookup; bot and subtype         message]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pop and return the real WSS URL for a relay token (one-time use).          Retur]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxies bot Slack Web API calls through SecurityPipeline.      Outbound flow (bo]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline.          For messa]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner.          In Slack, DM]] - rationale - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[SlackAPIProxy]] - code - gateway/proxy/slack_proxy.py
- [[TestBodyParsing]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestCallSlackApi]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestInviteChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestKickChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOutboundTracking]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestProvisionGroupChannel]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestRedactionCountErrorSwallow]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Thread reply with no cached corr → conversations.replies lookup recovers]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Tracker errors are non-fatal — Slack response still returned to bot.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Unparseable JSON body → warning logged, empty payload forwarded (no crash).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[_make_proxy()_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Slack_Proxy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Module Group 74]]
- 6 edges to [[_COMMUNITY_Slack Proxy Tests]]
- 2 edges to [[_COMMUNITY_Module Group 289]]
- 2 edges to [[_COMMUNITY_Module Group 109]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 496]]

## Top bridge nodes
- [[SlackAPIProxy]] - degree 37, connects to 7 communities
- [[.test_redaction_count_access_error_is_non_fatal()]] - degree 5, connects to 1 community
- [[.test_malformed_json_body_forwards_with_empty_payload()]] - degree 4, connects to 1 community
- [[.test_unknown_content_type_ignored()]] - degree 4, connects to 1 community
- [[.test_network_error_returns_synthetic_failure()]] - degree 4, connects to 1 community
