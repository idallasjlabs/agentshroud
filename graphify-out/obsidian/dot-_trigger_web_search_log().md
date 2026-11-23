---
source_file: "gateway/proxy/telegram_proxy.py"
type: "code"
community: "ToolResultInjectionScanner"
location: "L4005"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# ._trigger_web_search_log()

## Connections
- [[dot-_handle_outbound_tool_calls()]] - `calls` [EXTRACTED]
- [[Any_12]] - `references` [EXTRACTED]
- [[Log a web_search egress event with user attribution when raw JSON leaks.…]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `method` [EXTRACTED]
- [[_app_state()]] - `indirect_call` [INFERRED]
- [[normalize_input()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolResultInjectionScanner
