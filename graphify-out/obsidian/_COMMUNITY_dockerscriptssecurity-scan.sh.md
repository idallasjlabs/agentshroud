---
type: community
cohesion: 0.68
members: 8
---

# docker/scripts/security-scan.sh

**Cohesion:** 0.68 - moderately connected
**Members:** 8 nodes

## Members
- [[alert_if_critical()]] - code - docker/scripts/security-scan.sh
- [[dockerscriptssecurity-scan.sh]] - code - docker/scripts/security-scan.sh
- [[log()]] - code - docker/scripts/security-scan.sh
- [[run_clamav()]] - code - docker/scripts/security-scan.sh
- [[run_oscap()]] - code - docker/scripts/security-scan.sh
- [[run_sbom()]] - code - docker/scripts/security-scan.sh
- [[run_trivy()]] - code - docker/scripts/security-scan.sh
- [[security-scan.sh script]] - code - docker/scripts/security-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/scripts/security-scansh
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh_1]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]

## Top bridge nodes
- [[dockerscriptssecurity-scan.sh]] - degree 15, connects to 5 communities
