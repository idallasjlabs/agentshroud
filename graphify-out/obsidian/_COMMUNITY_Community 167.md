---
type: community
cohesion: 0.06
members: 40
---

# Community 167

**Cohesion:** 0.06 - loosely connected
**Members:** 40 nodes

## Members
- [[dot-__init__()_71]] - code - gateway/tests/test_egress_filter.py
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()]] - code - gateway/security/egress_filter.py
- [[dot-check()_1]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()]] - code - gateway/security/egress_filter.py
- [[dot-log_event()]] - code - gateway/tests/test_egress_filter.py
- [[dot-matches_domain()]] - code - gateway/security/egress_filter.py
- [[dot-matches_ip()]] - code - gateway/security/egress_filter.py
- [[dot-matches_port()]] - code - gateway/security/egress_filter.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore]] - code - gateway/tests/test_egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_167
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_Community 81]]
- 16 edges to [[_COMMUNITY_Community 185]]
- 14 edges to [[_COMMUNITY_Community 182]]
- 13 edges to [[_COMMUNITY_Community 52]]
- 9 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 4 edges to [[_COMMUNITY_Community 137]]
- 3 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 116]]
- 2 edges to [[_COMMUNITY_Community 86]]
- 2 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 1 edge to [[_COMMUNITY_Egress Filter & HTTP Proxy]]
- 1 edge to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 1 edge to [[_COMMUNITY_Community 322]]
- 1 edge to [[_COMMUNITY_Community 607]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 1 edge to [[_COMMUNITY_Prompt Guard & Context Integrity]]

## Top bridge nodes
- [[EgressAction]] - degree 45, connects to 15 communities
- [[EgressAttempt]] - degree 22, connects to 5 communities
- [[FakeAuditStore]] - degree 11, connects to 4 communities
- [[TestOpenClawResearchDomainsAllowlisted]] - degree 11, connects to 4 communities
- [[TestAuditStorePersistence]] - degree 10, connects to 4 communities