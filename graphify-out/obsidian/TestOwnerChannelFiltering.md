---
source_file: "gateway/tests/test_slack_proxy.py"
type: "code"
community: "Slack Proxy Tests"
location: "L213"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_Proxy_Tests
---

# TestOwnerChannelFiltering

## Connections
- [[.test_is_owner_channel_empty_owner_uid_always_false()]] - `method` [EXTRACTED]
- [[.test_is_owner_channel_matches_owner_uid()]] - `method` [EXTRACTED]
- [[.test_is_owner_channel_no_match_for_other()]] - `method` [EXTRACTED]
- [[.test_non_owner_clean_message_passes()]] - `method` [EXTRACTED]
- [[.test_non_owner_high_risk_leakage_blocked_before_pipeline()]] - `method` [EXTRACTED]
- [[.test_non_owner_info_filter_redaction_blocks()]] - `method` [EXTRACTED]
- [[.test_non_owner_pipeline_exception_fail_closed()]] - `method` [EXTRACTED]
- [[.test_non_owner_tailscale_hostname_blocked()]] - `method` [EXTRACTED]
- [[.test_owner_channel_uses_full_trust()]] - `method` [EXTRACTED]
- [[.test_owner_pipeline_exception_fail_open()]] - `method` [EXTRACTED]
- [[P0 security Slack outbound must differentiate owner vs collaborator channels.]] - `rationale_for` [EXTRACTED]
- [[SlackAPIProxy]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[test_slack_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_Proxy_Tests