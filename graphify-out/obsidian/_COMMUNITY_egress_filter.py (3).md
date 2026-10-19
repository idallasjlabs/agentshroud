---
type: community
members: 13
---

# egress_filter.py (3)

**Members:** 13 nodes

## Members
- [[FR1 Identification and Authentication Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR5 Restricted Data Flow]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR6 Timely Response to Events]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR7 Resource Availability]] - concept - docs/compliance/iec-62443-matrix.md
- [[agentshroud-openclaw bot container]] - concept - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh]] - code - scripts/backup-bot-memory.sh
- [[backup-bot-memory.sh script]] - code - scripts/backup-bot-memory.sh
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[disaster-recovery-backup.sh]] - code - scripts/disaster-recovery-backup.sh
- [[disaster-recovery-backup.sh script]] - code - scripts/disaster-recovery-backup.sh
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[iec-62443-matrix]] - document - docs/compliance/iec-62443-matrix.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/egress_filterpy_3
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue (2)]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine (2)]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_parse_clamscan_output]]
- 1 edge to [[_COMMUNITY_AuditEvent]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (3)]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py (2)]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]

## Top bridge nodes
- [[FR3 System Integrity]] - degree 9, connects to 6 communities
- [[iec-62443-matrix]] - degree 8, connects to 3 communities
- [[FR5 Restricted Data Flow]] - degree 4, connects to 3 communities
- [[heuristic_classifier.py]] - degree 3, connects to 2 communities
- [[agentshroud-openclaw bot container]] - degree 3, connects to 1 community
