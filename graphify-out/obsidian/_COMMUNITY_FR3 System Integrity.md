---
type: community
cohesion: 0.14
members: 26
---

# FR3: System Integrity

**Cohesion:** 0.14 - loosely connected
**Members:** 26 nodes

## Members
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[alert_if_critical()]] - code - docker/scripts/security-scan.sh
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[dockerscriptssecurity-scan.sh]] - code - docker/scripts/security-scan.sh
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[log()_3]] - code - docker/scripts/security-report.sh
- [[log()_4]] - code - docker/scripts/security-report-retention.sh
- [[log()_5]] - code - docker/scripts/security-scan.sh
- [[log()_6]] - code - docker/scripts/security-scheduler.sh
- [[run_clamav()]] - code - docker/scripts/security-scan.sh
- [[run_oscap()]] - code - docker/scripts/security-scan.sh
- [[run_sbom()]] - code - docker/scripts/security-scan.sh
- [[run_trivy()]] - code - docker/scripts/security-scan.sh
- [[scan.sh]] - code - docker/scripts/scan.sh
- [[scan.sh script]] - code - docker/scripts/scan.sh
- [[security-report-retention.sh]] - code - docker/scripts/security-report-retention.sh
- [[security-report-retention.sh script]] - code - docker/scripts/security-report-retention.sh
- [[security-report.sh]] - code - docker/scripts/security-report.sh
- [[security-report.sh script]] - code - docker/scripts/security-report.sh
- [[security-scan.sh (unified scan dispatcher)]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh script_1]] - code - docker/scripts/security-scan.sh
- [[security-scheduler.sh]] - code - docker/scripts/security-scheduler.sh
- [[security-scheduler.sh script]] - code - docker/scripts/security-scheduler.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FR3_System_Integrity
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_InjectionAction]]
- 2 edges to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_parse_clamscan_output]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py_1]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[FR3 System Integrity]] - degree 10, connects to 6 communities
- [[dockerscriptssecurity-scan.sh]] - degree 15, connects to 4 communities
- [[security-scan.sh (unified scan dispatcher)]] - degree 5, connects to 1 community
- [[heuristic_classifier.py]] - degree 3, connects to 1 community
- [[config_integrity.py]] - degree 2, connects to 1 community
