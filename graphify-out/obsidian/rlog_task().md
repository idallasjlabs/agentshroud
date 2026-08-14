---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Gateway Test Suite"
location: "L538"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# rlog_task()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[ws_client_connected()]] - `calls` [INFERRED]
- [[ws_client_connected() — lock-free flag read]] - `calls` [EXTRACTED]
- [[ws_client_send_log()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite