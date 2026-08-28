---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Community 90"
location: "L322"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_90
---

# tts_task()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[audio_play()]] - `calls` [EXTRACTED]
- [[audio_volume_tick()]] - `calls` [INFERRED]
- [[audio_volume_tick() — zipper-free ramp + NVS persist]] - `calls` [EXTRACTED]
- [[playback_gate_should_open()]] - `calls` [INFERRED]
- [[ui_face_set_state()]] - `calls` [INFERRED]
- [[wakeword_set_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Community_90