---
source_file: "chatbot/test_main.py"
type: "code"
community: "egress_filter.py"
location: "L142"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/egress_filterpy
---

# .test_internal_error_not_leaked()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[OpenAI exceptions should not leak internal details to the client.]] - `rationale_for` [EXTRACTED]
- [[TestErrorSanitization]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/egress_filterpy
