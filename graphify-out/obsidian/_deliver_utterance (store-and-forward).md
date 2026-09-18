---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "voice_task"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/voice_task
---

# _deliver_utterance (store-and-forward)

## Connections
- [[app_main.c]] - `contains` [EXTRACTED]
- [[voice_task]] - `calls` [EXTRACTED]
- [[vt_remote_log]] - `calls` [EXTRACTED]
- [[ws_client_connected]] - `calls` [INFERRED]
- [[ws_client_send_end()]] - `calls` [INFERRED]
- [[ws_client_send_listen()]] - `calls` [INFERRED]
- [[ws_client_send_listen_resume]] - `calls` [INFERRED]
- [[ws_client_send_pcm()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/voice_task