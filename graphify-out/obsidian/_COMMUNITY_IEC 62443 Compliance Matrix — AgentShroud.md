---
type: community
members: 32
---

# IEC 62443 Compliance Matrix — AgentShroud

**Members:** 32 nodes

## Members
- [[04-security]] - document - docs/diagrams/04-security.md
- [[11. Trust Boundary Diagram]] - document - docs/diagrams/04-security.md
- [[12. Credential Flow Diagram]] - document - docs/diagrams/04-security.md
- [[13. Network Security Diagram — Egress Controls]] - document - docs/diagrams/04-security.md
- [[AgentShroud — Security & Access Diagrams]] - document - docs/diagrams/04-security.md
- [[Credential Flow Diagram (op-proxy)]] - concept - docs/diagrams/04-security.md
- [[Current Assessment SL 2 (with SL 3 capabilities in FR 2, FR 3, FR 4, FR 6)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 1 Identification and Authentication Control (IAC)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 2 Use Control (UC)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 3 System Integrity (SI)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 4 Data Confidentiality (DC)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 5 Restricted Data Flow (RDF)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 6 Timely Response to Events (TRE)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 7 Resource Availability (RA)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR1 Identification and Authentication Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR2 Use Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR5 Restricted Data Flow]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR6 Timely Response to Events]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR7 Resource Availability]] - concept - docs/compliance/iec-62443-matrix.md
- [[IEC 62443 Compliance Matrix — AgentShroud]] - document - docs/compliance/iec-62443-matrix.md
- [[Key Components Referenced (v1.0.0)]] - document - docs/compliance/iec-62443-matrix.md
- [[Network Security Diagram — Egress Controls]] - concept - docs/diagrams/04-security.md
- [[Overview_4]] - document - docs/compliance/iec-62443-matrix.md
- [[Summary_18]] - document - docs/compliance/iec-62443-matrix.md
- [[agentshroud-openclaw bot container]] - concept - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh]] - code - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh script]] - code - scripts/backup-bot-memory.sh
- [[disaster-recovery-backup.sh]] - code - scripts/disaster-recovery-backup.sh
- [[disaster-recovery-backup.sh script]] - code - scripts/disaster-recovery-backup.sh
- [[iec-62443-matrix]] - document - docs/compliance/iec-62443-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IEC_62443_Compliance_Matrix__AgentShroud
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]]
- 1 edge to [[_COMMUNITY_AgentShroud Semgrep SAST Configuration]]
- 1 edge to [[_COMMUNITY_03-data]]

## Top bridge nodes
- [[FR2 Use Control]] - degree 3, connects to 2 communities
- [[FR3 System Integrity]] - degree 3, connects to 2 communities
- [[04-security]] - degree 4, connects to 1 community
- [[FR4 Data Confidentiality]] - degree 4, connects to 1 community
- [[agentshroud-openclaw bot container]] - degree 3, connects to 1 community
