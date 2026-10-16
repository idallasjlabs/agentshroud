---
type: community
cohesion: 0.07
members: 30
---

# ADR-005: SHA-256 Hash Chain Audit Integrity

**Cohesion:** 0.07 - loosely connected
**Members:** 30 nodes

## Members
- [[11 Cron Jobs]] - document - docs/architecture/agentic-os.md
- [[11. Automated Operations]] - document - docs/architecture/agentic-os.md
- [[ADR-005-sha256-hash-chain-audit-integrity]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[ADR-005 SHA-256 Hash Chain Audit Integrity]] - concept - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Approval Queue (human-in-the-loop)]] - concept - docs/architecture/agentic-os.md
- [[AuditEntry (data entity)]] - concept - docs/data/data-dictionary.md
- [[Blocked by default (private RFC1918 ranges)]] - image - docs/diagrams/images/diagram-05-network-topology.svg
- [[Consequences_1]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Context_2]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[DNS Filter]] - concept - docs/architecture/system-architecture.md
- [[Decision_3]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Egress Monitor]] - concept - docs/architecture/system-architecture.md
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - document - docs/api/api-reference.md
- [[Hash Chain Structure_1]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Implementation Details]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[InspectionResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[Ledger DB (SQLiteaiosqlite)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Negative Consequences]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[OpenClaw Integration Guide (v0.9.0)]] - document - docs/api/integration-guide.md
- [[Positive Consequences]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[SOC Dashboard]] - document - docs/architecture/agentic-os.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[Status_2]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[audit_entries SQLite table]] - code - docs/data/schema-documentation.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewaysocrouter.py (SOC Shared Command Layer)]] - code - docs/api/api-reference.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md
- [[ledger.py (audit trail, SHA-256 hashing)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp_audit_entries SQLite table]] - code - docs/data/schema-documentation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-005_SHA-256_Hash_Chain_Audit_Integrity
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)]]
- 1 edge to [[_COMMUNITY_AgentShroud Agentic OS]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context)]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 7, connects to 2 communities
- [[ADR-005 SHA-256 Hash Chain Audit Integrity]] - degree 10, connects to 1 community
- [[11. Automated Operations]] - degree 3, connects to 1 community
- [[Approval Queue (human-in-the-loop)]] - degree 2, connects to 1 community
- [[Ledger DB (SQLiteaiosqlite)]] - degree 2, connects to 1 community
