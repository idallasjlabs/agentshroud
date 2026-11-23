---
source_file: "gateway/security/egress_filter.py"
type: "code"
community: "EgressPolicy"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressPolicy
---

# EgressPolicy

## Connections
- [[dot-__init__()_175]] - `calls` [EXTRACTED]
- [[dot-get_policy()_1]] - `references` [EXTRACTED]
- [[dot-matches_domain()]] - `method` [EXTRACTED]
- [[dot-matches_ip()]] - `method` [EXTRACTED]
- [[dot-matches_port()]] - `method` [EXTRACTED]
- [[dot-set_agent_policy()]] - `references` [EXTRACTED]
- [[dot-setup_method()_29]] - `calls` [EXTRACTED]
- [[dot-setup_method()_11]] - `calls` [EXTRACTED]
- [[dot-test_agent_specific_policy()]] - `calls` [EXTRACTED]
- [[dot-test_allowed_cidr()]] - `calls` [EXTRACTED]
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - `calls` [EXTRACTED]
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `calls` [EXTRACTED]
- [[dot-test_default_policy_allows_imaps()]] - `calls` [EXTRACTED]
- [[dot-test_default_policy_allows_smtp_submission()]] - `calls` [EXTRACTED]
- [[dot-test_default_policy_allows_smtps()]] - `calls` [EXTRACTED]
- [[dot-test_deny_all_false()]] - `calls` [EXTRACTED]
- [[dot-test_egress_filter_blocks_mcp_exfil()]] - `calls` [INFERRED]
- [[dot-test_egress_filter_loaded()]] - `calls` [EXTRACTED]
- [[dot-test_empty_ports_allows_all()]] - `calls` [EXTRACTED]
- [[dot-test_matches_domain_exact()]] - `calls` [EXTRACTED]
- [[dot-test_matches_domain_wildcard()]] - `calls` [EXTRACTED]
- [[dot-test_matches_ip_cidr()]] - `calls` [EXTRACTED]
- [[dot-test_matches_ip_invalid()]] - `calls` [EXTRACTED]
- [[dot-test_matches_ip_single()]] - `calls` [EXTRACTED]
- [[dot-test_matches_port()]] - `calls` [EXTRACTED]
- [[dot-test_matches_port_empty_allows_all()]] - `calls` [EXTRACTED]
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - `calls` [EXTRACTED]
- [[dot-test_port_not_allowed()]] - `calls` [EXTRACTED]
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - `calls` [EXTRACTED]
- [[Egress policy for an agent or global default.]] - `rationale_for` [EXTRACTED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressPolicy]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEnforceMode]] - `uses` [INFERRED]
- [[TestIPRules]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPerAgentPolicy]] - `uses` [INFERRED]
- [[TestSMTPIMAPPorts]] - `uses` [INFERRED]
- [[_make_deny_all_filter()]] - `calls` [EXTRACTED]
- [[_make_full_pipeline()]] - `calls` [EXTRACTED]
- [[deep_security_test()]] - `uses` [INFERRED]
- [[egress_filter()]] - `uses` [INFERRED]
- [[egress_filter()_1]] - `uses` [INFERRED]
- [[egress_filter.py_2]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[t_egress()]] - `calls` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_egress_filter.py]] - `imports` [EXTRACTED]
- [[test_egress_filter_flush_without_notifier()]] - `uses` [INFERRED]
- [[test_egress_filter_no_notification_on_allow()]] - `uses` [INFERRED]
- [[test_egress_filter_notifies_on_deny()]] - `uses` [INFERRED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressPolicy
