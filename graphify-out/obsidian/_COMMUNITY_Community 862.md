---
type: community
cohesion: 0.22
members: 10
---

# Community 862

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[._check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[._check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[.scan()_4]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_862
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 2 edges to [[_COMMUNITY_Key Vault & Audit Chain]]
- 1 edge to [[_COMMUNITY_Community 70]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]
- 1 edge to [[_COMMUNITY_Community 30]]

## Top bridge nodes
- [[.scan()_4]] - degree 8, connects to 3 communities
- [[detect_base64_payloads()]] - degree 5, connects to 2 communities
- [[.scan_tool_result()_2]] - degree 4, connects to 2 communities
- [[._check_encoded_content()]] - degree 4, connects to 1 community
- [[._check_unicode_tricks()]] - degree 3, connects to 1 community