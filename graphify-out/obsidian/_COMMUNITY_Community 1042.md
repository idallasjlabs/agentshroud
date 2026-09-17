---
type: community
cohesion: 0.25
members: 8
---

# Community 1042

**Cohesion:** 0.25 - loosely connected
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
TABLE source_file, type FROM #community/Community_1042
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Egress Filter & HTTP Proxy]]
- 1 edge to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 1 edge to [[_COMMUNITY_Community 96]]

## Top bridge nodes
- [[TestPromptInjectionDetection]] - degree 14, connects to 3 communities