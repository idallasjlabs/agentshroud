---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_proxy()"
location: "L1851"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# Form-encoded draft payloads must not leak raw tool-call JSON.

## Connections
- [[.test_urlencoded_draft_payload_tool_json_is_rewritten()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy