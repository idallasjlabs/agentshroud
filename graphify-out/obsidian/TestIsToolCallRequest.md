---
source_file: "gateway/tests/test_file_sandbox_message_gate.py"
type: "code"
community: "File Sandbox Message Gate"
location: "L106"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/File_Sandbox_Message_Gate
---

# TestIsToolCallRequest

## Connections
- [[.test_empty_tool_calls_not_a_tool_call()]] - `method` [EXTRACTED]
- [[.test_empty_tool_results_not_a_tool_call()]] - `method` [EXTRACTED]
- [[.test_plain_chat_not_a_tool_call()]] - `method` [EXTRACTED]
- [[.test_tool_calls_key_detected()]] - `method` [EXTRACTED]
- [[.test_tool_results_key_detected()]] - `method` [EXTRACTED]
- [[.test_type_field_message_not_tool_call()]] - `method` [EXTRACTED]
- [[.test_type_field_tool_call()]] - `method` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Unit tests for the _is_tool_call_request helper (TDD RED phase).]] - `rationale_for` [EXTRACTED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_file_sandbox_message_gate.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/File_Sandbox_Message_Gate