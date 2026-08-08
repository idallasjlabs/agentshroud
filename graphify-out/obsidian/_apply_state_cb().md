---
source_file: "firmware/voice-terminal/main/ui_face.c"
type: "code"
community: "ESP32 Firmware"
location: "L315"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# _apply_state_cb()

## Connections
- [[_state_to_emotion()]] - `calls` [EXTRACTED]
- [[face_animation_pause()]] - `calls` [INFERRED]
- [[face_animation_pause() — freezes canvas redraw to protect WiFi stack]] - `calls` [EXTRACTED]
- [[face_set_emotion()]] - `calls` [INFERRED]
- [[face_set_emotion() (declared in header; drives eyemouth canvases)]] - `calls` [EXTRACTED]
- [[ui_face.c]] - `contains` [EXTRACTED]
- [[ui_face_set_state()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ESP32_Firmware