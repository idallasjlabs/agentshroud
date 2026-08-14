---
source_file: "firmware/voice-terminal/components/lvgl_kawaii_face/lvgl_kawaii_face.c"
type: "code"
community: "Gateway Test Suite"
location: "L157"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# face_animation_init()

## Connections
- [[app_main()]] - `calls` [INFERRED]
- [[draw_eye()]] - `calls` [EXTRACTED]
- [[draw_mouth()]] - `calls` [EXTRACTED]
- [[esp_err_t]] - `references` [EXTRACTED]
- [[face_config_t]] - `references` [EXTRACTED]
- [[face_lock()]] - `calls` [EXTRACTED]
- [[face_malloc_canvas()]] - `calls` [INFERRED]
- [[face_unlock()]] - `calls` [EXTRACTED]
- [[lvgl_kawaii_face.c]] - `contains` [EXTRACTED]
- [[ui_face_init()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite