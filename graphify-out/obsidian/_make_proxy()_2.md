---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "code"
community: "Slack Proxy"
location: "L22"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_Proxy
---

# _make_proxy()

## Connections
- [[.test_already_in_channel_is_idempotent_true()]] - `calls` [EXTRACTED]
- [[.test_cached_corr_without_colon_falls_back_to_channel()]] - `calls` [EXTRACTED]
- [[.test_cached_inbound_corr_skips_history_lookup()]] - `calls` [EXTRACTED]
- [[.test_cant_kick_self_is_idempotent_true()]] - `calls` [EXTRACTED]
- [[.test_dm_reply_recovers_inbound_via_conversations_history()]] - `calls` [EXTRACTED]
- [[.test_history_error_records_outbound_without_correlation()]] - `calls` [EXTRACTED]
- [[.test_malformed_json_body_forwards_with_empty_payload()]] - `calls` [EXTRACTED]
- [[.test_missing_args_return_false()]] - `calls` [EXTRACTED]
- [[.test_missing_args_return_false()_1]] - `calls` [EXTRACTED]
- [[.test_missing_channel_or_text_skips_tracking()]] - `calls` [EXTRACTED]
- [[.test_name_truncated_to_80_chars()]] - `calls` [EXTRACTED]
- [[.test_network_error_returns_synthetic_failure()]] - `calls` [EXTRACTED]
- [[.test_no_token_returns_false()]] - `calls` [EXTRACTED]
- [[.test_no_token_returns_false()_1]] - `calls` [EXTRACTED]
- [[.test_no_token_returns_none()]] - `calls` [EXTRACTED]
- [[.test_not_in_channel_is_idempotent_true()]] - `calls` [EXTRACTED]
- [[.test_other_error_returns_false()]] - `calls` [EXTRACTED]
- [[.test_other_error_returns_false()_1]] - `calls` [EXTRACTED]
- [[.test_recovery_exception_is_non_fatal()]] - `calls` [EXTRACTED]
- [[.test_redaction_count_access_error_is_non_fatal()]] - `calls` [EXTRACTED]
- [[.test_slack_error_returns_none()]] - `calls` [EXTRACTED]
- [[.test_structured_text_serialized_for_preview()]] - `calls` [EXTRACTED]
- [[.test_success_posts_with_bearer_token()]] - `calls` [EXTRACTED]
- [[.test_success_returns_channel_id_with_sanitized_name()]] - `calls` [EXTRACTED]
- [[.test_success_returns_true()]] - `calls` [EXTRACTED]
- [[.test_success_returns_true()_1]] - `calls` [EXTRACTED]
- [[.test_system_message_not_tracked()]] - `calls` [EXTRACTED]
- [[.test_thread_reply_recovers_inbound_via_conversations_replies()]] - `calls` [EXTRACTED]
- [[.test_tracker_exception_does_not_break_response()]] - `calls` [EXTRACTED]
- [[.test_unknown_content_type_ignored()]] - `calls` [EXTRACTED]
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - `rationale_for` [EXTRACTED]
- [[SlackAPIProxy_2]] - `references` [EXTRACTED]
- [[SlackAPIProxy]] - `calls` [EXTRACTED]
- [[test_slack_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_Proxy