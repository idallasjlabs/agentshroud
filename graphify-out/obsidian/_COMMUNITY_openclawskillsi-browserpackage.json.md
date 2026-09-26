---
type: community
cohesion: 0.22
members: 10
---

# openclaw/skills/i-browser/package.json

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[._scan_for_canary()]] - code - gateway/security/output_canary.py
- [[.check_response()]] - code - gateway/security/output_canary.py
- [[.get_status()_1]] - code - gateway/security/output_canary.py
- [[Any_53]] - code - gateway/security/output_canary.py
- [[CanaryResult_2]] - code - gateway/security/output_canary.py
- [[Check if response contains the session's canary (prompt leakage detected).]] - rationale - gateway/security/output_canary.py
- [[Result of checking a response for canary presence.]] - rationale - gateway/security/output_canary.py
- [[Return canary status for dashboard.          Args             session_id Sessi]] - rationale - gateway/security/output_canary.py
- [[Scan response text for a specific canary.          Args             session_id]] - rationale - gateway/security/output_canary.py
- [[output_canary.py]] - code - gateway/security/output_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw/skills/i-browser/packagejson
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]

## Top bridge nodes
- [[output_canary.py]] - degree 3, connects to 2 communities
- [[._scan_for_canary()]] - degree 5, connects to 1 community
- [[.check_response()]] - degree 4, connects to 1 community
- [[.get_status()_1]] - degree 3, connects to 1 community