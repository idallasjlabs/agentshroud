---
type: community
cohesion: 0.05
members: 49
---

# Production Safety Checklist (SKILL)

**Cohesion:** 0.05 - loosely connected
**Members:** 49 nodes

## Members
- [[._check_impl()]] - code - gateway/security/egress_filter.py
- [[._is_ipv6()]] - code - gateway/security/egress_filter.py
- [[._is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[._matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[._matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[._record()_1]] - code - gateway/security/egress_filter.py
- [[.check()_5]] - code - gateway/security/egress_filter.py
- [[.check_async()]] - code - gateway/security/egress_filter.py
- [[.flush_notifications()]] - code - gateway/security/egress_filter.py
- [[.get_log()]] - code - gateway/security/egress_filter.py
- [[.get_policy()]] - code - gateway/security/egress_filter.py
- [[.get_stats()_16]] - code - gateway/security/egress_filter.py
- [[.get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[.grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[.matches_domain()]] - code - gateway/security/egress_filter.py
- [[.matches_ip()]] - code - gateway/security/egress_filter.py
- [[.matches_port()]] - code - gateway/security/egress_filter.py
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[.set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[.set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[.set_notifier()]] - code - gateway/security/egress_filter.py
- [[.test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
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
- [[EgressFilter_1]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Production_Safety_Checklist_SKILL
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_ConsentFramework]]
- 20 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 20 edges to [[_COMMUNITY_test_http_proxy.py]]
- 8 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE]]
- 4 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_EgressPolicy]]
- 3 edges to [[_COMMUNITY_chatbotmain.py]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 3 edges to [[_COMMUNITY_test_approval_queue.py]]
- 2 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_AgentShroud Access Control Matrix]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_PromptProtection]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 103, connects to 20 communities
- [[EgressAttempt]] - degree 22, connects to 4 communities
- [[egress_filter()]] - degree 4, connects to 3 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities
- [[._record()_1]] - degree 6, connects to 2 communities