---
type: community
cohesion: 0.09
members: 29
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.09 - loosely connected
**Members:** 29 nodes

## Members
- [[dot-__init__()_106]] - code - gateway/security/prompt_protection.py
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_response()_2]] - code - gateway/security/prompt_protection.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Any_40]] - code - gateway/security/prompt_protection.py
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult_1]] - code - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestPromptProtection]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_InjectionAction]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[PromptProtection]] - degree 23, connects to 5 communities
- [[ProtectedContent]] - degree 5, connects to 1 community
- [[RedactionResult_1]] - degree 3, connects to 1 community
- [[System Prompt Protection Tests]] - degree 2, connects to 1 community
