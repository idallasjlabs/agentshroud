---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "_t()"
location: "L624"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_t
---

# _deliver_utterance()

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[delivery_resume_offset()]] - `calls` [INFERRED]
- [[delivery_track_sent_ok()]] - `calls` [INFERRED]
- [[voice_task()]] - `calls` [EXTRACTED]
- [[vt_remote_log()]] - `calls` [EXTRACTED]
- [[ws_client_connected()]] - `calls` [INFERRED]
- [[ws_client_send_end()]] - `calls` [INFERRED]
- [[ws_client_send_listen()]] - `calls` [INFERRED]
- [[ws_client_send_listen_resume()]] - `calls` [INFERRED]
- [[ws_client_send_pcm()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/_t