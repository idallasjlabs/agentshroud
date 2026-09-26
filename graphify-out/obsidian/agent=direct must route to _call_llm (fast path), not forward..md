---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "ToolACLEnforcer"
location: "L1523"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# ?agent=direct must route to _call_llm (fast path), not /forward.

## Connections
- [[test_ws_direct_agent_calls_call_llm()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolACLEnforcer