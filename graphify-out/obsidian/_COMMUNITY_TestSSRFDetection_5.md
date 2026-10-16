---
type: community
cohesion: 0.22
members: 10
---

# TestSSRFDetection

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-_scan_for_canary()]] - code - gateway/security/output_canary.py
- [[dot-check_response()]] - code - gateway/security/output_canary.py
- [[dot-get_status()]] - code - gateway/security/output_canary.py
- [[Any_5]] - code - gateway/security/output_canary.py
- [[CanaryResult]] - code - gateway/security/output_canary.py
- [[Check if response contains the session's canary (prompt leakage detected).]] - rationale - gateway/security/output_canary.py
- [[Result of checking a response for canary presence.]] - rationale - gateway/security/output_canary.py
- [[Return canary status for dashboard.          Args             session_id Sessi]] - rationale - gateway/security/output_canary.py
- [[Scan response text for a specific canary.          Args             session_id]] - rationale - gateway/security/output_canary.py
- [[output_canary.py]] - code - gateway/security/output_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFDetection
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TestOutputCanary]]

## Top bridge nodes
- [[output_canary.py]] - degree 3, connects to 2 communities
- [[dot-_scan_for_canary()]] - degree 5, connects to 1 community
- [[dot-check_response()]] - degree 4, connects to 1 community
- [[dot-get_status()]] - degree 3, connects to 1 community
