---
source_file: "gateway/proxy/telegram_proxy.py"
type: "code"
community: "ToolResultInjectionScanner"
location: "L2219"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ToolResultInjectionScanner
---

# ._collaborator_safe_notice()

## Connections
- [[dot-_apply_outbound_model_error_rewrites()]] - `calls` [EXTRACTED]
- [[dot-_apply_outbound_status_notices()]] - `calls` [EXTRACTED]
- [[dot-_check_collaborator_leakage()]] - `calls` [EXTRACTED]
- [[dot-_filter_inbound_updates()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound_multipart()]] - `calls` [EXTRACTED]
- [[dot-_handle_outbound_tool_calls()]] - `calls` [EXTRACTED]
- [[dot-_notify_collaborator_command_blocked()]] - `calls` [EXTRACTED]
- [[dot-_notify_user_blocked()]] - `calls` [EXTRACTED]
- [[dot-_redact_owner_ids()]] - `calls` [EXTRACTED]
- [[dot-_scan_outbound_text()]] - `calls` [EXTRACTED]
- [[dot-test_collaborator_safe_notice_maps_internal_network_probe_to_egress_notice()]] - `calls` [EXTRACTED]
- [[dot-test_collaborator_safe_notice_maps_metadata_probe_to_secret_notice()]] - `calls` [EXTRACTED]
- [[dot-test_collaborator_safe_notice_maps_obfuscated_probe_to_scope_notice()]] - `calls` [EXTRACTED]
- [[dot-test_collaborator_safe_notice_uses_canonical_header_with_blank_line()]] - `calls` [EXTRACTED]
- [[Concise collaborator-safe reason text without internal leakage.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `method` [EXTRACTED]
- [[normalize_input()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ToolResultInjectionScanner
