---
type: community
cohesion: 0.22
members: 10
---

# OutboundInfoFilter

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-scan()_4]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()_3]] - code - gateway/security/prompt_guard.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]

## Top bridge nodes
- [[dot-scan()_4]] - degree 8, connects to 3 communities
- [[detect_base64_payloads()]] - degree 5, connects to 2 communities
- [[dot-scan_tool_result()_3]] - degree 4, connects to 2 communities
- [[dot-_check_encoded_content()]] - degree 4, connects to 1 community
- [[dot-_check_unicode_tricks()]] - degree 3, connects to 1 community
