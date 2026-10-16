---
type: community
cohesion: 0.04
members: 63
---

# main.py.md

**Cohesion:** 0.04 - loosely connected
**Members:** 63 nodes

## Members
- [[1Password credential isolation]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud Security Perimeter]] - concept - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud — System Overview]] - document - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud — Vault Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Architecture Overview_1]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Architecture Overview]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Audit ledger (hash-verifiable chain)]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Boot Sequence (Numbered)]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Bot Container (`agentshroud-bot`)]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Common Issues]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Common Startup Failures]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Components_1]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Configuration & Infrastructure]] - document - docs/vault/00 - START HERE/Home.md
- [[Configuration Files]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Container Architecture]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Data Flow]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Diagrams]] - document - docs/vault/00 - START HERE/Home.md
- [[Enforce mode by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Environment Variables (required)]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Fail-closed by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[First-Boot Notes]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Full System Diagram]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Gateway Container (`agentshroud-gateway`)]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Gateway Internal Layer Order]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Health Checks]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Human-in-the-loop approval queue]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Key Design Decisions]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Key Ports]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Kill Switch]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Least privilege MCP permissions]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Logs]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Module Index]] - document - docs/vault/00 - START HERE/Home.md
- [[Navigate This Vault]] - document - docs/vault/00 - START HERE/Home.md
- [[Network Topology]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Operations]] - document - docs/vault/00 - START HERE/Home.md
- [[Overview_2]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[PII redacted before forwarding]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Quick Reference — AgentShroud]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Quick Reference]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Related Notes_7]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Related Notes_8]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Related Notes_9]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Related Notes_10]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Security Layers (in order)]] - document - docs/vault/00 - START HERE/System Overview.md
- [[Security Mode Toggle]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Shutdown & Recovery]] - document - docs/vault/01 - Architecture/Shutdown & Recovery.md
- [[Stage 1 Gateway Container Startup]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Stage 2 Gateway Application Initialization (main.py lifespan)]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Stage 3 Health Check]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Stage 4 Bot Container Startup]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Stage 5 Fully Operational]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Start  Stop]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Startup Indicators]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Startup Sequence_1]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Startup Sequence]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[Summary_1]] - document - docs/vault/01 - Architecture/Architecture Overview.md
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
- 5 edges to [[_COMMUNITY_DataLedger]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_EgressFilter_1]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_ledger.py]]
- 1 edge to [[_COMMUNITY_Docker Volumes]]
- 1 edge to [[_COMMUNITY_main.py_1]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_All Dependencies]]

## Top bridge nodes
- [[main.py]] - degree 17, connects to 10 communities
- [[Data Flow]] - degree 11, connects to 5 communities
- [[Startup Sequence]] - degree 10, connects to 5 communities
- [[ledger.py]] - degree 7, connects to 3 communities
- [[Shutdown & Recovery]] - degree 3, connects to 1 community
