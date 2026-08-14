---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Gateway Test Suite"
location: "L504"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# vt_remote_log()

## Connections
- [[_deliver_utterance()]] - `calls` [EXTRACTED]
- [[_on_event()]] - `calls` [INFERRED]
- [[_on_event() — dispatches statepcmctrl frames to registered callbacks]] - `calls` [EXTRACTED]
- [[_on_ws_ctrl()]] - `calls` [EXTRACTED]
- [[_ptt_start()]] - `calls` [EXTRACTED]
- [[app_main.c]] - `contains` [EXTRACTED]
- [[remote_log.h (WS-mirrored diagnostic log declaration)]] - `implements` [EXTRACTED]
- [[voice_task()]] - `calls` [EXTRACTED]
- [[wakeword_push_frame() — AFE feed + VAD endpointing]] - `calls` [EXTRACTED]
- [[wifi_event_handler()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite