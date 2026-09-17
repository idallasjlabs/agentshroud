---
type: community
cohesion: 0.06
members: 39
---

# Community 182

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_12]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_14]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_stats()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[EgressFilter]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_182
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 52]]
- 14 edges to [[_COMMUNITY_Community 167]]
- 13 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 11 edges to [[_COMMUNITY_Community 185]]
- 11 edges to [[_COMMUNITY_Community 81]]
- 6 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 5 edges to [[_COMMUNITY_Community 137]]
- 5 edges to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 4 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 3 edges to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 3 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 3 edges to [[_COMMUNITY_Community 92]]
- 3 edges to [[_COMMUNITY_Community 253]]
- 2 edges to [[_COMMUNITY_Community 157]]
- 2 edges to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 2 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 1 edge to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 1 edge to [[_COMMUNITY_Egress Filter & HTTP Proxy]]
- 1 edge to [[_COMMUNITY_Community 322]]
- 1 edge to [[_COMMUNITY_Community 86]]
- 1 edge to [[_COMMUNITY_Community 607]]
- 1 edge to [[_COMMUNITY_Community 189]]
- 1 edge to [[_COMMUNITY_Community 51]]
- 1 edge to [[_COMMUNITY_Community 268]]

## Top bridge nodes
- [[EgressFilter]] - degree 104, connects to 22 communities
- [[TestEgressFilter]] - degree 34, connects to 9 communities
- [[dot-setup_method()_14]] - degree 4, connects to 2 communities
- [[dot-test_deny_all_false()]] - degree 4, connects to 2 communities
- [[dot-get_log()]] - degree 4, connects to 1 community