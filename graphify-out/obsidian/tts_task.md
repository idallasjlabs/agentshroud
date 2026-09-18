---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "app_main.c"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/app_mainc
---

# tts_task

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[ui_face_set_state]] - `calls` [EXTRACTED]
- [[wakeword_set_tts_playing]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_clear()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/app_mainc