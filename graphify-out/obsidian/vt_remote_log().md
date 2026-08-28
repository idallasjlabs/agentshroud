---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Community 90"
location: "L521"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_90
---

# vt_remote_log()

## Connections
- [[_btn_pressed()]] - `calls` [INFERRED]
- [[_deliver_utterance()]] - `calls` [EXTRACTED]
- [[_on_event()]] - `calls` [INFERRED]
- [[_on_ws_ctrl()]] - `calls` [EXTRACTED]
- [[_ptt_start()]] - `calls` [INFERRED]
- [[_report_and_place_canvas()]] - `calls` [INFERRED]
- [[_touch_pressed()]] - `calls` [INFERRED]
- [[_touch_start_only()]] - `calls` [INFERRED]
- [[app_main.c]] - `contains` [EXTRACTED]
- [[remote_log.h (WS-mirrored diagnostic log declaration)]] - `implements` [EXTRACTED]
- [[voice_task()]] - `calls` [EXTRACTED]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_push_frame()]] - `calls` [INFERRED]
- [[wakeword_push_frame() — AFE feed + VAD endpointing]] - `calls` [EXTRACTED]
- [[wakeword_tick()]] - `calls` [INFERRED]
- [[wifi_event_handler()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_90