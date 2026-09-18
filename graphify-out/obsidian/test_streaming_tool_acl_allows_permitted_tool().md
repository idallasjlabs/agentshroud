---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L571"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_streaming_tool_acl_allows_permitted_tool()

## Connections
- [[Allowed tool blocks must pass through unchanged.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[_FakeSanitizer_1]] - `calls` [EXTRACTED]
- [[_FakeToolACL]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy