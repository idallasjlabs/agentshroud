---
type: community
cohesion: 0.16
members: 18
---

# Security Scheduler (scripts)

**Cohesion:** 0.16 - loosely connected
**Members:** 18 nodes

## Members
- [[_stamp_read()]] - code - docker/scripts/security-scheduler.sh
- [[_stamp_write()]] - code - docker/scripts/security-scheduler.sh
- [[alert_critical()]] - code - docker/scripts/security-entrypoint.sh
- [[gateway-seccomp.json (Docker seccomp profile)]] - code - docker/seccomp/gateway-seccomp.json
- [[gateway-start.sh]] - code - docker/scripts/gateway-start.sh
- [[gateway-start.sh script]] - code - docker/scripts/gateway-start.sh
- [[log()_1]] - code - docker/scripts/security-entrypoint.sh
- [[log()_3]] - code - docker/scripts/security-report.sh
- [[log()_2]] - code - docker/scripts/security-report-retention.sh
- [[log()_5]] - code - docker/scripts/security-scheduler.sh
- [[security-entrypoint.sh]] - code - docker/scripts/security-entrypoint.sh
- [[security-entrypoint.sh script]] - code - docker/scripts/security-entrypoint.sh
- [[security-report-retention.sh]] - code - docker/scripts/security-report-retention.sh
- [[security-report-retention.sh script]] - code - docker/scripts/security-report-retention.sh
- [[security-report.sh]] - code - docker/scripts/security-report.sh
- [[security-report.sh script]] - code - docker/scripts/security-report.sh
- [[security-scheduler.sh]] - code - docker/scripts/security-scheduler.sh
- [[security-scheduler.sh script]] - code - docker/scripts/security-scheduler.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Scheduler_scripts
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]

## Top bridge nodes
- [[security-scheduler.sh]] - degree 9, connects to 1 community
- [[security-entrypoint.sh]] - degree 5, connects to 1 community
- [[security-report.sh]] - degree 4, connects to 1 community