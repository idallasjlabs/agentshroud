---
type: community
cohesion: 0.47
members: 6
---

# PipelineAction (2)

**Cohesion:** 0.47 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return latest Falco alert summary from the local alert directory.      CC-20 If]] - rationale - gateway/security/scanner_integration.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PipelineAction_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_parse_clamscan_output]]
- 4 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_OpenClaw Skill Metadata Schema (frontmatter convention)]]

## Top bridge nodes
- [[get_falco_summary()]] - degree 13, connects to 3 communities
- [[TestGetFalcoSummary]] - degree 4, connects to 1 community
- [[dot-test_not_run_when_no_alert_dir()]] - degree 3, connects to 1 community
