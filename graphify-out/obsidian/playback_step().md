---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "Community 271"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_271
---

# playback_step()

## Connections
- [[face_set_state()]] - `calls` [EXTRACTED]
- [[playback_gate_should_open()]] - `calls` [INFERRED]
- [[test_drain_clears_playing_and_returns_idle()]] - `calls` [EXTRACTED]
- [[test_drain_keeps_face_off_idle_when_retriggered()]] - `calls` [EXTRACTED]
- [[test_gate_open_sets_speaking_and_tts_playing()]] - `calls` [EXTRACTED]
- [[test_gate_stays_closed_leaves_state_idle()]] - `calls` [EXTRACTED]
- [[test_playback_state.c]] - `contains` [EXTRACTED]
- [[wakeword_set_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Community_271