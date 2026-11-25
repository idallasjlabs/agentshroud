---
type: community
members: 40
---

# generate_report

**Members:** 40 nodes

## Members
- [[dot-test_all_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_empty_summaries()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_error_status_gets_50()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_format_report_string()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_generate_report()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_a()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_b()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_c()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_d()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_f()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_history_persistence()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_mixed_severities()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_one_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_partial_tools()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_perfect_score()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_score_floor()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trend_empty_db()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_24]] - code
- [[Calculate score for a single tool (0-100). Args summary Tool summary dict…]] - rationale - gateway/security/health_report.py
- [[Calculate weighted overall security score. Args summaries Dict mapping tool…]] - rationale - gateway/security/health_report.py
- [[Connection_1]] - code
- [[Convert score to letter grade. Args score Numeric score (0-100). Returns…]] - rationale - gateway/security/health_report.py
- [[Format a health report as a human-readable string. Args report Full report…]] - rationale - gateway/security/health_report.py
- [[Generate a full health report. Args summaries Dict mapping tool name to…]] - rationale - gateway/security/health_report.py
- [[Get score trend for the last N days. Args days Number of days to look back.…]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking. Args db_path Path to…]] - rationale - gateway/security/health_report.py
- [[Path_20]] - code
- [[Save a health report to history. Args score Overall score. grade Letter…]] - rationale - gateway/security/health_report.py
- [[TestHealthOverallScore]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthScoring]] - code - gateway/tests/test_security_toolchain.py
- [[calculate_overall_score()]] - code - gateway/security/health_report.py
- [[calculate_tool_score()]] - code - gateway/security/health_report.py
- [[format_report()]] - code - gateway/security/health_report.py
- [[generate_report()]] - code - gateway/security/health_report.py
- [[get_trend()]] - code - gateway/security/health_report.py
- [[health_report.py_2]] - code - gateway/security/health_report.py
- [[init_db()]] - code - gateway/security/health_report.py
- [[save_to_history()]] - code - gateway/security/health_report.py
- [[score_to_grade()]] - code - gateway/security/health_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/generate_report
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[health_report.py_2]] - degree 11, connects to 3 communities
- [[generate_report()]] - degree 12, connects to 1 community
- [[TestHealthScoring]] - degree 11, connects to 1 community
- [[calculate_tool_score()]] - degree 11, connects to 1 community
- [[calculate_overall_score()]] - degree 9, connects to 1 community
