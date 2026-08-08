---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "ESP32 Firmware"
location: "line 75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# playback_step() — reproduces tts_task's gate-open/drain branches for testing

## Connections
- [[playback_gate_should_open()]] - `calls` [EXTRACTED]
- [[wakeword_set_tts_playing()]] - `calls` [EXTRACTED]
- [[wakeword_triggered()]] - `calls` [EXTRACTED]
- [[wakeword_tts_stop_clear()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ESP32_Firmware