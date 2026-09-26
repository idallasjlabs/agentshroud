---
type: community
cohesion: 0.13
members: 20
---

# start-agentshroud.sh

**Cohesion:** 0.13 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_4]] - code - gateway/ingest_api/routes/health.py
- [[Detailed health check endpoint — authentication required.      Returns full syst]] - rationale - gateway/ingest_api/routes/health.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Request_5]] - code - gateway/ingest_api/routes/health.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/health.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()_1]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_A2APolicyEngine]]
- 3 edges to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_main.rs]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_REPORT STRUCTURE]]
- 1 edge to [[_COMMUNITY_InjectionSeverity]]

## Top bridge nodes
- [[health.py]] - degree 11, connects to 5 communities
- [[StatusResponse]] - degree 10, connects to 2 communities
- [[auth_dep()_4]] - degree 4, connects to 1 community