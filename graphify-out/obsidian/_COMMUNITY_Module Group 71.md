---
type: community
cohesion: 0.05
members: 55
---

# Module Group 71

**Cohesion:** 0.05 - loosely connected
**Members:** 55 nodes

## Members
- [[._is_ipv6()]] - code - gateway/security/egress_filter.py
- [[._is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[._matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[._matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[._record()_1]] - code - gateway/security/egress_filter.py
- [[.check()_4]] - code - gateway/security/egress_filter.py
- [[.check_async()]] - code - gateway/security/egress_filter.py
- [[.flush_notifications()]] - code - gateway/security/egress_filter.py
- [[.get_log()]] - code - gateway/security/egress_filter.py
- [[.get_policy()]] - code - gateway/security/egress_filter.py
- [[.get_stats()_15]] - code - gateway/security/egress_filter.py
- [[.get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[.grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[.set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[.set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[.set_notifier()]] - code - gateway/security/egress_filter.py
- [[.test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressFilter_1]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_71
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 13 edges to [[_COMMUNITY_Module Group 88]]
- 9 edges to [[_COMMUNITY_Module Group 79]]
- 8 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 7 edges to [[_COMMUNITY_Module Group 240]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_Module Group 72]]
- 3 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 2 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 2 edges to [[_COMMUNITY_Module Group 216]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_Module Group 283]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Container Config]]
- 1 edge to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 323]]
- 1 edge to [[_COMMUNITY_Module Group 285]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 88, connects to 17 communities
- [[EgressAttempt]] - degree 18, connects to 3 communities
- [[TestEgressFilterEnforcement]] - degree 14, connects to 3 communities
- [[._record()_1]] - degree 6, connects to 2 communities
- [[.check()_4]] - degree 13, connects to 1 community
