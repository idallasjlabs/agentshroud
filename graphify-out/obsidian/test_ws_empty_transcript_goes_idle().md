---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L892"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer_Pipeline
---

# test_ws_empty_transcript_goes_idle()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[Empty STT result no LLM call, state goes directly to idle.]] - `rationale_for` [EXTRACTED]
- [[Exception]] - `calls` [INFERRED]
- [[Exception_1]] - `calls` [INFERRED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer_Pipeline