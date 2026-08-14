---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "Gateway Test Suite"
location: "L249"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_drain_clears_playing_and_returns_idle()

## Connections
- [[main()_6]] - `calls` [EXTRACTED]
- [[playback_step()]] - `calls` [EXTRACTED]
- [[reset_all()]] - `calls` [EXTRACTED]
- [[test_playback_state.c]] - `contains` [EXTRACTED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite