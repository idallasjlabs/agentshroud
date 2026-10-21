---
type: community
members: 30
---

# First iteration ingests + records; second sees dedup and skips. (2)

**Members:** 30 nodes

## Members
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_1]] - code - gateway/security/egress_filter.py
- [[dot-check()_5]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_15]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-matches_domain()]] - code - gateway/security/egress_filter.py
- [[dot-matches_ip()]] - code - gateway/security/egress_filter.py
- [[dot-matches_port()]] - code - gateway/security/egress_filter.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/First_iteration_ingests__records_second_sees_dedup_and_skips_2
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 13 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)_1]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2)_1]]
- 1 edge to [[_COMMUNITY_Job details]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[EgressAttempt]] - degree 22, connects to 3 communities
- [[dot-_record()_1]] - degree 6, connects to 3 communities
- [[dot-check()_5]] - degree 6, connects to 2 communities
- [[dot-check_async()]] - degree 6, connects to 2 communities
- [[dot-get_policy()_1]] - degree 4, connects to 2 communities
