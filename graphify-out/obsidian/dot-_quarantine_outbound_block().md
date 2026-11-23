---
source_file: "gateway/proxy/telegram_proxy.py"
type: "code"
community: "ToolResultInjectionScanner"
location: "L6953"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# ._quarantine_outbound_block()

## Connections
- [[dot-_emit_quarantine_event()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound_multipart()]] - `calls` [EXTRACTED]
- [[dot-_handle_outbound_tool_calls()]] - `calls` [EXTRACTED]
- [[dot-_scan_outbound_text()]] - `calls` [EXTRACTED]
- [[Persist blocked outbound messages for admin review.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `method` [EXTRACTED]
- [[_app_state()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ToolResultInjectionScanner
