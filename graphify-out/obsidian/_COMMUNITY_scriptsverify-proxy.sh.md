---
type: community
members: 11
---

# scripts/verify-proxy.sh

**Members:** 11 nodes

## Members
- [[LOW Findings_1]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[MEDIUM Findings_1]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-L1 No Global Security Headers Middleware (Reopened from R2-L1)]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-L2 WebSocket Connection Leak in ws_logs (Reopened from R2-L2)]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-L3 OCI Image Version Labels Still Outdated (Reopened from R2-L3)]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-L4 Dashboard WS Activity Endpoint Accepts Both Master and Scoped Tokens]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-L5 Backup Files Contain Pre-Hardening Code]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-M1 Missing `aiohttp` Dependency in requirements.txt (Reopened from R2-M1)]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-M2 Management WebSocket Endpoints Still Use Master Auth Token (Reopened from R2-M2)]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[R3-M3 Stale Version String in Root Dashboard HTML]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md
- [[Round 3 New Findings]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-r3.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/verify-proxysh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Planning Docs]]

## Top bridge nodes
- [[Round 3 New Findings]] - degree 3, connects to 1 community