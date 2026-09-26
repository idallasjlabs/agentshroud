---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "ToolACLEnforcer"
location: "L1004"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# Empty STT result: no LLM call, state goes directly to idle.

## Connections
- [[test_ws_empty_transcript_goes_idle()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolACLEnforcer