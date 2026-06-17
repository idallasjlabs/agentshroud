---
type: community
cohesion: 0.24
members: 10
---

# Module Group 381

**Cohesion:** 0.24 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_clean_when_installed_but_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if the most recent report file was written within max_age_hours.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 29 AI Model & Supply Chain Integrity (0-5). MITRE ATLAS, OWASP LLM]] - rationale - gateway/security/scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[_is_fresh()]] - code - gateway/security/scanner_integration.py
- [[_score_ai_model_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_381
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Security Scanner Integration]]
- 4 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 2 edges to [[_COMMUNITY_Module Group 122]]
- 2 edges to [[_COMMUNITY_Module Group 228]]
- 2 edges to [[_COMMUNITY_Module Group 134]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 2 edges to [[_COMMUNITY_Module Group 210]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 269]]
- 1 edge to [[_COMMUNITY_Module Group 163]]
- 1 edge to [[_COMMUNITY_Module Group 335]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 9 communities
- [[_is_fresh()]] - degree 8, connects to 3 communities
- [[_score_ai_model_supply_chain()]] - degree 6, connects to 2 communities
- [[TestGetTrivySummary]] - degree 4, connects to 1 community
- [[.test_clean_when_installed_but_no_report()]] - degree 3, connects to 1 community