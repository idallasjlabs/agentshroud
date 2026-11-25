---
source_file: "gateway/tests/test_rate_limit_failover.py"
type: "code"
community: "test_anthropic_openai_translator.py"
location: "L72"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_anthropic_openai_translatorpy
---

# test_proxy_failover_on_post_retry_429()

## Connections
- [[A 429 that escaped the retry loop must trigger local failover.]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[asyncio_16]] - `references` [EXTRACTED]
- [[mock_forward()_1]] - `indirect_call` [INFERRED]
- [[test_rate_limit_failover.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_anthropic_openai_translatorpy
