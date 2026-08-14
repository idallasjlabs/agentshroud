---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L893"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Empty STT result: no LLM call, state goes directly to idle.

## Connections
- [[test_ws_empty_transcript_goes_idle()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline