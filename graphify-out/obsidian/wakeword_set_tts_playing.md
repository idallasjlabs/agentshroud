---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "test_playback_state.c"
location: "462"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_playback_statec
---

# wakeword_set_tts_playing

## Connections
- [[playback_step()]] - `calls` [INFERRED]
- [[playback_step() — reproduces tts_task's gate-opendrain branches for testing]] - `calls` [EXTRACTED]
- [[reset_all()]] - `calls` [INFERRED]
- [[tts_task]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_playback_statec