---
source_file: "gateway/proxy/telegram_proxy.py"
type: "code"
community: "ToolResultInjectionScanner"
location: "L3754"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# ._handle_outbound_tool_calls()

## Connections
- [[dot-_collaborator_safe_notice()]] - `calls` [EXTRACTED]
- [[dot-_extract_embedded_tool_call_json()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound()]] - `calls` [EXTRACTED]
- [[dot-_parse_tool_call_json()]] - `calls` [EXTRACTED]
- [[dot-_quarantine_outbound_block()]] - `calls` [EXTRACTED]
- [[dot-_resolve_collaborator_mode()]] - `calls` [EXTRACTED]
- [[dot-_trigger_web_fetch_approval()]] - `calls` [EXTRACTED]
- [[dot-_trigger_web_search_log()]] - `calls` [EXTRACTED]
- [[Any_12]] - `references` [EXTRACTED]
- [[Intercept leaked raw tool-call JSON in outbound text. Shared by the JSON and…]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolResultInjectionScanner
