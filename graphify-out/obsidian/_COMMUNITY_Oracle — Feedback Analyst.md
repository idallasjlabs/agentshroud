---
type: community
cohesion: 0.40
members: 5
---

# Oracle — Feedback Analyst

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_daily_fs_scan_skips_security_log_tree()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_skip_dirs_flag_when_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skip_dirs_added_to_command()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivySkipDirs]] - code - gateway/tests/test_daily_cve_report.py
- [[The daily fs scan of  must exclude varlogsecurity (trivy's own         cache]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Oracle__Feedback_Analyst
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_PrivacyPolicyEnforcer]]

## Top bridge nodes
- [[TestTrivySkipDirs]] - degree 4, connects to 1 community