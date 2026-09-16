---
type: community
cohesion: 0.11
members: 23
---

# Community 390

**Cohesion:** 0.11 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-test_add_message()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_conversation_history_limit()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_get_session_context_contains_user_id()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_prompt_addition_mentions_isolation()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_contains_security_notice()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_prepends_preamble()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_preserves_original_content()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_session_to_dict_and_back()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_update_trust_level()]] - code - gateway/tests/test_session_manager.py
- [[Create a UserSessionManager with a temp base workspace and an owner.]] - rationale - gateway/tests/test_session_manager.py
- [[History should be capped at 1000 messages.]] - rationale - gateway/tests/test_session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[Represents an isolated session for a user within a specific bot workspace.]] - rationale - gateway/security/session_manager.py
- [[TestConversationHistory]] - code - gateway/tests/test_session_manager.py
- [[TestSerialization_1]] - code - gateway/tests/test_session_manager.py
- [[TestSessionContext]] - code - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py
- [[TestTrustLevel]] - code - gateway/tests/test_session_manager.py
- [[UserSession]] - code - gateway/security/session_manager.py
- [[mgr()]] - code - gateway/tests/test_session_manager.py
- [[test_session_manager.py]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_390
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Ingest Middleware & File Sandbox]]
- 2 edges to [[_COMMUNITY_Community 1114]]
- 2 edges to [[_COMMUNITY_Community 1178]]
- 2 edges to [[_COMMUNITY_Community 1335]]
- 2 edges to [[_COMMUNITY_Community 383]]
- 2 edges to [[_COMMUNITY_Community 716]]
- 2 edges to [[_COMMUNITY_Community 520]]
- 1 edge to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 1 edge to [[_COMMUNITY_Community 747]]
- 1 edge to [[_COMMUNITY_Session Manager & PIIContext Guard]]

## Top bridge nodes
- [[UserSession]] - degree 18, connects to 9 communities
- [[test_session_manager.py]] - degree 14, connects to 7 communities
- [[TestSystemPromptReanchoring]] - degree 6, connects to 1 community
- [[TestConversationHistory]] - degree 5, connects to 1 community
- [[TestSessionContext]] - degree 5, connects to 1 community