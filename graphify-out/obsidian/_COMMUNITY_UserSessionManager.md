---
type: community
cohesion: 0.11
members: 23
---

# UserSessionManager

**Cohesion:** 0.11 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-test_empty_tool_calls_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_empty_tool_results_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_non_owner_cross_path_plain_message_still_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_owner_message_mentioning_other_users_file_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_owner_plain_message_with_path_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_plain_chat_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_plain_message_mentioning_config_yaml_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_plain_message_mentioning_etc_passwd_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_plain_message_mentioning_memory_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_tool_call_with_unauthorized_path_still_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_tool_calls_key_detected()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_tool_results_key_detected()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_type_field_message_not_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[dot-test_type_field_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[FileSandbox must NOT block plain chat messages that mention file-like words.]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[Owner (8096968754) must not be blocked by content-pattern scanning.     They sho]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[TestFileSandboxSkippedForPlainMessages]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[TestIsToolCallRequest]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[TestOwnerBypassContentPatternChecks]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[Unit tests for the _is_tool_call_request helper (TDD RED phase).]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[_plain_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[_tool_call_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[_tool_result_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_UserSessionManager_3]]
- 6 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestIsToolCallRequest]] - degree 12, connects to 2 communities
- [[TestFileSandboxSkippedForPlainMessages]] - degree 9, connects to 2 communities
- [[TestOwnerBypassContentPatternChecks]] - degree 8, connects to 2 communities
- [[_plain_msg()]] - degree 8, connects to 1 community
- [[_tool_call_msg()]] - degree 3, connects to 1 community
