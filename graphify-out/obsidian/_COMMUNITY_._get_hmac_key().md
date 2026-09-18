---
type: community
cohesion: 0.33
members: 6
---

# ._get_hmac_key()

**Cohesion:** 0.33 - loosely connected
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
TABLE source_file, type FROM #community/_get_hmac_key
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[.register_system_prompt()]] - degree 4, connects to 2 communities
- [[.verify_system_prompt()]] - degree 4, connects to 2 communities
- [[._get_hmac_key()]] - degree 4, connects to 1 community