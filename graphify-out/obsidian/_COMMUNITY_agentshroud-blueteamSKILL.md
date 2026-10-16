---
type: community
cohesion: 0.18
members: 14
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.18 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-__init__()_100]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Any_31]] - code - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Phase 1 — Raw Collection_3]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter_7]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_TestPromptProtection]]
- 1 edge to [[_COMMUNITY_dot-_redact_match]]
- 1 edge to [[_COMMUNITY_dot-test_protected_content_loading]]
- 1 edge to [[_COMMUNITY_dot-test_disabled_protection]]
- 1 edge to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[PromptProtection]] - degree 23, connects to 11 communities
- [[dot-_load_protected_content()]] - degree 4, connects to 1 community
- [[System Prompt Protection Tests]] - degree 2, connects to 1 community
