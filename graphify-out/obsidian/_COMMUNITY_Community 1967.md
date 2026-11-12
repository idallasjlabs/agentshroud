---
type: community
members: 6
---

# Community 1967

**Members:** 6 nodes

## Members
- [[._get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[.register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[.verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1967
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 22]]

## Top bridge nodes
- [[.register_system_prompt()]] - degree 4, connects to 2 communities
- [[.verify_system_prompt()]] - degree 4, connects to 2 communities
- [[._get_hmac_key()]] - degree 4, connects to 1 community