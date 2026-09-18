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
