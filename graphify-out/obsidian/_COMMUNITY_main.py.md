---
type: community
cohesion: 0.06
members: 42
---

# main.py.md

**Cohesion:** 0.06 - loosely connected
**Members:** 42 nodes

## Members
- [[1Password credential isolation]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud Security Perimeter]] - concept - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud — System Overview]] - document - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud — Vault Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Architecture Overview]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Audit ledger (hash-verifiable chain)]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Common Issues]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Components_1]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Configuration & Infrastructure]] - document - docs/vault/00 - START HERE/Home.md
- [[Configuration Files]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Data Flow]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Diagrams]] - document - docs/vault/00 - START HERE/Home.md
- [[Enforce mode by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Environment Variables (required)]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Fail-closed by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Health Checks]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Human-in-the-loop approval queue]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Key Design Decisions]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Key Ports]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Kill Switch]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Least privilege MCP permissions]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Logs_1]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Module Index]] - document - docs/vault/00 - START HERE/Home.md
- [[Navigate This Vault]] - document - docs/vault/00 - START HERE/Home.md
- [[Operations]] - document - docs/vault/00 - START HERE/Home.md
- [[PII redacted before forwarding]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Quick Reference — AgentShroud]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Quick Reference_1]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Related Notes_18]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Related Notes_19]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Security Layers (in order)]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Security Mode Toggle]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Shutdown & Recovery]] - document - docs/vault/01 - Architecture/Shutdown & Recovery.md
- [[Start  Stop]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Startup Sequence]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[System Overview]] - document - docs/vault/00 - START HERE/System Overview.md
- [[What It Is]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Who Depends On It]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Why It Exists]] - document - docs/vault/00 - START HERE/System Overview.md
- [[ledger.py]] - document - docs/vault/02 - Modules/Gateway Core/ledger.py.md
- [[main.py]] - document - docs/vault/02 - Modules/Gateway Core/main.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mainpymd
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 3 edges to [[_COMMUNITY_DataLedger]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_main.py_3]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_main.py_2]]
- 1 edge to [[_COMMUNITY_ledger.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_Docker Volumes]]
- 1 edge to [[_COMMUNITY_main.py_1]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_All Dependencies]]

## Top bridge nodes
- [[main.py]] - degree 17, connects to 9 communities
- [[Startup Sequence]] - degree 10, connects to 6 communities
- [[Data Flow]] - degree 11, connects to 5 communities
- [[ledger.py]] - degree 7, connects to 4 communities
- [[Architecture Overview]] - degree 6, connects to 1 community
