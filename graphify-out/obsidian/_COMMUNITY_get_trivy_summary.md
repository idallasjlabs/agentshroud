---
type: community
cohesion: 0.12
members: 22
---

# get_trivy_summary

**Cohesion:** 0.12 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-test_clean_when_installed_but_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_latest_sbom()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_no_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_sbom_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_empty_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return True if the most recent report file was written within max_age_hours.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[Return the latest SBOM (Software Bill of Materials) as parsed JSON.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 29 AI Model & Supply Chain Integrity (0-5). MITRE ATLAS, OWASP LLM]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 3 Supply Chain (0-5).      0=no SBOM, 2=SBOM exists, 3=SBOM has pa]] - rationale - gateway/security/scanner_integration.py
- [[TestGetSbom_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSupplyChain]] - code - gateway/tests/test_scanner_integration.py
- [[_is_fresh()]] - code - gateway/security/scanner_integration.py
- [[_score_ai_model_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[_score_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_sbom()_1]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_trivy_summary
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 7 edges to [[_COMMUNITY_scanner_integration.py]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_scanner_integration.py_1]]
- 3 edges to [[_COMMUNITY_Path_2]]
- 2 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY__load_latest_json]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 7 communities
- [[get_sbom()_1]] - degree 9, connects to 3 communities
- [[_score_supply_chain()]] - degree 9, connects to 3 communities
- [[_is_fresh()]] - degree 8, connects to 3 communities
- [[_score_ai_model_supply_chain()]] - degree 6, connects to 2 communities
