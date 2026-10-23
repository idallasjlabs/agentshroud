---
type: community
cohesion: 0.14
members: 18
---

# Deploying AgentShroud on macOS (Apple Silicon / Intel)

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-__init__()_162]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()_1]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-test_disabled_protection()]] - code - gateway/tests/test_prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Any_61]] - code - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[Test that disabled protection passes through content unchanged.]] - rationale - gateway/tests/test_prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Deploying_AgentShroud_on_macOS_Apple_Silicon_/_Intel
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AgentShroud Module Inventory]]
- 3 edges to [[_COMMUNITY_Any]]
- 2 edges to [[_COMMUNITY_Mode B — Comprehensive review sweep (3)]]
- 2 edges to [[_COMMUNITY_AgentShroud v1.0.0 Fortress Release Announcement]]
- 1 edge to [[_COMMUNITY_TestAiModelSupplyChain]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration (2)]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]

## Top bridge nodes
- [[PromptProtection]] - degree 21, connects to 7 communities
- [[dot-add_protected_content()]] - degree 4, connects to 1 community
- [[dot-test_disabled_protection()]] - degree 3, connects to 1 community
- [[System Prompt Protection Tests]] - degree 2, connects to 1 community
