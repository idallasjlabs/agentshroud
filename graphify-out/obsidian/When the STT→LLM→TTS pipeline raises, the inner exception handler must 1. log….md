---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "test_voice_gateway.py"
location: "L1752"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# When the STT→LLM→TTS pipeline raises, the inner exception handler must: 1. log…

## Connections
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_gatewaypy