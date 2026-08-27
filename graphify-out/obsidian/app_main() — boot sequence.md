---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Community 711"
location: "line 901"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_711
---

# app_main() — boot sequence

## Connections
- [[audio_init() — micspeaker codec init]] - `calls` [EXTRACTED]
- [[audio_preinit() — claims I2S at 16 kHz before display init]] - `calls` [EXTRACTED]
- [[ota_check()]] - `calls` [EXTRACTED]
- [[ui_face_init()]] - `calls` [EXTRACTED]
- [[ui_face_set_agent()]] - `calls` [EXTRACTED]
- [[ui_face_set_state()]] - `calls` [EXTRACTED]
- [[wakeword_init()]] - `calls` [EXTRACTED]
- [[ws_client_create() — registers callbacks + starts client]] - `calls` [EXTRACTED]
- [[ws_client_set_ctrl_cb()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_711