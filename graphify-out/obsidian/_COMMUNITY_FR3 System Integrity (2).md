---
type: community
members: 9
---

# FR3: System Integrity (2)

**Members:** 9 nodes

## Members
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[log()_9]] - code - docker/scripts/security-report-retention.sh
- [[log()_10]] - code - docker/scripts/security-scheduler.sh
- [[security-report-retention.sh]] - code - docker/scripts/security-report-retention.sh
- [[security-report-retention.sh script]] - code - docker/scripts/security-report-retention.sh
- [[security-scheduler.sh]] - code - docker/scripts/security-scheduler.sh
- [[security-scheduler.sh script]] - code - docker/scripts/security-scheduler.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FR3_System_Integrity_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_FR3 System Integrity]]

## Top bridge nodes
- [[security-scheduler.sh]] - degree 9, connects to 1 community
