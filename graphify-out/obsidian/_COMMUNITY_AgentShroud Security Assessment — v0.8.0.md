---
type: community
members: 16
---

# AgentShroud Security Assessment — v0.8.0

**Members:** 16 nodes

## Members
- [[dot-test_baseline_three_when_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_all_passing_no_report_on_disk()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_oscap_binary_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_five_when_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_openscap_running_with_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_not_run()_1]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 10 Compliance Auditing (0-5).      0=not run, 2=has failures, 3=ze]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 4 Container Hardening (0-5).      Baseline of 3 because docker-com]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreComplianceAuditing_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreContainerHardening_1]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_warn()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_compliance_auditing()]] - code - gateway/security/scanner_integration.py
- [[_score_container_hardening()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Security_Assessment__v080
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_parse_clamscan_output]]
- 4 edges to [[_COMMUNITY_AgentShroud Docker Configuration]]
- 4 edges to [[_COMMUNITY_PipelineAction (2)_1]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_Incident ConduitHermes instability 2026-10-16]]

## Top bridge nodes
- [[_score_compliance_auditing()]] - degree 10, connects to 5 communities
- [[_score_container_hardening()]] - degree 8, connects to 4 communities
- [[_openscap_not_run()]] - degree 7, connects to 3 communities
- [[_openscap_clean()]] - degree 6, connects to 3 communities
- [[TestScoreComplianceAuditing_1]] - degree 5, connects to 1 community
