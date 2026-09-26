---
type: community
cohesion: 0.06
members: 39
---

# SkillGuard

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[.__init__()_75]] - code - gateway/security/egress_filter.py
- [[.test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[Egress management endpoints (manageegress)]] - code - gateway/ingest_api/main.py
- [[EgressAllowlistUpdate]] - code - gateway/web/management.py
- [[Falco runtime security alerts viewer.]] - rationale - gateway/web/management.py
- [[Get current egress allowlist configuration.]] - rationale - gateway/web/management.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[PERMANENT_EGRESS_DOMAINS canonical allowlist]] - code - gateway/security/egress_config.py
- [[Request model for updating egress allowlist.]] - rationale - gateway/web/management.py
- [[Security tools overview — links to all tool-specific dashboards.]] - rationale - gateway/web/management.py
- [[Serve the SSH hosts page.]] - rationale - gateway/web/management.py
- [[Serve the approval queue page.]] - rationale - gateway/web/management.py
- [[Serve the audit log page.]] - rationale - gateway/web/management.py
- [[Serve the collaborators page (dynamic — fetches live activity data).]] - rationale - gateway/web/management.py
- [[Serve the emergency kill switch page.]] - rationale - gateway/web/management.py
- [[Serve the main dashboard page.]] - rationale - gateway/web/management.py
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[Serve the security modules page (dynamic — fetches live data).]] - rationale - gateway/web/management.py
- [[Test that config can be saved and retrieved.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[Wazuh HIDS alerts and FIM events viewer.]] - rationale - gateway/web/management.py
- [[approvals()]] - code - gateway/web/management.py
- [[audit()_1]] - code - gateway/web/management.py
- [[collaborators()]] - code - gateway/web/management.py
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard.html (Control Center Template)]] - code - gateway/web/templates/dashboard.html
- [[dashboard_main()]] - code - gateway/web/management.py
- [[egress_config.py]] - code - gateway/security/egress_config.py
- [[falco_dashboard()]] - code - gateway/web/management.py
- [[get_egress_allowlist()]] - code - gateway/web/management.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[killswitch()_1]] - code - gateway/web/management.py
- [[management.py]] - code - gateway/web/management.py
- [[modules()]] - code - gateway/web/management.py
- [[security_overview()]] - code - gateway/web/management.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[ssh()]] - code - gateway/web/management.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py
- [[wazuh_dashboard()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SkillGuard
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ConsentFramework]]
- 7 edges to [[_COMMUNITY_OpenClaw Bot Container]]
- 3 edges to [[_COMMUNITY_chatbotmain.py]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_main.rs]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY__call_agent_stream()]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]

## Top bridge nodes
- [[egress_config.py]] - degree 13, connects to 7 communities
- [[management.py]] - degree 27, connects to 6 communities
- [[EgressAllowlistUpdate]] - degree 6, connects to 3 communities
- [[.__init__()_75]] - degree 4, connects to 3 communities
- [[get_egress_config()]] - degree 10, connects to 2 communities