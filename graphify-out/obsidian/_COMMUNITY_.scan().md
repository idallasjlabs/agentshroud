---
type: community
cohesion: 0.14
members: 15
---

# .scan()

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[._check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[._check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[.scan()_2]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_2]] - code - gateway/security/tool_result_injection.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scan
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_tool_result_injection.py]]
- 2 edges to [[_COMMUNITY_InjectionSeverity]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]

## Top bridge nodes
- [[.scan_tool_result()_2]] - degree 7, connects to 4 communities
- [[.scan()_2]] - degree 8, connects to 3 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
- [[input_normalizer.py]] - degree 4, connects to 2 communities
- [[.scan_tool_result()]] - degree 4, connects to 2 communities