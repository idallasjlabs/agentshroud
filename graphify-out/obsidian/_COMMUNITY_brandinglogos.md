---
type: community
members: 25
---

# branding/logos

**Members:** 25 nodes

## Members
- [[.test_all_modules_have_copyright()]] - code - gateway/tests/test_security_audit.py
- [[.test_format_report_string()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_generate_report()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_history_persistence()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_no_eval_or_exec_in_security()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_hardcoded_secrets_in_source()]] - code - gateway/tests/test_security_audit.py
- [[.test_trend_empty_db()]] - code - gateway/tests/test_security_toolchain.py
- [[All security modules should have copyright header.]] - rationale - gateway/tests/test_security_audit.py
- [[Any_41]] - code - gateway/security/health_report.py
- [[Connection]] - code - gateway/security/health_report.py
- [[Format a health report as a human-readable string.      Args         report Fu]] - rationale - gateway/security/health_report.py
- [[Generate a full health report.      Args         summaries Dict mapping tool n]] - rationale - gateway/security/health_report.py
- [[Get score trend for the last N days.      Args         days Number of days to]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking.      Args         db_path]] - rationale - gateway/security/health_report.py
- [[No hardcoded secrets in Python source files.]] - rationale - gateway/tests/test_security_audit.py
- [[Path_13]] - code - gateway/security/health_report.py
- [[Save a health report to history.      Args         score Overall score.]] - rationale - gateway/security/health_report.py
- [[Security modules should not call eval() or exec().          Uses AST analysis]] - rationale - gateway/tests/test_security_audit.py
- [[TestHealthReport]] - code - gateway/tests/test_security_toolchain.py
- [[format_report()]] - code - gateway/security/health_report.py
- [[generate_report()]] - code - gateway/security/health_report.py
- [[get_trend()]] - code - gateway/security/health_report.py
- [[health_report.py]] - code - gateway/security/health_report.py
- [[init_db()]] - code - gateway/security/health_report.py
- [[save_to_history()]] - code - gateway/security/health_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/branding/logos
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Planning Docs]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_Auth & Exception Types]]
- 4 edges to [[_COMMUNITY_Security Docs]]
- 3 edges to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_Slack API Proxy]]

## Top bridge nodes
- [[health_report.py]] - degree 10, connects to 4 communities
- [[generate_report()]] - degree 12, connects to 3 communities
- [[Any_41]] - degree 6, connects to 2 communities
- [[TestHealthReport]] - degree 6, connects to 2 communities
- [[Path_13]] - degree 10, connects to 1 community