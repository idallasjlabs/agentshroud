---
type: community
cohesion: 0.10
members: 23
---

# Restart Procedure

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Members
- [[After Config Change]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[After Secret Rotation]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[AgentShroud Minimal Docker Compose]] - document - examples/docker-compose.minimal.yml
- [[AgentShroud Production Docker Compose]] - document - examples/docker-compose.production.yml
- [[Bot Only Restart]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Container Errors]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Crash Recovery]] - document - docs/vault/08 - Runbooks/Crash Recovery.md
- [[First Time Setup]] - document - docs/vault/08 - Runbooks/First Time Setup.md
- [[Full Stack Restart]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Gateway Only Restart]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Health Checks]] - document - docs/vault/08 - Runbooks/Health Checks.md
- [[Kill Switch Procedure]] - document - docs/vault/08 - Runbooks/Kill Switch Procedure.md
- [[Related Notes_17]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Restart Procedure_1]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Restart Procedure]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Restart Verification]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Startup Errors]] - document - docs/vault/07 - Errors & Troubleshooting/Startup Errors.md
- [[Troubleshooting Matrix]] - document - docs/vault/07 - Errors & Troubleshooting/Troubleshooting Matrix.md
- [[When to Restart]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Zero-Downtime Restart (Advanced)]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[docker-commands]] - document - examples/docker-commands.md
- [[store.py]] - code - gateway/approval_queue/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Restart_Procedure
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_aiosqlite]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_Container Errors]]
- 1 edge to [[_COMMUNITY_Gateway Container Startup Failures]]
- 1 edge to [[_COMMUNITY_troubleshooting]]
- 1 edge to [[_COMMUNITY_Crash Recovery]]
- 1 edge to [[_COMMUNITY_First Time Setup]]
- 1 edge to [[_COMMUNITY_Health Checks]]
- 1 edge to [[_COMMUNITY_Kill Switch Procedure]]
- 1 edge to [[_COMMUNITY_Docker Commands Reference]]

## Top bridge nodes
- [[aiosqlite_1]] - degree 5, connects to 4 communities
- [[Troubleshooting Matrix]] - degree 8, connects to 3 communities
- [[store.py]] - degree 7, connects to 3 communities
- [[Container Errors]] - degree 4, connects to 2 communities
- [[Crash Recovery]] - degree 6, connects to 1 community