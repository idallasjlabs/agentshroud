---
type: community
cohesion: 0.22
members: 10
---

# Iec 62443 Matrix (compliance)

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[FR1 Identification and Authentication Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR5 Restricted Data Flow]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR6 Timely Response to Events]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR7 Resource Availability]] - concept - docs/compliance/iec-62443-matrix.md
- [[agentshroud-openclaw bot container]] - concept - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh]] - code - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh script]] - code - scripts/backup-bot-memory.sh
- [[disaster-recovery-backup.sh]] - code - scripts/disaster-recovery-backup.sh
- [[disaster-recovery-backup.sh script]] - code - scripts/disaster-recovery-backup.sh
- [[iec-62443-matrix]] - document - docs/compliance/iec-62443-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Iec_62443_Matrix_compliance
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Audit Export]]
- 1 edge to [[_COMMUNITY_Egress Approval (security)]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Health Report (security)]]
- 1 edge to [[_COMMUNITY_Export Bot Conversations (scripts)]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Iec 62443 Matrix (compliance)]]
- 1 edge to [[_COMMUNITY_04 Security (diagrams)]]

## Top bridge nodes
- [[iec-62443-matrix]] - degree 8, connects to 4 communities
- [[FR5 Restricted Data Flow]] - degree 4, connects to 3 communities
- [[FR7 Resource Availability]] - degree 3, connects to 1 community
- [[agentshroud-openclaw bot container]] - degree 3, connects to 1 community
- [[FR6 Timely Response to Events]] - degree 2, connects to 1 community