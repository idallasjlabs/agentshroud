---
type: community
cohesion: 0.15
members: 24
---

# run_multi_host

**Cohesion:** 0.15 - loosely connected
**Members:** 24 nodes

## Members
- [[_sunday_trivy_db_fresh()]] - code - scripts/lib/sunday-scan.sh
- [[_sunday_warn_expiring_acceptances()]] - code - scripts/lib/sunday-scan.sh
- [[die()_2]] - code - scripts/lib/sunday-scan.sh
- [[err()_2]] - code - scripts/lib/sunday-scan.sh
- [[log()_7]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh]] - code - scripts/lib/sunday-scan.sh
- [[sunday-scan.sh script]] - code - scripts/lib/sunday-scan.sh
- [[sunday_deadline_epoch()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_dev_handoff_gate()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_ensure_trivy()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_handoff_status()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_hermes_container()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_notify_direct()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_refresh_trivy_db()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_resolve_scan_image()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_restore_stack()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_run_scan_gate()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_run_summary()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_stack_check()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_stack_rollback()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_stack_start()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_stop_apply()]] - code - scripts/lib/sunday-scan.sh
- [[sunday_telegram_post()]] - code - scripts/lib/sunday-scan.sh
- [[warn()_4]] - code - scripts/lib/sunday-scan.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run_multi_host
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY__wrap_response() (2)]]

## Top bridge nodes
- [[sunday-scan.sh]] - degree 28, connects to 3 communities
- [[sunday_run_scan_gate()]] - degree 12, connects to 2 communities
- [[_sunday_warn_expiring_acceptances()]] - degree 4, connects to 1 community
- [[sunday_dev_handoff_gate()]] - degree 2, connects to 1 community
- [[sunday_handoff_status()]] - degree 2, connects to 1 community
