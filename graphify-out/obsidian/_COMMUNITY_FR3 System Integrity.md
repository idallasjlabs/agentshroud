---
type: community
cohesion: 0.14
members: 18
---

# FR3: System Integrity

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
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
TABLE source_file, type FROM #community/FR3_System_Integrity
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier_1]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[FR3 System Integrity]] - degree 10, connects to 7 communities
- [[heuristic_classifier.py]] - degree 3, connects to 2 communities
- [[security-scheduler.sh]] - degree 9, connects to 1 community
- [[security-scan.sh (unified scan dispatcher)]] - degree 5, connects to 1 community
- [[security-report.sh]] - degree 5, connects to 1 community
