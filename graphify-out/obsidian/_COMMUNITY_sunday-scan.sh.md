---
type: community
members: 11
---

# sunday-scan.sh

**Members:** 11 nodes

## Members
- [[_sunday_warn_expiring_acceptances()]] - code - scripts/lib/sunday-scan.sh
- [[die()_2]] - code - scripts/lib/sunday-scan.sh
- [[log()_9]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh script]] - code - scripts/lib/sunday-scan.sh
- [[sunday_dev_handoff_gate()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_ensure_trivy()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_handoff_status()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_resolve_scan_image()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_run_scan_gate()]] - code - scripts/lib/sunday-scan.sh
- [[warn()_4]] - code - scripts/lib/sunday-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday-scansh
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_colima-health-check.sh]]
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 1 edge to [[_COMMUNITY_Sunday Upgrade prompt]]

## Top bridge nodes
- [[sunday-scan.sh]] - degree 15, connects to 3 communities
- [[sunday_run_scan_gate()]] - degree 9, connects to 2 communities
- [[_sunday_warn_expiring_acceptances()]] - degree 4, connects to 1 community
