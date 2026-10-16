---
type: community
cohesion: 0.22
members: 10
---

# Phase 1 — Raw Collection

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_response()_1]] - code - gateway/security/prompt_protection.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_1__Raw_Collection
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]

## Top bridge nodes
- [[dot-scan_response()_1]] - degree 5, connects to 2 communities
- [[ProtectedContent]] - degree 5, connects to 1 community
- [[dot-add_protected_content()]] - degree 4, connects to 1 community
- [[dot-_calculate_similarity()]] - degree 4, connects to 1 community
- [[dot-_redact_fuzzy_match()]] - degree 4, connects to 1 community
