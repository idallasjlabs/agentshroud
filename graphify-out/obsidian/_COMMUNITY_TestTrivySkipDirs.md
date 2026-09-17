---
type: community
cohesion: 0.40
members: 5
---

# TestTrivySkipDirs

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_daily_fs_scan_skips_security_log_tree()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_skip_dirs_flag_when_omitted()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skip_dirs_added_to_command()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivySkipDirs_1]] - code - gateway/tests/test_daily_cve_report.py
- [[The daily fs scan of  must exclude varlogsecurity (trivy's own         cache]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTrivySkipDirs
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestTrivySkipDirs_1]] - degree 4, connects to 1 community
- [[The daily fs scan of  must exclude varlogsecurity (trivy's own         cache]] - degree 2, connects to 1 community