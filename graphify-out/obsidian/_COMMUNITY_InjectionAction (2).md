---
type: community
members: 8
---

# InjectionAction (2)

**Members:** 8 nodes

## Members
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InjectionAction_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]

## Top bridge nodes
- [[dot-scan_tool_result()_1]] - degree 7, connects to 3 communities
- [[dot-_detect_encoded_injection()]] - degree 4, connects to 2 communities
- [[dot-_detect_unicode_obfuscation()]] - degree 4, connects to 2 communities
- [[InjectionResult]] - degree 3, connects to 1 community
