---
source_file: "firmware/voice-terminal/main/ui_face.c"
type: "code"
community: "ESP32 Firmware"
location: "L172"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ESP32_Firmware
---

# _touch_pressed()

## Connections
- [[face_animation_pause()]] - `calls` [INFERRED]
- [[face_animation_pause() — freezes canvas redraw to protect WiFi stack]] - `calls` [EXTRACTED]
- [[face_set_emotion()]] - `calls` [INFERRED]
- [[lv_event_t]] - `references` [EXTRACTED]
- [[ui_face.c]] - `contains` [EXTRACTED]
- [[ui_face_init()]] - `calls` [EXTRACTED]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish() — tap-to-stop force-end]] - `calls` [EXTRACTED]
- [[wakeword_ptt_press()]] - `calls` [INFERRED]
- [[wakeword_ptt_release()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_request()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ESP32_Firmware