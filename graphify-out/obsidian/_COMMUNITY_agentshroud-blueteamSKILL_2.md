---
type: community
cohesion: 0.08
members: 26
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-filter_response()_1]] - code - gateway/security/xml_leak_filter.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-setup_method()_23]] - code - gateway/tests/test_xml_leak_filter.py
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
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult]] - code - gateway/security/xml_leak_filter.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_InjectionAction]]

## Top bridge nodes
- [[FilterResult]] - degree 8, connects to 2 communities
- [[TestCommandInjectionScan]] - degree 9, connects to 1 community
- [[TestXMLLeakFilter]] - degree 9, connects to 1 community
- [[test_xml_leak_filter.py]] - degree 4, connects to 1 community
- [[dot-filter_response()_1]] - degree 3, connects to 1 community
