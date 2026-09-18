---
type: community
cohesion: 0.25
members: 8
---

# AgentShroud Security Perimeter

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[1Password credential isolation]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[AgentShroud Security Perimeter]] - concept - docs/vault/00 - START HERE/System Overview.md
- [[Audit ledger (hash-verifiable chain)]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Enforce mode by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Fail-closed by default]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Human-in-the-loop approval queue]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[Least privilege MCP permissions]] - rationale - docs/vault/00 - START HERE/System Overview.md
- [[PII redacted before forwarding]] - rationale - docs/vault/00 - START HERE/System Overview.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Perimeter
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[AgentShroud Security Perimeter]] - degree 8, connects to 1 community
- [[Audit ledger (hash-verifiable chain)]] - degree 2, connects to 1 community
- [[Human-in-the-loop approval queue]] - degree 2, connects to 1 community