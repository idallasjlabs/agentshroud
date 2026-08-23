---
type: community
cohesion: 0.08
members: 27
---

# Adr 005 Sha256 Hash (adr)

**Cohesion:** 0.08 - loosely connected
**Members:** 27 nodes

## Members
- [[ADR-005-sha256-hash-chain-audit-integrity]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[ADR-005 SHA-256 Hash Chain Audit Integrity]] - concept - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[AuditEntry (data entity)]] - concept - docs/data/data-dictionary.md
- [[Blocked by default (private RFC1918 ranges)]] - image - docs/diagrams/images/diagram-05-network-topology.svg
- [[Consequences_4]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Context_4]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[DNS Filter]] - concept - docs/architecture/system-architecture.md
- [[Decision_6]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Egress Monitor]] - concept - docs/architecture/system-architecture.md
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - document - docs/api/api-reference.md
- [[Hash Chain Structure]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Implementation Details]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[Ingest API (POST ingest)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[InspectionResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[Ledger DB (SQLiteaiosqlite)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Negative Consequences_4]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[OpenClaw Integration Guide (v0.9.0)]] - document - docs/api/integration-guide.md
- [[Positive Consequences_4]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[SecurityFinding (data entity)]] - concept - docs/data/data-dictionary.md
- [[Status_4]] - document - docs/architecture/adr/ADR-005-sha256-hash-chain-audit-integrity.md
- [[URLAnalysisResult (data entity)]] - concept - docs/data/data-dictionary.md
- [[audit_entries SQLite table]] - code - docs/data/schema-documentation.md
- [[egress-config.yml]] - code - docs/data/schema-documentation.md
- [[gatewayingest_apimain.py]] - code - docs/api/api-reference.md
- [[gatewaywebapi.py (Web control center)]] - code - docs/api/api-reference.md
- [[ledger.py (audit trail, SHA-256 hashing)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[mcp_audit_entries SQLite table]] - code - docs/data/schema-documentation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Adr_005_Sha256_Hash_adr
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Adr 009 Enforce By (adr)]]
- 1 edge to [[_COMMUNITY_Diagram 03 Gateway Components (images)]]
- 1 edge to [[_COMMUNITY_Diagram 07 Data Flow (images)]]
- 1 edge to [[_COMMUNITY_Diagram 01 C4 Context (images)]]

## Top bridge nodes
- [[Gateway ManagementControl-Plane API (v1.3.0)]] - degree 7, connects to 2 communities
- [[ADR-005 SHA-256 Hash Chain Audit Integrity]] - degree 10, connects to 1 community
- [[Ledger DB (SQLiteaiosqlite)]] - degree 2, connects to 1 community