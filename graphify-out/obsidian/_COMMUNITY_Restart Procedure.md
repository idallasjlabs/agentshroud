---
type: community
cohesion: 0.09
members: 24
---

# Restart Procedure

**Cohesion:** 0.09 - loosely connected
**Members:** 24 nodes

## Members
- [[AgentShroud Minimal Docker Compose]] - document - examples/docker-compose.minimal.yml
- [[AgentShroud Production Docker Compose]] - document - examples/docker-compose.production.yml
- [[Container Errors_1]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Container Errors]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Container Won't Stop (Stuck in Stopping)]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Crash Recovery]] - document - docs/vault/08 - Runbooks/Crash Recovery.md
- [[Database Files]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Exit Code Reference]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Health Checks_1]] - document - docs/vault/08 - Runbooks/Health Checks.md
- [[Kill Switch Procedure]] - document - docs/vault/08 - Runbooks/Kill Switch Procedure.md
- [[OOM Kill (Exit Code 137)]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Port Already in Use_1]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Purpose_69]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Read-Only Filesystem Errors]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Related Notes_24]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Related Notes_25]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[Troubleshooting Matrix]] - document - docs/vault/07 - Errors & Troubleshooting/Troubleshooting Matrix.md
- [[WAL Mode]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Where Used_5]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[`no-new-privileges` Security Denial]] - document - docs/vault/07 - Errors & Troubleshooting/Container Errors.md
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[docker-commands]] - document - examples/docker-commands.md
- [[store.py]] - code - gateway/approval_queue/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Restart_Procedure
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_First Time Setup]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_AuditEvent]]
- 1 edge to [[_COMMUNITY_troubleshooting]]
- 1 edge to [[_COMMUNITY_Crash Recovery]]
- 1 edge to [[_COMMUNITY_Health Checks]]
- 1 edge to [[_COMMUNITY_Kill Switch Procedure]]
- 1 edge to [[_COMMUNITY_Docker Commands Reference]]

## Top bridge nodes
- [[Troubleshooting Matrix]] - degree 8, connects to 4 communities
- [[store.py]] - degree 7, connects to 3 communities
- [[aiosqlite]] - degree 5, connects to 3 communities
- [[Crash Recovery]] - degree 6, connects to 2 communities
- [[Container Errors]] - degree 4, connects to 2 communities
