---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "Security Pipeline Core"
location: "L190"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Pipeline_Core
---

# If the pipeline raises mid-synthesis, synthesize() raises RuntimeError.

## Connections
- [[test_tts_kokoro_synthesis_failure_raises()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Pipeline_Core