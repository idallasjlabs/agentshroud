---
source_file: "gateway/proxy/telegram_proxy.py"
type: "code"
community: "._filter_outbound"
location: "L3593"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_filter_outbound
---

# ._scan_outbound_text()

## Connections
- [[dot-_collaborator_safe_notice()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound_multipart()]] - `calls` [EXTRACTED]
- [[dot-_quarantine_outbound_block()]] - `calls` [EXTRACTED]
- [[dot-_set_outbound_block_cascade()]] - `calls` [EXTRACTED]
- [[dot-info_filter_redaction_count()]] - `indirect_call` [INFERRED]
- [[Core outbound security scan shared by JSON, form, and multipart branches. Runs…]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `method` [EXTRACTED]
- [[_OutboundScan]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_filter_outbound
