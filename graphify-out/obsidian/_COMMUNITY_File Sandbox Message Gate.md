---
type: community
cohesion: 0.10
members: 28
---

# File Sandbox Message Gate

**Cohesion:** 0.10 - loosely connected
**Members:** 28 nodes

## Members
- [[.test_empty_tool_calls_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_empty_tool_results_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_non_owner_cross_path_plain_message_still_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_owner_message_mentioning_other_users_file_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_owner_plain_message_with_path_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_plain_chat_not_a_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_plain_message_mentioning_config_yaml_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_plain_message_mentioning_etc_passwd_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_plain_message_mentioning_memory_not_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_tool_call_with_unauthorized_path_still_blocked()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_tool_calls_key_detected()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_tool_results_key_detected()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_type_field_message_not_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[.test_type_field_tool_call()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[FileSandbox must NOT block plain chat messages that mention file-like words.]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[MiddlewareManager with real session_manager, all other deps mocked.      Uses __]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[Owner (8096968754) must not be blocked by content-pattern scanning.     They sho]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[TestFileSandboxSkippedForPlainMessages]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[TestIsToolCallRequest]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[TestOwnerBypassContentPatternChecks]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[Unit tests for the _is_tool_call_request helper (TDD RED phase).]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[_plain_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[_tool_call_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[_tool_result_msg()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[manager()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[session_manager()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[temp_workspace()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[test_file_sandbox_message_gate.py]] - code - gateway/tests/test_file_sandbox_message_gate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/File_Sandbox_Message_Gate
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 5 edges to [[_COMMUNITY_Middleware & Session Isolation]]

## Top bridge nodes
- [[test_file_sandbox_message_gate.py]] - degree 12, connects to 2 communities
- [[TestIsToolCallRequest]] - degree 12, connects to 2 communities
- [[TestFileSandboxSkippedForPlainMessages]] - degree 9, connects to 2 communities
- [[TestOwnerBypassContentPatternChecks]] - degree 8, connects to 2 communities
- [[session_manager()]] - degree 2, connects to 1 community