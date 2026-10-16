---
type: community
cohesion: 0.16
members: 23
---

# FR3: System Integrity

**Cohesion:** 0.16 - loosely connected
**Members:** 23 nodes

## Members
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[alert_if_critical()]] - code - docker/scripts/security-scan.sh
- [[dockerscriptssecurity-scan.sh]] - code - docker/scripts/security-scan.sh
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[log()_6]] - code - docker/scripts/security-report.sh
- [[log()_7]] - code - docker/scripts/security-report-retention.sh
- [[log()_8]] - code - docker/scripts/security-scan.sh
- [[log()_9]] - code - docker/scripts/security-scheduler.sh
- [[run_clamav()]] - code - docker/scripts/security-scan.sh
- [[run_oscap()]] - code - docker/scripts/security-scan.sh
- [[run_sbom()]] - code - docker/scripts/security-scan.sh
- [[run_trivy()]] - code - docker/scripts/security-scan.sh
- [[scan.sh_1]] - code - docker/scripts/scan.sh
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
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh_2]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]
- 1 edge to [[_COMMUNITY_ServiceManager_1]]

## Top bridge nodes
- [[dockerscriptssecurity-scan.sh]] - degree 15, connects to 5 communities
- [[security-scan.sh (unified scan dispatcher)]] - degree 5, connects to 2 communities
