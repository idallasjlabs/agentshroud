---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "compute_scorecard()"
location: "L322"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/compute_scorecard
---

# tts_task()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[audio_play()]] - `calls` [INFERRED]
- [[audio_volume_tick()]] - `calls` [INFERRED]
- [[playback_gate_should_open()]] - `calls` [INFERRED]
- [[ui_face_set_state()]] - `calls` [INFERRED]
- [[wakeword_set_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/compute_scorecard