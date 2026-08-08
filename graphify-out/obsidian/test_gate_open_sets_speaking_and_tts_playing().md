---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "ESP32 Firmware"
location: "L216"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# test_gate_open_sets_speaking_and_tts_playing()

## Connections
- [[main()_6]] - `calls` [EXTRACTED]
- [[playback_step()]] - `calls` [EXTRACTED]
- [[reset_all()]] - `calls` [EXTRACTED]
- [[test_playback_state.c]] - `contains` [EXTRACTED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ESP32_Firmware