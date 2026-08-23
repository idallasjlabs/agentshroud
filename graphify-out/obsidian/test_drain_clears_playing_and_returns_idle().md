---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "Playback State (test_playback_state)"
location: "L249"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Playback_State_test_playback_state
---

# test_drain_clears_playing_and_returns_idle()

## Connections
- [[main()_8]] - `calls` [EXTRACTED]
- [[playback_step()]] - `calls` [EXTRACTED]
- [[reset_all()]] - `calls` [EXTRACTED]
- [[test_playback_state.c]] - `contains` [EXTRACTED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Playback_State_test_playback_state