---
type: community
members: 39
---

# management.py

**Members:** 39 nodes

## Members
- [[AgentShroud Management Dashboard routes. All manage routes require…]] - rationale - gateway/web/management.py
- [[BaseModel_3]] - code
- [[EgressAllowlistResponse]] - code - gateway/web/management.py
- [[EgressAllowlistUpdate]] - code - gateway/web/management.py
- [[Falco runtime security alerts viewer.]] - rationale - gateway/web/management.py
- [[Get current egress allowlist configuration.]] - rationale - gateway/web/management.py
- [[Get overall credential health score and status summary.]] - rationale - gateway/web/management.py
- [[Get status of all managed credentials including age and rotation schedule.]] - rationale - gateway/web/management.py
- [[Request model for updating egress allowlist.]] - rationale - gateway/web/management.py
- [[Response model for egress allowlist.]] - rationale - gateway/web/management.py
- [[Security tools overview — links to all tool-specific dashboards.]] - rationale - gateway/web/management.py
- [[Serve the SSH hosts page.]] - rationale - gateway/web/management.py
- [[Serve the approval queue page.]] - rationale - gateway/web/management.py
- [[Serve the audit log page.]] - rationale - gateway/web/management.py
- [[Serve the collaborators page (dynamic — fetches live activity data).]] - rationale - gateway/web/management.py
- [[Serve the emergency kill switch page.]] - rationale - gateway/web/management.py
- [[Serve the main dashboard page.]] - rationale - gateway/web/management.py
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[Serve the security modules page (dynamic — fetches live data).]] - rationale - gateway/web/management.py
- [[Trigger manual rotation for a specific credential (owner only).]] - rationale - gateway/web/management.py
- [[Wazuh HIDS alerts and FIM events viewer.]] - rationale - gateway/web/management.py
- [[approvals()]] - code - gateway/web/management.py
- [[audit()_1]] - code - gateway/web/management.py
- [[collaborators()]] - code - gateway/web/management.py
- [[credentials_health()]] - code - gateway/web/management.py
- [[credentials_status()]] - code - gateway/web/management.py
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard_main()]] - code - gateway/web/management.py
- [[falco_dashboard()]] - code - gateway/web/management.py
- [[get_4]] - code
- [[get_egress_allowlist()]] - code - gateway/web/management.py
- [[killswitch()]] - code - gateway/web/management.py
- [[management.py]] - code - gateway/web/management.py
- [[modules()]] - code - gateway/web/management.py
- [[post_3]] - code
- [[rotate_credential()]] - code - gateway/web/management.py
- [[security_overview()]] - code - gateway/web/management.py
- [[ssh()]] - code - gateway/web/management.py
- [[wazuh_dashboard()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/managementpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_EgressFilterConfig]]
- 4 edges to [[_COMMUNITY_KeyRotationConfig]]
- 4 edges to [[_COMMUNITY_KeyRotationManager]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py]]
- 1 edge to [[_COMMUNITY_fastapi]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[management.py]] - degree 30, connects to 8 communities
- [[credentials_health()]] - degree 5, connects to 2 communities
- [[credentials_status()]] - degree 5, connects to 2 communities
- [[rotate_credential()]] - degree 5, connects to 2 communities
- [[get_egress_allowlist()]] - degree 5, connects to 1 community
