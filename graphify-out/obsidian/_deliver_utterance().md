---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Ws Client (main)"
location: "L596"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Ws_Client_main
---

# _deliver_utterance()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[delivery_resume_offset()]] - `calls` [EXTRACTED]
- [[delivery_track_sent_ok()]] - `calls` [EXTRACTED]
- [[voice_task()]] - `calls` [EXTRACTED]
- [[vt_remote_log()]] - `calls` [EXTRACTED]
- [[ws_client_connected()]] - `calls` [INFERRED]
- [[ws_client_connected() — lock-free flag read]] - `calls` [EXTRACTED]
- [[ws_client_send_end()]] - `calls` [INFERRED]
- [[ws_client_send_listen()]] - `calls` [INFERRED]
- [[ws_client_send_listen_resume()]] - `calls` [INFERRED]
- [[ws_client_send_pcm()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Ws_Client_main