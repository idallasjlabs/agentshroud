---
type: community
members: 17
---

# FR3: System Integrity

**Members:** 17 nodes

## Members
- [[FR3 System Integrity]] - concept - docs/compliance/iec-62443-matrix.md
- [[alert_if_critical()]] - code - docker/scripts/security-scan.sh
- [[config_integrity.py]] - code - gateway/security/config_integrity.py
- [[dockerscriptssecurity-scan.sh]] - code - docker/scripts/security-scan.sh
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[log()_6]] - code - docker/scripts/security-report.sh
- [[log()_7]] - code - docker/scripts/security-scan.sh
- [[run_clamav()]] - code - docker/scripts/security-scan.sh
- [[run_oscap()]] - code - docker/scripts/security-scan.sh
- [[run_sbom()]] - code - docker/scripts/security-scan.sh
- [[run_trivy()]] - code - docker/scripts/security-scan.sh
- [[scan.sh_1]] - code - docker/scripts/scan.sh
- [[scan.sh script]] - code - docker/scripts/scan.sh
- [[security-report.sh]] - code - docker/scripts/security-report.sh
- [[security-report.sh script]] - code - docker/scripts/security-report.sh
- [[security-scan.sh (unified scan dispatcher)]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh script_1]] - code - docker/scripts/security-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FR3_System_Integrity
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_FR3 System Integrity (2)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh (3)]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine (2)]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_PipelineAction (2)]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_egress_filter.py (2)]]

## Top bridge nodes
- [[FR3 System Integrity]] - degree 10, connects to 6 communities
- [[dockerscriptssecurity-scan.sh]] - degree 15, connects to 5 communities
- [[security-scan.sh (unified scan dispatcher)]] - degree 5, connects to 2 communities
- [[heuristic_classifier.py]] - degree 3, connects to 2 communities
- [[security-report.sh]] - degree 5, connects to 1 community
