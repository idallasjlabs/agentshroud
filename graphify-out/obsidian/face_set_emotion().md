---
source_file: "firmware/voice-terminal/components/lvgl_kawaii_face/lvgl_kawaii_face.c"
type: "code"
community: "Lvgl Kawaii Face (lvgl_kawaii_face)"
location: "L2043"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Lvgl_Kawaii_Face_lvgl_kawaii_face
---

# face_set_emotion()

## Connections
- [[_apply_state_cb()]] - `calls` [INFERRED]
- [[_touch_pressed()]] - `calls` [INFERRED]
- [[app_main()]] - `calls` [INFERRED]
- [[draw_eye()]] - `calls` [EXTRACTED]
- [[draw_mouth()]] - `calls` [EXTRACTED]
- [[emotion_cycle_task()]] - `calls` [INFERRED]
- [[face_emotion_t]] - `references` [EXTRACTED]
- [[face_lock()]] - `calls` [EXTRACTED]
- [[face_unlock()]] - `calls` [EXTRACTED]
- [[lvgl_kawaii_face.c]] - `contains` [EXTRACTED]
- [[ui_face_init()]] - `calls` [INFERRED]
- [[update_emotion_parameters()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Lvgl_Kawaii_Face_lvgl_kawaii_face