---
type: community
members: 7
---

# TestSystemPromptReanchoring

**Members:** 7 nodes

## Members
- [[dot-test_reanchor_contains_security_notice()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_prepends_preamble()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_preserves_original_content()]] - code - gateway/tests/test_session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSystemPromptReanchoring
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_session_manager.py]]

## Top bridge nodes
- [[TestSystemPromptReanchoring]] - degree 4, connects to 1 community
