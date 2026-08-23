---
type: community
cohesion: 0.06
members: 36
---

# Management (web)

**Cohesion:** 0.06 - loosely connected
**Members:** 36 nodes

## Members
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
- [[dashboard.html (Control Center Template)]] - code - gateway/web/templates/dashboard.html
- [[dashboard_main()]] - code - gateway/web/management.py
- [[falco_dashboard()]] - code - gateway/web/management.py
- [[get_egress_allowlist()]] - code - gateway/web/management.py
- [[killswitch()_1]] - code - gateway/web/management.py
- [[management.py]] - code - gateway/web/management.py
- [[modules()]] - code - gateway/web/management.py
- [[rotate_credential()]] - code - gateway/web/management.py
- [[security_overview()]] - code - gateway/web/management.py
- [[ssh()]] - code - gateway/web/management.py
- [[wazuh_dashboard()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Management_web
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Egress Filter]]
- 6 edges to [[_COMMUNITY_Key Rotation (security)]]
- 6 edges to [[_COMMUNITY_Key Rotation]]
- 3 edges to [[_COMMUNITY_Api (web)]]
- 2 edges to [[_COMMUNITY_Router (soc)]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Dashboard Endpoints (web)]]

## Top bridge nodes
- [[management.py]] - degree 27, connects to 6 communities
- [[EgressAllowlistUpdate]] - degree 6, connects to 4 communities
- [[EgressAllowlistResponse]] - degree 6, connects to 3 communities
- [[credentials_health()]] - degree 4, connects to 2 communities
- [[credentials_status()]] - degree 4, connects to 2 communities