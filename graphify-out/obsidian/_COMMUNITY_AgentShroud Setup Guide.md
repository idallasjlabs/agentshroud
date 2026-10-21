---
type: community
members: 28
---

# AgentShroud Setup Guide

**Members:** 28 nodes

## Members
- [[dot-filter_response()]] - code - gateway/security/xml_leak_filter.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-setup_method()_21]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult_1]] - code - gateway/security/xml_leak_filter.py
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[Scan outbound text for command  code injection patterns.          Does NOT modi]] - rationale - gateway/security/xml_leak_filter.py
- [[Set up test fixtures._3]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Setup_Guide
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]

## Top bridge nodes
- [[xml_leak_filter.py]] - degree 4, connects to 2 communities
- [[TestCommandInjectionScan]] - degree 9, connects to 1 community
- [[TestXMLLeakFilter]] - degree 9, connects to 1 community
- [[FilterResult_1]] - degree 8, connects to 1 community
- [[test_xml_leak_filter.py]] - degree 4, connects to 1 community
