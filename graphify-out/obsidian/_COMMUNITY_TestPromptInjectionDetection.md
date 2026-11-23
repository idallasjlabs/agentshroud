---
type: community
members: 8
---

# TestPromptInjectionDetection

**Members:** 8 nodes

## Members
- [[dot-test_clean_content_no_injection()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_data_exfil_instruction_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ignore_instructions_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_adds_security_headers()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_role_override_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_system_delimiter_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_tool_invocation_detected()]] - code - gateway/tests/test_web_proxy.py
- [[TestPromptInjectionDetection]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPromptInjectionDetection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_WebProxy]]

## Top bridge nodes
- [[TestPromptInjectionDetection]] - degree 8, connects to 1 community
