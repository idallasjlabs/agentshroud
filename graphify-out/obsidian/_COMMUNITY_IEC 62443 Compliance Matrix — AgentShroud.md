---
type: community
cohesion: 0.07
members: 33
---

# IEC 62443 Compliance Matrix — AgentShroud

**Cohesion:** 0.07 - loosely connected
**Members:** 33 nodes

## Members
- [[Current Assessment SL 2 (with SL 3 capabilities in FR 2, FR 3, FR 4, FR 6)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 1 Identification and Authentication Control (IAC)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 2 Use Control (UC)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 3 System Integrity (SI)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 5 Restricted Data Flow (RDF)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 6 Timely Response to Events (TRE)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR 7 Resource Availability (RA)]] - document - docs/compliance/iec-62443-matrix.md
- [[FR1 Identification and Authentication Control]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR5 Restricted Data Flow]] - concept - docs/compliance/iec-62443-matrix.md
- [[FR6 Timely Response to Events]] - concept - docs/compliance/iec-62443-matrix.md
- [[IEC 62443 Compliance Matrix — AgentShroud]] - document - docs/compliance/iec-62443-matrix.md
- [[Key Components Referenced (v1.0.0)]] - document - docs/compliance/iec-62443-matrix.md
- [[Overview_29]] - document - docs/compliance/iec-62443-matrix.md
- [[Summary_21]] - document - docs/compliance/iec-62443-matrix.md
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[iec-62443-matrix]] - document - docs/compliance/iec-62443-matrix.md
- [[log()_4]] - code - docker/scripts/security-report.sh
- [[log()_5]] - code - docker/scripts/security-report-retention.sh
- [[log()_6]] - code - docker/scripts/security-scheduler.sh
- [[scan.sh_1]] - code - docker/scripts/scan.sh
- [[scan.sh script]] - code - docker/scripts/scan.sh
- [[security-report-retention.sh]] - code - docker/scripts/security-report-retention.sh
- [[security-report-retention.sh script]] - code - docker/scripts/security-report-retention.sh
- [[security-report.sh]] - code - docker/scripts/security-report.sh
- [[security-report.sh script]] - code - docker/scripts/security-report.sh
- [[security-scan.sh (unified scan dispatcher)]] - code - docker/scripts/security-scan.sh
- [[security-scheduler.sh]] - code - docker/scripts/security-scheduler.sh
- [[security-scheduler.sh script]] - code - docker/scripts/security-scheduler.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IEC_62443_Compliance_Matrix__AgentShroud
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_TestHeuristicClassifier]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]
- 1 edge to [[_COMMUNITY_AgentShroud Semgrep SAST Configuration]]

## Top bridge nodes
- [[FR3 System Integrity]] - degree 9, connects to 5 communities
- [[iec-62443-matrix]] - degree 8, connects to 3 communities
- [[FR5 Restricted Data Flow]] - degree 4, connects to 3 communities
- [[heuristic_classifier.py]] - degree 3, connects to 2 communities
- [[IEC 62443 Compliance Matrix — AgentShroud]] - degree 11, connects to 1 community