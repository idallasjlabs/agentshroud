---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "Playback State (test_playback_state)"
location: "L443"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Playback_State_test_playback_state
---

# wakeword_set_tts_playing()

## Connections
- [[playback_step()]] - `calls` [INFERRED]
- [[playback_step() — reproduces tts_task's gate-opendrain branches for testing]] - `calls` [EXTRACTED]
- [[reset_all()]] - `calls` [INFERRED]
- [[tts_task()]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Playback_State_test_playback_state