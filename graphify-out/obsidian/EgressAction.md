---
source_file: "gateway/security/egress_filter.py"
type: "code"
community: "EgressFilter"
location: "L30"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/EgressFilter
---

# EgressAction

## Connections
- [[dot-_record()_2]] - `references` [EXTRACTED]
- [[Enum_38]] - `inherits` [EXTRACTED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[TestEgressAttempt]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressFilterEnforcement]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEgressWiringEndToEnd]] - `uses` [INFERRED]
- [[TestEnforceMode]] - `uses` [INFERRED]
- [[TestIPRules]] - `uses` [INFERRED]
- [[TestInteractiveApproval]] - `uses` [INFERRED]
- [[TestLogging]] - `uses` [INFERRED]
- [[TestMonitorMode_1]] - `uses` [INFERRED]
- [[TestOpenClawResearchDomainsAllowlisted]] - `uses` [INFERRED]
- [[TestPerAgentPolicy]] - `uses` [INFERRED]
- [[TestSMTPIMAPPorts]] - `uses` [INFERRED]
- [[TestURLParsing]] - `uses` [INFERRED]
- [[egress_filter.py_2]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[http_proxy.py]] - `imports` [EXTRACTED]
- [[run()]] - `uses` [INFERRED]
- [[str_21]] - `inherits` [EXTRACTED]
- [[test_connect_denied_by_egress_filter_returns_403()]] - `uses` [INFERRED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `uses` [INFERRED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `uses` [INFERRED]
- [[test_egress_blocks_unauthorized_after_trust_check()]] - `uses` [INFERRED]
- [[test_egress_enforce.py]] - `imports` [EXTRACTED]
- [[test_egress_filter.py]] - `imports` [EXTRACTED]
- [[test_full_pipeline_clean_message()]] - `uses` [INFERRED]
- [[test_grant_timed_approval_allows_domain()]] - `uses` [INFERRED]
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - `uses` [INFERRED]
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - `uses` [INFERRED]
- [[test_http_proxy.py]] - `imports` [EXTRACTED]
- [[test_module_stats.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/EgressFilter
