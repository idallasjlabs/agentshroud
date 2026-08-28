---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Community 50"
location: "L511"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_50
---

# EgressFilter

## Connections
- [[.test_allow_is_not_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[.test_allowed_cidr()]] - `calls` [EXTRACTED]
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [EXTRACTED]
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - `calls` [EXTRACTED]
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `calls` [EXTRACTED]
- [[.test_deny_is_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[.test_egress_filter_allows_in_enforce_mode()]] - `calls` [EXTRACTED]
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - `calls` [EXTRACTED]
- [[.test_port_not_allowed()]] - `calls` [EXTRACTED]
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - `calls` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[_make_deny_all_filter()]] - `references` [EXTRACTED]
- [[_make_filter()]] - `calls` [EXTRACTED]
- [[test_egress_filter_flush_without_notifier()]] - `calls` [EXTRACTED]
- [[test_egress_filter_no_notification_on_allow()]] - `calls` [EXTRACTED]
- [[test_egress_filter_notifies_on_deny()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_50