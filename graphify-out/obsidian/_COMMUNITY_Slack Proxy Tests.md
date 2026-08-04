---
type: community
cohesion: 0.05
members: 62
---

# Slack Proxy Tests

**Cohesion:** 0.05 - loosely connected
**Members:** 62 nodes

## Members
- [[.test_attachments_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_blocks_scanned_even_when_text_present()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_chat_postmessage_content_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_chat_update_content_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_connections_open_missing_url_passthrough()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_connections_open_rewrites_url()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_connections_open_skips_content_pipeline()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_connections_open_slack_error_passthrough()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_consume_relay_token_one_time()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_consume_relay_token_unknown()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_each_reconnect_issues_unique_token()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_file_upload_initial_comment_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_get_stats_returns_counters()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_is_owner_channel_empty_owner_uid_always_false()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_is_owner_channel_matches_owner_uid()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_is_owner_channel_no_match_for_other()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_no_bot_token_returns_error()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_message_method_not_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_owner_clean_message_passes()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_owner_high_risk_leakage_blocked_before_pipeline()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_owner_info_filter_redaction_blocks()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_owner_pipeline_exception_fail_closed()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_owner_tailscale_hostname_blocked()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_outbound_blocked_returns_error()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_owner_channel_uses_full_trust()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_owner_pipeline_exception_fail_open()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_post_ephemeral_scanned()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_sanitized_text_replaces_original()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_structured_field_sanitization_blocks_delivery()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_system_notification_skips_pipeline()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_text_sanitization_still_applied()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_urlencoded_body_parsed()]] - code - gateway/tests/test_slack_proxy.py
- [[A secret hidden in blocks must be caught even if `text` is benign.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Create a SlackAPIProxy with test credentials and no real IO.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Each call to apps.connections.open issues a distinct relay token.]] - rationale - gateway/tests/test_slack_proxy.py
- [[If the pipeline wants to redact inside blocks JSON, delivery is blocked]] - rationale - gateway/tests/test_slack_proxy.py
- [[Legacy attachments are scanned for leaked content.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Non-owner channel Tailscale hostname triggers leakage pre-check → blocked.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Non-owner channel clean message with no leakage passes through.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Non-owner channel high-risk leakage detected before pipeline → blocked.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Non-owner channel pipeline exception → blocked (fail-closed).]] - rationale - gateway/tests/test_slack_proxy.py
- [[Non-owner channel pipeline passes but info_filter_redaction_count  0 → blocked]] - rationale - gateway/tests/test_slack_proxy.py
- [[Owner channel pipeline called with user_trust_level=FULL, message forwarded.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Owner channel pipeline exception → logged but message still forwarded.]] - rationale - gateway/tests/test_slack_proxy.py
- [[P0 security Slack outbound must differentiate owner vs collaborator channels.]] - rationale - gateway/tests/test_slack_proxy.py
- [[Plain-text sanitization keeps working (redacted text forwarded).]] - rationale - gateway/tests/test_slack_proxy.py
- [[TestMultiFieldOutboundScanning]] - code - gateway/tests/test_slack_proxy.py
- [[TestOwnerChannelFiltering]] - code - gateway/tests/test_slack_proxy.py
- [[TestProxyOutbound]] - code - gateway/tests/test_slack_proxy.py
- [[TestSocketModeRelay]] - code - gateway/tests/test_slack_proxy.py
- [[_make_proxy()_1]] - code - gateway/tests/test_slack_proxy.py
- [[_pass_result()]] - code - gateway/tests/test_slack_proxy.py
- [[apps.connections.open Slack error response returned unchanged.]] - rationale - gateway/tests/test_slack_proxy.py
- [[apps.connections.open pipeline is NOT invoked (not a message method).]] - rationale - gateway/tests/test_slack_proxy.py
- [[apps.connections.open real WSS URL is stored and relay URL returned.]] - rationale - gateway/tests/test_slack_proxy.py
- [[apps.connections.open response without url field returned unchanged.]] - rationale - gateway/tests/test_slack_proxy.py
- [[blocksattachments and upload text must be scanned, not just `text`.      Regres]] - rationale - gateway/tests/test_slack_proxy.py
- [[chat.postEphemeral text goes through the pipeline like postMessage.]] - rationale - gateway/tests/test_slack_proxy.py
- [[consume_relay_token returns None for unknown tokens.]] - rationale - gateway/tests/test_slack_proxy.py
- [[consume_relay_token returns the URL once then None.]] - rationale - gateway/tests/test_slack_proxy.py
- [[files.upload initial_commenttitle text is scanned.]] - rationale - gateway/tests/test_slack_proxy.py
- [[test_slack_proxy.py]] - code - gateway/tests/test_slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Slack_Proxy_Tests
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Module Group 74]]
- 6 edges to [[_COMMUNITY_Slack Proxy]]
- 5 edges to [[_COMMUNITY_Webhook Receiver]]
- 2 edges to [[_COMMUNITY_Module Group 289]]
- 1 edge to [[_COMMUNITY_Module Group 496]]

## Top bridge nodes
- [[test_slack_proxy.py]] - degree 10, connects to 4 communities
- [[_make_proxy()_1]] - degree 36, connects to 2 communities
- [[TestOwnerChannelFiltering]] - degree 14, connects to 2 communities
- [[TestProxyOutbound]] - degree 12, connects to 2 communities
- [[TestMultiFieldOutboundScanning]] - degree 10, connects to 2 communities
