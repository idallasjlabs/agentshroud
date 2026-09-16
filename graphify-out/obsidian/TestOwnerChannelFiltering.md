---
source_file: "gateway/tests/test_slack_proxy.py"
type: "code"
community: "Community 78"
location: "L213"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_78
---

# TestOwnerChannelFiltering

## Connections
- [[dot-test_is_owner_channel_empty_owner_uid_always_false()]] - `method` [EXTRACTED]
- [[dot-test_is_owner_channel_matches_owner_uid()]] - `method` [EXTRACTED]
- [[dot-test_is_owner_channel_no_match_for_other()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_clean_message_passes()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_high_risk_leakage_blocked_before_pipeline()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_info_filter_redaction_blocks()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_pipeline_exception_fail_closed()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_tailscale_hostname_blocked()]] - `method` [EXTRACTED]
- [[dot-test_owner_channel_uses_full_trust()]] - `method` [EXTRACTED]
- [[dot-test_owner_pipeline_exception_fail_open()]] - `method` [EXTRACTED]
- [[P0 security Slack outbound must differentiate owner vs collaborator channels.]] - `rationale_for` [EXTRACTED]
- [[SlackAPIProxy_1]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[test_slack_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_78