---
source_file: "gateway/tests/test_slack_proxy.py"
type: "code"
community: "Slack Proxy"
location: "L16"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_Proxy
---

# _make_proxy()

## Connections
- [[.test_attachments_scanned()]] - `calls` [EXTRACTED]
- [[.test_blocks_scanned_even_when_text_present()]] - `calls` [EXTRACTED]
- [[.test_chat_postmessage_content_scanned()]] - `calls` [EXTRACTED]
- [[.test_chat_update_content_scanned()]] - `calls` [EXTRACTED]
- [[.test_connections_open_missing_url_passthrough()]] - `calls` [EXTRACTED]
- [[.test_connections_open_rewrites_url()]] - `calls` [EXTRACTED]
- [[.test_connections_open_skips_content_pipeline()]] - `calls` [EXTRACTED]
- [[.test_connections_open_slack_error_passthrough()]] - `calls` [EXTRACTED]
- [[.test_consume_relay_token_one_time()]] - `calls` [EXTRACTED]
- [[.test_consume_relay_token_unknown()]] - `calls` [EXTRACTED]
- [[.test_each_reconnect_issues_unique_token()]] - `calls` [EXTRACTED]
- [[.test_file_upload_initial_comment_scanned()]] - `calls` [EXTRACTED]
- [[.test_get_stats_returns_counters()]] - `calls` [EXTRACTED]
- [[.test_is_owner_channel_empty_owner_uid_always_false()]] - `calls` [EXTRACTED]
- [[.test_is_owner_channel_matches_owner_uid()]] - `calls` [EXTRACTED]
- [[.test_is_owner_channel_no_match_for_other()]] - `calls` [EXTRACTED]
- [[.test_no_bot_token_returns_error()]] - `calls` [EXTRACTED]
- [[.test_non_message_method_not_scanned()]] - `calls` [EXTRACTED]
- [[.test_non_owner_clean_message_passes()]] - `calls` [EXTRACTED]
- [[.test_non_owner_high_risk_leakage_blocked_before_pipeline()]] - `calls` [EXTRACTED]
- [[.test_non_owner_info_filter_redaction_blocks()]] - `calls` [EXTRACTED]
- [[.test_non_owner_pipeline_exception_fail_closed()]] - `calls` [EXTRACTED]
- [[.test_non_owner_tailscale_hostname_blocked()]] - `calls` [EXTRACTED]
- [[.test_outbound_blocked_returns_error()]] - `calls` [EXTRACTED]
- [[.test_owner_channel_uses_full_trust()]] - `calls` [EXTRACTED]
- [[.test_owner_pipeline_exception_fail_open()]] - `calls` [EXTRACTED]
- [[.test_post_ephemeral_scanned()]] - `calls` [EXTRACTED]
- [[.test_sanitized_text_replaces_original()]] - `calls` [EXTRACTED]
- [[.test_structured_field_sanitization_blocks_delivery()]] - `calls` [EXTRACTED]
- [[.test_system_notification_skips_pipeline()]] - `calls` [EXTRACTED]
- [[.test_text_sanitization_still_applied()]] - `calls` [EXTRACTED]
- [[.test_urlencoded_body_parsed()]] - `calls` [EXTRACTED]
- [[Create a SlackAPIProxy with test credentials and no real IO.]] - `rationale_for` [EXTRACTED]
- [[SlackAPIProxy]] - `calls` [EXTRACTED]
- [[SlackAPIProxy_1]] - `references` [EXTRACTED]
- [[test_slack_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_Proxy