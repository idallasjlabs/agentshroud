---
type: community
cohesion: 0.14
members: 18
---

# web/management-dashboard.html

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[proxystatus Endpoint (blocked_count)]] - concept - web/management-dashboard.html
- [[1Password Service Account Integration (setup wizard)]] - concept - web/setup-wizard.html
- [[AgentShroud Setup Wizard (setup-wizard.html)]] - code - web/setup-wizard.html
- [[Dashboard API Client (api-client.js)]] - concept - web/management-dashboard.html
- [[Dashboard Agent Trust Levels Panel]] - concept - web/management-dashboard.html
- [[Dashboard Audit Trail Panel]] - concept - web/management-dashboard.html
- [[Dashboard Kill Switch Panel (emergency termination)]] - concept - web/management-dashboard.html
- [[Dashboard Live Events Panel (WebSocket)]] - concept - web/management-dashboard.html
- [[Dashboard Security Modules Panel]] - concept - web/management-dashboard.html
- [[Dashboard WebSocket Connection]] - concept - web/management-dashboard.html
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[Wizard Step 2 Container Runtime Detection (DockerPodman)]] - concept - web/setup-wizard.html
- [[Wizard Step 3 Config (Proxy Mode vs Sidecar Mode, gateway port 8080, ws port 8081)]] - concept - web/setup-wizard.html
- [[Wizard Step 4 Secrets Management (1Password SA or manual files)]] - concept - web/setup-wizard.html
- [[Wizard Step 5 Deploy (docker-compose  podman-compose command generation)]] - concept - web/setup-wizard.html
- [[Wizard Step 6 System Verification  Health Checks]] - concept - web/setup-wizard.html
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard.html (Control Center Template)]] - code - gateway/web/templates/dashboard.html

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/web/management-dashboardhtml
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Competitive Intel Store]]
- 1 edge to [[_COMMUNITY_Web Control Center]]

## Top bridge nodes
- [[dashboard()]] - degree 12, connects to 2 communities