---
type: community
cohesion: 0.29
members: 8
---

# agentshroud-ssh-exec.sh

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[Daily CVE Triage & Remediation Scan]] - document - docker/config/openclaw/cron/jobs.json
- [[_fmt()]] - code - docker/config/openclaw/cron/scripts/daily-checkin.sh
- [[_json_escape()]] - code - docker/scripts/agentshroud-ssh-exec.sh
- [[_read_token_file()]] - code - docker/scripts/agentshroud-ssh-exec.sh
- [[agentshroud-ssh-exec.sh]] - code - docker/scripts/agentshroud-ssh-exec.sh
- [[agentshroud-ssh-exec.sh script]] - code - docker/scripts/agentshroud-ssh-exec.sh
- [[daily-checkin.sh]] - code - docker/config/openclaw/cron/scripts/daily-checkin.sh
- [[daily-checkin.sh script]] - code - docker/config/openclaw/cron/scripts/daily-checkin.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-ssh-execsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 1 edge to [[_COMMUNITY_agent_cve_registry.py]]

## Top bridge nodes
- [[agentshroud-ssh-exec.sh]] - degree 6, connects to 1 community
- [[Daily CVE Triage & Remediation Scan]] - degree 2, connects to 1 community
