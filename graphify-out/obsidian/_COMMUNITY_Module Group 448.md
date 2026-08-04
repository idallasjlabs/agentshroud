---
type: community
cohesion: 0.25
members: 8
---

# Module Group 448

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_clean_content_no_injection()]] - code - gateway/tests/test_web_proxy.py
- [[.test_data_exfil_instruction_detected()]] - code - gateway/tests/test_web_proxy.py
- [[.test_ignore_instructions_detected()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_adds_security_headers()]] - code - gateway/tests/test_web_proxy.py
- [[.test_role_override_detected()]] - code - gateway/tests/test_web_proxy.py
- [[.test_system_delimiter_detected()]] - code - gateway/tests/test_web_proxy.py
- [[.test_tool_invocation_detected()]] - code - gateway/tests/test_web_proxy.py
- [[TestPromptInjectionDetection]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_448
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 1 edge to [[_COMMUNITY_Security Pipeline & Audit Chain]]

## Top bridge nodes
- [[TestPromptInjectionDetection]] - degree 14, connects to 2 communities
