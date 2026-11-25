---
source_file: "gateway/security/egress_config.py"
type: "code"
community: "EgressFilterConfig"
location: "L200"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressFilterConfig
---

# EgressFilterConfig

## Connections
- [[dot-__init__()_220]] - `references` [EXTRACTED]
- [[dot-_matches_any_pattern()]] - `method` [EXTRACTED]
- [[dot-from_environment()]] - `method` [EXTRACTED]
- [[dot-get_effective_allowlist()]] - `method` [EXTRACTED]
- [[dot-is_denylisted()]] - `method` [EXTRACTED]
- [[dot-setup_method()_29]] - `calls` [EXTRACTED]
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [EXTRACTED]
- [[dot-test_config_roundtrip()]] - `calls` [EXTRACTED]
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - `calls` [EXTRACTED]
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `calls` [EXTRACTED]
- [[dot-test_default_config()_6]] - `calls` [EXTRACTED]
- [[dot-test_deny_all_false()]] - `calls` [EXTRACTED]
- [[dot-test_deny_is_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[dot-test_denylist_monitor_mode()]] - `calls` [EXTRACTED]
- [[dot-test_denylist_overrides_allowlist()]] - `calls` [EXTRACTED]
- [[dot-test_denylist_wildcards()]] - `calls` [EXTRACTED]
- [[dot-test_domains_in_default_allowlist()]] - `calls` [EXTRACTED]
- [[dot-test_domains_not_denylisted()]] - `calls` [EXTRACTED]
- [[dot-test_effective_allowlist_basic()]] - `calls` [EXTRACTED]
- [[dot-test_effective_allowlist_with_denylist()]] - `calls` [EXTRACTED]
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - `calls` [EXTRACTED]
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - `calls` [EXTRACTED]
- [[dot-test_invalid_mode_handling()]] - `calls` [EXTRACTED]
- [[dot-test_logging_differences_by_mode()]] - `calls` [EXTRACTED]
- [[dot-test_monitor_mode_allows_unknown_domains()]] - `calls` [EXTRACTED]
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - `calls` [EXTRACTED]
- [[dot-test_per_agent_policy()]] - `calls` [EXTRACTED]
- [[dot-test_port_filtering()]] - `calls` [EXTRACTED]
- [[dot-test_private_ip_blocking()]] - `calls` [EXTRACTED]
- [[dot-test_url_parsing()_1]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_allowlist_matching()]] - `calls` [EXTRACTED]
- [[Configuration for egress filtering enforcement.]] - `rationale_for` [EXTRACTED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[TestAuditStorePersistence]] - `uses` [INFERRED]
- [[TestEgressConfigDefaultEnforce]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressFilterConfig]] - `uses` [INFERRED]
- [[TestEgressFilterEnforcement]] - `uses` [INFERRED]
- [[TestEgressManagementAPI]] - `uses` [INFERRED]
- [[TestInteractiveApproval]] - `uses` [INFERRED]
- [[TestOpenClawResearchDomainsAllowlisted]] - `uses` [INFERRED]
- [[TestSMTPIMAPPorts]] - `uses` [INFERRED]
- [[_make_deny_all_filter()]] - `calls` [EXTRACTED]
- [[_make_filter()]] - `calls` [EXTRACTED]
- [[_make_full_pipeline()]] - `calls` [EXTRACTED]
- [[egress_config.py_2]] - `contains` [EXTRACTED]
- [[egress_filter()]] - `uses` [INFERRED]
- [[egress_filter()_1]] - `uses` [INFERRED]
- [[egress_filter.py_2]] - `imports` [EXTRACTED]
- [[get_egress_config()]] - `references` [EXTRACTED]
- [[management.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [INFERRED]
- [[set_egress_config()]] - `references` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_egress_enforce.py]] - `imports` [EXTRACTED]
- [[test_egress_filter.py]] - `imports` [EXTRACTED]
- [[test_egress_filter_flush_without_notifier()]] - `uses` [INFERRED]
- [[test_egress_filter_no_notification_on_allow()]] - `uses` [INFERRED]
- [[test_egress_filter_notifies_on_deny()]] - `uses` [INFERRED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_round2_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[update_egress_allowlist()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/EgressFilterConfig
