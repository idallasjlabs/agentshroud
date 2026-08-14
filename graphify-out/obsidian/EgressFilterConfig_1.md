---
source_file: "gateway/security/egress_filter.py"
type: "code"
community: "Gateway Test Suite"
location: "L105"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# EgressFilterConfig

## Connections
- [[.__init__()_72]] - `references` [EXTRACTED]
- [[.test_allow_is_not_persisted_to_audit_store()]] - `calls` [INFERRED]
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [INFERRED]
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - `calls` [INFERRED]
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `calls` [INFERRED]
- [[.test_deny_is_persisted_to_audit_store()]] - `calls` [INFERRED]
- [[.test_domains_in_default_allowlist()]] - `calls` [INFERRED]
- [[.test_domains_not_denylisted()]] - `calls` [INFERRED]
- [[.test_egress_filter_allows_in_enforce_mode()]] - `calls` [INFERRED]
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - `calls` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[_make_deny_all_filter()]] - `calls` [INFERRED]
- [[_make_filter()]] - `calls` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[test_egress_filter_flush_without_notifier()]] - `calls` [INFERRED]
- [[test_egress_filter_no_notification_on_allow()]] - `calls` [INFERRED]
- [[test_egress_filter_notifies_on_deny()]] - `calls` [INFERRED]
- [[update_egress_allowlist()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite