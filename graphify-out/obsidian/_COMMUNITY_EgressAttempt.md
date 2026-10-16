---
type: community
cohesion: 0.10
members: 24
---

# EgressAttempt

**Cohesion:** 0.10 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_1]] - code - gateway/security/egress_filter.py
- [[dot-check()_3]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
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
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressAttempt
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EgressFilter]]
- 8 edges to [[_COMMUNITY__make_filter]]
- 7 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_test_egress_filter.py]]
- 2 edges to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_A2AMethod]]

## Top bridge nodes
- [[EgressAttempt]] - degree 22, connects to 5 communities
- [[dot-_record()_1]] - degree 6, connects to 3 communities
- [[dot-check()_3]] - degree 6, connects to 2 communities
- [[dot-check_async()]] - degree 6, connects to 2 communities
- [[dot-get_policy()_1]] - degree 4, connects to 2 communities
