---
source_file: "firmware/voice-terminal/main/ui_face.c"
type: "code"
community: "wakeword.c"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/wakewordc
---

# _touch_pressed

## Connections
- [[lv_event_t]] - `references` [EXTRACTED]
- [[ui_face.c]] - `contains` [EXTRACTED]
- [[vt_remote_log]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish]] - `calls` [INFERRED]
- [[wakeword_ptt_press]] - `calls` [INFERRED]
- [[wakeword_ptt_release]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_request]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/wakewordc