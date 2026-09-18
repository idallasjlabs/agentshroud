---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "asyncio"
location: "L1523"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/asyncio
---

# ?agent=direct must route to _call_llm (fast path), not /forward.

## Connections
- [[test_ws_direct_agent_calls_call_llm()]] - `rationale_for` [EXTRACTED]
- [[test_ws_direct_agent_calls_call_llm()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/asyncio