---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Playback State (test_playback_state)"
location: "L316"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Playback_State_test_playback_state
---

# tts_task()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[audio_play()]] - `calls` [EXTRACTED]
- [[audio_volume_tick()]] - `calls` [INFERRED]
- [[audio_volume_tick() — zipper-free ramp + NVS persist]] - `calls` [EXTRACTED]
- [[playback_gate_should_open()]] - `calls` [INFERRED]
- [[ui_face_set_state()]] - `calls` [EXTRACTED]
- [[wakeword_set_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Playback_State_test_playback_state