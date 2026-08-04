---
type: community
cohesion: 0.09
members: 40
---

# Module Group 114

**Cohesion:** 0.09 - loosely connected
**Members:** 40 nodes

## Members
- [[.test_all_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_empty_summaries()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_error_status_gets_50()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_format_report_string()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_generate_report()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_grade_a()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_grade_b()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_grade_c()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_grade_d()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_grade_f()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_history_persistence()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_mixed_severities()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_one_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_partial_tools()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_perfect_score()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_score_floor()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_trend_empty_db()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_37]] - code - gateway/security/health_report.py
- [[Calculate score for a single tool (0-100).      Args         summary Tool summ]] - rationale - gateway/security/health_report.py
- [[Calculate weighted overall security score.      Args         summaries Dict ma]] - rationale - gateway/security/health_report.py
- [[Connection]] - code - gateway/security/health_report.py
- [[Convert score to letter grade.      Args         score Numeric score (0-100).]] - rationale - gateway/security/health_report.py
- [[Format a health report as a human-readable string.      Args         report Fu]] - rationale - gateway/security/health_report.py
- [[Generate a full health report.      Args         summaries Dict mapping tool n]] - rationale - gateway/security/health_report.py
- [[Get score trend for the last N days.      Args         days Number of days to]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking.      Args         db_path]] - rationale - gateway/security/health_report.py
- [[Path_12]] - code - gateway/security/health_report.py
- [[Save a health report to history.      Args         score Overall score.]] - rationale - gateway/security/health_report.py
- [[TestHealthOverallScore]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthScoring]] - code - gateway/tests/test_security_toolchain.py
- [[calculate_overall_score()]] - code - gateway/security/health_report.py
- [[calculate_tool_score()]] - code - gateway/security/health_report.py
- [[format_report()]] - code - gateway/security/health_report.py
- [[generate_report()]] - code - gateway/security/health_report.py
- [[get_trend()]] - code - gateway/security/health_report.py
- [[health_report.py]] - code - gateway/security/health_report.py
- [[init_db()]] - code - gateway/security/health_report.py
- [[save_to_history()]] - code - gateway/security/health_report.py
- [[score_to_grade()]] - code - gateway/security/health_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_114
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 141]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]

## Top bridge nodes
- [[TestHealthScoring]] - degree 12, connects to 2 communities
- [[health_report.py]] - degree 10, connects to 2 communities
- [[TestHealthReport]] - degree 6, connects to 2 communities
- [[TestHealthOverallScore]] - degree 5, connects to 2 communities
- [[generate_report()]] - degree 12, connects to 1 community
