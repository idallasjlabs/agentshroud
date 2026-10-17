---
type: community
members: 11
---

# InjectionAction (2)

**Members:** 11 nodes

## Members
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-scan_tool_result()_2]] - code - gateway/security/tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[input_normalizer.py_2]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InjectionAction_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_InjectionAction]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py (3)]]

## Top bridge nodes
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
- [[input_normalizer.py_2]] - degree 4, connects to 3 communities
- [[dot-scan_tool_result()_2]] - degree 7, connects to 2 communities
- [[dot-_detect_encoded_injection()]] - degree 4, connects to 2 communities
- [[dot-_detect_unicode_obfuscation()]] - degree 4, connects to 2 communities
