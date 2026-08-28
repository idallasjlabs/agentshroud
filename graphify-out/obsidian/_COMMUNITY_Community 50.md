---
type: community
cohesion: 0.04
members: 83
---

# Community 50

**Cohesion:** 0.04 - loosely connected
**Members:** 83 nodes

## Members
- [[.__init__()_155]] - code - gateway/tests/test_egress_filter.py
- [[._matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[.get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[.is_denylisted()]] - code - gateway/security/egress_config.py
- [[.log_event()_2]] - code - gateway/tests/test_egress_filter.py
- [[.matches_allowlist()]] - code - gateway/security/egress_config.py
- [[.test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_config()_1]] - code - gateway/tests/test_egress_enforce.py
- [[.test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[.test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter_2]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[FakeAuditStore]] - code - gateway/tests/test_egress_filter.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[OpenClaw researchweb_search domains pre-approved after 210-denial SOC saturation incident]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Public does domain match any pattern in the effective default allowlist]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_50
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 78]]
- 31 edges to [[_COMMUNITY_Community 98]]
- 21 edges to [[_COMMUNITY_Community 217]]
- 14 edges to [[_COMMUNITY_Community 30]]
- 9 edges to [[_COMMUNITY_Community 174]]
- 9 edges to [[_COMMUNITY_Community 18]]
- 5 edges to [[_COMMUNITY_Community 20]]
- 4 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 4 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 3 edges to [[_COMMUNITY_Community 28]]
- 3 edges to [[_COMMUNITY_Community 75]]
- 3 edges to [[_COMMUNITY_Community 227]]
- 2 edges to [[_COMMUNITY_Community 19]]
- 2 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 2 edges to [[_COMMUNITY_Community 105]]
- 2 edges to [[_COMMUNITY_Community 420]]
- 2 edges to [[_COMMUNITY_Community 116]]
- 2 edges to [[_COMMUNITY_Community 51]]
- 1 edge to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Community 553]]
- 1 edge to [[_COMMUNITY_Community 88]]
- 1 edge to [[_COMMUNITY_Community 103]]

## Top bridge nodes
- [[EgressFilterConfig]] - degree 101, connects to 15 communities
- [[EgressAction]] - degree 45, connects to 13 communities
- [[EgressFilter_2]] - degree 21, connects to 4 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 4 communities
- [[FakeAuditStore]] - degree 11, connects to 4 communities