---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "ESP32 Firmware"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# reset_all()

## Connections
- [[test_drain_clears_playing_and_returns_idle()]] - `calls` [EXTRACTED]
- [[test_drain_keeps_face_off_idle_when_retriggered()]] - `calls` [EXTRACTED]
- [[test_gate_open_sets_speaking_and_tts_playing()]] - `calls` [EXTRACTED]
- [[test_gate_stays_closed_leaves_state_idle()]] - `calls` [EXTRACTED]
- [[test_playback_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_set_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ESP32_Firmware