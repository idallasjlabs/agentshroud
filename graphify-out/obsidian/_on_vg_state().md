---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "compute_scorecard()"
location: "L409"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/compute_scorecard
---

# _on_vg_state()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[ui_face_set_state()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]
- [[ws_vg_state_t]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/compute_scorecard