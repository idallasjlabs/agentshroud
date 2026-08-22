---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Playback State (test_playback_state)"
location: "L392"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Playback_State_test_playback_state
---

# _on_vg_state()

## Connections
- [[_on_event() — dispatches statepcmctrl frames to registered callbacks]] - `calls` [EXTRACTED]
- [[app_main.c]] - `contains` [EXTRACTED]
- [[ui_face_set_state()]] - `calls` [EXTRACTED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]
- [[ws_client_create() — registers callbacks + starts client]] - `calls` [EXTRACTED]
- [[ws_vg_state_t]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Playback_State_test_playback_state