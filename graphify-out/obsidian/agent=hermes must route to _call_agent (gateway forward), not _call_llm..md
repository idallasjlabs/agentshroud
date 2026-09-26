---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "ToolACLEnforcer"
location: "L1574"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# ?agent=hermes must route to _call_agent (gateway /forward), not _call_llm.

## Connections
- [[test_ws_hermes_agent_calls_call_agent()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolACLEnforcer