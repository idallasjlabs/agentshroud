---
type: community
cohesion: 0.18
members: 20
---

# health_report.py

**Cohesion:** 0.18 - loosely connected
**Members:** 20 nodes

## Members
- [[Any_55]] - code - gateway/security/health_report.py
- [[Calculate score for a single tool (0-100).      Args         summary Tool summ]] - rationale - gateway/security/health_report.py
- [[Calculate weighted overall security score.      Args         summaries Dict ma]] - rationale - gateway/security/health_report.py
- [[Connection]] - code - gateway/security/health_report.py
- [[Convert score to letter grade.      Args         score Numeric score (0-100).]] - rationale - gateway/security/health_report.py
- [[Format a health report as a human-readable string.      Args         report Fu]] - rationale - gateway/security/health_report.py
- [[Generate a full health report.      Args         summaries Dict mapping tool n]] - rationale - gateway/security/health_report.py
- [[Get score trend for the last N days.      Args         days Number of days to]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking.      Args         db_path]] - rationale - gateway/security/health_report.py
- [[Path_31]] - code - gateway/security/health_report.py
- [[Save a health report to history.      Args         score Overall score.]] - rationale - gateway/security/health_report.py
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
TABLE source_file, type FROM #community/health_reportpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_wazuh_client.py]]
- 2 edges to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[health_report.py]] - degree 21, connects to 9 communities