---
type: community
members: 17
---

# StatusResponse

**Members:** 17 nodes

## Members
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[AuthRequired_1]] - code
- [[Detailed health check endpoint — authentication required. Returns full system…]] - rationale - gateway/ingest_api/routes/health.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Minimal health check endpoint — no authentication required. Returns only basic…]] - rationale - gateway/ingest_api/routes/health.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[get_2]] - code
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StatusResponse
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_GatewayConfig]]

## Top bridge nodes
- [[StatusResponse]] - degree 10, connects to 2 communities
- [[health_check_detail()]] - degree 5, connects to 1 community
- [[health_check()]] - degree 3, connects to 1 community
