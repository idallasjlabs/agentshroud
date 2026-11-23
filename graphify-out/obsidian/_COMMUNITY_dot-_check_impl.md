---
type: community
members: 24
---

# ._check_impl

**Members:** 24 nodes

## Members
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_2]] - code - gateway/security/egress_filter.py
- [[dot-check()_6]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_16]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed. Args agent_id The agent making…]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP. Covers RFC…]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80), then…_1]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_check_impl
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY__make_filter]]
- 1 edge to [[_COMMUNITY_test_module_stats.py]]
- 1 edge to [[_COMMUNITY_DraftEntry]]

## Top bridge nodes
- [[EgressAttempt]] - degree 8, connects to 3 communities
- [[dot-_record()_2]] - degree 6, connects to 3 communities
- [[dot-check()_6]] - degree 6, connects to 2 communities
- [[dot-check_async()]] - degree 6, connects to 2 communities
- [[dot-get_policy()_1]] - degree 4, connects to 2 communities
