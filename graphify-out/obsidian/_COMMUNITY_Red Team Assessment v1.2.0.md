---
type: community
members: 12
---

# Red Team Assessment v1.2.0

**Members:** 12 nodes

## Members
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[log()_8]] - code - docker/scripts/security-report.sh
- [[log()_9]] - code - docker/scripts/security-report-retention.sh
- [[log()_10]] - code - docker/scripts/security-scheduler.sh
- [[security-report-retention.sh]] - code - docker/scripts/security-report-retention.sh
- [[security-report-retention.sh script]] - code - docker/scripts/security-report-retention.sh
- [[security-report.sh]] - code - docker/scripts/security-report.sh
- [[security-report.sh script]] - code - docker/scripts/security-report.sh
- [[security-scheduler.sh]] - code - docker/scripts/security-scheduler.sh
- [[security-scheduler.sh script]] - code - docker/scripts/security-scheduler.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Red_Team_Assessment_v120
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Regression guard (2026-08-30) the report scanned latest tags while deploys…]]

## Top bridge nodes
- [[security-scheduler.sh]] - degree 8, connects to 1 community
- [[security-report.sh]] - degree 4, connects to 1 community
