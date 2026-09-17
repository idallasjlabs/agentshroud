---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "app_main.c"
location: "L511"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/app_mainc
---

# wakeword_tts_stop_requested()

## Connections
- [[_on_tts_pcm]] - `calls` [INFERRED]
- [[_on_vg_state]] - `calls` [INFERRED]
- [[test_drain_clears_playing_and_returns_idle()]] - `calls` [INFERRED]
- [[tts_task]] - `calls` [INFERRED]
- [[voice_task]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/app_mainc