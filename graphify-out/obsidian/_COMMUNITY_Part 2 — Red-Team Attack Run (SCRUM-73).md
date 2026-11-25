---
type: community
members: 14
---

# Part 2 — Red-Team Attack Run (SCRUM-73)

**Members:** 14 nodes

## Members
- [[Part 2 — Red-Team Attack Run (SCRUM-73)]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-1 · Prompt injection — PARTIALLY BLOCKED]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-10 · Subagent  delegation privilege escalation — BLOCKED]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-11 · MCP-server compromise — BLOCKED-if-configured  dormant-by-default]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-12 · Skill supply-chain — PARTIALLY BLOCKED]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-2 · Inbound encoding bypass — EXPLOITABLE]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-3 · Cross-collaborator data access — BLOCKED (isolation)  gated by RT-6]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-4 · Cross-group access — data BLOCKED  group tool-ACL UNWIRED]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-5 · Shared-memory write poisoning — EXPLOITABLE]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-6 · Owner-identity spoofing via `forward` body — EXPLOITABLE → FIXED]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-7 · Egress exfiltration — BLOCKED in practice  pipeline hook is dead code + residual bypass]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-8 · Multi-bot lateral movement (trust ledger) — EXPLOITABLE (inert)]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-9 · Approval-queue bypass — PARTIALLY EXPLOITABLE]] - document - docs/security/ws-e-audit-v1.2.md
- [[RT-9b · Approval privilege-separation — EXPLOITABLE]] - document - docs/security/ws-e-audit-v1.2.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Part_2__Red-Team_Attack_Run_SCRUM-73
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)]]

## Top bridge nodes
- [[Part 2 — Red-Team Attack Run (SCRUM-73)]] - degree 14, connects to 1 community
