---
type: community
members: 10
---

# export-bot-conversations.py (2)

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
TABLE source_file, type FROM #community/export-bot-conversationspy_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_AuditEvent]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (3)]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue (2)]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]

## Top bridge nodes
- [[iec-62443-matrix]] - degree 8, connects to 4 communities
- [[FR5 Restricted Data Flow]] - degree 4, connects to 3 communities
- [[agentshroud-openclaw bot container]] - degree 3, connects to 1 community
- [[FR7 Resource Availability]] - degree 3, connects to 1 community
- [[FR6 Timely Response to Events]] - degree 2, connects to 1 community
